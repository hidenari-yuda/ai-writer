from http.server import BaseHTTPRequestHandler, HTTPServer
from config.config import load_env
from usecase.trasnlate import Translate

# load env variables
load_env()

translate = Translate()
str = translate.translate_to_japanese("this is a pen")
print(str)

# class routers(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("User-Agent", "test1")
#         self.end_headers()
#         html = "abc"
#         self.wfile.write(html.encode())

#     def do_POST(self):
#         self.send_response(200)
#         self.send_header("User-Agent", "test1")
#         self.end_headers()
#         html = "abc"
#         self.wfile.write(html.encode())


#     def do_PUT(self):
#         self.send_response(200)
#         self.send_header("User-Agent", "test1")
#         self.end_headers()
#         html = "abc"
#         self.wfile.write(html.encode())

#     def do_DELETE(self):
#         self.send_response(200)
#         self.send_header("User-Agent", "test1")
#         self.end_headers()
#         html = "abc"
#         self.wfile.write(html.encode())


# ip = "127.0.0.1"
# port = 8000

# httpd = HTTPServer((ip, port), routers)
# httpd.serve_forever()