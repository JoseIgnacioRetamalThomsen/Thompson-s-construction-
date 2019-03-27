# Shunting algorithm

# Jose Retamal
# Graph theory project GMIT 2019

# This algorithm is base on:
# http://www.oxfordmathcenter.com/drupal7/node/628
# https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90

class Converter:
    """
       Methods for converting string.
       toPofix() implement, method that convert a infix string into a
       postfix string.
    """

    def toPofix(self, infix):
        """
        Convert infix string to postfix string.
        :param infix: infix string to convert
        :return: postfix string.
        """

        # Order of preference for specials characters
        specials = {'-': 60, '*': 50, '+': 46, '?': 43, '.': 40, '|': 30}

        # Stack for convert.
        stack = list()

        # For create the postfix result string.
        pofix = ""

        for c in infix:
            if c == '(':
                # Push to stack.
                # Will server as a marker.
                stack.append(c)
            elif c == ')':
                # Look at the stack.
                # stack[-1] works as stack.peek().
                while stack[-1] is not '(':
                    # pop from stack and append it to postfix result
                    pofix = pofix + stack.pop()

                # Remove '(' from the stack.
                stack.pop()

            elif c == '/':
                # escape character, append it to stack
                pofix = pofix + c

            elif c in specials:
                # While there is something on the stack
                # and C (actual) precedence is less or equals of the last special on the stack
                # pop from stack and put into pofix.
                # get(c,0) look for c and if is not in returns 0.
                while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                    # pop from stack and then add it to postfix result
                    pofix = pofix + stack.pop()

                # add character to stack
                stack.append(c)
            else:
                # Normal character just added to postfix regular expression.
                pofix = pofix + c;

        # Push anything left in the stack to the end of the pofix.
        while stack:
            # Push character from stack.
            pofix = pofix + stack.pop()

        # return result
        return pofix
