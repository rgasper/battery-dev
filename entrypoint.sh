#!/usr/bin/env bash

cd /app
jupyter lab --allow-root --port=$JUPYTER_PORT --no-browser --ip=0.0.0.0