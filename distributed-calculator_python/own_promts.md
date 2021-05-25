
**Running the quickstart locally**
cd <working dir>
pip3 install wheel python-dotenv flask_cors flask

sudo dapr run --app-id addapp --app-port 6000 --dapr-http-port 3513 python3 app.py
sudo dapr run --app-id multiplyapp --app-port 5000 --dapr-http-port 3511 python3 app.py
sudo dapr run --app-id divideapp --app-port 4000 --dapr-http-port 3515 python3 app.py
sudo dapr run --app-id multiplyapp --app-port 5000 --dapr-http-port 3518 python3 app.py
sudo dapr run --app-id subtractapp --app-port 7000 --dapr-http-port 3514 python3 app.py
sudo dapr run --app-id sqrtapp --app-port 9000 --dapr-http-port 3519 python3 app.py

npm install
npm install cjs-module
npm run buildclient
dapr run --app-id frontendapp --app-port 8080 --dapr-http-port 3500 node server.js

Open a browser window and go to http://localhost:8080/

**Uploding to the docker**
sudo docker build -t app.py .
sudo docker tag app.py vika1990z/adder_app_python:latest
sudo docker login
sudo docker push vika1990z/adder_app_python:latest

sudo docker tag app.py vika1990z/dividing_app_python:latest
sudo docker push vika1990z/dividing_app_python:latest

sudo docker tag vika1990z/react_app_python:latest
sudo docker push vika1990z/react_app_python:latest

sudo docker tag app.py vika1990z/multiplication_app_python:latest
sudo docker push vika1990z/multiplication_app_python:latest

sudo docker tag app.py vika1990z/substraction_app_python:latest
sudo docker push vika1990z/substraction_app_python:latest

sudo docker tag app.py vika1990z/sqrt_app_python:latest
sudo docker push vika1990z/sqrt_app_python:latest

**Running the quickstart in a Kubernetes environment**
-Access to the cluster
sudo apt update
sudo apt install python3-pip
sudo pip3 install python-openstackclient
sudo pip3 install python-magnumclient
nano openrc
. openrc
openstack coe cluster list
mkdir ~/testc2_cluster
cd ~/testc2_cluster
openstack coe cluster config --dir ~/testc2_cluster/ testc2
export KUBECONFIG=/home/ubuntu/testc2_cluster/config

-Install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client
kubectl get nodes

-Install dapr
wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
dapr init -k

-Create and configure a Redis store
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install redis bitnami/redis
kubectl get pods

-Configure Dapr components
nano redis-state.yaml
nano redis-pubsub.yaml
kubectl apply -f redis-state.yaml
kubectl apply -f redis-pubsub.yaml
kubectl get pods --all-namespaces

-Deploy Application
git clone https://github.com/Vika1990Z/calculator.git
cd calculator/distributed-calculator_python/deploy/
kubectl apply -f appconfig.yaml
kubectl apply -f react-calculator.yaml
kubectl apply -f go-adder.yaml
kubectl apply -f dotnet-subtractor.yaml
kubectl apply -f node-divider.yaml
kubectl apply -f python-multiplier.yaml
kubectl apply -f sqrt.yaml

kubectl port-forward service/calculator-front-end 8000:80
kubectl get svc

