# Docker Project
This is a simple project to set up and run a Docker container.

## Files:

| File Name | Description |
| --------- | ----------- |
| [Dockerfile](Dockerfile)   | The Dockerfile to build the Docker image. |
| [server.py](server.py)     | A FastAPI server to serve a simple WebPage. |
| [database.py](database.py) | A simple SQLite3 database script. |

## Commands

### Method 1 : Direct Run:
```bash
docker run -it -p 7575:7575 first_project
```

### Method 2 : Build, Create and Start:
1. First build the Docker image:
    ```bash
    docker build -t first_project:latest .
    ```

2. Then create a Docker container from the image:
    ```bash
    docker create --name first_container -p 7575:7575 first_project:latest
    ```

3. Finally, start the Docker container:
    ```bash
    docker start first_container
    ```

4. To access the container's shell, use:
    ```bash
    docker exec -it first_container bash
    ```


## Tech Stack
- Docker
- Python
- FastAPI
- SQLite3