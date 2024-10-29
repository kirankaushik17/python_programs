from colorsys import yiq_to_rgb


class arithmetic_op:
    def sum(self):
        x=20
        y=30
        return x+y
    def mul(self):
        a=20
        b=5
        return a*b
    def sub(self):
        p=10
        q=5
        return p-q
    def div(self):
        a=20
        b=5
        return a/b
    def mod(self):
        a=200
        b=2
        return a%b

    def even_odd(self):
        n=10
        if(n%2==0):
         print("given no is even")
        else:
            print("given no is odd")

    def positive_negative(self):
                n=10
                if(n<0):
                    print("given no is positive")
                else:
                    print("given no is negative")

    def fact(self):
        num=4
        i=1
        fact=1
        while (i<=num):
            fact=fact*i
            i=i+1
        return fact

    def prime_no(self):
        count = 0
        n = 5
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 2:
            print("given number is prime")
        else:
            print("given number is not a prime")

    def mobile_no_validation(self):
        z = "9440914677"

        if len(z) == 10:
            print("given number is valid")
        else:
            print("given number is invalid")