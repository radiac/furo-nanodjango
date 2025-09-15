FROM python:3.13-slim

WORKDIR /project

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install our theme when container starts
CMD ["sh", "-c", "cd theme && pip install -e . && cd ../test-docs && sphinx-autobuild . _build/html --host 0.0.0.0 --port 8000"]