FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# Install pip and pipenv
RUN pip install -U pip
RUN pip install -U pipenv

# Copy pipenv dependencies
COPY ./Pipfile .
COPY ./Pipfile.lock .

# Install dependencies
RUN pipenv install --system --deploy

# Copy script
COPY ./starter.py .

ENTRYPOINT ["python", "starter.py"]

