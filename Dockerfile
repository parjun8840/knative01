# Dockerfile

# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application into the container
COPY app.py .

# Install Flask
RUN pip install Flask

# Specify the command to run the Flask application
CMD ["python", "app.py"]
