# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app.py and templates
COPY app.py .
COPY templates/ .

# Install Flask and PyMongo
RUN pip install Flask pymongo

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
