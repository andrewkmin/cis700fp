# CIS 700 Final Project

## Description
This project is for CIS 700-003: Topics on privacy and anonymity, at the University of Pennsylvania (Spring 2019). In summary, this project explores the notion of "search neutrality," i.e. the impact that search engines/providers may have on their users in terms of creating information bubbles. They're able to create such bubbles via following users through cookies, or gleaning information about them based on location/ISP or even the date/time of the request. A slide deck for my simple presentation can be found [here](https://docs.google.com/presentation/d/1FlfdMiPt_D1AJ7Yd5l980BO7q32fm5uQXUVSkMuGg2c/edit?usp=sharing). I created a demo web app using Flask (backend API provider), Stem (Tor controller for Python), and Socks (serves proxies through which a device can connect to Tor), among other things.

## How it works
Upon initialization of the server, a Tor process will also be initialized, with an exit node specified to be based in the US (this can be changed in the tor process config object). Subsequent requests made through this server will thus be "sent from" that exit node. The specific IP of the exit node can be found at the top of the page of the web app; you can use a who-is type of service to resolve where this specific IP might be located within the country. In the server, requests are made to both Google and DuckDuckGo back-to-back with the provided query. The resulting HTML responses are then parsed, and then fed to a template renderer to be displayed on the webpage. 

## Instructions
 - Git clone this repo
 - In the `new_headers` dictionary, replace the commented-out dummy `cookie` and `x-client-data` fields with valid values, which you can find under your request headers in your web browser.
 - Use `pipenv` to create a virtual environment.
 - Download all specified packages (via `pip install`).
 - Run final.py via `python final.py` within the virtual environment.
 - Navigate to `localhost:5000/search/<QUERY>` (or whatever port Flask tells you to open) in a web browser, and replace `<QUERY>` with a search query.
 - Feel free to remove the Flask API altogether and instead repeatedly run this Python script with different queries. Add comments as you may see fit in the server code to print out responses, etc.
 - To be safe, navigate to `localhost:5000/exit` when you are finished, before quitting the Flask server. This is to explicitly end the Tor process; if the Tor process is not correctly stopped/cleared, follow the next instruction below. This step might not always be necessary, but it is just for best practices.
 - In the case that you see an error message saying a socket/port is already in use, run `ps -ef | grep tor` and find the Tor process and manually kill it using `kill -9 <PROCESS ID #>`. Note that you may have to use `sudo` to gain privileges to kill the Tor process. 
 - If you would like to make modifications to the frontend, change the `index.html` file directly where it is; it needs to be left in the `templates` folder for Flask to be able to correctly find and render it.
 - Files for previous attempts are stored in the `prev` folder.

## FAQ
Q: Why do I need to use my own cookies/x-client-data information?  
A: Otherwise, Google will very likely think that you're a bot and won't respond with any search results at all. 

Q: How do I extract `cookie` and `x-client-data`?  
A: Open up the developer tools console in a web browser like Chrome or Firefox. Navigate to the Network tab and click on a request that is made. If there's nothing there, refresh the page and watch it populate. Upon clicking a request, you should see a host of associated information, including request headers. You should be able to find fields such as `cookie` and `x-client-data` here.

Q: I've included my `cookies` and `x-client-data` but Google still isn't responding with any results. What do I do?  
A: Check if you are logged in to Google; cookies associated with a logged-in account are probably much more likely to not get categorized as a bot by Google.

Q: Why not just use Tor Browser?  
A: It's arguably easier to just straight up use the Tor Browser, but even then, Google may still think you're a bot (possible due to many Google searches being made from the same Tor exit node). You could then, theoretically, just juxtapose two browser windows. This web app is just an easier/cleaner way to do this.

## Notes
Please note the security implications of storing your cookies/x-client-data and using it to make a request through Tor. These cookies will most likely be associated with your accounts, and nodes within the Tor network might know about these associations. Also, such cookies will likely be tied to your location as well, so keep this in mind as you are making searches through this project implementation (Google stores a lot of info in those cookies).

## Further work
 - It would be great to find a way to not get detected by Google's bot-detection system, without using real cookies.
 - A simple textbox/webform on the frontend would be much more usable than directly manipulating the address bar to make new searches. 

Please feel free to create an issue here in case you guys run into a bug that was not mentioned here. Thanks!













