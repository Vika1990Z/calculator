
**Running the quickstart locally**
cd <working dir>
go get -u github.com/gorilla/mux
go build app.go
dapr run --app-id addapp --app-port 6000 --dapr-http-port 3503 ./app

-----
dapr run --app-id divideapp --app-port 4000 --dapr-http-port 3505 ./app
dapr run --app-id multiplyapp --app-port 5000 --dapr-http-port 3508 ./app
dapr run --app-id subtractapp --app-port 7000 --dapr-http-port 3504 ./app
dapr run --app-id sqrtapp --app-port 9000 --dapr-http-port 3509 ./app

npm install
npm install cjs-module
npm run buildclient
dapr run --app-id frontendapp --app-port 8080 --dapr-http-port 3500 node server.js

Open a browser window and go to http://localhost:8080/

**Running the quickstart in a Kubernetes environment**
-Access to the cluster

sudo apt install docker-ce
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl restart docker
sudo systemctl status docker
sudo chmod 666 /var/run/docker.sock
docker login

dapr init -k
kubectl apply -f redis-state.yaml
kubectl apply -f redis-pubsub.yaml

git clone https://github.com/Vika1990Z/calculator.git
cd deploy
kubectl apply -f appconfig.yaml
kubectl apply -f react-calculator.yaml
kubectl apply -f go-adder.yaml
kubectl apply -f dotnet-subtractor.yaml
kubectl apply -f node-divider.yaml
kubectl apply -f python-multiplier.yaml
kubectl apply -f sqrt.yaml

kubectl port-forward service/calculator-front-end 8000:80
kubectl get svc

