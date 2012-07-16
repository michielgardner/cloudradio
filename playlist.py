#!/usr/bin/env python
import requests
import urllib
import csv
import pickle
from config import config
from cStringIO import StringIO

'''

Download the latest playlist table

'''

table = requests.get('https://www.google.com/fusiontables/api/query?sql=' + urllib.quote_plus('SELECT * FROM %s' % config['table']))
rows = csv.reader(StringIO(table.content))


'''

Insert the track metadata into a dictionary

'''

playlist = {}

for row, (id, artist, title, twitter) in enumerate(rows): # loop through all tracks
  if row == 0:
    continue # skip first row

  playlist[id] = (artist, title, twitter) # store the track metadata in a dictionary


'''

Write the metadata to disk

'''

output = open('../db/playlist.pkl', 'wb')

pickle.dump(playlist, output)
output.close()
