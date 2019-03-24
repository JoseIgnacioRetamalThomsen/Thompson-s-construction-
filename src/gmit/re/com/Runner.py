from src.gmit.re.com import ThomsonsMap
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        # print("hello")
        #
        ThomsonsMap.NFA.initStateCount(1)

        string = "a*.b?.c"
        p = Shunting.Converter().toPofix(string)
        n = ThomsonsMap.compile(p)
        print(n.run("aaaaaabcc"))
