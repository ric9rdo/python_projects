# numero primo - quando for divisivel por 1 e por ele proprio
# Input do utilizador

num = int(input("Introduza um numero "))

# se o numero introduzido for maior que 1

if num >= 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "nao primo")
            break
    else:
        print(num, "primo")

# se o numero introduzido for 0

else:
    print(num, "nao primo")
