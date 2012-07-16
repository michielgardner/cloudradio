#!/usr/bin/env python
import pickle
import beanstalkc

'''

Get all playlist data and create a Beanstalk job for every track

'''

b = beanstalkc.Connection()
data = open('../db/playlist.pkl', 'rb')
playlist = pickle.load(data)

data.close()

for id, (artist, title, twitter) in playlist.iteritems():
  b.put(pickle.dumps((id, artist, title, twitter)))
