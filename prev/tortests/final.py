# tor/browser stuff
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

# server stuff
from flask import Flask, Response, jsonify, render_template
from flask_restful import Api, Resource, reqparse

# Tor searches
session = requests.session()

SOCKS_PORT = 7000

# Set socks proxy and wrap the urllib module

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
socket.socket = socks.socksocket

# Perform DNS resolution through the socket

def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo


# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.

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
    'cookie': 'ANID=AHWqTUn95ISuwnZpW4yc_7Us_mrVyKXquO_NoLf51CML9NF1Tjal5HMlXwC7ylbR; SID=VgfRIossKfKDMtliWOffqv0f8v2P3-q2GFy28yWvUP_Q6UpxJvOCz9Hjw0GRmmHSwA7tGg.; HSID=AEYSSV5TKu2yttYQe; SSID=A1fN-ZlYt1orl_8lj; APISID=0Hux_fPcVPDg5XZv/AGRW-QnPZsMClW2UL; SAPISID=GzIWigexS_D7_NR0/AE6bq0GbXVCl9ErBX; CONSENT=YES+US.en+20161213-01-0; NID=181=wpliWgjEbH5Fdsn8rZxR14StlzVdjRdAXf2p4bOXrkrgMI2Jl-TiSwmy0SVpbNXRVXTFsn5hXi8dThbwouwWYKTJK5Ih_y1olVCvWoiATKJKe_5AghBKGxiCBlVVwoXmcVCa2tk4BGuiF4DCrJ6wZI0EQAOl9OHTu_VsRVuNAXW03NtCEStaTqKXhQnC2Hh0sNlB4_IedlEbW35i; 1P_JAR=2019-4-23-3; DV=o1Nbl6B8jsZRELXrd6iumDQIQaWCpNYGGjFTFCYbPQAAAOB85pD-5LPtOQAAAOwZ_awmB2dqGAAAAAKrLPZJ7nerCgAAAA; SIDCC=AN0-TYsIc9ao8HSl8ErVpCFrEf0JYQbOHu-ttenPp8mfKx-rY-Z6GPOJqgW0snerz0czS1As5w',
    'x-client-data': 'CIu2yQEIprbJAQipncoBCKijygEI4qjKAQ==',
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

ip_addr = r.text

# server code

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/google/<query>')
def google(query):
    params={
        'q': 'weather'
    }

    print('GETTING URL CONTENT')
    r = session.get('https://www.google.com/search', params=params, headers=new_headers)
    # r = session.get('https://www.google.com/', headers = new_headers)
    content = r.text    
    # print(content)

    soup = BeautifulSoup(content, "html.parser")
    samples = soup.find_all(class_="LC20lb")
    ret_val = []

    for elem in samples:
        ret_val.append(elem.text)

    resp = jsonify(ret_val)
    resp.status_code = 200
    return resp
    # return "Google Query: \n" + samples, 200

@app.route('/ddg/<query>')
def ddg(query):
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
        
    return render_template('index.html', results = ret_val)

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

app.run(debug=False)