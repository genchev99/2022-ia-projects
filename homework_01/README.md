# Homework 01

As you may already know last week we were working on our own version of [pastebin](https://pastebin.com/).
The tasks were separated into 2 categories:

1. Create the backend of the application [http-api](../http-api/)
2. Create the UI of the application [http-user-interface](../http-user-interface/)

For this homework you will have to implement 5 key functionalities (part of [http-api](../http-api/) and [http-user-interface](../http-user-interface/))

1. An API endpoint that allows you to get a specific paste

###### example:
```
GET http://localhost:8080/api/pastes/<paste-id>

Returns: <the-content-of-paste-with-id-equal-to-paste-id>
``` 

2. An API endpoint that allows you to get a list of all pastes


###### example:
```
GET http://localhost:8080/api/pastes/

Returns: <a-list-of-all-the-pastes>
``` 

3. An API endpoint that allows you to create a new paste


###### example:
```
POST http://localhost:8080/api/pastes/

Returns: None
``` 

4. A frontend page that allows you to create a new post using the API endpoint (3)

###### example:
```
(When you load a url in the browser it will send a get request to that url and it will display the result)
GET http://localhost:8080/pastes/

Returns: <HTML-file-that-has-a-field-to-create-new-pastes>
``` 

5. A frontend page that allows you to gather paste information using the API endpoint (1)


###### example:
```
(When you load a url in the browser it will send a get request to that url and it will display the result)
GET http://localhost:8080/pastes/<paste-id>

Returns: <HTML-file-that-has-the-content-of-paste-with-id-paste-id>
``` 
