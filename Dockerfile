# Use an official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy application files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Set the environment variable (optional; can be overridden at runtime)
ENV MY_WEB_APP_STATUS="Running"

# Expose port 8017
EXPOSE 8017

# Command to run the application
CMD ["python", "app.py"]
