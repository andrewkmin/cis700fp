import io
import pycurl
from bs4 import BeautifulSoup
import stem.process
from stem.util import term
import urllib
import requests
import webbrowser

SOCKS_PORT = 7000


def query(url):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

  output = io.BytesIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)


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

print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))

# results = query("https://duckduckgo.com/?q=playoffs&ia=web")
results = query("https://www.google.com/search?q=playoff")


with open('output.html', 'wb') as f:
   f.write(results)
webbrowser.open('output.html')

print(results)

# html = term.format(results)
soup = BeautifulSoup(results, 'lxml')
for g in soup.find_all(class_='result__body links_main links_deep'):
    print(g.text)
    print('-----')

tor_process.kill()  # stops tor