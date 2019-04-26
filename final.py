# tor/browser packages
import io
import pycurl
from bs4 import BeautifulSoup
import stem.process
from stem.util import term
import socks  # SocksiPy module
import socket
import urllib
import requests
from time import sleep 

# server packages
from flask import Flask, Response, jsonify, render_template
from flask_restful import Api, Resource, reqparse

# Tor searches
session = requests.session()
SOCKS_PORT = 7000

# Set socks proxy with respect to local host
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
socket.socket = socks.socksocket

# Perform DNS resolution through the socket
def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

# Start an instance of Tor configured to only exit through the US (can specify certain countries in the 'ExitNodes'
# field of the config dictionary). This prints Tor's bootstrap information as it starts. 
# Note that this likely will not work if you have another Tor instance running.

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))

print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
    config = {
        'SocksPort': str(SOCKS_PORT),
        'ExitNodes': '{us}',
    },
    init_msg_handler = print_bootstrap_lines,
)

new_headers = {
    # 'cookie': '<INSERT COOKIE HEADER HERE>
    # 'x-client-data': <INSERT X-CLIENT-DATA HEADER HERE>,
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'content-type': 'text/plain;charset=UTF-8',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0'
}


ddg_headers = {
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
  'content-type': 'text/plain;charset=UTF-8',
  'accept-language': 'en-US,en;q=0.9',
  'content-length': '0'
}

print('PRINTING HEADERS OUTSIDE OF API')
r = session.get('http://httpbin.org/headers', headers=new_headers)
print(r.text)

print('PRINTING IP OUTSIDE OF API')
r = session.get('http://httpbin.org/ip')
print(r.text)

ip_addr = r.text # for later use to send to front end

# server code
app = Flask(__name__)
api = Api(app)

# gets top 10 results from DuckDuckGo, and the a page's worth of results from Google
# uses template rendering to pass data to a frontend webpage
@app.route('/search/<query>')
def search(query):
    ddg_params = {
        'q':query,
    }
    r = session.get('https://duckduckgo.com/html/', params=ddg_params, headers=ddg_headers)
    content = r.text

    soup = BeautifulSoup(content, "html.parser")
    samples = soup.find_all(class_="result__title")[:10]
    ret_val = []

    for elem in samples:
        ret_val.append(elem.text.strip())

    r = session.get('https://www.google.com/search', params=ddg_params, headers=new_headers)
    content = r.text    

    soup = BeautifulSoup(content, "html.parser")
    samples = soup.find_all(class_="LC20lb")
    google_val = []

    for elem in samples:
        google_val.append(elem.text)

    return render_template('index.html', 
        google_results = google_val,
        ddg_results = ret_val,
        ip_addr = ip_addr
    )

@app.route('/exit')
def exit():
    tor_process.kill()  # stops tor
    return "Shutting down Tor processes", 200

# if debug=True, the server will automatically restart during initialization, which
# leads to a reinitialization of the tor_process, which then leads to a 
# socket/port error
app.run(debug=False)