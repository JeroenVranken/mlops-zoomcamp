import os
from datetime import datetime
import pandas as pd

import batch

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)



def test_s3():

    # create fake dataframe
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    df_prepped = batch.prepare_data(df, columns)

    # save to s3
    output_file = 'file.parquet'
    batch.save_data(df_prepped, output_file)

    # Load from S3
    df_from_s3 = batch.read_data(output_file, columns)


    # Check if the data was saved and loaded correctly
    assert df_from_s3.shape == (2, 5)


# Q5: Verify that data was written correctly using:
# aws s3 ls s3://nyc-duration --endpoint-url http://localhost:4566 --human-readable
# The size of the file is 3.5 KiB =± 3620

    
