# midi2data

This small program creates 
assembly data dump
from a specified track of a MIDI file,
extracting the Note On pitch values 
to a list of bytes.

Requires Python3 and `mido` module.

CLI arguments:
 - midi file name (mandatory)
 - output style: midi/const (mandatorys)
 - number of columns (mandatory)
 - note offset (optional, default: 0)
 - track number (optional, default: 1)

Launch `example.sh` for demonstration,
it will print:

	MIDI pitch values:
		;---- Boesendorfer Grand Piano ----
		db 67,74,79,86,82,91
		db 60,67,75,82,79,87
		db 65,72,77,84,81,89
		db 58,65,74,81,77,86
		db 55,62,67,74,70,79
		db 60,67,75,82,79,87
		db 62,69,74,81,78,86
		db 55,62,71,79,74,83
	
	Const notes, shifted octave up:
		;---- Boesendorfer Grand Piano ----
		db G_6,D_7,G_7,D_8,As7,G_8
		db C_6,G_6,Ds7,As7,G_7,Ds8
		db F_6,C_7,F_7,C_8,A_7,F_8
		db As5,F_6,D_7,A_7,F_7,D_8
		db G_5,D_6,G_6,D_7,As6,G_7
		db C_6,G_6,Ds7,As7,G_7,Ds8
		db D_6,A_6,D_7,A_7,Fs7,D_8
		db G_5,D_6,H_6,G_7,D_7,H_7
