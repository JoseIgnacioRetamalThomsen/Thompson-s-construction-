from src.gmit.re.com import ThomsonsMap
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        # print("hello")
        #
        ThomsonsMap.NFA.initStateCount(1)

        string = "(a.b)*.c"
        sp = Shunting.Converter().toPofix(string)
        print(sp)

        nfa = ThomsonsMap.compile(sp)
        string1 = "ababc"
        print(nfa.run(string1))

        print(Thomsons.match(string, string1))