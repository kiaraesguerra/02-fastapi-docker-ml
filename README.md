# 02-fastapi-docker-ml

This repository contains code to train and use a machine learning using FastAPI with Docker


## Getting Started
Follow these steps to set up your development environment and start working on the project.


1. Clone the repository and switch to branch

```
git clone (https://github.com/kiaraesguerra/02-fastapi-docker-ml/
git branch 03-train-inference-compose
```

2. Set up virtual environment

First, create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```
pip install -r app/requirements.txt
```

4. Run the notebook to generate the training and test data
5. Run docker-compose
```
cd fastapi-docker-ml
docker-compose up --build
```
