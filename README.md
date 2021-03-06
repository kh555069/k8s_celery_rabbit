# k8s-celery-rabbit

## 更新
### 20190712
* 新增 MongoDB container ，儲存抓下來的資料，以及簡單讀取MongoDB資料的 script

******

使用 kubernetes 達成快速部署分散式爬蟲

透過 virtualbox 用 minikube 來跑單一節點的 kubernetes cluster，其中有3個yaml檔 rabbitmq-service.yaml rabbitmq-controller.yaml , celery-rabbitmq.yaml 取自 https://github.com/kubernetes/kubernetes/tree/release-1.1/examples/celery-rabbitmq


## Installation
本次示範需要安裝 docker , kubectl , minikube , virtualbox

docker 安裝: `sudo apt-get update ; sudo apt-get install docker.io -y`

kubectl 安裝: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux

minikube 安裝: https://kubernetes.io/docs/tasks/tools/install-minikube/

virtualbox 安裝: https://tecadmin.net/install-oracle-virtualbox-on-ubuntu/



## Start
執行 `./build.sh` 就能完成部署

build 完之後可以透過 `kubectl get pods` 查看 pods 狀況
![image](https://github.com/kh555069/k8s_celery_rabbit/blob/master/pictures/get-pods.png)

pods剛啟動需要等待大約1分鐘的時間
![image](https://github.com/kh555069/k8s_celery_rabbit/blob/master/pictures/watch.png)


執行 `minikube ip` 查詢 ip ，沒意外應該是 `192.168.99.100`

到 http://192.168.99.100:30002 就能看到 celery 的狀況。
(帳號密碼皆為 guest)
![image](https://github.com/kh555069/k8s_celery_rabbit/blob/master/pictures/rabbit-management.png)


執行 `./start.sh` 開始ptt爬蟲，執行 `./watch_log.sh` 查看爬蟲過程 (下方是 gif 請耐心等候~
![image](https://github.com/kh555069/k8s_celery_rabbit/blob/master/pictures/k8s-start.gif)
按 `Ctrl+C` 退出查看。


執行 `./getdata.sh` 可以看剛剛抓下來的文章

## Note

1. 如果想產生兩個 celery worker 可透過<br></br>
  `kubectl scale replicationcontroller --replicas 2 celery-controller` <br></br>
達到 scale up
![image](https://github.com/kh555069/k8s_celery_rabbit/blob/master/pictures/scale-up.png)<br></br>
或是將 `./kubefile/celery-controller.yaml` 中的 `replicas: 1`  改成 2



2. 刪除本示範<br></br>
執行 `./delete.sh` 即可清空剛剛建立的 pods, services, container...
