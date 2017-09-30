"""PyAudio Example: Play a wave file (callback version)"""
import wave

import pyaudio

from wavPlayer import WavPlayer

p = pyaudio.PyAudio()
waveFile = wave.open('lilKick.wav', 'rb')

index=0
for i in range(1000):
	print("yeah " + str(index))
	index += 1
	w = WavPlayer(waveFile, p)
