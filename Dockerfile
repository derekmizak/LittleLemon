# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile to the container
COPY Pipfile /app/

# Install dependencies using pipenv without creating a lock file
RUN pipenv install --skip-lock

# Copy the content of the local src directory to the working directory
COPY . /app/
