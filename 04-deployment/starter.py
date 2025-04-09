#!/usr/bin/env python
# coding: utf-8


import pickle
import pandas as pd
import argparse


def load_model(path: str):
    """Loads the model from specfied path"""

    with open(path, 'rb') as f_in:
        dv, model = pickle.load(f_in)

    return dv, model

def read_data(filename: str, categorical):
    """Reads data from the specified filename (which can be url)."""
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def predict(df, dv, model, categorical):
    """Predicts on the dataframe using the specified model"""
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    print(f"The mean predicted duration of y_pred : {y_pred.mean()}")

    return y_pred


def prepare_output(df, y_pred, year, month):
    """Converts the dataframe to the required output format"""
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df['y_pred'] = y_pred

    return df


def save_output(output, year, month):
    """Saves the prediction outputs locally"""
    output_file = f'yellow_tripdata_{year:04d}-{month:02d}_predictions.parquet'
    df_result = output[['ride_id', 'y_pred']]

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )


def run(year, month):
    
    categorical = ['PULocationID', 'DOLocationID']

    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet', categorical)
    dv, model = load_model("model.bin")

    y_pred = predict(df, dv, model, categorical)

    output = prepare_output(df, y_pred, year, month)

    save_output(output, year, month)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process month and year as integers.")
    parser.add_argument('--month', type=int, required=True, help='Month as an integer (1-12)', default=3)
    parser.add_argument('--year', type=int, required=True, help='Year as a four-digit integer', default=2023)

    args = parser.parse_args()

    print(f"Month: {args.month}")
    print(f"Year: {args.year}")

    run(args.year, args.month)    
