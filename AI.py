from abc import ABCMeta, abstractmethod
from enum import Enum, unique


class AI:
	__metaclass__ = ABCMeta

	@unique
	class Action (Enum):
		MOVEUP = 0
		MOVEDOWN = 1
		MOVELEFT = 2
		MOVERIGHT = 3
		
	@abstractmethod
	def getAction(self, number: int):
		pass