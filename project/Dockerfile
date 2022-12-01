FROM python:3.8-slim-bullseye

SHELL ["/bin/bash", "-c"]

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo -e "alias populate=\"python populate_db.py\"\n" >> ~/.bashrc
RUN echo -e "alias test=\"python -m unittest discover tests\"\n" >> ~/.bashrc
RUN echo -e "alias bio=\"python script.py\"\n" >> ~/.bashrc
RUN source ~/.bashrc