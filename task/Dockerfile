FROM python:3.5.2
WORKDIR /task/

COPY . /task/

RUN pip install --upgrade pip && \
    pip install -r /task/pkg.txt

ENV C_FORCE_ROOT=true

CMD ["celery", "-A", "tasks", "worker", "--concurrency=20", "--config=celeryconfig" , "--loglevel=info", "-f", "/task/celery.log"]
