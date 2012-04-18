#!/usr/bin/env python
import requests
import urllib
import csv
import pickle
from config import config
from cStringIO import StringIO

table = requests.get('https://www.google.com/fusiontables/api/query?sql=' + urllib.quote_plus('SELECT * FROM %s' % config['table']))
rows = csv.reader(StringIO(table.content))
playlist = {}

for row, (id, artist, title, twitter) in enumerate(rows):
  if row == 0:
    continue # skip first row

  playlist[id] = (artist, title, twitter)

output = open('db/playlist.pkl', 'wb')

pickle.dump(playlist, output)
output.close()
