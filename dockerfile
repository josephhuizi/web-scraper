# Use an official Python 3.11 image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the uv.lock file
COPY uv.lock .

# Copy the pyproject.toml file
COPY pyproject.toml .

# Install the dependencies using UV
RUN pip install uv && uv install --verbose

# Copy the application code
COPY . .

# Run app.py when the container launches
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]