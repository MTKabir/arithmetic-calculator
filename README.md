# Basic arithmetic calculator rest api


## Project overview

- Addition, subtraction, multiplication, division, history
- Versioneed rest api
- Layered n-tier architecture
- Unit tests controller, service
- Docker and docker compose


## Architecture Overview

The application follows a layered n-tier architecture with clear separation of concerns and single responsibity of each class:

## APi endpoints 
- http://127.0.0.1:8000/api/calculator/adition
- http://127.0.0.1:8000/api/calculator/substruction
- http://127.0.0.1:8000/api/calculator/multiplication
- http://127.0.0.1:8000/api/calculator/divition
- http://127.0.0.1:8000/api/calculator/history

## Expected requested body
{
  "first_number": first_number,
  "second_number": second_number
}
## Response 
{
    "result": result
}
## History response example 
{
  "history": [
    {
      "operation": "add",
      "first_number": 1,
      "second_number": 2,
      "result": 3
    }
  ]
}

## Testing 
Testing are done for each layer to test all our function are working as intended.
To run all test `poetry run pytest`

## Docker 
RUn and build docker image `docker-compose up --build`

## Api will be available in http://localhost:8000

http://localhost:8000

## Future Improvements

- Authentication and authorization
- Replace in memory storage with a persistent database
- Pagination for history endpoint
- Custom validation and global exception handling
- Cicd  pipeline using GitHub Actions and deploy it to openshift 
- display openshift metrics to grafana to monitor our endpoitns
- do hammer testing to our endpoint with tons of responses and observe the behaviour 
