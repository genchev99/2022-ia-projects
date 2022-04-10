import json
import random
import socketserver
import string

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


def random_string(length: int = 10) -> str:
    """
    Returns a random string with length
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


class MyServer(BaseHTTPRequestHandler):
    def __init__(self, request: bytes, client_address, server: socketserver.BaseServer):
        pastes_fd = open("pastes.json", "r")
        # Reads the pastes json file and loads it into a dict
        self.pastes = json.load(pastes_fd)
        pastes_fd.close()
        super().__init__(request, client_address, server)

    def _sync_pastes_file(self):
        with open("pastes.json", "w") as pastes_fd:
            # Writes the pastes object to a local file
            json.dump(self.pastes, pastes_fd, indent=2)

    def do_GET(self):
        """
        Handles get requests
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path.startswith("/api"):
            # In this case we'll handle api requests
            if self.path == "/api/pastes" or self.path == "/api/pastes/":
                self.wfile.write(bytes(json.dumps(self.pastes), "utf-8"))
            elif self.path.startswith("/api/pastes/"):
                # "/api/pastes/238e78321" -> after split -> ["", "api", "pastes", "238e78321"]
                paste_id = self.path.split("/")[3]

                # TODO: return the full information about a paste with id paste_id and the paste itself
                response = {
                    "content": "REPLACE",
                    "title": "REPLACE",
                    "path": "REPLACE",
                    "password": "REPLACE",
                    "use_password": "REPLACE",
                    "code": "REPLACE",
                    "burn_after_read": "REPLACE",
                }

                # Return the response
                self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            # In this case we return HTML files
            if self.path.startswith("/pastes/"):
                with open("./public/preview_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))
            else:
                with open("./public/create_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))

    def do_POST(self):
        """
        Handles post requests
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        parsed_body = json.loads(post_data)
        paste_content = parsed_body['paste']
        paste_id = random_string(10)
        paste_path = f"./pastes/{paste_id}.txt"

        with open(paste_path, "w") as fd:
            fd.write(paste_content)

        # updates the pastes dictionary
        self.pastes.update({
            paste_id: {
                "title": parsed_body['title'],
                "path": paste_path,
                "password": parsed_body['password'],
                "use_password": parsed_body['use_password'],
                "code": parsed_body['code'],
                "burn_after_read": parsed_body['burn_after_read'],
            }
        })

        self._sync_pastes_file()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
