FROM python:3.13.3-alpine

RUN adduser -D devops

USER devops
WORKDIR /home/devops

ENV VIRTUALENV=/home/devops/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=devops:devops dist/*.whl /tmp/

RUN pip install -U pip && \
    pip install --no-cache-dir /tmp/*.whl && \
    rm -rf /tmp/*.whl

EXPOSE 5000

ENTRYPOINT [ "sample-api", "--mode", "prod" ]