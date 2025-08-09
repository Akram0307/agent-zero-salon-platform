# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy the shared directory
COPY ../../shared ./shared

# Set environment variable for port
ENV PORT=8080

# Set PYTHONPATH to include the project root
ENV PYTHONPATH=/app

# Expose the port
EXPOSE 8080

# Run the application
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
