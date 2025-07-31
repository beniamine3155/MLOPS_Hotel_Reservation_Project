# Use a lightweight Python image
FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# Set the working directory
WORKDIR /app

# Install system dependencies required by LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -e .

# Train the model (optional, but okay)
RUN python pipeline/training_pipeline.py

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Start the Flask app on Cloud Run compatible port
CMD ["python", "application.py"]
