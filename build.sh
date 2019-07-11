#!/bin/sh

if ! hash kubectl 2>/dev/null; then
    echo "kubectl Not found."
    exit 0
fi

if ! hash minikube 2>/dev/null; then
    echo "minikube Not found."
    echo "please install minikube"
    exit 0
fi

if ! hash docker 2>/dev/null; then
    echo "docker Not found."
    echo "please install docker"
    echo "    apt-get install docker.io -y"
    exit 0
fi

eval $(minikube docker-env)
docker build -t celery-rabbit:k8s ./task
docker pull mongo:4.1 && docker run --name mongo -p 27017:27017 -d mongo:4.1
eval $(minikube docker-env -u)
kubectl create -f ./kubefile
