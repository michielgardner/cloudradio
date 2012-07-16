#!/usr/bin/env python
import beanstalkc
import pickle
import requests
import json
import os
from config import config

'''

Wait for queued tracks, added by queue.py

'''

b = beanstalkc.Connection()

while True:
  job = b.reserve()
  id, artist, title, twitter = pickle.loads(job.body)

  if os.path.isfile('../mp3/%s.mp3' % id) is True: # don't download files that already exist
    # TODO: check if the previous download was incomplete
    job.delete()
    continue

  '''

  Download the mp3, first to /tmp (to prevent the station from streaming incomplete sets), then move it to the MP3 directory

  '''

  track = requests.get('http://api.soundcloud.com/tracks/%s/stream?consumer_key=%s' % (id, config['consumer_key']))
  output = open('/tmp/%s.mp3' % id, 'wb')
  chunks = track.iter_content(chunk_size=1048576)

  for chunk in chunks:
    output.write(chunk)

  output.close()
  os.rename('/tmp/%s.mp3' % id, '../mp3/%s.mp3' % id)
  job.delete()
