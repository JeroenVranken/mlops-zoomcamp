# Instructions for running

## 0: Activate environment
```bash
pipenv shell
```

## 1: Bring up localstack:
```bash
docker-compose up
```

## 2: Create a bucket:
```bash
aws s3 mb s3://nyc-duration --endpoint-url http://localhost:4566
```

Make sure the endpoint url matches with the endpoint specifiec in the `docker-compose.yaml`

## 3: Check if the bucket was created
```bash
aws s3 ls --endpoint-url http://localhost:4566
```

## 4: Run the tests using pytest
```bash
pytest
```

If all tests ran succesfully, the file should now be available on localstack, you can check using the following command:
```bash
aws s3 ls s3://nyc-duration  --endpoint-url http://localhost:4566 --human-readable
```


# Solutions to questions

## Q1:

The `if` statement should look like this:
```python
if __name__=="__main__":
    # do your functions here
```

## Q2:
We need an `__init__.py` file

## Q3:
There should be 2 rows

## Q4:
We need to set the `--endpoint-url`

## Q5:
The size of the file is 3.5 KiB =± 3620

## Q6:
The sum of predicted durations for the test dataframe is 36.28