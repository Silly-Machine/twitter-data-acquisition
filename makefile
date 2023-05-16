ifndef ENV_NAME
	ENV_NAME = twitter-data-acquisition
endif

create_environment:
	conda create -y -n $(ENV_NAME) python=3.8

activate_environment:
	conda init bash
	conda activate $(ENV_NAME) 

setup_environment:
	pip install poetry
	pip install ipykernel
	poetry install

all: create_environment activate_environment setup_environment