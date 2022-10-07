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
    print("LED is turned", "ON" if LED_STATE_ON else "OFF")

PAGE="""\
<html>
<head>
<title>ULUG Yocto Demo</title>
<script>
function on() {
document.getElementById("state").innerText = "ON";
fetch("/on");
}
function off() {
document.getElementById("state").innerText = "OFF";
fetch("/off");
}
</script>
</head>
<body>
<h1>ULUG Yocto Demo</h1>
<table><tr>
<td>LED is:</td> <td id="state" style="font-weight: bold">{LED_STATE_PLACEHOLDER}</td>
</tr>
<table>
<p> Turn LED:
<button onclick="on()" type="button">On</button>
<button onclick="off()" type="button">Off</button>
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

        if self.path=='/on':
            LED_STATE_ON=True
            update_led_output()
        elif self.path=='/off':
            LED_STATE_ON=False
            update_led_output()
        else:
            content = PAGE.replace('{LED_STATE_PLACEHOLDER}', 'ON' if LED_STATE_ON else 'OFF').encode('utf-8')
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
