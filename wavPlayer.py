"""PyAudio Example: Play a wave file (callback version)"""

import pyaudio
import time


class WavPlayer(object):
	def __init__(self, waveFile, pyAudio):
		self._wf = waveFile

		self._pyAudio = pyAudio

		self._stream = self._pyAudio.open(format=self._pyAudio.get_format_from_width(self._wf.getsampwidth()),
						channels=self._wf.getnchannels(),
						rate=self._wf.getframerate(),
						output=True,
						stream_callback=self.callback)
		self._stream.start_stream()

		# while self._stream.is_active():
		time.sleep(0.1)

		self._stream.stop_stream()
		# self._stream.close()
		self._wf.rewind()

	def callback(self, in_data, frame_count, time_info, status):
		data = self._wf.readframes(frame_count)
		return (data, pyaudio.paContinue)



