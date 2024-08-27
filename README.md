# FastAPI and Celery Application

## Description

This application is based on FastAPI and Celery, providing a robust setup for asynchronous task processing and API handling.

## Running the Application

1. **Make the script executable and run it:**

    ```bash
    chmod +x run.sh && ./run.sh
    ```

2. **Open the API in your web browser:**

    Visit [http://localhost:8000/api](http://localhost:8000/api) to see the results.

## Initial Setup

1. **Generate random details:**

    Execute the `/v2/generate` endpoint in the web application. This step is required for setup.

2. **Submit Orders:**

    Submit orders as desired using the `/v2/orders` endpoint.

## Viewing Logs

To view the logs for Celery worker, use the following command:

```bash
docker logs celery_worker
