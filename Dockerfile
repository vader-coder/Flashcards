FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN [ "echo", "docker run -i <image>" ]
CMD ["python", "./flashcards.py"]
