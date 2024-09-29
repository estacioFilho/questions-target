def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

def check_fibonacci(number_to_check):
    if number_to_check < 0:
        return "O número deve ser maior ou igual a 0."
    
    fib_sequence = fibonacci_sequence(number_to_check)
    if number_to_check in fib_sequence:
        sequence = fibonacci_sequence(number_entered)
        return f"O número {number_to_check} pertence à sequência de Fibonacci.\nSeguêcia: {sequence}"
    else:
        return f"O número {number_to_check} NÃO pertence à sequência de Fibonacci."

number_entered = int(input("Digite um número para verficar se existe na seguêcia de Fibonacci: "))
result = check_fibonacci(number_entered)
print( f"{result}")