import requests
from bs4 import BeautifulSoup
from time import sleep

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

headers = {}
headers["User-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# r = session.get('https://httpbin.org/user-agent', headers=headers)
# print(r.text)

sleep(2)

r = session.get('http://httpbin.org/ip')
print(r.text)
# r = session.get('http://httpbin.org/headers')
# print(r.text)

sleep(2)

params={
    'q': 'weather'
    # 'key': 'AIzaSyBHq31tbO-Fg5JQBqxFcIjY5MG2p5J3NLo'
}

# new_headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#     'dnt': '1',
#     'x-client-data': 'CJC2yQEIprbJAQjBtskBCKmdygEIqKPKAQixp8oBCOKoygEI8anKAQivrMoBCLmsygEYz6rKAQ==',
#     'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; CONSENT=YES+US.en+20161213-01-0; gsScrollPos-368=; gsScrollPos-514=; gsScrollPos-523=; gsScrollPos-1761=0; ANID=AHWqTUl3Js3WfkiAhApF_VyHS3D1W4HzhZfP8ft1bxYbGzuWN9YKk7BDFZiUMahs; gsScrollPos-1065=; S=billing-ui-v3=BI2DTZC1kjyM8zoWozMEBtn58k5ycf4q:billing-ui-v3-efe=BI2DTZC1kjyM8zoWozMEBtn58k5ycf4q; gsScrollPos-45=0; gsScrollPos-1725=; gsScrollPos-185=0; gsScrollPos-320=0; gsScrollPos-976=; gsScrollPos-1024=; gsScrollPos-1558=; gsScrollPos-251=0; gsScrollPos-253=0; gsScrollPos-430=0; gsScrollPos-435=0; gsScrollPos-431=; NID=181=xGngcmNDbc-xFq52aIzdvWPsd51ocv67ZPNROdH9e5niWxUNtzbS_HYpPVs8u_0qO3PWVchaYauxapsFzIuhOq74hY1d_b2WyYJjgCRYeA3KqbHaUcRV-FhqHY0urzxnwb94NkPpRhzrY9HmeDW9WLm4s7-NDvnEhvUZV_WvmVYzWbzIUkhNhImx-MQZr4wkyI-zKft42Rz-slTf0qwYp2-mWsaBbDVnIrt-wqyOb_y6t8o0tvFQ6uO1c6geEmfOeKSQcnWO_ah7s0muw8gXGUN4r9PssvWg5_r0ctThxsT7E-8MUCWBo9ChwRAGfjkANqUUkTOpf2sYfC-Y8HEK6_CG_JoqdBGkN7Q96Dnm9kC7UEi1KsViN56gxH8QOMxEoTN-cWlUWKuozt3Zg3BdzaU16DxP--0nlo9dYqJhUF40nxqkTmEsRCayQGXCvQB2JyBUEwhrE9KzQpaMxw1VT1Ce0jPl4hqjYHcCi8BdnbRoUY9hFM_HyfPUSYJ1e05F0LRqwaUOTfCyx7iq; HSID=Av2wY4f1KsSn0tgRR; SSID=ARc3pXwytGmxAg4tF; APISID=nBZMDp8LZwKFrFDG/AmJ6xj5tJ5aroFHh2; SAPISID=b82Dd9BpnNfiBmif/AliLTB-Y6dqn9ff4R; SID=Vgf9STxRy6wBerXz1ypc8m7PmjgqGi_4j2GYaE8N7AIhk6CB4kN0B-Kft9fD8Ck2pQmKLQ.; DV=k6ssuQkZyqopILDKYp_kfrdKvrCBpJYgIx69Y29Vx_jOBAA; SIDCC=AN0-TYvGV-A89mabXB8SabXPF9rIqJkUkHF1ve33NBh--IO9Btu4jlhpAE-3T_z_Hhb8uQrUefE; 1P_JAR=2019-4-23-2',
#     'accept-language': 'accept-language: en-US,en;q=0.9'
# }

new_headers = {
    'cookie': 'ANID=AHWqTUn95ISuwnZpW4yc_7Us_mrVyKXquO_NoLf51CML9NF1Tjal5HMlXwC7ylbR; SID=VgfRIossKfKDMtliWOffqv0f8v2P3-q2GFy28yWvUP_Q6UpxJvOCz9Hjw0GRmmHSwA7tGg.; HSID=AEYSSV5TKu2yttYQe; SSID=A1fN-ZlYt1orl_8lj; APISID=0Hux_fPcVPDg5XZv/AGRW-QnPZsMClW2UL; SAPISID=GzIWigexS_D7_NR0/AE6bq0GbXVCl9ErBX; CONSENT=YES+US.en+20161213-01-0; NID=181=wpliWgjEbH5Fdsn8rZxR14StlzVdjRdAXf2p4bOXrkrgMI2Jl-TiSwmy0SVpbNXRVXTFsn5hXi8dThbwouwWYKTJK5Ih_y1olVCvWoiATKJKe_5AghBKGxiCBlVVwoXmcVCa2tk4BGuiF4DCrJ6wZI0EQAOl9OHTu_VsRVuNAXW03NtCEStaTqKXhQnC2Hh0sNlB4_IedlEbW35i; 1P_JAR=2019-4-23-3; DV=o1Nbl6B8jsZRELXrd6iumDQIQaWCpNYGGjFTFCYbPQAAAOB85pD-5LPtOQAAAOwZ_awmB2dqGAAAAAKrLPZJ7nerCgAAAA; SIDCC=AN0-TYsIc9ao8HSl8ErVpCFrEf0JYQbOHu-ttenPp8mfKx-rY-Z6GPOJqgW0snerz0czS1As5w',
    'x-client-data': 'CIu2yQEIprbJAQipncoBCKijygEI4qjKAQ==',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'content-type': 'text/plain;charset=UTF-8',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0'
}

r = session.get('http://httpbin.org/headers', headers=new_headers)
# r = session.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyBHq31tbO-Fg5JQBqxFcIjY5MG2p5J3NLo&q=playoffs')
print(r.text)

r = session.get('https://www.google.com/search', params=params, headers=new_headers)
content = r.text

soup = BeautifulSoup(content, "html.parser")
samples = soup.find_all(class_="LC20lb")

# print(r.url)
print(samples)
