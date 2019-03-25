from src.gmit.re.com import ThomsonsMap
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        # print("hello")
        #
        ThomsonsMap.NFA.initStateCount(1)

        string = "/*.((a-z)|(0-9)|/.)*.@.((a-z)|(0-9))*./..(a-z)+"
        p = Shunting.Converter().toPofix(string)
        print(p)
        n = ThomsonsMap.compile(p)
        n.tf.printF()
        print(n.run("*af5.af@fdaf1a.ie"))

        n = ThomsonsMap.NFA("z")
        n.plus()
        print(n.run(""))
        n.tf.printF()

        print("last")
        print(Thomsons.match("b-y","z"))