#FATORIAL COM RECURSÃO

def fatorial(num):
    if num <= 1:
        return 1
    else:
        return(num * fatorial(num -1))

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

x = input("Digite um valor inteiro p/ calcular o fatorial dele: ")
x = int(x)
print(fatorial(x))

#FIBONACCI COM RECURSÃO

y = input("Digite um valor inteiro p/ saber a sequência fibonacci dele: ")
y = int(y)
print(fib(y))
for i in [1,2,3,4,5]:
    print(i, '=>', fib(i))
