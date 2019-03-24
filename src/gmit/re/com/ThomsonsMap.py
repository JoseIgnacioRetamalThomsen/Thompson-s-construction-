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

    # constructor
    def __init__(self, initial_state):

        # map that define the transitions
        self.m = {0: {-1: {initial_state}}}  # send to initial state

    # prints the transitions
    def printF(self):
        print(self.m)

    # get set of states for the state and symbol in the parameters
    def getTransition(self, state, symbol):

        # check state in map
        if self.m.get(state) is not None:
            x = self.m.get(state)

            # check symbol in
            if x.get(symbol) is not None:
                # return the state after if it is
                return x.get(symbol)

    #  add new transition to map
    def addTransition(self, state, symbol, results={}):

        # check if state is in map
        x = self.m.get(state)
        if x is not None:
            # check if symbol is in state map
            if symbol in x.keys():
                # state and symbol are in so append
                x[symbol] = x.get(symbol) | results
            else:
                # only state is so add the new sybmol to map
                self.m.get(state).append({symbol: results})
        else:
            # add new entry to map
            self.m[state] = {symbol: results}


class NFA:
    # class state count
    stateCount = int

    @staticmethod
    def initStateCount(init):
        NFA.stateCount = init

    # give the next state
    @staticmethod
    def getNexState():
        NFA.stateCount += 1
        return NFA.stateCount

    # create the simple NFA with 1 transtion (accept a one symbol string)
    def __init__(self, symbol):
        # all different states
        # self.stateCount = initialState
        self.stateCount = NFA.getNexState()

        # the map of transitions
        self.tf = TransitionFunctionNFA(self.stateCount)

        # the initial state
        self.initialState = self.stateCount

        # actual set of states
        self.actualState = set()

        # add transition for symbol

        # the transition will go to the accept state
        self.acceptState = NFA.getNexState()
        self.tf.addTransition(self.initialState, ord(symbol), {self.acceptState})

    # run the automate
    # returnt true if string is accepted false if not
    def run(self, string):

        # actual state
        actualState = self.actualState

        # go to initial state
        # note o and -1 are always used for start
        actualState = actualState | self.tf.getTransition(0, -1)

        # results states after run one symbol
        nextState = set()

        # loop through each character in the string
        for symbol in string:
            # loop througj all acutal states
            for state in actualState:
                # check for trasition on state  and symbol
                tempStates = self.tf.getTransition(state, ord(symbol))
                if tempStates is not None:
                    # all new states
                    nextState = nextState | tempStates

            # add states for next symbol
            actualState = set() | nextState
            # clear
            nextState.clear()

        # check if any of the last state is accepted
        if self.acceptState in actualState:
            return True
        return False

    # concatenate 2 automatas (and)
    def concat(self, automata):
        print("concat")

        # remove the initial transition
        temp = automata.tf.m.pop(0)

        # any transition that get to initial state of the first automata(this)
        # should now go  also to the initial state of the second automata(the one on
        # function paramet).

        # loop through all key values (i = key, j = value)
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automata

                if self.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {automata.initialState})
                    # also, all empty string transition from start state of second automata
                    self.tf.addTransition(i, i1, temp.get(-1))

        # the second automata accept state become the accept state
        self.acceptState = automata.acceptState

        # we just merge al other transitions
        self.tf.m = {**self.tf.m, **automata.tf.m}

    # union
    def union(self, automata):
        print("union")

        # remove the initial transition from automata 2

        # the initial state goes to both automatas initial state
        #  create new initial state  give by NFA.getNextState()
        #  update automata initial transition, add both initial state and the new state
        states = automata.tf.m.pop(0).get(-1) | self.tf.m.pop(0).get(-1) | {NFA.getNexState()}
        self.tf.addTransition(0, -1, states)

        # merge two automatas
        self.tf.m = {**self.tf.m, **automata.tf.m}

        # create new state for be the accept state
        newState = NFA.getNexState()

        # all transition that goes to accept state of automata one and two
        #  now go to the final accepted state
        # loop through all key values (i = key, j = value)
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automata

                if self.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {newState})

                if automata.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {newState})

        # set accept state to the new
        self.acceptState = newState


    def star(self):
        print("star")

        # update intial state
        # create new inital and accepted state
        newInitial = NFA.getNexState()
        newAccept = NFA.getNexState()
        oldInitialTransition = self.tf.getTransition(0,-1)
        self.tf.addTransition(0,-1,{newInitial,newAccept})

        # eveething that get to old acept state goes to old initial state and new accept state
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automata

                if self.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    #  we also need to add all the states that this state goes when move on it, mean oldInitial
                    self.tf.addTransition(i, i1, {self.initialState,newAccept} | oldInitialTransition)



        # change initial state and accept state

        self.initialState = newInitial
        self.acceptState = newAccept


def compile(pofix):

    stack = list();
    for symbol in pofix:
        if symbol == '|':
            print('ds')
            second = stack.pop()
            first = stack.pop()
            first.union(second)
            stack.append(first)

        elif symbol == '.':
            second = stack.pop()
            first = stack.pop()
            first.concat(second)
            stack.append(first)
        elif symbol =='*':
            stack[-1].star()
        else:
            stack.append(NFA(symbol))

    print(len(stack))
    nfa = stack.pop();
    nfa.tf.printF()
    return nfa
