# battery-dev
Project repository for battery dev team code-better

## Setup

To get started, first install Docker for your operating system: https://docs.docker.com/get-docker/.

Then it's as easy as:

```console
docker compose build
docker compose up
```

And you'll have the correctly configured environment up and running on your computer! When it launches, jupyter will recommend 3 urls to you to link into it:

```console
jupyter    |     To access the server, open this file in a browser:
jupyter    |         file:///root/.local/share/jupyter/runtime/jpserver-7-open.html
jupyter    |     Or copy and paste one of these URLs:
jupyter    |         http://04cde2523688:8888/lab?token=b30eb555d814d414311c7e4a5c9806ca0572c9e445857b30
jupyter    |      or http://127.0.0.1:8888/lab?token=b30eb555d814d414311c7e4a5c9806ca0572c9e445857b30
```

Pick the last one that begins in `http://127.0.0.1:8888`. The other two won't work, as those can only be reached from a browser running inside the container.

Stop the server by issuing the keyboard interrupt command for your OS in the terminal.

## Repo Guide

Currently all code lives in python scripts in `jupyter_app/`. Everything else is just configuration.
