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

		self.processTrack(True)
		self.processTrack(False)


	def processTrack(self, readable):

		self.pitchOffset = 0
		self.noteCounter = 0
		self.stamp = 0
		self.column = 0

		for message in self.track: 
			self.processMessage(message, readable)
		print()


	def processMessage(self, message, readable):

		if message.type == "note_on":
			self.last = message
		
		if message.type != "note_off":
			return

		on = self.last
		off = message

		duration = off.time
		onTime = self.stamp + on.time

		if on.time != 0: 
			print( self.renderNote(None, on.time, readable), end="")
			self.newColumn(readable)
		print( self.renderNote(on.note, duration, readable), end="")
		self.newColumn(readable)

		self.stamp += on.time + duration


	def newColumn(self, readable):
		
		if not readable: return

		self.column += 1
		if self.column < 4: 
			print("  ", end="")
			return

		self.column = 0
		print()

	def renderNote(self, pitch, duration, readable = False):

		self.noteCounter += 1

		if (pitch is None):
			octave = ""
			note = "---"
		else:
			octave = str( math.floor(pitch/12) )
			note = (
					"C_","Cs","D_","Ds","E_","F_",
					"Fs","G_","Gs","A_","As","H_"
			)[pitch % 12]
		
		ticks = int( duration / 120 )

		if readable:
			return note + octave + "(" + str(ticks) + ")"

		else:
			if pitch is None: pitch = 0
			return str(pitch) + ":" + str(ticks) + " "


if __name__ == "__main__":
	(ParseMidi()).main()