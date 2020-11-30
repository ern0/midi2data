#!/usr/bin/env python3 -B

try: import mido
except: quit("missing module: mido")
import sys


class MidiToData:

	def main(self):

		if len(sys.argv) < 2:
			quit("midi2data <filename> <columns> [<offset> = 0] [<track> = 1]")

		try: mid = mido.MidiFile(sys.argv[1])
		except: quit("error loading MIDI file")		

		try: self.cols = int(sys.argv[2])
		except: print("missing column count")

		try: self.offset = int(sys.argv[3])
		except: offset = 0

		try: selectedTrackNumber = int(sys.argv[4])
		except: selectedTrackNumber = 1

		isAnyTrackProcessed = False
		actualTrackNumber = 0
		for i,track in enumerate(mid.tracks):
			
			actualTrackNumber += 1
			if selectedTrackNumber != actualTrackNumber: 
				continue

			isAnyTrackProcessed = True

			self.prepare(track.name)
			for message in track:
				self.process(message)
			self.post()

		if not isAnyTrackProcessed:
			quit("invalid track number")


	def prepare(self, trackName):
		self.columnCounter = 0
		print("\t;---- " + trackName + " ----")


	def process(self, message):

		if message.type != "note_on": return

		if self.columnCounter == 0:
			print("\tdb ", end="")
		else:
			print(",",end="")

		print(message.note + self.offset, end="")

		self.columnCounter += 1
		if (self.columnCounter == self.cols):
			self.columnCounter = 0
			print("")


	def post(self):
		if (self.columnCounter != 0):
			print("")


if __name__ == "__main__":
	(MidiToData()).main()