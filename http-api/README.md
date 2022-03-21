# HTTP API

This time around we'll create a service similar to paste bin. For this exercise we'll focus on the `backend` of the service. 
In essence [pastebin](https://pastebin.com/) allows you to create pastes (text files pasted from you clipboard) and share them 
with other people via unique links. To recreate this service we'll need to essential functionalities

1. A way to create a new paste
2. A way to get the content of an existing one

In addition we need a way send `HTTP requests` in order to test our `API` - https://www.postman.com/

# Problem 01

To accomplish problem 01 you need to implement the following steps.

1. Create a new http endpoint that can handle `POST` requests (handling post requests is essential because we need to send information
with the request) - `http://localhost:8080/` - https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
2. Extract the text content comming from the `request body`
3. Create a unique name for the paste - https://www.javatpoint.com/python-program-to-generate-a-random-string
4. Store the text content in a local file with that name (remember how to read and write files in python?)
5. Return the generate unique name in the response (this will be used by the user to get the contents of his file when needed)

# Problem 02

To accomplish problem 02 you need to implement the following steps.

1. Create a new http endpoint that can handle `GET` requests (this time we use get requests because we gather data from the server) - `http://localhost:8080/<unique-name>`
2. Extract the `unique-name` from the `self.path` variable
3. Find and read the local file with name `unique-name`
4. Return the content of the file in the body of the response
