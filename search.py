# Import libraries
import webbrowser
import time
import random

# Prompt user input and store in variable
site = input("Enter website (without http://): ")

# define variable and function to create website address from list below
def open_website(domain, service_url):
    url = service_url.format(domain)
    webbrowser.open(url)

#list of sites to visit
services = {
    "Viewdns": "https://viewdns.info/whois/?domain={}",
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Certificates": "https://crt.sh/?q={}",
    "Malware": "https://www.virustotal.com/gui/domain/{}",
    "builtwith": "https://builtwith.com/relationships/{}",
    "dnslytics": "https://dnslytics.com/domain/{}",
    "archive.org": "https://web.archive.org/web/*/{}",
    "host.io": "https://host.io/{}"
}

#open each site from service list in the format from open_website
for service_name,service_url in services.items():
    open_website(site, service_url)

#randomize opening time to imitate human browsing
sleep_time = random.uniform(1, 5)
time.sleep(sleep_time)
