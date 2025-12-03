# Problem-3.py
# If a is odd -> print first a odd numbers
# If a is even -> print first (a-1) odd numbers

def pattern_numbers(a):
    a = int(a)
    if a <= 0:
        return []
    length = a if (a % 2 == 1) else (a - 1)
    return [2*i + 1 for i in range(length)]

def main():
    raw = input("Enter a number: ").strip()
    try:
        a = int(raw)
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    result = pattern_numbers(a)
    if not result:
        print("No values to display.")
    else:
        print(", ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
