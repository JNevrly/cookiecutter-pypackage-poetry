FROM python:{{ cookiecutter.python_version }}-slim

# Install git and other dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry
