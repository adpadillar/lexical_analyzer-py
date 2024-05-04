from types import NoneType
from typing import Callable


class State():
    def __init__(self, name: str, value: str, isFinal: bool):
        self.name = name
        self.isFinal = isFinal
        self.value = value
        self.transitions: dict[str, 'State'] = {}
        self.onNavigates: dict[str, Callable[['State', str], NoneType]] = {}

    def addTransition(self, symbol: str, state: 'State', onNavigate: Callable[['State', str], NoneType] = None):
        self.transitions[symbol] = state
        self.onNavigates[symbol] = onNavigate

    def getNextState(self, symbol: str):
        return self.transitions.get(symbol)
