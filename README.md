# Smart To-Do App

A simple command-line to-do list manager that allows users to add, view, mark, and delete tasks. The tasks are stored in a persistent `tasks.json` file, ensuring data is saved even after the container stops.

---

## 📌 Features

- Add new tasks with title, description, and due date.
- View all tasks with their status (Pending/Done).
- Mark tasks as completed.
- Delete tasks from the list.
- Persistent storage using Docker volumes.

---

## 🛠️ Setup Instructions

### 1. Prerequisites:
Ensure you have the following installed on your system:
- **Docker** 🐳

### 2. Clone the Repository
```bash
git clone https://github.com/your-repo/smart-todo.git
cd smart-todo
```
### 3. **Build the Docker Image**
To build the Docker image, navigate to the project directory and run
```bash
docker build -t image-name
```
### 4. **Run the Container**

```
docker run -it --name container-name -v $(pwd):/app/data image-name
```
### 5. **Start the Container (If Already Created)**
```
docker start -ai container-name
```
## 📌 Usage Examples

Once the app is running inside the Docker container, you will see a menu with options. You can interact with the app by entering the corresponding number for each action.

```bash
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
```

### 1. **Add Task**
**Input**
```
Enter choice: 1
Enter title: Buy groceries
Enter description: Milk, Eggs, Bread
Enter due date (YYYY-MM-DD): 2025-02-15
```
**Output**
```
Task added successfully!
```

### 2. **View Tasks**
>**Input**
>```
>Enter choice: 2
>```
>**Output**
>```
>1. Buy groceries - Milk, Eggs, Bread - Due: 2025-02-15 - Status: Pending
>```

### 3. **Mark Task as Done**
>**Input**
>```
>Enter choice: 3
>Enter task ID to mark as done: 1
>```
>**Output**
>```
>Task marked as done!
>```

>### 4. **Delete a Task**
>**Input**
>```
>Enter choice: 4
>Enter task ID to delete: 1
>```
>**Output**
>```
>Task deleted successfully!
>```

>### 5. **Exit the App**
>**Input**
>```
>Enter choice: 5
>```
>**Output**
>```
>Exiting...
>```

# 🐳 Docker Concepts
<h2 align="center">Dockerfile Description</h2>


### 1. Base Image:
```
FROM python:3.9-slim
```
The instruction `FROM python:3.9-slim` is used in a Dockerfile to specify the base image for a Docker container. In this case:

- **`python:3.9-slim`**: This is a lightweight version of the official Python 3.9 image, optimized for smaller size by excluding unnecessary files and packages.

In short, it means the container will start with a minimal Python 3.9 environment, saving space and resources.


### 2. Working Directory:
```
WORKDIR /app
```
The instruction `WORKDIR /app` in a Dockerfile sets the working directory inside the container to `/app`. 

### 3. Copying Files:
```
COPY . /app

```
The instruction `COPY . /app` in a Dockerfile copies files and directories from the local machine (the current directory, represented by .) into the /app directory inside the Docker container.


### 4. Installing Dependencies:
```
RUN pip install --no-cache-dir -r requirements.txt
```
There are not dependencies required to run this console app, however, in future we may nedd one. If needed, the dependcies will be listed in the `requirements.txt file`.The instruction `RUN pip install --no-cache-dir -r requirements.txt` in a Dockerfile installs Python dependencies listed in the `requirements.txt` file into the container.

In short:
- **`pip install`**: Installs Python packages.
- **`--no-cache-dir`**: Prevents pip from storing downloaded packages in a cache, reducing the image size.
- **`-r requirements.txt`**: Specifies the file (`requirements.txt`) that lists the packages to install.

This ensures all required dependencies for  application are installed in the container.

### 5. Persistent Data Storage:
```
VOLUME /app/data
```
The instruction `VOLUME /app/data` in a Dockerfile mounts a directory at `/app/data` inside the container.
- It designates `/app/data` as a storage location for persistent or shared data.
- Data stored in `/app/data` will survive even if the container is deleted.
- It can also be used to share data between the host machine and the container or between multiple containers.

This is useful for storing databases, logs, or other files that need to persist or be accessed externally.


### 6. Container Execution:
```
ENTRYPOINT ["python", "src/app.py"]

```
The instruction `ENTRYPOINT ["python", "src/app.py"]` in a Dockerfile defines the default command that will be executed when the container starts.
- It runs the Python script `src/app.py` using the `python` interpreter.
- This command becomes the main process of the container.
- Any additional arguments passed to `docker run` will be appended to this command.

This is typically used to specify the main application or service that the container is meant to run.


## Docker Images and Container 

### 3. **Build the Docker Image**
To build the Docker image, navigate to the project directory and run
```bash
docker build -t image-name
```
The command `docker build -t image-name` builds a Docker image from a Dockerfile and assigns it a name (`image-name`) for easy reference.

1. **`docker build`**: This tells Docker to build an image using the instructions in the Dockerfile located in the current directory (or a specified path).
2. **`-t image-name`**: The `-t` flag is used to tag the image with a name (e.g., `image-name`). This name helps to  identify and reference the image later when running containers.
3. **Context**: By default, Docker uses the current directory (`.`) as the build context, which includes the Dockerfile and any files referenced in it.


### 4. **Run the Container**

```
docker run -it --name container-name -v $(pwd):/app/data image-name
```
The command `docker run -it --name container-name -v $(pwd):/app/data image-name` is used to create and start a Docker container with specific options.
1. **`docker run`**: This command creates and starts a new container from an image.
2. **`-it`**: 
   - `-i` keeps the container's input stream open, allowing user to interact with it.
   - `-t` allocates a pseudo-terminal, making the container behave like a command-line interface.
   - Together, `-it` lets user interact with the container in an interactive terminal.
3. **`--name container-name`**: Assigns a custom name (`container-name`) to the container for easier management.
4. **`-v $(pwd):/app/data`**:
   - `-v` creates a volume mount, linking a directory on user host machine to a directory in the container.
   - `$(pwd)` is a shell command that returns the current directory on user host machine.
   - `/app/data` is the directory inside the container where the host directory will be mounted.
   - This allows the container to access and modify files in the host's current directory.
5. **`image-name`**: Specifies the Docker image to use for creating the container.


### 5. **Start the Container (If Already Created)**
```
docker start -ai container-name
```
The command `docker start -ai container-name` is used to start an existing stopped container and attach to it interactively.

1. **`docker start`**: This command starts a stopped container.
2. **`-a`**: Attaches the terminal to the container's standard input, output, and error streams, so you can see the output and interact with it.
3. **`-i`**: Keeps the input stream open, allowing you to interact with the container (if it supports interactive input).
4. **`container-name`**: The name of the stopped container you want to start and attach to.

### 6. Tagging & Versioning
This set of commands is used to build, tag, and manage Docker images. Here's a breakdown of what each command does:

---

### 1. **Build with a specific version**
```bash
docker build -t smartapp:1.0 .
```
- **What it does**: Builds a Docker image from the Dockerfile in the current directory (`.`).
- **`-t smartapp:1.0`**: Tags the image with the name `smartapp` and version `1.0`.
- **Result**: A Docker image named `smartapp:1.0` is created.

---

### 2. **Tag for multiple environments**
```bash
docker tag smartapp:1.0 smartapp:latest
docker tag smartapp:1.0 smartapp:staging
```
- **What it does**: Creates additional tags for the same image (`smartapp:1.0`).
  - `smartapp:latest`: Tags the image as `latest`, which is often used as the default version.
  - `smartapp:staging`: Tags the image as `staging`, which could be used for a staging environment.
- **Result**: The same image is now accessible with three tags:
  - `smartapp:1.0`
  - `smartapp:latest`
  - `smartapp:staging`

---

### 3. **List local images with tags**
```bash
docker images
```
- **What it does**: Lists all Docker images stored locally on your machine, including their:
  - Repository (e.g., `smartapp`)
  - Tag (e.g., `1.0`, `latest`, `staging`)
  - Image ID
  - Size
- **Result**: You can see all the images and their tags, including the ones you just built and tagged.

---

![Alt text](screenshot\docker-images.png)

This workflow is useful for managing different versions and environments (e.g., production, staging) of your Dockerized application.


# **Application Screenshots**

**1. Add Task**

![Alt text](screenshot\add_task.png)

**2. View Task**

![Alt text](screenshot\view_task.png)

**3. Mark task as Done**

![Alt text](screenshot\mark_done.png)

**4. View Task after marked done**

![Alt text](screenshot\view-after-done.png)

The change in the json data.

![Alt text](screenshot\data-change-for-mark-as-done.png)

**2. Delete Task**

![Alt text](screenshot\task-deleted.png)

**2. Exit Application**

![Alt text](screenshot\exiting.png)


