#1.
lambda a,b: a + b

#2.
lambda n: n%2

#3.
lambda a,b: abs(a - b)

#4.
lambda a, b, c: max(a, b, c)

#5
lambda score: "PASS" if score >= 60 else "FAIL"

#6
def squere(x):
    return x * x

#7
def return_full_name(first, last):
    return  first + " " + last

#8
def return_is_positive(n):
    return n > 0

#9
def return_discount_price(price):
    return  price * 0.9 if price > 100 else price

#10
def return_last_char(s):
    return s[-1]

#11
lambda n: n + 10

#12
lambda a,b: a * b

#13
lambda age: True if 18 <= age <= 65 else False

#14
lambda string: (string.upper(), len(string))

#15
lambda n: abs(n) if n < 0 else n * n

#16.
lambda score: "A" if score >= 90 else "B" if score >=80 else "C" if score >= 70 else "F"

#17.
lambda a, b, c: max(a, b, c) - min(a, b, c)

#18.
lambda a, b:  "Cannot divide" if b == 0 else a/b

#19.
lambda n: "FizzBuzz" if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n

#20.
lambda price, is_member: price * 0.85 if is_member else price * 0.95 if price > 200 else price