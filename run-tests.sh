#!/bin/bash

# Script to run pytest tests in Docker container
# Usage: ./run-tests.sh [test_file] [additional_pytest_args]

set -e

# Default test file
TEST_FILE=${1:-"tests/ui/registration/test_registration_stability.py"}
shift || true
PYTEST_ARGS="$@"

echo "🐳 Building Docker image..."
docker build -t pytest-ui-tests .

echo "🧪 Running tests: $TEST_FILE"
echo "📁 Test results will be saved to ./test-results/"

# Create test-results directory if it doesn't exist
mkdir -p test-results

# Run the container with the specified test file
docker run --rm \
    -v "$(pwd)/test-results:/app/test-results" \
    -v "$(pwd)/tests:/app/tests" \
    -v "$(pwd)/actors:/app/actors" \
    -v "$(pwd)/api:/app/api" \
    -v "$(pwd)/ui:/app/ui" \
    -v "$(pwd)/models:/app/models" \
    -v "$(pwd)/utils:/app/utils" \
    -v "$(pwd)/environment:/app/environment" \
    -v "$(pwd)/data_factory:/app/data_factory" \
    --name pytest-runner-$(date +%s) \
    pytest-ui-tests \
    pytest "$TEST_FILE" -v --tb=short $PYTEST_ARGS

echo "✅ Tests completed!"
echo "📊 Check ./test-results/ for test outputs"
