from src.gmit.re.com import ThomsonsMap
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        print("hello")

        ThomsonsMap.NFA.initStateCount(1)

        string = "/*.((a-z)|(0-9)|/.)*.@.((a-z)|(0-9))*./..(a-z)+"
        #s1 = "(0|(1.(0.1*(0.0)*.0)*.1)*)*"
        s1 = "a?"
        p = Shunting.Converter().toPofix(s1)
        print(p)
        n = ThomsonsMap.compile(p)
       # n.tf.printF()
        print(n.run("aa"))

        n = ThomsonsMap.NFA("z")
        n.plus()
        print(n.run(""))
        n.tf.printF()

        print("last")
        print(Thomsons.match("(a-z)*.@.((a-z)|(0-9))*./.","af@fd4d3a."))
        print(Thomsons.match("(a.b.c)+", ""))
        print(Shunting.Converter().toPofix("a|(((a.b)*.(a|b)).a*)"))