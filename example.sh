#!/bin/bash
clear

echo MIDI pitch values:
./midi2data.py peregrinacion-size.mid const 6 0 1
echo " "
echo Const notes, shifted octave up:
./midi2data.py peregrinacion-size.mid const 6 12 1
