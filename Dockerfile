# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Expose the port that the FastAPI application will be running on
EXPOSE 8080

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
