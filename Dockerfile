# Use Python 3.11 with Ubuntu base for better browser support
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for Playwright and other packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    procps \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps chromium firefox webkit

# Copy the entire project
COPY . .

# Create directories for test outputs
RUN mkdir -p test-results/videos test-results/screenshots

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTEST_CURRENT_TEST=""
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Default command to run the specific test
CMD ["pytest", "tests/ui/registration/test_registration_stability.py", "-v", "--tb=short"]
