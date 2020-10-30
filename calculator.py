def operations(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': 
        try:    
            n = a / b
            return n
        except ZeroDivisionError:
            print ("you can not divide number by zero")

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def calculator(expression):
    tokens = expression
    values = []
    ops = []
    i = 0
    while i < len(tokens):
#space manage         
        if tokens[i] == ' ':
            i += 1
            continue
# appending "(" in tokens list        
        elif tokens[i] == '(':
            ops.append(tokens[i])
# appending values in values list
        elif tokens[i].isdigit():
            val = 0
 
            while (i < len(tokens) and
                tokens[i].isdigit()):
             
                val = (val * 10) + int(tokens[i])
                i += 1
             
            values.append(val)

             
            i-=1
    
#calculating value wthin brackets        
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
             
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(operations(val1, val2, op))
             
            ops.pop()
         
        else:
#calculating values based on precendence         
            while (len(ops) != 0 and precedence(ops[-1]) >=precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(operations(val1, val2, op))
             
# appending operators
            ops.append(tokens[i])
        
        i += 1
 
    return values[-1]
    
expression = input("give your expression = ")
print(calculator(expression))