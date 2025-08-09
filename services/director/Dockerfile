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

# Expose the port
EXPOSE 8000
ENV PORT=8000

# Run the application
CMD uvicorn agents.core.director.main:app --host 0.0.0.0 --port $PORT
