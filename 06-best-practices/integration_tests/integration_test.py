import os
from datetime import datetime
import pandas as pd

import batch

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)



def test_s3():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    df_prepped = batch.prepare_data(df, columns)

    S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL', None)
    
    if S3_ENDPOINT_URL:
        options = {
            'client_kwargs': {
                'endpoint_url': S3_ENDPOINT_URL
            }
        }

        # df = pd.read_parquet('s3://bucket/file.parquet', storage_options=options)

        df_prepped.to_parquet(
            's3://nyc-duration/file.parquet',
            engine='pyarrow',
            compression=None,
            index=False,
            storage_options=options
        )   
    else:
        print("S3_ENDPOINT_URL not set, reading from local file")
        # df = pd.read_parquet(filename)


    
