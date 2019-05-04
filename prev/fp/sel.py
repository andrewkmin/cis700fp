import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

tbb_dir = "/home/andrew/Desktop/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US/"
tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
    driver.load_url("https://check.torproject.org")

print("Done")
tor_process.kill()

# from tbselenium.tbdriver import TorBrowserDriver
# with TorBrowserDriver("/home/andrew/Desktop/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US/") as driver:
#     driver.get('https://check.torproject.org')