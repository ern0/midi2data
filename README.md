# midi2data

This small program creates 
assembly data dump
from a single track of a MIDI file,
extraxting Note On pitch values 
to a list of bytes.

Requires Python3 and module named `mido`.

Args:
 - midi file name (mandatory)
 - number of columns (mandatory)
 - note offset (optional, default: 0)
 - track number (optional, default: 1)

Launch `example` for demonstration:

  ;---- Boesendorfer Grand Piano ----
      db 67,74,79,86,82,91
      db 60,67,75,82,79,87
      db 65,72,77,84,81,89
      db 58,65,74,81,77,86
      db 55,62,67,74,70,79
      db 60,67,75,82,79,87
      db 62,69,74,81,78,86
      db 55,62,71,79,74,83