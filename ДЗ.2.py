import random

class Cipher:
    def __init__(self, number):
        self.__number = number
        self.calculate()

    def calculate(self):
        x = random.choice(['*', '/'])
        i = random.randint(7,20)
        if x == '*':
            self.__number *= i
        elif x == '/':
            self.__number /= i
    def __str__(self):
        return str(self.__number)

number = int(input("Enter a number:"))
cipher = Cipher(number)
print(cipher)
while True:
    pas = input("\nEnter password: ")
    if pas == '2765':
        print(number)
        break
    else:
        print("Wrong password")




