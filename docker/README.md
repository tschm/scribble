# 🐳 Docker Support for Scribble

This directory contains Docker-related files for containerizing the
Scribble application. Docker enables consistent deployment across different
environments, simplifies dependency management, and provides isolation for the application.

## 🚀 Overview

The Docker setup in this project allows you to:

- Package the Scribble application with all its dependencies
- Run the application in an isolated container
- Deploy the application consistently across different environments
- Test the application in a production-like environment
- Automate testing through CI/CD pipelines

## 📄 Files and Their Purpose

- `Dockerfile`: Defines the container image build process
  - Uses Python 3.13 slim as the base image
  - Installs dependencies using the fast `uv` package manager
  - Sets up a non-root user (`app_user`) for security
  - Configures the application to run with Marimo

- `Dockerfile.dockerignore`: Optimizes the build context
by excluding unnecessary files
  - Uses a "deny by default, allow explicitly" approach
  - Only includes essential files for the build
  - Excludes Python cache files to reduce image size

- `test_docker.sh`: Comprehensive test script for validating the Docker container
  - Performs multiple validation checks
  - Provides colorful, easy-to-read output
  - Includes proper error handling and cleanup

- `Makefile`: Provides convenient commands for building and testing
  - Simplifies Docker commands with easy-to-remember targets
  - Includes help documentation for available commands

## 🏗️ Building and Running the Docker Image

You can build and run the Docker image using the `build` target in the Makefile:

```bash
make build
```

This command:

1. Builds the Docker image with the tag `marimo-app`
2. Runs the container with the following configuration:
   - Interactive mode (`-it`)
   - Automatic cleanup when stopped (`--rm`)
   - Port 7860 exposed to the host (`-p 7860:7860`)
   - Marimo application running inside

Note: The test_docker.sh script uses port 7862 for testing, while
the Makefile uses port 7860 for running the container.

### 🔍 What Happens During the Build

1. Starts with a minimal Python 3.13 slim base image
2. Installs the `uv` package manager for faster dependency installation
3. Sets environment variables for optimization
4. Creates a non-root user (`app_user`) for security
5. Installs dependencies from `requirements.txt`
6. Copies the application code and the `pyscribble` package
7. Configures the container to run as a non-root user
8. Sets up a health check to monitor the application
9. Configures the entry point to run the Marimo application

## 🧪 Testing the Docker Container

The Docker container can be tested using the `test-docker` target in the Makefile:

```bash
make test-docker
```

This runs the `test_docker.sh` script, which performs a series of validation checks:

1. 🏗️ **Build Test**: Verifies that the Docker image builds successfully
   - Ensures the Dockerfile is valid and all dependencies can be installed

2. 🚀 **Run Test**: Checks that the container starts correctly
   - Confirms the container can be launched without errors

3. 🌐 **HTTP Test**: Ensures the application is accessible on port 7862
   - Validates that the web interface is responding to requests

4. 💓 **Health Check**: Verifies the container's health check is working
   - Confirms the built-in Docker health monitoring is functioning
   - Handles cases where no health check is defined

5. 👤 **User Test**: Confirms the container is running as the non-root user
   - Validates the security configuration is working correctly

6. 📦 **Marimo Test**: Checks that Marimo is installed correctly
   - Ensures the application framework is available

## 🔄 CI/CD Integration

The Docker container is automatically tested on each push
and pull request using GitHub Actions:

- The workflow is defined in `.github/workflows/docker-test.yml`
- It runs the same tests as the local `test_docker.sh` script
- It provides feedback on the Docker build in pull requests
- It ensures the Docker setup remains functional as the codebase evolves

This integration helps maintain the quality and reliability
of the Docker setup over time.

## 📦 pyscribble Package

The Docker container includes the `pyscribble` package, which
provides the core functionality for the Scribble application:

- **letter**: Defines the points that make up each letter
- **series**: Applies mathematical transformations to the letters
- **create**: Generates the visual representation of the transformed text

The package is installed in the Docker container during the build process.

## 🔒 Security Features

The Docker container includes several security features to follow best practices:

- **Non-root User**: Runs as a dedicated user (`app_user`) with limited privileges
  - Reduces the potential impact if the container is compromised
  - Follows the principle of least privilege

- **Minimal Base Image**: Uses Python slim to reduce the attack surface
  - Contains only essential packages
  - Results in a smaller image with fewer potential vulnerabilities

- **Layer Optimization**: Minimizes the number of layers
  - Combines related commands to reduce complexity
  - Makes the image more maintainable and secure

- **Health Monitoring**: Includes a health check
  - Allows Docker to monitor the application's status
  - Enables automatic recovery in orchestration systems

## 🛠️ Customization

You can customize the Docker build by modifying the following:

### Port Mapping

Change the host port while keeping the container port at 7860 (or 7862 for testing):

```bash
docker run -it --rm -p 8080:7860 marimo-app
```

This maps the container's port 7860 to the host's port 8080.

For testing with the test_docker.sh script, the port mapping would be:

```bash
docker run -it --rm -p 8080:7862 marimo-app
```

### Environment Variables

You can pass environment variables to the container:

```bash
docker run -it --rm -p 7860:7860 -e DEBUG=1 marimo-app
```

For testing with the test_docker.sh script:

```bash
docker run -it --rm -p 7862:7860 -e DEBUG=1 marimo-app
```

### Volume Mounts

For development, you can mount local directories into the container:

```bash
docker run -it --rm -p 7860:7860 -v $(pwd)/data:/app/data marimo-app
```

For testing with the test_docker.sh script:

```bash
docker run -it --rm -p 7862:7860 -v $(pwd)/data:/app/data marimo-app
```

## 🔧 Troubleshooting

### Container Won't Start

If the container fails to start:

1. Check the Docker logs: `docker logs <container_id>`
2. Verify port availability: `netstat -tuln | grep 7860`
(or `netstat -tuln | grep 7862` for testing)
3. Ensure you have the latest image: `docker pull marimo-app`

### Application Not Accessible

If you can't access the application:

1. Verify the container is running: `docker ps`
2. Check the container's health:
   `docker inspect --format='{{.State.Health.Status}}' <container_id>`
3. Try accessing with the IP directly: `curl http://localhost:7860/`
(or `curl http://localhost:7862/` for testing)

### Performance Issues

If the application is slow:

1. Check container resource usage: `docker stats <container_id>`
2. Consider allocating more resources: `docker run --memory=1g --cpus=1 ...`
