#!/bin/bash
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test name for the container
TEST_CONTAINER_NAME="scribble-test"

echo "🔍 Testing Dockerfile in scribble..."

# Step 1: Build the Docker image
echo "🏗️  Building Docker image..."
docker build -f Dockerfile -t scribble-app-test ..

# Step 2: Run the container in detached mode
echo "🚀 Starting container..."
docker run -d --name $TEST_CONTAINER_NAME -p 7862:7860 scribble-app-test

# Step 3: Wait for the container to start (give it some time to initialize)
echo "⏳ Waiting for container to initialize..."
sleep 5

# Step 4: Test that the application is accessible
echo "🌐 Testing HTTP connection..."
if curl -s -f http://localhost:7862/ > /dev/null; then
    echo -e "${GREEN}✅ HTTP connection successful${NC}"
else
    echo -e "${RED}❌ HTTP connection failed${NC}"
    docker logs $TEST_CONTAINER_NAME
    docker stop $TEST_CONTAINER_NAME
    docker rm $TEST_CONTAINER_NAME
    exit 1
fi

# Step 5: Check the container's health status
echo "💓 Checking container health..."
# Get the health status and remove any newline characters
HEALTH_STATUS=$(docker inspect --format='{{.State.Health.Status}}' $TEST_CONTAINER_NAME 2>/dev/null | tr -d '\n' || echo "none")

# If health status is empty, set it to "none"
if [ -z "$HEALTH_STATUS" ]; then
    HEALTH_STATUS="none"
fi

if [ "$HEALTH_STATUS" = "healthy" ] || [ "$HEALTH_STATUS" = "starting" ] || [ "$HEALTH_STATUS" = "none" ]; then
    echo -e "${GREEN}✅ Container health check passed: $HEALTH_STATUS${NC}"
    # If health status is "none", the container doesn't have a health check defined
    if [ "$HEALTH_STATUS" = "none" ]; then
        echo -e "${GREEN}ℹ️ No health check defined for this container${NC}"
    fi
else
    echo -e "${RED}❌ Container health check failed: $HEALTH_STATUS${NC}"
    docker logs $TEST_CONTAINER_NAME
    docker stop $TEST_CONTAINER_NAME
    docker rm $TEST_CONTAINER_NAME
    exit 1
fi

# Step 6: Verify the container is running with the correct user
echo "👤 Checking container user..."
CONTAINER_USER=$(docker exec $TEST_CONTAINER_NAME whoami)
if [ "$CONTAINER_USER" = "user" ]; then
    echo -e "${GREEN}✅ Container is running as the expected user: $CONTAINER_USER${NC}"
else
    echo -e "${RED}❌ Container is running as unexpected user: $CONTAINER_USER${NC}"
    docker stop $TEST_CONTAINER_NAME
    docker rm $TEST_CONTAINER_NAME
    exit 1
fi

# Step 7: Verify marimo is installed correctly
echo "📦 Checking marimo installation..."
if docker exec $TEST_CONTAINER_NAME which marimo > /dev/null; then
    echo -e "${GREEN}✅ Marimo is installed correctly${NC}"
else
    echo -e "${RED}❌ Marimo is not installed correctly${NC}"
    docker stop $TEST_CONTAINER_NAME
    docker rm $TEST_CONTAINER_NAME
    exit 1
fi

# Clean up
echo "🧹 Cleaning up..."
docker stop $TEST_CONTAINER_NAME
docker rm $TEST_CONTAINER_NAME

echo -e "${GREEN}✅ All Docker tests passed successfully!${NC}"
