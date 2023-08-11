a = 24
b = 44
c = 27
# test expression
if a <= 0:
    print(a)
    # statement to be run
print(b)

if a > b:
    print("a is greater than b")
elif a < b:  #else if vira elif
    print("a is less than b")
else:
    print("a is equal to b")

# condicionais aninhados

if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else:
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


# operadores and e or

if a == 34 and b == 44:
    print(a + b)

if a == 34 or b == 44:
    print(a + b)

n = None

if not n:
    print("none é considerado falso")

m = 0

if not m:
    print("0 é considerado falso")