#!/usr/bin/env python
import shout
import os
import random
import pickle
from config import config

'''

Shoutcast/Icecast settings; to configure, edit config.py

'''

s = shout.Shout()
s.host = config['icecast_host']
s.port = config['icecast_port']
s.user = config['icecast_user']
s.password = config['icecast_password']
s.mount = config['icecast_mount']
s.format = 'mp3'
s.name = config['name']
s.description = config['description']
s.genre = config['genre']
s.url = config['url']

s.open()

last_track = None

while True: # endless loop to stay on air ;-)

  '''

  Choose a random MP3 from the music directory 

  '''

  files = os.listdir('../mp3') # create a list of all mp3s
  track = random.choice(files) # choose random track

  if track == last_track:
    continue # don't play the same track twice


  '''

  Get metadata for this track

  '''

  data = open('../db/playlist.pkl', 'rb')
  playlist = pickle.load(data)
  
  data.close()

  try:
    artist, title, twitter = playlist[track.split('.')[0]]
  except KeyError: # we don't have metadata for this mp3
    continue


  '''

  Load the MP3 and play it

  '''

  f = open('../mp3/' + track)

  s.set_metadata({'song': 'Now on %s: %s - %s' % (config['name'], artist, title)})

  while True: # play the track
    buf = f.read(4096)

    if len(buf) == 0: # end of file
      break

    s.send(buf)
    s.sync()

  f.close()

  last_track = track


  '''

  Finished playing this track, go to the next one

  '''

s.close() # just to be sure, but we should never end up here
