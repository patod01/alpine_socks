#! /bin/bash

# correr desde la carpeta raiz del proyecto.
# truco: `alias r=tools/run.sh`
# truco: `alias i=tools/img.sh`

sudo docker run --rm -it \
--name mac \
-p 5173:10001 \
-w /server \
-v "$(pwd)/app":/server/app \
python:3.12.3-alpine3.20 \
ash -c "
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
cd app
pip install --no-cache-dir -r req.txt
ash
# python vale.py dev 10001
"
