FROM python:3.12-slim-bookworm

LABEL maintainer="Bhushan Songire <bhushanbsongire@gmail.com>"
LABEL description="This is a Dockerfile for a simple FastAPI server and SQLite Database based website."
LABEL version="2.0"

# Update first:
RUN echo "[#] Updating the system packages..."    
RUN apt update && apt upgrade -y && rm -rf /var/lib/apt/lists/*

# Copy the application files
COPY ./assets /app/assets
COPY index.html /app/index.html
COPY ./server.py /app/server.py
COPY ./requirements.txt /app/requirements.txt
COPY ./database.py /app/database.py

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN echo "[#] Installing Python dependencies..."
# RUN pip3 install --prefer-binary -r requirements.txt
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Expose the port on which the FastAPI server will run
EXPOSE 7575

# Set environment variables
ENV ENV_TYPE="Development"

# Echo success message
RUN echo "[#] Application setup complete. Check here: http://localhost:7575"

# Set the entrypoint to run the FastAPI server
CMD ["python3", "server.py"]
