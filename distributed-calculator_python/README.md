# Distributed calculator

This quickstart shows method invocation and state persistent capabilities of Dapr through a distributed calculator where each operation is powered by a different service written in a go-lang:

- **Addition**;
- **Multiplication**;
- **Division**;
- **Subtraction**;
- **Square root**;

The front-end application consists of a server and a client written in [React](https://reactjs.org/). 
Kudos to [ahfarmer](https://github.com/ahfarmer) whose [React calculator](https://github.com/ahfarmer/calculator) 

The following architecture diagram illustrates the components that make up this quickstart: 

![Architecture Diagram](./img/Architecture_Diagram.png)

## Prerequisites for running the quickstart
Clone the quickstarts repository
   ```bash
   git clone [-b <dapr_version_tag>] https://github.com/dapr/quickstarts.git
   ```
> **Note**: See https://github.com/dapr/quickstarts#supported-dapr-runtime-version for supported tags. Use `git clone https://github.com/dapr/quickstarts.git` when using the edge version of dapr runtime.

### - Run locally
1. Install [Docker](https://www.docker.com/products/docker-desktop)
2. Install [.Net Core SDK 3.1](https://dotnet.microsoft.com/download)
3. Install [Dapr CLI](https://github.com/dapr/cli)
4. Install [Go](https://golang.org/doc/install)
5. Install [Python3](https://www.python.org/downloads/)
6. Install [Npm](https://www.npmjs.com/get-npm)
7. Install [Node](https://nodejs.org/en/download/)

### - Run in Kubernetes environment
1. Dapr-enabled Kubernetes cluster. Follow [these instructions](https://docs.dapr.io/getting-started/install-dapr/#install-dapr-on-a-kubernetes-cluster) to set this up.


## Running the quickstart locally

These instructions start the four calculator operator apps (add, subtract, multiply and divide) along with the dapr sidecar locally and then run the front end app which persists the state in a local redis state store.


1. Add App - Open a terminal window and navigate to the add_go directory and follow the steps below:
- Install required packages
   ```bash
   pip3 install wheel python-dotenv flask_cors flask
   ```

- Start dapr using the command:
   ```bash
   sudo dapr run --app-id addapp --app-port 6000 --dapr-http-port 3513 python3 app.py
   ```   

2. Subtract App - Open a terminal window and navigate to the subtract_csharp directory and follow the steps below:
- Start dapr using the command:
   ```bash
   sudo dapr run --app-id subtractapp --app-port 7000 --dapr-http-port 3514 python3 app.py
   ```   

3. Divide App - Open a terminal window and navigate to the divide_node directory and follow the steps below:
- Start dapr using the command:
   ```bash
   sudo dapr run --app-id divideapp --app-port 4000 --dapr-http-port 3515 python3 app.py
   ```  

4. Multiply App - Open a terminal window and navigate to the multiply_python directory and follow the steps below:
- Start dapr using the command:
   ```bash
   sudo dapr run --app-id multiplyapp --app-port 5000 --dapr-http-port 3511 python3 app.py
   ```

4. Sqrt App - Open a terminal window and navigate to the sqrt directory and follow the steps below:
- Start dapr using the command:
   ```bash
   sudo dapr run --app-id sqrtapp --app-port 9000 --dapr-http-port 3519 python3 app.py
   ```

6. Frontend Calculator app - Open a terminal window and navigate to the react-calculator directory and follow the steps below:

- Install the required modules
   ```bash
   npm install
   npm run buildclient
   ```

- Start Dapr using command below:
   ```bash
   sudo dapr run --app-id frontendapp --app-port 8080 --dapr-http-port 3500 node server.js
   ```

7. Open a browser window and go to http://localhost:8080/. From here, you can enter the different operations.

    ![Calculator Screenshot](./img/calculator-screenshot2.png)

7. Open your browser's console window (using F12 key) to see the logs produced as you use the calculator. Note that each time you click a button, you see logs that indicate state persistence and the different apps that are contacted to perform the operation. 

8. **Optional:** Curl Validate

- To make sure all the apps are working, you can run the following curl commands which will test all the operations:
   ```bash
   curl -w "\n" -s 'http://localhost:8080/calculate/add' -H 'Content-Type: application/json' --data '{"operandOne":"56","operandTwo":"3"}'
   curl -w "\n" -s 'http://localhost:8080/calculate/subtract' -H 'Content-Type: application/json' --data '{"operandOne":"52","operandTwo":"34"}'
   curl -w "\n" -s 'http://localhost:8080/calculate/divide' -H 'Content-Type: application/json' --data '{"operandOne":"144","operandTwo":"12"}'
   curl -w "\n" -s 'http://localhost:8080/calculate/multiply' -H 'Content-Type: application/json' --data '{"operandOne":"52","operandTwo":"34"}'
   curl -w "\n" -s 'http://localhost:8080/persist' -H 'Content-Type: application/json' --data '[{"key":"calculatorState","value":{"total":"54","next":null,"operation":null}}]'
   curl -s 'http://localhost:8080/state' | jq '.total'
   ```

- You should get the following output:
   ```bash
   59
   18
   12
   1768.0
   
   "54"
   ```

9. Cleanup

- Cleanup microservices

   ```bash
   dapr stop --app-id addapp
   dapr stop --app-id subtractapp
   dapr stop --app-id divideapp
   dapr stop --app-id multiplyapp
   dapr stop --app-id frontendapp
   ```

- Uninstall node modules by navigating to the node directory and run:
  ```
  npm uninstall
  ```

## Running the quickstart in a Kubernetes environment
1. Navigate to the deploy directory in this quickstart directory: `cd deploy`
   > **Note**: `appconfig.yaml` is not used directly for this quickstart but is present for the [observability quickstart](../observability).
2. Follow [these instructions](https://docs.dapr.io/getting-started/configure-redis/) to create and configure a Redis store
3. Deploy all of your resources: 

```bash 
kubectl apply -f .
``` 

  > **Note**: Services could also be deployed one-by-one by specifying the .yaml file: `kubectl apply -f go-adder.yaml`.

Each of the services will spin up a pod with two containers: one for your service and one for the Dapr sidecar. It will also configure a service for each sidecar and an external IP for the front-end, which allows us to connect to it externally.

4. Kubernetes deployments are asyncronous. This means you'll need to wait for the deployment to complete before moving on to the next steps. You can do so with the following commands:

```bash
kubectl rollout status deploy/addapp
kubectl rollout status deploy/subtractapp
kubectl rollout status deploy/divideapp
kubectl rollout status deploy/multiplyapp
kubectl rollout status deploy/calculator-front-end
```


You can view the status of the running pods with:

```bash
kubectl get pods
```

When everything is running properly, you'll see output like this:

```
NAME                                    READY   STATUS    RESTARTS   AGE
addapp-5ff9586df6-5bpll                 2/2     Running   0          16s
calculator-front-end-56dc959b58-bb8vw   2/2     Running   0          16s
divideapp-c64f744d6-wljcc               2/2     Running   0          16s
multiplyapp-6989454d77-tkd6c            2/2     Running   0          16s
subtractapp-869b74f676-9mw94            2/2     Running   0          16s
```

5. Next, setup access to your service

There are several different ways to access a Kubernetes service depending on which platform you are using. Port forwarding is one consistent way to access a service, whether it is hosted locally or on a cloud Kubernetes provider like AKS.


```bash
kubectl port-forward service/calculator-front-end 8000:80
```

This will make your service available on http://localhost:8000. Navigate to this address with your browser and voilà! You have a working distributed calculator!

> **Optional**: If you are using a public cloud provider, you can substitue your EXTERNAL-IP address instead of port forwarding. You can find it with:

```bash 
kubectl get svc
```

```bash
NAME                          TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)            AGE
dapr-api                      ClusterIP      10.103.71.22   <none>          80/TCP             135m
dapr-placement                ClusterIP      10.103.53.127  <none>          80/TCP             135m
dapr-sidecar-injector         ClusterIP      10.104.220.35  <none>          443/TCP            135m
addapp-dapr                   ClusterIP      10.0.1.170     <none>          80/TCP,50001/TCP   2m
calculator-front-end          LoadBalancer   10.0.155.131   40.80.152.125   80:32633/TCP       3m
calculator-front-end-dapr     ClusterIP      10.0.230.219   <none>          80/TCP,50001/TCP   3m
divideapp-dapr                ClusterIP      10.0.240.3     <none>          80/TCP,50001/TCP   1m
kubernetes                    ClusterIP      10.0.0.1       <none>          443/TCP            33d
multiplyapp-dapr              ClusterIP      10.0.217.211   <none>          80/TCP,50001/TCP   1m
subtractapp-dapr              ClusterIP      10.0.146.253   <none>          80/TCP,50001/TCP   2m
```

Each service ending in "-dapr" represents your services respective sidecars, while the `calculator-front-end` service represents the external load balancer for the React calculator front-end.


![Calculator Screenshot](./img/calculator-screenshot2.png)

6. Open your browser's console window (using F12 key) to see the logs produced as you use the calculator. Note that each time you click a button, you see logs that indicate state persistence: 

```js
Persisting State:
{total: "21", next: "2", operation: "x"}
```

`total`, `next`, and `operation` reflect the three pieces of state a calculator needs to operate. The app persists these to a Redis store (see [Simplified State Management](#simplified-state-management) section below). By persisting these, you can refresh the page or take down the front-end pod and still jump right back where you were. Try it! Enter something into the calculator and refresh the page. The calculator should have retained the state, and the console should read: 

```js
Rehydrating State:
{total: "21", next: "2", operation: "x"}
```

Also note that each time you enter a full equation (e.g. "126 ÷ 3 =") the logs indicate that a call is made to the service: 

```js
Calling divide service
```

The client code calls to an Express server, which routes the calls through Dapr to the back-end services. In this case the divide endpoint is called on the nodejs application.

7. **Optional:** If your environment doesn't have easy access to a browser, or you just like using curl


Then you can use the following curl commands to make sure each one of the microservies is working:

```bash 
curl -w "\n" -s 'http://localhost:8000/calculate/add' -H 'Content-Type: application/json' --data '{"operandOne":"56","operandTwo":"3"}'
curl -w "\n" -s 'http://localhost:8000/calculate/subtract' -H 'Content-Type: application/json' --data '{"operandOne":"52","operandTwo":"34"}'
curl -w "\n" -s 'http://localhost:8000/calculate/divide' -H 'Content-Type: application/json' --data '{"operandOne":"144","operandTwo":"12"}'
curl -w "\n" -s 'http://localhost:8000/calculate/multiply' -H 'Content-Type: application/json' --data '{"operandOne":"52","operandTwo":"34"}'
curl -w "\n" -s 'http://localhost:8000/persist' -H 'Content-Type: application/json' --data '[{"key":"calculatorState","value":{"total":"54","next":null,"operation":null}}]'
curl -s 'http://localhost:8000/state' | jq '.total'
```

You should get the following output:

   ```bash
   59
   18
   12
   1768.0
   
   "54"
   ```

## Cleanup

### Kubernetes environment cleanup
- Once you're done, you can spin down your Kubernetes resources by navigating to the `./deploy` directory and running:

  ```bash
  kubectl delete -f .
  ```

This will spin down each resource defined by the .yaml files in the `deploy` directory, including the state component.

## The Role of Dapr

This quickstart demonstrates how to use Dapr as a programming model for simplifying the development of distributed systems. In this quickstart, Dapr is enabling polyglot programming, service discovery and simplified state management.

### Polyglot programming

Each service in this quickstart is written in a different programming language, but they're used together in the same larger application. Dapr itself is language agnostic - none of the services have to include any dependency in order to work with Dapr. This empowers developers to build each service however they want, using the best language for the job or for a particular dev team.

### Service invocation

When the front-end server calls the respective operation services (see `server.js` code below), it doesn't need to know what IP address they live at or how they were built. Instead it calls their local dapr side-car by name, which knows how to invoke the method on the service, taking advantage of the platform’s service discovery mechanism, in this case Kubernetes DNS resolution.

The code below shows calls to the “add” and “subtract” services via the Dapr URLs:
```js
const daprUrl = `http://localhost:${daprPort}/v1.0/invoke`;

app.post('/calculate/add', async (req, res) => {
  const addUrl = `${daprUrl}/addapp/method/add`;
  req.pipe(request(addUrl)).pipe(res);
});

app.post('/calculate/subtract', async (req, res) => {
  const subtractUrl = `${daprUrl}/subtractapp/method/subtract`;
  req.pipe(request(subtractUrl)).pipe(res);
});
...
```

Microservice applications are dynamic with scaling, updates and failures causing services to change their network endpoints. Dapr enables you to call service endpoints with a consistent URL syntax, utilizing the hosting platform’s service discovery capabilities to resolve the endpoint location.

Learn more about Dapr [service invocation](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/).

### Simplified state management

Dapr sidecars provide [state management](https://docs.dapr.io/developing-applications/building-blocks/state-management/). In this quickstart, the calculator's state is persisted each time a new button is clicked. This means a user can refresh the page, close the page or even take down the `calculator-front-end` pod, and still retain the same state when they next open it. Dapr adds a layer of indirection so that the app doesn't need to know where it's persisting state. It doesn't have to keep track of keys, handle retry logic or worry about state provider specific configuration. All it has to do is GET or POST against its Dapr sidecar's state endpoint: `http://localhost:3500/v1.0/state/${stateStoreName}`.

Take a look at `server.js` in the `react-calculator` directory. Note that it exposes two state endpoints for the React client to get and set state: the GET `/state` endpoint and the POST `/persist` endpoint. Both forward client calls to the Dapr state endpoint: 

```js
const stateUrl = `http://localhost:${daprPort}/v1.0/state/${stateStoreName}`;
```

Our client persists state by simply POSTing JSON key-value pairs (see `react-calculator/client/src/component/App.js`): 

```js
    const state = [{ 
      key: "calculatorState", 
      value 
    }];
    
    fetch("/persist", {
      method: "POST",
      body: JSON.stringify(state),
      headers: {
        "Content-Type": "application/json"
      }
    });
```

## Next Steps

- Explore additional [quickstarts](../README.md#quickstarts).