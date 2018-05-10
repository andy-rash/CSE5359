import re
import requests
from bs4 import BeautifulSoup

CODE_REGEX = re.compile(r'\+[\d]{1,3}\:', re.MULTILINE)

page = requests.get('https://en.wikipedia.org/wiki/List_of_country_calling_codes')
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table')

tokens = table.text.split()

codes = sorted([x[1:-1] for x in tokens if CODE_REGEX.match(x)])

print('('+'|'.join(codes)+')')

