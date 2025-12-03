# Problem-2.py
# Print first 'a' odd numbers starting from 1
# Example: a = 4 -> 1, 3, 5, 7

def first_a_odds(a):
    a = int(a)
    if a <= 0:
        return []
    return [2*i + 1 for i in range(a)]

def main():
    raw = input("Enter a positive integer: ").strip()
    try:
        a = int(raw)
    except ValueError:
        print("Please enter a valid integer.")
        return

    odds = first_a_odds(a)
    if not odds:
        print("No numbers to show.")
    else:
        print(", ".join(str(x) for x in odds))

if __name__ == "__main__":
    main()
