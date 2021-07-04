# valor = 3  # Digite o valor do termo que deseja identificar na sequencia Fibonacci
from timeit import timeit

def fib_sequence(valor: int) -> int:
    global valor_seq
    ult_num = 1
    pen_nun = 1

    if valor == 0:
        return 0
    elif valor == 1 or valor == 2:
        return 1
    else:
        for count in range(2, valor):
            valor_seq = ult_num + pen_nun
            pen_nun = ult_num
            ult_num = valor_seq
            count += 1
        return valor_seq


if __name__ == '__main__':
#    print(f'O número equivalente ao termo {valor} na sequência Fibonacci é: {fib_sequence(valor)}')

# Teste
    assert fib_sequence(0) == 0, f"The function returned {fib_sequence(0)}"
    assert fib_sequence(1) == 1, f"The function returned {fib_sequence(1)}"
    assert fib_sequence(2) == 1, f"The function returned {fib_sequence(2)}"
    assert fib_sequence(5) == 5, f"The function returned {fib_sequence(5)}"
    assert fib_sequence(10) == 55, f"The function returned {fib_sequence(10)}"

    print(timeit('fib_sequence(15)', globals=globals(), number=10000))