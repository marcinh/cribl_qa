## Project with tests for sample app consiting of 4 instances
#### Apps are deployed using docker with dedicated dockerfiles 
#### Functional tests are written in python 

### Prerequisites:
* docker
* python 3.9

In order to run tests outside CI/CD

```bash
docker compose up

pip install --no-cache-dir -r tests/requirements.txt

pytest tests
```

