FROM python:3.8.1
RUN apt install python3
COPY hello.py ./
CMD ["python", "hello.py"]
