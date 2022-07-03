import socketserver
from http.server import BaseHTTPRequestHandler
import time
import threading
from main import get_page, get_query_params

def some_function():
    print('test')


class MyTCPServer(socketserver.TCPServer):
    def server_bind(self):
        import socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = ''
        if '/get_page' in self.path:
            url = get_query_params(self.path)['url'][0]
            response = get_page(url)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            print(self.wfile)
            self.wfile.write(response)
        if self.path.startswith('/kill_server'):
            print("Server is going down, run it again manually!")

            def kill_me_please(server):
                server.shutdown()
            threading.Thread(target=kill_me_please, args=(httpd,),).start()
            self.send_error(500)





# httpd = socketserver.TCPServer(("", 8080), MyHandler)
# httpd.shutdown()

server_address = ('', 8000)
httpd = MyTCPServer(server_address, MyHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    httpd.server_close()
httpd.server_close()