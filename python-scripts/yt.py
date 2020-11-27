#!/usr/bin/env python
import os
import sys
from pytube import YouTube

if len(sys.argv) > 1:
  output = sys.argv[1]
else:
  output = "no argument found"

yt = YouTube(output)
video = {"title": yt.title, "length": yt.length, "Available": yt.streams}

print(video)
