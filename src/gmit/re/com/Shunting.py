
# http://www.oxfordmathcenter.com/drupal7/node/628
# https://web.microsoftstream.com/video/29de6c7c-9379-46d3-99e8-8a3dbafe391f?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D467
class Converter:
    print ("Converter")

    def toPofix(self,infix):

        #
        specials = {'*':50,'.':40,'|':30}

        stack = ""
        pofix = ""

        for c in infix:
            if c== '(':
                # push to stack
                # will server as a marker
                stack = stack + c
            elif c ==')':
                 # look at the stack
                 # -1 element in string represent the last character in the string
                while stack[-1] is not '(':
                    # push character from stack
                    pofix = pofix + stack[-1]
                    # remove from stack?
                    stack = stack[:-1]
                stack = stack[:-1]
            elif c in specials:
                # while there is something on the stack
                # and C (actual) precedence is less or equals of the last special on the stack
                # pop from stack and put into pofix
                # get(c,0) look for c and if is not in returns 0
                while stack and specials.get(c,0) <= specials.get(stack[-1],0):
                    pofix = pofix + stack[-1]
                    # remove from stack?
                    stack = stack[:-1]
                stack = stack +c

            else:
                # normal character just added to postfix regular expresion
                pofix = pofix + c;

        # push anything left in the stack to the end of the pofix
        while stack:
            # push character from stack
            pofix = pofix + stack[-1]
            # remove from stack?
            stack = stack[:-1]
        stack = stack[:-1]

        return pofix