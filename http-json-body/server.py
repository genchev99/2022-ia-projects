from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import string

hostName = "localhost"
serverPort = 8080

def random_string(length: int = 10) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))    

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("new_paste.html", "r") as fd:
            self.wfile.write(bytes(fd.read(), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        parsed_body = json.loads(post_data)
        paste_content = parsed_body['paste']
        paste_id = random_string(10)
        paste_path = f"{paste_id}.txt"
        
        files = {}

        with open(paste_path, "w") as fd:
            fd.write(paste_content)

        with open("pastes.json", "r") as pastes_fd:
            files = json.loads(pastes_fd.read())

        files.update({
            paste_id: {
                "title": parsed_body['title'],
                "password": parsed_body['password'],
                "use_password": parsed_body['use_password'],
                "code": parsed_body['code'],
                "burn_after_read": parsed_body['burn_after_read'],
                "path": paste_path,
            }
        })

        with open("pastes.json", "w") as pastes_fd:
            pastes_fd.write(json.dumps(files))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
