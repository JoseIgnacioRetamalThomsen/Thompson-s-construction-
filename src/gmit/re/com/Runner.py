from src.gmit.re.com import MapTransitionFunction



class Runner:
    # main method, start of program
    if __name__ == '__main__':

        # create automata that regonize only 1
        n = MapTransitionFunction.NFA(1)
        print(n.run("1"))
        print(n.run("01"))
        print(n.run("11"))
        # add transition for the automata to recognize any number of 1'
        n.tf.addTransition(2,1,{2})
        print(n.run("111111111111111111111"))
        print(n.run("1111111111111111111110"))
        print(n.run("0111111111111111111111"))

        n1=MapTransitionFunction.NFA(0);
        print(n1.run("0"))