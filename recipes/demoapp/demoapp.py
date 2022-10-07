#!/usr/bin/env python3

import RPi.GPIO as GPIO
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

LED_STATE_ON = False
LED_PIN=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)

def update_led_output():
    GPIO.output(LED_PIN, 0 if LED_STATE_ON else 1)

PAGE="""\
<html>
<head>
<title>ULUG Yocto Demo</title>
</head>
<body>
<h1>ULUG Yocto Demo</h1>
<p> LED is: <b>{}</b> </p>
<p> Turn LED:
<button onclick="location.href='/on'" type="button">On</button>
&nbsp
<button onclick="location.href='/off'" type="button">Off</button>
</p>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        global LED_STATE_ON

        self.do_HEAD()

        if self.path=='/':
            pass
        elif self.path=='/on':
            LED_STATE_ON=True
        elif self.path=='/off':
            LED_STATE_ON=False
        update_led_output()

        content = PAGE.format('ON' if LED_STATE_ON else 'OFF',
                              'ON' if LED_STATE_ON else 'OFF').encode('utf-8')
        self.wfile.write(content)

class MyServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    update_led_output()

    address = ('', 8000)
    server = MyServer(address, MyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

    GPIO.cleanup()
