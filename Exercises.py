
#fibonacci
def fibonacci(n):
    a = 0
    b = 1

    for k in range(n):
        c = a + b
        a = b
        b = c

    return b

for x in range(20):
    print(fibonacci(x))




#pallidrome
palindromoe = [
    'este no es un palindromo',
    'anita lava la tina',
    'oso',
    123321
]

def es_palindromo(p):
    estandar = str(p).lower().replace(' ', '')
    return estandar == estandar[::-1]

if __name__ == '__main__':
    for p in palindromoe:
        result = es_palindromo(p)
        print(result)




#num = int(input("Enter a number"))
num = 15

if num<=1:
    print (num, "is not a prime number")
else:
    for i in range(2,num):
        if(num%i)==0:
            print (num,"is not a prime number")
            break
    else:
        print (num, "is a prime number")
