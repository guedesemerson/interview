# External Engineer Interview

We would like you to push your known knowledge bounds and attempt to create a simple AWS based application using novel technologies.

We request that your final submission is clearly documented (eg. markdown, code comments, etc.) and is actively deployed on the dev AWS environment we provide you.

username: provided via email
   - please keep this information secret
pwd: proivded via email 
   -please keep this information secret 
user-sercret: provided via email
   -please keep this information secret
aws regions: us-east-1
   -please place all applicable aws output in this region and add tag "external" to all services you create. 
account: propstream-dev

Please submit all code as a pull request to this repo. Also, create a seperate readme file documenting your approach and outcome with enough details a 3rd-party could effectively test your deployed applications without additional guidence. 

## Objective

Using the provided database tables, aws account, and object please accomplish the following tasks:

Using AWS services: 
Server-side:
   1. Data management:
   - You are provided two data table containing properities in the USA. Please link these table based on common attributes. Note you might need to do some manipulation and fuzzy matching to accomplish the highest match rates. 
      - Validate the raw data provided for formatting, structure, and common fields. 
      - Link the datasets by key attributes to create an integrated dataset.
      - Store the integrated dataset in a common data model/data warehouse.
   2. Setup a simple lambda function to query the linked table through an AWS appsync graphql point. 

Client-side: 
   1. Create a python application that make a request to the graphql endpoint you created and summarizes metrics on the merged dataset. 
      - Package this python application into a docker container and deploy it as an aws ECS containerized application. 
   2. Save the output summary to an S3 bucket you create in a json format.
      - summary measure can include, but are not limited to, number of matched properties, average and median estimated values, frequencies by bedroom. 


Additional, discuss:

- Areas that need to be further considered for the application to be used in a real world setting
- Other open sources tools/libraries that you are curious about and would like to integrate into the application to enhance its features and reliability

Some ideas may (or may not) include:

- How the data component would change as amount of data and variety of errors increase?
- Dev ops and security considerations
- Or, any topics that peaks your interest :)
