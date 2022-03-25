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

> Important: To get around CORS you need to make your server host this HTML file (look at the first code example)

###### example:
```
(When you load a url in the browser it will send a get request to that url and it will display the result)
GET http://localhost:8080/pastes/

Returns: <HTML-file-that-has-a-field-to-create-new-pastes>
``` 

5. A frontend page that allows you to gather paste information using the API endpoint (1)

> Important: To get around CORS you need to make your server host this HTML file (look at the first code example)

###### example:
```
(When you load a url in the browser it will send a get request to that url and it will display the result)
GET http://localhost:8080/pastes/<paste-id>

Returns: <HTML-file-that-has-the-content-of-paste-with-id-paste-id>
``` 

## Code that you can use

### An http server that has one GET request handle and on GET it returns the contents of file called index.html (from the same directory)

```py
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "r") as fd:
            self.wfile.write(bytes(fd.read(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
```

### An http server that knows how to treat requests that are sent to the API and requests that are requesting HTML pages

```py
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path.startswith("/api"):
            # In this case we'll handle api requests
            if self.path == "/api/pastes" or self.path == "/api/pastes/":
                # Implement problem (2.)
                # Find a way to read all pastes and return them in a list
                pass
            elif self.path.startswith("/api/pastes/"):
                # Implement problem (1.)
                # Extract the name of the paste from self.path, find the paste and return its content
                pass
        else:
            # In this case we return HTML files
            if self.path == "/pastes" or self.path == "/pastes/":
                # Implement problem (4.)
                with open("create_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))
            elif self.path.startswith("/pastes/"):
                # Implement problem (5.)
                with open("read_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
```

### An html file that has a field for a user the enter some text and then sends an HTTP POST request to our API (create_paste.html)

```html
<html>
    <head>
        <!-- META info -->
        <script>
            function handleNewPasteClick() {
                const textareaElement = document.getElementById("paste-content")
                const pasteContent = textareaElement.value
                
                console.log("paste contnet: ", pasteContent)
                // send http request to our api with paste content
                submitPaste(pasteContent)
                    .then(() => {
                        cleanup()
                    })
                    .catch((e) => {
                        alert(e)
                    })
            }

            async function submitPaste(pasteContent) {
                if (!pasteContent) {
                    return
                }
                const url = "http://localhost:8080/api/pastes"
                
                return await fetch(url, {
                    method: 'POST', // *GET, POST, PUT, DELETE, etc.
                    mode: 'cors', // no-cors, *cors, same-origin
                    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                    credentials: 'same-origin', // include, *same-origin, omit
                    headers: {
                        'Content-Type': 'application/text'
                    },
                    redirect: 'follow', // manual, *follow, error
                    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                    body: pasteContent
                })
            }

            function cleanup() {
                const textareaElement = document.getElementById("paste-content")
                textareaElement.value = ""
            }
        </script>
    </head>
    <body>
        <textarea class="primary-border half-width" id="paste-content"></textarea>
        <button onclick="handleNewPasteClick()">Create paste</button>
    </body>
</html>
```

### An http server that has a POST request handle that saves the content of the body to a local file

```py
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        with open("request_body.txt", "w") as fd:
            fd.write(post_data.decode('utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
```
