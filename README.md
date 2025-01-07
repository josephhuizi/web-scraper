# Domain Data Storage Solution

This solution is designed to store domain data in a BigQuery table using a FastAPI application. The application is divided into several layers to ensure scalability and maintainability.

## Architecture

The solution consists of the following layers:

### Persistence

* This layer contains the BigQuery Client instance, which is used to interact with the BigQuery database.
* The BigQuery Client instance is stored in this layer to make it accessible to the repository layer.

### Repositories

* This layer contains the repositories of the application, which are responsible for encapsulating the data access logic.
* For this solution, only the `postsRepository` is available, which is responsible for storing and retrieving post data from the BigQuery table.

### Models

* This layer contains the models of the application, which are used to improve the consistency between the services responsible for reading data and the store service.
* For now, only the `post` model is available, which represents a post entity.

### Routers

* This layer contains the routers of the application, which are responsible for handling incoming requests and routing them to the corresponding services.
* For now, only the `data_router` is available, which handles requests related to posts.

### Services

* This layer contains the services of the application, which are responsible for injecting data from the web scraper and Whois API into the BigQuery table.
* The services are responsible for completing the process of storing domain data inside the BigQuery table.

## Run Script

The `run_script` file in the root of the project contains instructions on how to use the different services to complete the process of storing domain data inside the BigQuery table.

