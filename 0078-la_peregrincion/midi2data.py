#!/usr/bin/env python3 -B

try: import mido
except: quit("missing module: mido")
import sys
import math


class MidiToData:

	def main(self):

		self.parseArgs()
		self.processFile()


	def parseArgs(self):

		if len(sys.argv) < 2:
			quit("midi2data <filename> <format> <columns> [<offset> = 0] [<track> = 1]")

		try: self.midiData = mido.MidiFile(sys.argv[1])
		except: quit("error loading MIDI file")		

		self.format = sys.argv[2]
		if not (self.format == "midi" or self.format == "const"):
			quit("format must be \"midi\" or \"const\"")

		try: self.cols = int(sys.argv[3])
		except: print("missing column count")

		try: self.offset = int(sys.argv[4])
		except: offset = 0

		try: self.selectedTrackNumber = int(sys.argv[5])
		except: self.selectedTrackNumber = 1


	def processFile(self):

		isAnyTrackProcessed = False
		actualTrackNumber = 0
		for i,track in enumerate(self.midiData.tracks):
			actualTrackNumber += 1

			if self.selectedTrackNumber == actualTrackNumber: 
				isAnyTrackProcessed = True
				self.processTrack(track)

		if not isAnyTrackProcessed:
			quit("invalid track number")


	def processTrack(self, track):

			self.prepareData(track.name)
			for message in track: 
				self.processMessage(message)
			self.postProcessTrack()


	def prepareData(self, trackName):
		self.columnCounter = 0
		print("\t;---- " + trackName + " ----")


	def processMessage(self, message):

		if message.type != "note_on": return

		if self.columnCounter == 0:
			print("\tdb ", end="")
		else:
			print(",",end="")

		pitch = message.note + self.offset
		if self.format == "midi":
			print(pitch, end="")
		else:
			print(self.renderConst(pitch), end="")

		self.columnCounter += 1
		if (self.columnCounter == self.cols):
			self.columnCounter = 0
			print("")


	def postProcessTrack(self):

		if (self.columnCounter != 0):
			print("")


	def renderConst(self, pitch):

		octave = str( math.floor(pitch/12) )
		note = (
				"C_","Cs","D_","Ds","E_","F_",
				"Fs","G_","Gs","A_","As","H_"
		)[pitch % 12]

		return note + octave


if __name__ == "__main__":
	(MidiToData()).main()