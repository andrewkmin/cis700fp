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

session = requests.session()

SOCKS_PORT = 7000

# Set socks proxy and wrap the urllib module

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
socket.socket = socks.socksocket

# Perform DNS resolution through the socket

def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

def query(url):
  """
  Uses urllib to fetch a site using SocksiPy for Tor over the SOCKS_PORT.
  """

  try:
    return urllib.urlopen(url).read()   
  except:
    return "Unable to reach %s" % url


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

sleep(2)

# print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))

# results = query("https://www.google.com/search?q=nba")

# print(results)

print('PRINTING IP ADDRESS')
r = session.get('http://httpbin.org/ip')
print(r.text)

sleep(2)

# tor browser
# new_headers = {
#     # 'cookie': 'CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg; 1P_JAR=2019-04-23-04; NID=181=io1uaiXx1DFQq0MliJJ4yB-0HyKiSJHnjdrQEn5JQ9MILpDy4jXkwNgI85Xm-F8gJ7YF8vn9kWVONjJNTcSYgcMEPHgs1iEclsPmdj09W5WEEZgiXinoToFQyF9Ea1hb9xfMUdWzqJkozN_j1HMPQrimUvD3Nt8ObKWmE19neEw; DV=o1YM2allSmQjYEuIbfArY17wdmGGpFZsaeJKUBB27wMAAAA; ANID=AHWqTUmP0HluU8XWUpp0txLtiLhz85Av5NlZE_V9pLUInB90j34edMTqYXyYWyAl',
#     'cookie': 'ANID=AHWqTUn95ISuwnZpW4yc_7Us_mrVyKXquO_NoLf51CML9NF1Tjal5HMlXwC7ylbR; SID=VgfRIossKfKDMtliWOffqv0f8v2P3-q2GFy28yWvUP_Q6UpxJvOCz9Hjw0GRmmHSwA7tGg.; HSID=AEYSSV5TKu2yttYQe; SSID=A1fN-ZlYt1orl_8lj; APISID=0Hux_fPcVPDg5XZv/AGRW-QnPZsMClW2UL; SAPISID=GzIWigexS_D7_NR0/AE6bq0GbXVCl9ErBX; CONSENT=YES+US.en+20161213-01-0; NID=181=wpliWgjEbH5Fdsn8rZxR14StlzVdjRdAXf2p4bOXrkrgMI2Jl-TiSwmy0SVpbNXRVXTFsn5hXi8dThbwouwWYKTJK5Ih_y1olVCvWoiATKJKe_5AghBKGxiCBlVVwoXmcVCa2tk4BGuiF4DCrJ6wZI0EQAOl9OHTu_VsRVuNAXW03NtCEStaTqKXhQnC2Hh0sNlB4_IedlEbW35i; 1P_JAR=2019-4-23-3; DV=o1Nbl6B8jsZRELXrd6iumDQIQaWCpNYGGjFTFCYbPQAAAOB85pD-5LPtOQAAAOwZ_awmB2dqGAAAAAKrLPZJ7nerCgAAAA; SIDCC=AN0-TYsIc9ao8HSl8ErVpCFrEf0JYQbOHu-ttenPp8mfKx-rY-Z6GPOJqgW0snerz0czS1As5w',
#     'x-client-data': 'CIu2yQEIprbJAQipncoBCKijygEI4qjKAQ==',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
#     'content-type': 'text/plain;charset=UTF-8',
#     'accept-language': 'en-US,en;q=0.5',
#     'content-length': '0',
#     'cache-control': 'max-age=0',
#     'connection': 'keep-alive',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'accept-encoding': 'deflate, br',
#     'host': 'www.google.com',
#     'referrer': 'https://www.google.com/'
# }

new_headers = {
    'cookie': 'ANID=AHWqTUn95ISuwnZpW4yc_7Us_mrVyKXquO_NoLf51CML9NF1Tjal5HMlXwC7ylbR; SID=VgfRIossKfKDMtliWOffqv0f8v2P3-q2GFy28yWvUP_Q6UpxJvOCz9Hjw0GRmmHSwA7tGg.; HSID=AEYSSV5TKu2yttYQe; SSID=A1fN-ZlYt1orl_8lj; APISID=0Hux_fPcVPDg5XZv/AGRW-QnPZsMClW2UL; SAPISID=GzIWigexS_D7_NR0/AE6bq0GbXVCl9ErBX; CONSENT=YES+US.en+20161213-01-0; NID=181=wpliWgjEbH5Fdsn8rZxR14StlzVdjRdAXf2p4bOXrkrgMI2Jl-TiSwmy0SVpbNXRVXTFsn5hXi8dThbwouwWYKTJK5Ih_y1olVCvWoiATKJKe_5AghBKGxiCBlVVwoXmcVCa2tk4BGuiF4DCrJ6wZI0EQAOl9OHTu_VsRVuNAXW03NtCEStaTqKXhQnC2Hh0sNlB4_IedlEbW35i; 1P_JAR=2019-4-23-3; DV=o1Nbl6B8jsZRELXrd6iumDQIQaWCpNYGGjFTFCYbPQAAAOB85pD-5LPtOQAAAOwZ_awmB2dqGAAAAAKrLPZJ7nerCgAAAA; SIDCC=AN0-TYsIc9ao8HSl8ErVpCFrEf0JYQbOHu-ttenPp8mfKx-rY-Z6GPOJqgW0snerz0czS1As5w',
    'x-client-data': 'CIu2yQEIprbJAQipncoBCKijygEI4qjKAQ==',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'content-type': 'text/plain;charset=UTF-8',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0'
}

print('PRINTING HEADERS')
r = session.get('http://httpbin.org/headers', headers=new_headers)
print(r.text)

# this is to check where we actually are
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

# print(r.url)
# print(samples)

for elem in samples:
    print(elem.text)


print('END OF GOOGLE RESULTS')


ddg_headers = {
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
  'content-type': 'text/plain;charset=UTF-8',
  'accept-language': 'en-US,en;q=0.9',
  'content-length': '0'
}

ddg_params = {
  'q':'weather',
  # 't': 'h_',
  # 'ia': 'web'
}
r = session.get('https://duckduckgo.com/html/', params=ddg_params, headers=ddg_headers)
content = r.text

soup = BeautifulSoup(content, "html.parser")
samples = soup.find_all(class_="result__title")[:len(samples)]

# print(r.url)
# print(samples)

for elem in samples:
    print(elem.text.strip())

tor_process.kill()  # stops tor