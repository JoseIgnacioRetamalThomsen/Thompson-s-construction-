# Thomson's contruction using map(python dictionary) and set
# Jose Retamal
# Graph theory project GMIT 2019

# Represent a transition function for a NDA
# alphabet is represent with positive integers (1,2,3,...)
# -1 represent the empty string so first state
# state are represented as positive integers (1,2,3)
# -1 represent the state before initial state

import Shunting

class TransitionFunctionNFA:
    """
    Define a transition function using map and set.
    """

    def __init__(self, initial_state):
        """
        Create transition function with the parameterized initial state.
        :param initial_state: The initial state
        """

        # Create the map that define the transitions
        # Always (0,-1) will be used for start running the automaton
        # {actualState : { symbol : {nextStates}}
        self.m = {0: {-1: {initial_state}}}

    def printF(self):
        """
        Prints the transitions.
        :return: Nothing.
        """
        print(self.m)

    def getTransition(self, state, symbol):
        """
        Return set of next states from actual state and symbol.
        :param state: Actual state.
        :param symbol: Symbol of the alphabet.
        :return: Set of states from state with symbol, None if no states.
        """

        # check state in map
        if self.m.get(state) is not None:
            x = self.m.get(state)
            # check symbol in
            if x.get(symbol) is not None:
                # return the state after if it is
                return x.get(symbol)

    def addTransition(self, state, symbol, results={}):
        """
        Add new transition to map.
        :param state: Actual state.
        :param symbol: Symbol for transition.
        :param results: Set of states to add for the transition.
        :return: Nothing.
        """
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
    """
    Define a Nondeterministic finite automaton using the transition function and a accept state.
    state count must be initialized using initStateCount() function.
    """
    # class variable, keep count of states.
    stateCount = int

    @staticmethod
    def initStateCount(init):
        """
        Start the count
        :param init: first state on count.
        :return: Nothing.
        """
        NFA.stateCount = init

    @staticmethod
    def getNexState():
        """
        Give new state.
        :return: The next state.
        """
        # Increase count.
        NFA.stateCount += 1
        # Return new state number.
        return NFA.stateCount

    def __init__(self, symbol=None):
        """
        Create the  most basic NFA, that accept the symbol on the parameter.
        Symbol must be a character, it will be then convert to the corresponding number.
        :param symbol: Symbol that accept this automaton, if this parameter is black ir None will create a
        NFA that accept zero occurrences.
        """
        # Create NFA that accept zero occurrences
        if symbol is None:

            # Get next state
            self.stateCount = NFA.getNexState()

            # Create transition function map
            self.tf = TransitionFunctionNFA(self.stateCount)
            # set accept state
            self.acceptState = self.stateCount

            # actual set of states
            self.actualState = set()

        else:
            # Get next state.
            self.stateCount = NFA.getNexState()

            # Create transition function map
            self.tf = TransitionFunctionNFA(self.stateCount)

            # Set initial state
            self.initialState = self.stateCount

            # actual set of states
            self.actualState = set()

            # add transition for symbol
            # Set accept state
            self.acceptState = NFA.getNexState()
            # the transition will go to the accept state
            self.tf.addTransition(self.initialState, ord(symbol), {self.acceptState})

    def run(self, string):
        """
        Run the automaton.
        Return true if string is accepted false if not
        :param string: String for run on this NFA
        :return: true if the string is accept.
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

    def concat(self, automata):
        """
        Concatenate 2 automatas, this and the parameter.
        :param automata: Automaton to concadenate to this.
        :return: Nothing.
        """

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
                    # all transition that got to accept state of the first automaton.
                    # now goes also to the start state of the second automaton.
                    self.tf.addTransition(i, i1, {automata.initialState})
                    # we can remove accept state for performance
                    self.tf.m[i][i1].remove(self.acceptState)
                    # also, all empty string transition from start state of second automaton
                    self.tf.addTransition(i, i1, temp.get(-1))

        # the second automaton accept state become the accept state
        self.acceptState = automata.acceptState

        # we just merge al other transitions
        self.tf.m = {**self.tf.m, **automata.tf.m}

    def union(self, automaton):
        """
        Union of this automaton parameter automaton
        :param automaton: The automaton for perform union operation.
        :return: Nothing.
        """

        # Join to initial states
        states = automaton.tf.m.pop(0).get(-1) | self.tf.m.pop(0).get(-1)
        self.tf.addTransition(0, -1, states)

        # merge automatons
        self.tf.m = {**self.tf.m, **automaton.tf.m}

        # create new state for new accept state
        newState = NFA.getNexState()

        # all transition that goes to accept state of automaton one and two
        #  now go to the new  accepted state
        # loop through all key values (i = key, j = value)
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automata

                if self.acceptState in j1:
                    # all transition that got to accept state of the first automaton
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {newState})
                    # remove old accept state
                    self.tf.m[i][i1].remove(self.acceptState)


                elif automaton.acceptState in j1:
                    # all transition that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    self.tf.addTransition(i, i1, {newState})
                    # remove old accept state
                    self.tf.m[i][i1].remove(automaton.acceptState)

        # set accept state to the new
        self.acceptState = newState

    def star(self):
        """
        Kleene star expression, 0 or more.
        :return: Nothing.
        """

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
                # we are looking for the maps that have transition to the accepted state of first automaton

                if self.acceptState in j1:
                    # all transtion that got to accept state of the first automata
                    # now goes also to the start state of the second automate
                    #  we also need to add all the states that this state goes when move on it, mean oldInitial
                    self.tf.addTransition(i, i1, {self.initialState, newAccept} | oldInitialTransition)

        # change initial state and accept state
        self.initialState = newInitial
        self.acceptState = newAccept

    def plus(self):
        """
        Perform plus operation on this automaton, mean 1 or more.
        :return: Nothing.
        """

        # update intial state
        # create new inital and accepted state
        newInitial = NFA.getNexState()
        newAccept = NFA.getNexState()
        oldInitialTransition = self.tf.getTransition(0, -1)
        self.tf.addTransition(0, -1, {newInitial})

        # everything that get to old accept state goes to old initial state and new accept state
        for i, j in self.tf.m.items():
            # loop through all key an values in the sub map
            for i1, j1 in j.items():
                # we are looking for the maps that have transition to the accepted state of first automatn

                if self.acceptState in j1:
                    # all transtions that got to accept state of the first automaton
                    # now goes also to the start state of the second automate
                    #  we also need to add all the states that this state goes when move on it, mean oldInitial
                    self.tf.addTransition(i, i1, {self.initialState, newAccept} | oldInitialTransition)

        # change initial state and accept state
        self.initialState = newInitial
        self.acceptState = newAccept


def compile(pofix):
    """
    Create a NFA from a postfix string.
    Return the created NFA.
    :param pofix: Pofix reger for create automaton.
    :return: Compiled NFA.
    """

    # init state count
    NFA.initStateCount(1)

    stack = list();

    isEscape = False;

    for symbol in pofix:
        # Check for escape character
        if isEscape:
            # If is escape, add NFA to stack/
            stack.append(NFA(symbol))

            # For read next character as normal.
            isEscape = False
        else:
            if symbol == '/':
                # Escape for next character
                isEscape = True
            elif symbol == '|':
                # Pop first and second character from stack.
                second = stack.pop()
                first = stack.pop()
                # Union second automaton to first.
                first.union(second)
                # Push new NFA to stack.
                stack.append(first)

            elif symbol == '.':
                # Pop from stack
                second = stack.pop()
                first = stack.pop()
                # Concatenate second automaton to first.
                first.concat(second)
                # Push new NFA to stack.
                stack.append(first)
            elif symbol == '*':
                # Apply star to the top NFA in the stack.
                stack[-1].star()
            elif symbol == '?':
                # Pop top of stack
                first = stack.pop()
                # Create a NFA that accept any
                n = NFA()
                # Union the first NFA to the any for none or one.
                first.union(n)
                # Push to stack
                stack.append(first)
            elif symbol == '+':
                # Apply plus to NFA on top of the stack.
                stack[-1].plus()
            elif symbol == '-':
                # Remove top elements from stack
                second = stack.pop()
                first = stack.pop()
                # Get the first character for the range
                init = list(first.tf.m.get(first.initialState).keys())[-1]
                # Get second charracter for range
                last = list(second.tf.m.get(second.initialState).keys())[-1]
                # Union of all characters on range
                for i in range(init + 1, last + 1):
                    first.union(NFA(chr(i)))
                # Push new NFA to stack.
                stack.append(first)


            else:
                # Add new NFA to stack, most basic.
                stack.append(NFA(symbol))

    # Return the new created NFA
    # Since we are using Thomson's constructions we are guarantee that
    # There is only one character left on the stack.
    return stack.pop()


class Runner:
    """
    For run several stings on one automaton.
    """

    # Compiled NFA/
    nfa = None

    # actual state
    actualState = set()

    # results states after run one symbol
    nextState = set()

    def __init__(self, infix):
        """
        Create object with a infix regex, compile the nfa with it.
        :param infix: The infix regex
        """
        # Convert infix string into postfix and then compile the NFA.
        self.nfa = compile(Shunting.Converter().toPofix(infix))

        # add initial state
        self.actualState |= self.nfa.tf.getTransition(0, -1)

    def runNext(self, string):
        """
        Run a string on the NFA
        :param string: String to run
        :return: No return.
        """
        # loop through each character in the string
        for symbol in string:
            # loop througj all acutal states
            for state in self.actualState:
                # check for trasition on state  and symbol
                tempStates = self.nfa.tf.getTransition(state, ord(symbol))
                if tempStates is not None:
                    # all new states
                    self.nextState |= tempStates

            # add states for next symbol
            self.actualState = set() | self.nextState
            # clear
            self.nextState.clear()

    def finish(self):
        """
        Finish the run on the automaton
        :return: True if the string match on the automaton
        """

        # check if any of the last state is accepted
        return (self.nfa.acceptState in self.actualState)


class RunChar:
    """
    For run one character at a time on a automaton.
    """
    # Compiled NFA/
    nfa = None

    # actual state
    actualState = set()

    # results states after run one symbol
    nextState = set()

    previus = set()

    def __init__(self, infix):
        """
        Create object with a infix regex, compile the nfa with it.
        :param infix: The infix regex
        """
        # Convert infix string into postfix and then compile the NFA.
        self.nfa = compile(Shunting.Converter().toPofix(infix))

        # add initial state
        self.actualState |= self.nfa.tf.getTransition(0, -1)

    def run(self, symbol):
        """
        Run one symbon on automaton
        :param symbol: symbol to run on automaton
        :return: true if there are states from transition
        """
        # loop througj all acutal states
        for state in self.actualState:
            # check for trasition on state  and symbol
            tempStates = self.nfa.tf.getTransition(state, ord(symbol))
            if tempStates is not None:
                # all new states
                self.nextState |= tempStates

        # add states for next symbol, replace actual state by next state set
        self.actualState = set() | self.nextState

        # clear
        self.nextState.clear()

        return (len(self.actualState) != 0)

    def check(self):
        """
        Finish the run on the automaton
        :return: True if the string match on the automaton
        """

        # check if any of the last state is accepted
        return (self.nfa.acceptState in self.actualState)

    def clear(self):
        # actual state
        actualState = set()

        # results states after run one symbol
        nextState = set()
        # add initial state
        self.actualState |= self.nfa.tf.getTransition(0, -1)
