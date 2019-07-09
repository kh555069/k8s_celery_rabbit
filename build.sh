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
eval $(minikube docker-env -u)
kubectl create -f ./kubefile
