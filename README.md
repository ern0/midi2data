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
			db G_5,D_6,G_6,D_7,As6,G_7
			db C_5,G_5,Ds6,As6,G_6,Ds7
			db F_5,C_6,F_6,C_7,A_6,F_7
			db As4,F_5,D_6,A_6,F_6,D_7
			db G_4,D_5,G_5,D_6,As5,G_6
			db C_5,G_5,Ds6,As6,G_6,Ds7
			db D_5,A_5,D_6,A_6,Fs6,D_7
			db G_4,D_5,H_5,G_6,D_6,H_6
		
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
			