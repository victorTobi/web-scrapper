from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import requests
import sys

url = "https://www.mckinsey.com/industries/electric-power-and-natural-gas/how-we-help-clients"

session = requests.session()
session.headers["user-Agent"] = "Mozilla/5.0 (X11 Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

html = session.get(url).content

soup = bs(html, 'html.parser')
script_files = []

for script in soup.find_all("scripts"):
    if script.attrs.get("src"):
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

css_files = []

for css in soup.find_all("link"):
    if css.attrs.get('href'):
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)

print("total script files in the page:", len(script_files))
print("total  CSS files in the page: ", len(css_files))

with open("javascript_files.txt", "w") as f:
    for js_file in script_files:
        print(js_file, file=f)

with open("css_files.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)