from typing import Callable


class State():
    def __init__(self, name: str, value: str, isFinal: bool):
        self.name = name
        self.isFinal = isFinal
        self.value = value
        self.transitions: dict[str, list['State']] = {}
        self.onNavigates: dict[str, Callable[['State', str], 'None']] = {}

    def addTransition(self, symbol: str, state: 'State', onNavigate: Callable[['State', str], 'None'] = None):
        if symbol in self.transitions:
            self.transitions[symbol].append(state)
        else:
            self.transitions[symbol] = [state]

        self.onNavigates[symbol] = onNavigate

    def getNextState(self, symbol: str):
        return self.transitions.get(symbol)
    
    def make_final(self):
        self.isFinal = True
