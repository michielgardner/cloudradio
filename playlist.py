#!/usr/bin/env python
import requests
import urllib
import csv
import pickle
from config import config
from cStringIO import StringIO
import simplejson as json

'''

Download the latest playlist table

'''

table = requests.get('https://www.googleapis.com/fusiontables/v1/query?sql=' + urllib.quote_plus('SELECT * FROM %s' % config['table']) + '&key=' + config['google_key'])
rows = json.loads(table.content)['rows']


'''

Insert the track metadata into a dictionary

'''

playlist = {}

for (id, artist, title, twitter) in rows: # loop through all tracks
  playlist[id] = (artist, title, twitter) # store the track metadata in a dictionary


'''

Write the metadata to disk

'''

output = open('../db/playlist.pkl', 'wb')

pickle.dump(playlist, output)
output.close()
