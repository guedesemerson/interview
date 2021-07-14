# External Engineer Interview

We would like you to push the bounds of your knowledge and create an AWS based application using novel technologies. AWS account credentials will be provided via email and please use the tag 'external' whenever possible for the services you create. 

The final submission should be:

- achieve the objectives described below
- deployed to the AWS environment provided
- documented (via README and code comments) describing the approach and outcome such that another developer could effectively test the application without additional guidence

## Objective

Using the provided database tables, aws account, and object please accomplish the following tasks:

1. Using IPython/Jupyter notebook:
   - Join the provided datasets containing properties in the US based on common attributes. Note you might need to do some manipulation and fuzzy matching to accomplish the highest match rates.
   - Store the integrated dataset in a SQL table. 
   - Document your thought process on identifying ways to join the dataset (common formatting/structure/fields between the datasets, fuzzy matching, etc.) and how many properties were match between the datasets
2. Using AWS AppSync GraphQL endpoints w/ Lambda resolvers to fetch data from the table, including endpoints to:
   - List of all property IDs
   - Fetch a property record via ID
3. Create a Python script that:
   - Fetches data from the GraphQL endpoint you created
   - Summarizes various metrics from the properties dataset (eg. average and median estimated values, frequencies by bedroom)
   - Save the output summary to a S3 bucket
   - Create a Docker image which will execute the script

Additional, discuss:

- Areas that need to be further considered for the application to be used in a real world setting
- Other open sources tools/libraries that you are curious about and would like to integrate into the application to enhance its features and reliability

Some ideas may (or may not) include:

- How the data component would change as amount of data and variety of errors increase?
- Dev ops and security considerations
- Or, any topics that peaks your interest :)
