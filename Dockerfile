### actual sh1t ###
FROM python:3.12.3-alpine3.20 AS pydep

ENV PATH="/server/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/server/.venv"

WORKDIR /server
RUN python -m venv .venv
RUN python -m pip install --upgrade pip
COPY ./app/req.txt .
RUN pip install --no-cache-dir -r req.txt


### actual sh2t ###
FROM python:3.12.3-alpine3.20

ENV MODE="dev"
ENV PORT="10001"

WORKDIR /server/app
COPY --from=pydep /server/.venv ../.venv
COPY ./app .

CMD source ../.venv/bin/activate && python vale.py $MODE $PORT
