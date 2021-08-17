# Backend Engineer Interview

Design and implement an application responsible for managing data access and retrieval from two separate databases, where one contains properties records and another contains MLS listing records, with a one to many relationship between property to MLS listings and `property_id` column in the `mls_listings` table corresponds to the `id` column in the `properties` table. 

The application will be composed of three Python FastAPI services where: 

- two of them are connected to their respective databases and will be responsible for retrieving and responding the data between client and databases
- and, an additional third service to validates API keys, logs requests, and coordinates communications - this is also the service that will manage the endpoints for the client to interact with the application as a whole

The system as a whole should be:

- deployed to AWS ECS as containerized services
- provide a single set of endpoints (from the third service) to serve the users with data on a property, a property plus associated MLS listings records, and MLS listing only records by ID (ie. the three services should be meshed together)
- authenticate via API Key
- log useful usage information to additional tables either one of the RDS databases provided (eg, API key used, timestamp,and quanity/endpoint)

AWS account credentials will be provided via email and please use the tag 'external' whenever possible for the services you create. Please create all services in us-west-1 this where the credentials will have all permissions restricted to. The database user credentials will allow to make modifications to the two RDS instances provided. 

In addition, discuss any modifications or alternative services you would use if this application were to be deployed in a real world setting, some ideas may include authentication services/methods, best practices for microservice integration/decomposition, caching, etc.
