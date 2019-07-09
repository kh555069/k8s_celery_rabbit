#!/bin/sh
kubectl exec $(kubectl get pods | grep -o -e "celery-controller-\w\+") -- bash -c "python start.py"
