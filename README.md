<h1 align="center"> Python Pizza Planet </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is an example software for a pizzeria that takes customizable orders.

## Table of Contents

- [Getting started](#getting-started)
- [Running the backend project](#running-the-backend-project)
- [Running the frontend](#running-the-frontend)
- [Testing the backend](#testing-the-backend)
- [Running the Infrastructure with Docker-compose](#Setting-up-the-local-infrastructure)


## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.8.x](https://www.python.org/downloads/release/python-3810/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Running the backend project

- Clone the repo

```bash
git clone https://github.com/ioet/python-pizza-planet.git
```

- Create a virtual environment in the root folder of the project

```bash
python3 -m venv venv
```

- Activate the virtual environment (In vscode if you select the virtual env for your project it will activate once you open a new console window)

_For linux/MacOS users:_

```bash
source venv/bin/activate 
```

_For windows users:_

```cmd
\path\to\env\Scripts\activate
```

- Install all necessary dependencies:

```bash
pip3 install -r requirements.txt
```

- Start the database (Only needed for the first run):

```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

- If you want to use the hot reload feature set FLASK_ENV before running the project:

_For linux/MacOS users:_

```bash
export FLASK_ENV=development 
```

_For windows users:_

```CMD
set FLASK_ENV=development
```

- Run the project with:

```bash
python3 manage.py run
```

## Running the frontend

- Clone git UI submodule

```bash
git submodule update --init
```

- Install Live Server extension if you don't have it from [here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) on VSCode Quick Open (`Ctrl + P`)

```bash
ext install ritwickdey.LiveServer
```

- To run the frontend, start `ui/index.html` file with Live Server (Right click `Open with Live Server`)

- **Important Note** You have to open vscode in the root folder of the project.

- **To avoid CORS errors** start the backend before the frontend, some browsers have CORS issues otherwise

### Testing the backend

- Make sure that you have `pytest` installed

- Run the test command

```bash
python3 manage.py test
```

### Setting up the infrastructure tests with Docker-compose

- Make sure you have Docker and Docker Compose installed on your system. If not, you can download them from the official website.


- Create a .env file in the root of your project directory, and add the following line:

```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

- At root level, Run the following command to build the container:

```
docker-compose up --build
```

- After having the image running on your machine, you don't need to compose anymore, just run:

```
docker-compose up
```

- Now you should be able to go inside the docker desktop, and seeing the terraform init, plan, apply being performed.


## Deployment of infrastructure

- After having the infrastrucre deployed without problems in your docker machine, you should test the deployment against the AWS Pizza planet sandbox.

#### Prerequisites

- Terraform installed on your system. You can download the appropriate version for your operating system from the Terraform website.

- An AWS account. If you don't have one, you can sign up for a free trial here.

- AWS access key and secret key with appropriate permissions. You can create these in the AWS Management Console under the "Security Credentials" section. Make sure to give these keys permissions to create resources in the services you plan to use (e.g. EC2, RDS, S3, etc.).

- Familiarity with the AWS Management Console and basic AWS service