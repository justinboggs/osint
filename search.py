import webbrowser
import time
import random

site = input("Enter website (without http://): ")

def open_website(domain, service_url):
    url = service_url.format(domain)
    webbrowser.open(url)

services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    "Certificates": "https://crt.sh/?q={}",
    "Subdomains": "https://securitytrails.com/domain/{}",
    "Malware": "https://www.virustotal.com/gui/domain/{}",
    "builtwith": "https://builtwith.com/relationships/{}",
    "dnslytics": "https://dnslytics.com/domain/{}",
    "archive.org": "https://web.archive.org/web/*/{}",
    "host.io": "https://host.io/{}"
}

for service_name,service_url in services.items():
    open_website(site, service_url)

sleep_time = random.uniform(1, 5)
time.sleep(sleep_time)
