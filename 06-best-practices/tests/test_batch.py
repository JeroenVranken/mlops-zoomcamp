from datetime import datetime
import pandas as pd

import batch

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)



def test_prepare_data():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    df_prepped = batch.prepare_data(df, columns)


    assert df_prepped.shape == (2, 5)

    ## Homework question 3: There should be two rows in the expected dataframe



    