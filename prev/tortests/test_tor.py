import unittest
import tbselenium.common as cm
from time import sleep
from tbselenium.tbdriver import TorBrowserDriver

# Point the path to the tor-browser_en-US directory in your system
tbpath = '/home/andrew/Desktop/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US/'
# driver = TorBrowserDriver(tbpath, tbb_logfile_path='test.log', tor_cfg=cm.USE_STEM)
driver = TorBrowserDriver(tbpath, tbb_logfile_path='test.log', tor_cfg=cm.USE_RUNNING_TOR)

# driver.add_cookie({'name': 'ANID', 'value': 'AHWqTUn95ISuwnZpW4yc_7Us_mrVyKXquO_NoLf51CML9NF1Tjal5HMlXwC7ylbR'})
# driver.add_cookie({'name': 'SID', 'value': 'VgfRIossKfKDMtliWOffqv0f8v2P3-q2GFy28yWvUP_Q6UpxJvOCz9Hjw0GRmmHSwA7tGg.'})
# driver.add_cookie({'name': 'HSID', 'value': 'AEYSSV5TKu2yttYQe'})
# driver.add_cookie({'name': 'SSID', 'value': 'A1fN-ZlYt1orl_8lj'})

# driver.add_cookie({'name': 'APISID', 'value': '0Hux_fPcVPDg5XZv/AGRW-QnPZsMClW2UL'})
# driver.add_cookie({'name': 'SAPISID', 'value': 'GzIWigexS_D7_NR0/AE6bq0GbXVCl9ErBX'})
# driver.add_cookie({'name': 'CONSENT', 'value': 'YES+US.en+20161213-01-0'})
# driver.add_cookie({'name': 'NID', 'value': '181=wpliWgjEbH5Fdsn8rZxR14StlzVdjRdAXf2p4bOXrkrgMI2Jl-TiSwmy0SVpbNXRVXTFsn5hXi8dThbwouwWYKTJK5Ih_y1olVCvWoiATKJKe_5AghBKGxiCBlVVwoXmcVCa2tk4BGuiF4DCrJ6wZI0EQAOl9OHTu_VsRVuNAXW03NtCEStaTqKXhQnC2Hh0sNlB4_IedlEbW35i'})
# driver.add_cookie({'name': '1P_JAR', 'value': '2019-4-23-3'})
# driver.add_cookie({'name': 'DV', 'value': 'o1Nbl6B8jsZRELXrd6iumDQIQaWCpNYGGjFTFCYbPQAAAOB85pD-5LPtOQAAAOwZ_awmB2dqGAAAAAKrLPZJ7nerCgAAAA'})
# driver.add_cookie({'name': 'SIDCC', 'value': 'AN0-TYsIc9ao8HSl8ErVpCFrEf0JYQbOHu-ttenPp8mfKx-rY-Z6GPOJqgW0snerz0czS1As5w'})

# url = "https://check.torproject.org"
url = "https://www.google.com/search?q=playoffs"

headers = {}
headers["User-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"


driver.load_url(url)
# driver.context()

# Find the element for success
element = driver.find_element_by_class_name('LC20lb')
print(element)
sleep(2)  # So that we can see the page

driver.close()


# class TestSite(unittest.TestCase):
#     def setUp(self):
#         # Point the path to the tor-browser_en-US directory in your system
#         tbpath = '/home/andrew/Desktop/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US/'
#         self.driver = TorBrowserDriver(tbpath, tbb_logfile_path='test.log', tor_cfg=cm.USE_STEM)
#         self.url = "https://check.torproject.org"

#     def tearDown(self):
#         # We want the browser to close at the end of each test.
#         self.driver.close()

#     def test_available(self):
#         self.driver.load_url(self.url)
#         # Find the element for success
#         element = self.driver.find_element_by_class_name('on')
#         self.assertEqual(str.strip(element.text),
#                          "Congratulations. This browser is configured to use Tor.")
#         sleep(2)  # So that we can see the page


# if __name__ == '__main__':
#     unittest.main()

# https://kushaldas.in/posts/tor-browser-and-selenium.html