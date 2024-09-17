# Define the argument before its first use
FROM python:3.9-slim

# get utilities in the container
RUN apt-get update && apt-get install -y procps ssh git net-tools htop build-essential libsqlite3-dev

# Install pip dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install gnews pysqlite3