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

		if False:
			self.processTrack(1)
		else:
			self.processTrack(1)
			self.processTrack(2)
			self.processTrack(3)

		print()	

		durationOk = "FAIL"
		if self.totalDuration == 128:
			durationOk = "okay"

		print(
			"duration: " 
			+ str(self.totalDuration)
			+ " - "
			+ durationOk
		)

		noteCountOk = "FAIL"
		if self.noteCounter == 61:
			noteCountOk = "perfect"
		if self.noteCounter < 61:
			noteCountOk = "so-so"

		print(
			"note count: " 
			+ str(self.noteCounter)
			+ "/61 - "
			+ noteCountOk
		)


	def processTrack(self, readableParm):

		self.readable = readableParm
		self.pitchOffset = 0
		self.noteCounter = 0
		self.totalDuration = 0
		self.column = 0
		self.index = 0

		if self.readable == 3: 
			print('"', end="")

		for message in self.track: 
			self.processMessage(message)
		
		if self.readable == 3: 
			print('"', end="")
		print()


	def processMessage(self, message):

		if message.type == "note_on":
			self.last = message

		if message.type == "note_off":
			self.processNote(self.last, message)
			self.index += 1


	def processNote(self, on, off):

		pauseDuration = int(on.time / 120)
		noteDuration = int(off.time / 120)

		if self.index == 19: noteDuration = 6

		if self.readable == 0:
			print(self.index, on.time, off.time)

		if pauseDuration > 0:
				self.renderNote(None, pauseDuration)
				self.newColumn()
		
		self.renderNote(on.note, noteDuration)
		self.newColumn()


	def newColumn(self):
		
		if self.readable == 0: return
		if self.readable == 3: return

		self.column += 1
		if self.column < 4: 
			print(" ", end="")
			return

		self.column = 0
		print("")


	def renderNote(self, pitch, duration):

		self.noteCounter += 1
		self.totalDuration += duration

		if (pitch is None):
			octave = ""
			note = "---"
		else:
			octave = str( math.floor(pitch/12) )
			note = (
					"C_","Cs","D_","D#","E_","F_",
					"F#","G_","Gs","A_","A#","H_"
			)[pitch % 12]

		if self.readable == 0: return

		if self.readable == 1:
			print (
				str(self.index).rjust(3)
				+ ":"
				+ note 
				+ octave 
				+ ":" 
				+ str(duration) 
			,end="")
			return

		e = note + octave + ":" + str(duration)

		if pitch is None: 
			note = 0
		else:
			note = pitch - 81

		value = (((duration-1) << 4) | note) + 34

		if self.readable == 2:
			star = "-"
			if (value > 127): star = "*"
			print (
				str(value).rjust(3) 
				+ star 
				+ str(note).rjust(2) 
				+ ":" + str(duration)
			,end="")
			return

		invalid = False
		if pitch is not None and note == 0: invalid = True
		if value < 32: invalid = True
		if note > 15: invalid = True
		if value == ord("<"): invalid = True
		if value == ord(">"): invalid = True

		if invalid: 
			print("\" /* " + chr(value) + " " + e + " */ \"", end="")
		else:
			print(chr(value), end="")

if __name__ == "__main__":
	(ParseMidi()).main()