# Backend Engineer Interview

Design and implement an application responsible for managing data access and retrieval from two separate databases, where one contains properties records and another contains MLS listing records, with a one to many relationship between property to MLS listings and `property_id` column in the `mls_listings` table corresponds to the `id` column in the `properties` table. 

The application will be composed of: 

- Python FastAPI based backends for each database, responsible for retrieving data from the database and responding the data back to the request client
- an additional service to validates API keys, logs requests, and coordinates communications 

The system as a whole should be:

- deployed to AWS ECS as containerized services
- contain endpoints to get data on a property, a property plus associated MLS listings records, or MLS listing only records by ID
- log useful usage information to an external database (eg. a new schema in either of the RDS databases) 

AWS account credentials will be provided via email and please use the tag 'external' whenever possible for the services you create. 

In addition, discuss any modifications or alternative services you would use if this application were to be deployed in a real world setting, some ideas may include authentication services/methods, best practices for microservice integration/decomposition, caching, etc.
