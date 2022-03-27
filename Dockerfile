#Base image
FROM python:3.9-slim-buster

ENV PIPENV_VENV_IN_PROJECT 1

RUN apt update && apt install -y gcc

# Copy the project files
COPY ./ /code

# Set the working directory
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose a port
ENV export PORT=5000
EXPOSE $PORT

# Executables
# ENTRYPOINT [ "python", "app.py" ]
CMD ["python", "app.py"]

