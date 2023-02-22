#!/bin/python

from time import sleep
from injector import inject
from distutils.spawn import find_executable
from pynput.keyboard import Controller
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
from threading import Thread

import subprocess
import logging
import psutil
import sys

hostName = "localhost"
serverPort = 8080

logger = logging.getLogger(__name__)
keyboard = Controller()

class KeyboardServer(BaseHTTPRequestHandler):
    def do_GET(self):
        data = unquote(self.path)[1:].replace("size=56", "size=48").replace("&quality=lossless", "")

        # write url into chatbox and send it
        for key in data:
            keyboard.type(key)
            sleep(0.001)
        keyboard.type('\n')

        self.send_response(200)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    target = find_executable('discord') or find_executable('discord.exe') or sys.argv[1]
    print('Discord executable found at:', target)

    if target is None:
        print('Could not find discord program, please pass the path to the executable.')
        exit(0)

    # check if discord is already running
    running = 'Discord' in (p.name() for p in psutil.process_iter())

    if running is True:
        subprocess.Popen(target, shell=True)
        exit(0)

    # start discord with injecting script
    try:
        proc = inject(target, './script.js').proc

        # Start server
        webServer = HTTPServer((hostName, serverPort), KeyboardServer)
        print("Server started http://%s:%s" % (hostName, serverPort))
        server_thread = Thread(target=webServer.serve_forever, args=())
        server_thread.start()

        # Wait until discord stops
        while proc.poll() is None:
            sleep(1)

    except KeyboardInterrupt:
        pass

    webServer.shutdown()
