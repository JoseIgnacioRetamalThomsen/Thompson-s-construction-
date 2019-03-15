from src.gmit.re.com import MapTransitionFunction
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        # print("hello")
        #
        MapTransitionFunction.NFA.initStateCount(1)
        #
        # a1 = MapTransitionFunction.NFA(1)
        # a2 = MapTransitionFunction.NFA(2)
        #
        # # 12
        # a1.concat(a2)
        #
        # a3 = MapTransitionFunction.NFA(1)
        # a4 = MapTransitionFunction.NFA(2)
        #  # 1 or 2
        # a3.union(a4)
        #
        # a3.star()
        # # 12.(1or2)*
        # a1.concat(a3)
        #
        # print(a1.run("1211"))
        #
        # a5 = MapTransitionFunction.NFA(2)
        # a6 = MapTransitionFunction.NFA(2)
        # a5.concat(a6)
        # a1.concat(a5)
        # # 12.(1or2)*.22
        #print(a1.run("1211111122"))

        u1 = MapTransitionFunction.NFA(1)
        u2= MapTransitionFunction.NFA((int)(2))
        u1.concat(u2)

        print(u1.run("12"))

        u3 = MapTransitionFunction.NFA((int)(3))
        u4 = MapTransitionFunction.NFA((int)(4))

        u3.concat(u4)

        u1.union(u3)

        print(u1.run(""))

        s = Shunting.Converter()
        print(s.toPofix("(a.b)|(c*.d)"))

        print(Thomsons.compile(("(a.b)|(c*.d)")))