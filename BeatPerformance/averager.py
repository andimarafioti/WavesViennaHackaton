from numpy import mean


class Averager(object):
	COUNT = 8

	def __init__(self):
		self._values = []

	def addValue(self, value):
		if len(self._values) < self.COUNT:
			self._values.append(value)
		else:
			meaned = mean(self._values[-self.COUNT:])
			if abs(value - meaned) / meaned < 0.75:
				self._values.append(value)

	def getAverage(self):
		return mean(self._values[-8:])
