import multiprocessing
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from . import playlocalsound as pls

class HandleSongRequest():
    def __init__(self):
        self.body = ""

    def playSong(filename):
        # strip the qoutes
        filename = filename.strip("\"")
        filename = filename.strip("%22")
        playProcess = multiprocessing.Process(target=pls.playLocalFileSystem, args=[filename])
        playProcess.start()
        playProcess.join()
        # print(f"Playing song: {filename}")
    def playSongPyDub(filename):
        filename = filename.strip("\"")
        filename = filename.strip("%22")
        playProcess = multiprocessing.Process(target=pls.playLocalFilePyDub, args=[filename])
        playProcess.start()
        playProcess.join()


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        decoded_data = post_data.decode('utf-8')
        # if it is : seperated:
        if ":" in decoded_data:
            req_list = decoded_data.split(':')
        # If it is = seperated
        if "=" in decoded_data:
            req_list = decoded_data.split('=')
        print(f"post-DATA : : : {req_list[1]}")
        HandleSongRequest.playSongPyDub(req_list[1])
        print(f"post-DATA : : : {self.rfile}")
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()