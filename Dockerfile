FROM ubuntu:22.04
LABEL maintainer="Bhushan Songire <bhushanbsongire@gmail.com>"
LABEL description="This is a Dockerfile for a simple FastAPI server and SQLite Database based website."
LABEL version="1.0"

# Update first:
RUN echo "[#] Updating the system packages..."    
RUN apt update && apt upgrade -y

# Install necessary packages
RUN apt install -y python3 python3-pip python3-venv git

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
RUN pip3 install --prefer-binary -r requirements.txt

# Create database and tables
RUN echo "[#] Setting up the database..."
RUN python3 database.py

# Expose the port on which the FastAPI server will run
EXPOSE 7575

# Set environment variables
ENV ENV_TYPE="Development"

# Echo success message
RUN echo "[#] Application setup complete. Check here: http://localhost:7575"

# Set the entrypoint to run the FastAPI server
CMD ["python3", "server.py"]
ENTRYPOINT ["python3", "server.py"]
