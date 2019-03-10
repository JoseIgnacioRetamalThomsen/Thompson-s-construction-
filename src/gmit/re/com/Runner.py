from src.gmit.re.com import MapTransitionFunction


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        print("hello")

        MapTransitionFunction.NFA.initStateCount(1)

        a1 = MapTransitionFunction.NFA(1)

        a1.tf.printF()

        a2 = MapTransitionFunction.NFA(2)

        a2.tf.printF()

        print(a1.run("0"))
        a1.concat(a2)
        print(a1.run("12"))
