# Problem-4.py
# Count how many numbers in the list are divisible by each of 1..9

def parse_numbers(line):
    # Accepts comma-separated or space-separated input
    line = line.strip().replace(",", " ")
    parts = line.split()
    numbers = []
    for p in parts:
        try:
            numbers.append(int(p))
        except:
            # ignore things that are not integers
            pass
    return numbers

def count_divisibles(nums):
    result = {}
    for d in range(1, 10):   # 1 to 9
        count = 0
        for n in nums:
            if n % d == 0:
                count += 1
        result[d] = count
    return result

def main():
    line = input("Enter numbers (comma or space separated): ").strip()
    nums = parse_numbers(line)
    
    if not nums:
        print("No valid numbers found.")
        return
    
    output = count_divisibles(nums)
    print(output)

if __name__ == "__main__":
    main()
