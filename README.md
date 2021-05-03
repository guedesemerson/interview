# Full Stack Interview

We would like you to push your known knowledge bounds and attempt to create a simple "full-stack" application using novel technologies.

We request that your final submission is clearly documented (eg. markdown, code comments, etc.) and can be deployed via Docker Compose or similar methods.

## Objective

Create a containerized application that performs in the following areas:

1. Data management:

   - Validate the raw data provided for formatting, structure, and common fields
   - Link the datasets by key attributes to create an integrated dataset.
   - Store the integrated dataset in a common data model/data warehouse

2. Web application backend using Python's [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart) library

3. Front-end visualization tool that can:

   - Display the integrated dataset as a map (e.g., [leaflet](https://leafletjs.com/), [Mapbox](https://www.mapbox.com/))
   - Provide interactive features to display the attributes (beyond the spatial location) of the data points on-click

Additional, discuss:

- Areas that need to be further considered for the application to be used in a real world setting
- Other open sources tools/libraries that you are curious about and would like to integrate into the application to enhance its features and reliability

Some ideas may (or may not) include:

- How the data component would change as amount of data and variety of errors increase?
- Dev ops and security considerations
- Merits of different frameworks and design philosophies (serverless vs non serverless, React vs. Vue vs. others, different backend languages, etc.)
- Or, any topics that peaks your interest :)
