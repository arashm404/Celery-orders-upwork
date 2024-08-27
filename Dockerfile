# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /api

# Copy the current directory contents into the container at /api
COPY ./api /api

# Copy requirements file and install dependencies
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the application
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
