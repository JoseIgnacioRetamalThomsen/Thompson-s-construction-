# Represent a transition function for a NDA
# alphabet is represent with positive integers (0,1,...)
# 0 represent the empty string so first state
# state are represented as any integer
# -1 represent the state before initial state
# 0 intitial state
class TransitionFuncion:

    def __init__(self):
        self.m = {}
        self.addTransition(0, -1, {1})

    # add states to the map
    # parameters:
    # initialState : initial state of the transaction
    # simbol : simbol of the alphabet (0,1)
    # final state : set of states after the transition
    def addTransition(self, initialState, symbol, finalStates={}):

        # check if there is any transition in the inputed states and symbol
        # if the is a transition it will append the new final states
        # Check if the state is in the transition function
        if initialState in self.m:
            if symbol in self.m[initialState]:
                self.m[initialState][symbol] = self.m[initialState][symbol].union(finalStates)
            else:
                self.m[initialState].append[{symbol: finalStates}]
        else:
            self.m[initialState] = [{symbol: finalStates}]

    def getstate(self, actualstate, symbol):
        if actualstate in self.m:
            if symbol in self.m[actualstate]:
                return self.m[actualstate][symbol]


class TransitionFunctionNFA:

    def __init__(self, initial_state):

        # map that define the transitions
        self.m = {0: [{-1: {initial_state}}]}  # send to initial state

    # prints the transitions
    def printF(self):
        print(self.m)

    # get set of states for the state and symbol in the parameters
    def getTransition(self, state, symbol):
        # loop for all the maps of states in m
        if self.m.get(state) != None:
            for x in self.m.get(state):
                # check if the current map has the symbol as key
                if (symbol in x.keys()):
                    # if the map has that key return the set of states
                    return x.get(symbol)

    def addTransition(self, state, symbol, results={}):
        # check if the state and symbol are in the structure
        states = self.getTransition(state, symbol)

        if states != None:
            for x in self.m.get(state):
                if symbol in x.keys():
                    x[symbol] = x.get(symbol) | results
                    break
        else:
            if self.m.get(state) != None:
                self.m.get(state).append({symbol: results})
            else:
                self.m[state] = [{symbol: results}]


class NFA:
    stateCount = 1

    def __init__(self, symbol):

        self.tf = TransitionFunctionNFA(self.stateCount)
        self.initialState = self.stateCount
        self.stateCount += 1
        self.actualState = {}

        # add transition for symbol
        self.tf.addTransition(self.initialState, symbol, {self.stateCount})
        self.acceptState = self.stateCount
        self.stateCount += 1

    def run(self, string):
        self.actualState = set()
        self.actualState = self.actualState | self.tf.getTransition(0, -1)

        self.nextState = set()

        for symbol in string:

            for state in self.actualState:

                if self.tf.getTransition(state, int(symbol)) is not None:
                    self.nextState = self.nextState | self.tf.getTransition(state, int(symbol))

                self.actualState = set() | self.nextState
                if len(self.actualState) is 0:
                    return False

                self.nextState.clear()

        if self.acceptState in self.actualState:
            return True
        return False
