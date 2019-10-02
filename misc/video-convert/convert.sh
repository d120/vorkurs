#!/bin/sh
# Converts videos recorded by OBS into a format that is recognizable and
# streamable by all major browsers.
ffmpeg -i "$1.mkv" -movflags +faststart -vcodec copy -acodec copy "$1.mp4"
