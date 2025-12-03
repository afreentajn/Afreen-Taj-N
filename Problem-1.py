# Problem-1.py
# Simple calculator using a class

class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b


def main():
    print("Simple Calculator")
    a = input("Enter a: ")
    b = input("Enter b: ")
    op = input("Enter operation (add / sub / mul / div): ").lower()

    try:
        calc = Calculator(a, b)
    except:
        print("Invalid numbers.")
        return

    if op == "add":
        print(calc.add())
    elif op == "sub":
        print(calc.sub())
    elif op == "mul":
        print(calc.mul())
    elif op == "div":
        print(calc.div())
    else:
        print("Unknown operation.")

if __name__ == "__main__":
    main()
