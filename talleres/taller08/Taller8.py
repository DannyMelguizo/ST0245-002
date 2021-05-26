def evaluate():
    result = 0
    exp = input('Ingrese la expresion a evaluar: ')
    exp = exp.split()
    for i in exp:
        if i.isnumeric():
            exp.push(int(i))
        else:
            result = operate(i, exp.pop(), exp.pop())
            exp.push(result)
    return result

def operate(op, a, b):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }.get(op, 'Operando No Aceptado')

print(evaluate())