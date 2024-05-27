# 02-fastapi-docker-ml

This repository contains code to train and use a machine learning using FastAPI with Docker


## Getting Started
Follow these steps to set up your development environment and start working on the project.


1. Clone the repository

```
git clone (https://github.com/kiaraesguerra/02-fastapi-docker-ml/
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
5. Create the Docker image
```
cd 02-fastapi-docker-ml
docker build -t 02-fastapi-docker-ml .
```

6. Run docker with the train and test datasets as volume attachments
```
docker run -tid \
--name 02-fastapi-docker-ml-training \
-v /path/to/train_data.csv:/app/train_data.csv \
-v /path/to/test_data.csv:/app/test_data.csv \
<image id>
```

7. (If using Docker Desktop) Try out these commands on the exec tab of the container:
```
curl http://localhost:8000/ping
curl http://localhost:8000/read_root
curl -X POST "http://localhost:8000/train" -H "accept: application/json" -F "file=@/app/train_data.csv"
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -F "file=@/app/test_data.csv"
```
