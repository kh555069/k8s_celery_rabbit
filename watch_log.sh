#!/bin/sh

kubectl exec -it $(kubectl get pods | grep -o -e "celery-controller-\w\+") -- bash -c "watch -n 0 tail -n 15 celery.log"
