#!/bin/sh
if ! hash kubectl 2>/dev/null; then
    echo "kubectl Not found."
    exit 0
fi

if ! hash minikube 2>/dev/null; then
    echo "minikube Not found."
    exit 0
fi

if ! hash docker 2>/dev/null; then
    echo "docker Not found."
    exit 0
fi

kubectl delete replicationcontrollers rabbitmq-controller celery-controller
kubectl delete services rabbitmq-management rabbitmq-service

while [ -n "$(kubectl get pods | grep celery-controller)" ]
do
    echo "waiting pods delete"
    sleep 3
done

eval $(minikube docker-env)
docker rmi celery-rabbit:k8s
docker stop mongo && docker rm mongo && docker rmi mongo:4.1
eval $(minikube docker-env -u)
