#!/usr/bin/env python
import requests
import urllib
import csv
from config import config
from cStringIO import StringIO

table = requests.get('https://www.google.com/fusiontables/api/query?sql=' + urllib.quote_plus('SELECT * FROM %s' % config['table']))
rows = csv.reader(StringIO(table.content))

for id, artist, title, twitter in rows:
  print id, artist, title, twitter

