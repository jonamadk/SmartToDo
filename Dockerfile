# Use the official Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies (if any, e.g., Flask or other dependencies in the future)
RUN pip install --no-cache-dir -r requirements.txt

# Set the volume mount for persistent storage of tasks.json
VOLUME /app/data

# Set the entry point to run the Python script
ENTRYPOINT ["python","\task-manager\app.py"]
