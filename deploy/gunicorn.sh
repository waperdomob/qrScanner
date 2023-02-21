#!/bin/bash

NAME="QR_scanner"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-qrscanner.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=wilmer
GROUP=wilmer
NUM_WORKERS=5
DJANGO_WSGI_MODULE=qrScanner.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR