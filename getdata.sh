#!/bin/sh
kubectl exec $(kubectl get pods | grep -o -e "celery-controller-\w\+") -c celery -- bash -c "python getdata.py"
