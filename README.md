# krm_template_python

A minimal python application template, using KRM via Skaffold and Kustomize to deploy an application onto GKE.

## Overview

This repo deploys a fastapi server. GitHub actions orchestrate deployment to Google Kubernetes Engine via Workload Identity authentication and generates kubernetes resources for two environments using Skaffold and Kustomize.

## Notable Tools

- [Skaffold](https://skaffold.dev/docs/install/)
- [Kustomize](https://kustomize.io/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Docker](https://docs.docker.com/get-docker/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Contributing

Pull requests and issues are very welcome.
