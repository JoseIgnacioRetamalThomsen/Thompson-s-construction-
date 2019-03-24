# Thomson's contruction using map(ptython dictionary) and set

# Jose Retamal

# Represent a transition function for a NDA
# alphabet is represent with positive integers (1,2,3,...)
# -1 represent the empty string so first state
# state are represented as positive integers (1,2,3)
# -1 represent the state before initial state

class TransitionFunctionNFA:
    """Define a transtion function using map and set."""

    # constructor
    def __init__(self, initial_state):
        """Create transition function with the parameterized initial state."""

        # map that define the transitions
        self.m = {0: {-1: {initial_state}}}  # send to initial state

    # prints the transitions
    def printF(self):
        print(self.m)

    def getTransition(self, state, symbol):
        """ Return set of next states from actual state and symbol."""

        # check state in map
        if self.m.get(state) is not None:
            x = self.m.get(state)

            # check symbol in
            if x.get(symbol) is not None:
                # return the state after if it is
                return x.get(symbol)

    def addTransition(self, state, symbol, results={}):
        """Add new transition to map."""

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
    """ Define a Nondeterministic finite automaton using the transition function and a accept state.
        state count must be initialized using initStateCount() function.
    """
    # class variable, keep count of states.
    stateCount = int

    @staticmethod
    def initStateCount(init):
        """Initialize state count."""
        NFA.stateCount = init

    @staticmethod
    def getNexState():
        """Gives next state. """
        NFA.stateCount += 1
        return NFA.stateCount




    def __init__(self, symbol = None):
        """ Create the  most basic NFA, that accept the symbol on the parameter.
            Symbol must be a character, it will be then convert to the corresponding number.
        """
        if symbol is None:
            # self.stateCount = initialState
            self.stateCount = NFA.getNexState()

            # the map of transitions
            self.tf = TransitionFunctionNFA(self.stateCount)
            self.acceptState = self.stateCount

            # actual set of states
            self.actualState = set()

        else:
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
            # Set accept state
            self.acceptState = NFA.getNexState()
            # the transition will go to the accept state
            self.tf.addTransition(self.initialState, ord(symbol), {self.acceptState})

    #
    # return true if string is accepted false if not
    def run(self, string):
        """ Run the automaton.
            Return true if string is accepted false if not.
        """

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
        """Concatenate this automata to the one on the parameter."""

        # remove the initial transition
        temp = automata.tf.m.pop(0)

        # any transition that get to initial state of the first automaton(this)
        # should now go  also to the initial state of the second automaton(the one on
        # function parameter).

        # loop through all key values (i = key, j = value)
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automaton
                if self.acceptState in j1:
                    # all transition that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {automata.initialState})
                    # also, all empty string transition from start state of second automaton
                    self.tf.addTransition(i, i1, temp.get(-1))

        # the second automaton accept state become the accept state
        self.acceptState = automata.acceptState

        # we just merge al other transitions
        self.tf.m = {**self.tf.m, **automata.tf.m}

    # union
    def union(self, automata):
        """ Union of this automaton to the parameter one."""

        # remove the initial transition from automaton 2

        # the initial state goes to both automatas initial state
        #  create new initial state  give by NFA.getNextState()
        #  update automaton initial transition, add both initial state and the new state
        states = automata.tf.m.pop(0).get(-1) | self.tf.m.pop(0).get(-1) | {NFA.getNexState()}
        self.tf.addTransition(0, -1, states)

        # merge two automaton
        self.tf.m = {**self.tf.m, **automata.tf.m}

        # create new state for be the accept state
        newState = NFA.getNexState()

        # all transition that goes to accept state of automaton one and two
        #  now go to the final accepted state
        # loop through all key values (i = key, j = value)
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automata

                if self.acceptState in j1:
                    # all transition that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {newState})

                if automata.acceptState in j1:
                    # all transition that got to accept state of the first automata
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
        oldInitialTransition = self.tf.getTransition(0, -1)
        self.tf.addTransition(0, -1, {newInitial, newAccept})

        # everything that get to old accept state goes to old initial state and new accept state
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automatn

                if self.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    #  we also need to add all the states that this state goes when move on it, mean oldInitial
                    self.tf.addTransition(i, i1, {self.initialState, newAccept} | oldInitialTransition)

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
        elif symbol == '*':
            stack[-1].star()
        elif symbol =='?':
            first = stack.pop()
            n = NFA()
            first.union(n)
            stack.append(first)
        else:
            stack.append(NFA(symbol))

    print(len(stack))
    nfa = stack.pop();
    nfa.tf.printF()
    return nfa
