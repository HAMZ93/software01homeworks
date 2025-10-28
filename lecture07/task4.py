def remove_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_nums = remove_odd_numbers(nums)
    print("Original list:", nums)
    print("Even numbers only:", even_nums)

if __name__ == "__main__":
    main()