
# battery-dev

Project repository for battery dev team code-better
Please see 'notebooks/results' for an overview of the model (quite simple) and approach.
Here, we have tried to use best-practices to ensure model reproducibility, and hope others will show interest in these tools for their own projects.
## Architecture Choices
The tools used to ensure model reproducibility include
- Github: needs no introduction, you're here
- Docker: allows no ambiguity and easy setup for environment dependencies
- Jupyter Lab: a flexible and highly adopted entrypoint for writing & debugging python code
- Data Version Control (DVC): fully defined workflows and easy data sharing when combined with the cloud

Note: this is not finished, there isn't really a model here. The fundamental issue is the low amount of data. I think an interesting direction to go is to implement a RNN that from a history of charge/discharge profiles predicts the next charge/discharge profile, though defining what is input data and what is target data in that case becomes very muddy.

## Setup

We're using Docker to ensure we all have identical environments to work in. To get started, first install Docker for your operating system: https://docs.docker.com/get-docker/.

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

### dvc setup

I've hosted the dvc remote cache on a folder in my google drive. I believe it should be sufficient based on [gdrive limits](https://support.google.com/a/answer/7338880). When you first run `dvc pull` or `dvc push` you will be prompted to login. Just paste the auth code back into the terminal like dvc asks and you should be good to go!

When you launch for the first time, to get data, simply run `dvc pull`.

### daemon mode

If you would like the jupyter container to run in the background, and not have it occupy your terminal with logs:

```console
docker compose up -d
```

Do your stuff, then when you're done and want to turn it off:

```console
cd path/to/battery-dev # if you navigated around with your terminal
docker compose down
```

## Repo Guide

All code in the top-level directory is configuration, container setup, or the container executable.

- /data
  - contains data csvs used by the models
  - entire dir tracked by dvc
- /models
  - any model files or saved parameter values
- /stages
  - code for each stage of the model development process
  - stages are called in order by dvc, following the dvc.yaml file in the main directory
- /results
  - any output files reporting predictions

