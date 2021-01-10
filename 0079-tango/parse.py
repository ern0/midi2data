#!/usr/bin/env python3 -B

try: import mido
except: quit("missing module: mido")
import sys
import math


class ParseMidi:

	def main(self):

		try: self.midiData = mido.MidiFile(sys.argv[1])
		except: quit("error loading MIDI file")	

		self.track = self.midiData.tracks[0]

		print("file=" + sys.argv[1], end=" ")
		print("track=" + self.track.name)

		self.processTrack(1)
		self.processTrack(2)
		self.processTrack(3)

		print("note count: " + str(self.noteCounter))
		print("duration: " + str(self.totalDuration))


	def processTrack(self, readableParm):

		self.readable = readableParm
		self.pitchOffset = 0
		self.noteCounter = 0
		self.totalDuration = 0
		self.stamp = 0
		self.column = 0

		if self.readable == 3: print('"', end="")

		for message in self.track: 
			self.processMessage(message)
		
		if self.readable == 3: print('"', end="")
		print()


	def processMessage(self, message):

		if message.type == "note_on":
			self.last = message

		if message.type == "note_off":
			self.processNote(self.last, message)


	def processNote(self, on, off):

		duration = off.time
		onTime = self.stamp + on.time

		if on.time != 0: 
			print( self.renderNote(None, on.time), end="")
			self.newColumn()
		print( self.renderNote(on.note, duration), end="")
		self.newColumn()

		self.stamp += on.time + duration


	def newColumn(self):
		
		if self.readable == 3: return

		self.column += 1
		if self.column < 4: 
			print(" ", end="")
			return

		self.column = 0
		print()


	def renderNote(self, pitch, duration):

		self.noteCounter += 1

		if (pitch is None):
			octave = ""
			note = "---"
		else:
			octave = str( math.floor(pitch/12) )
			note = (
					"C_","Cs","D_","D#","E_","F_",
					"F#","G_","Gs","A_","A#","H_"
			)[pitch % 12]

		ticks = int( duration / 120 )
		self.totalDuration += ticks

		if self.readable == 1:
			return (
				note 
				+ octave 
				+ ":" 
				+ str(ticks) 
				+ "(" 
				+ str(duration) 
				+ ")"
			)

		e = note + octave + ":" + str(ticks)

		if pitch is None: 
			note = 0
		else:
			note = pitch - 81

		value = (((ticks-1) << 4) | note) + 34

		if self.readable == 2:
			star = "-"
			if (value > 127): star = "*"
			return (
				str(value).rjust(3) 
				+ star 
				+ str(note).rjust(2) 
				+ ":" + str(ticks)
				+ "("
				+ str(self.totalDuration).rjust(3)
				+ ")"
			)

		invalid = False
		if pitch is not None and note == 0: invalid = True
		if value < 32: invalid = True
		if note > 15: invalid = True
		if value == ord("<"): invalid = True
		if value == ord(">"): invalid = True
	
		if invalid: 
			return "\" /* " + chr(value) + " " + e + " */ \""
		else:
			return chr(value)

if __name__ == "__main__":
	(ParseMidi()).main()