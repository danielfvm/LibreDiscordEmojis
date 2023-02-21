#!/bin/python

from time import sleep
from injector import inject
from distutils.spawn import find_executable
from pynput.keyboard import Controller
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

import logging
import psutil
import sys


keyboard = Controller()

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        data = unquote(self.path)[1:].replace("size=56", "size=48").replace("&quality=lossless", "")

        for key in data:
            keyboard.type(key)
            sleep(0.001)
        keyboard.type('\n')

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body></body>", "utf-8"))

def start_discord():
    logging.basicConfig(level=logging.DEBUG)

    target = find_executable('discord') or find_executable('discord.exe') or sys.argv[1]
    running = 'Discord' in (p.name() for p in psutil.process_iter())

    if running is True:
        print('Please stop discord before starting this script.')
        return

    if target is None:
        print('Could not find discord program, please pass the path to the executable.')
        return

    print('Discord executable found at:', target)
    inject(target, './script.js')

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        start_discord()
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
