#Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
#The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should 
#return 5 + 3 = 8. For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
#should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
#You can assume the given expression is always valid.

#In comparison testing of reverse Polish notation with algebraic notation, reverse Polish has 
#been found to lead to faster calculations, for two reasons. The first reason is that 
#reverse Polish calculators do not need expressions to be parenthesized, fewer operations 
#need to be entered to perform typical calculations. Additionally,users of reverse Polish 
#calculators made fewer mistakes than for other types of calculator.[9] [10] Later research 
#clarified that the increased speed from reverse Polish notation may be attributed to the smaller number of 
#keystrokes needed to enter this notation, rather than to a smaller cognitive load on its users.
#[11] However, anecdotal evidence suggests that reverse Polish notation is more 
#difficult for users to learn than algebraic notation.[10]

#for each token in the postfix expression:
#  if token is an operator:
#    operand_2 ← pop from the stack
#    operand_1 ← pop from the stack
#    result ← evaluate token with operand_1 and operand_2
#    push result back onto the stack
#  else if token is an operand:
#    push token onto the stack
#result ← pop from the stack

ops = {
        "+": (lambda a,b: a+b),
        "-": (lambda a,b: a-b),
        "*": (lambda a,b: a*b),
        "/": (lambda a,b: a/b)
        }


def eval(expression):
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token in ops:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = ops[token](operand1,operand2)
            stack.append(result)
        else:
            stack.append(int(token))
        #Sprint (stack)
    return stack

print(eval("15 7 1 1 + - / 3 * 2 1 1 + + -"))