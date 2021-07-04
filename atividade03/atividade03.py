#! /usr/bin/python3.8
""""
Beleza então dever de casa número 2
Construa uma função que gere N números da sequência de Fibonacci
Input um valor N.
Output o número equivalente a N na sequência
Exemplo:
Para input n igual a 3
A sequência Fibonacci segue: 0 1 1 2 3 5 8...
A resposta é: 2
"""
from timeit import timeit

def fib_sequence(valor: int) -> int:
    fibo1, fibo2 = 0, 1
    if valor == 0 or valor == 1:
        return valor

    while valor > 1:
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        valor -= 1
    return  fibo2

if __name__ == '__main__':


#    valor = int(input('Digite um número: '))
#    print(f'O número equivalente a {valor} na sequências Fibonacci é {fib_sequence(valor)}')

# Tests
    assert fib_sequence(0) == 0, f"The function returned {fib_sequence(0)}"
    assert fib_sequence(1) == 1, f"The function returned {fib_sequence(1)}"
    assert fib_sequence(2) == 1, f"The function returned {fib_sequence(2)}"
    assert fib_sequence(5) == 5, f"The function returned {fib_sequence(5)}"
    assert fib_sequence(10) == 55, f"The function returned {fib_sequence(10)}"

    print(timeit('fib_sequence(100)', globals=globals(), number=10000))
