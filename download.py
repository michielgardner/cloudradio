#!/usr/bin/env python
import beanstalkc
import pickle
import requests
import json
import os
from config import config

b = beanstalkc.Connection()

while True:
  job = b.reserve()
  id, artist, title, twitter = pickle.loads(job.body)

  if os.path.isfile('mp3/%s.mp3' % id) is True:
    job.delete()
    continue

  track = requests.get('http://api.soundcloud.com/tracks/%s/stream?consumer_key=%s' % (id, config['consumer_key']))
  output = open('mp3/%s.mp3' % id, 'wb')
  chunks = track.iter_content(chunk_size=1048576)

  for chunk in chunks:
    output.write(chunk)

  output.close()
  job.delete()
