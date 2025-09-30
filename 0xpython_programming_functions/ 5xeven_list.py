


def generate_even_numbers(start, stop):
    # Validate input types
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Both start and stop must be integers.")
    
    # Handle case where start > stop
    if start > stop:
        return []
    
    even_numbers = [num for num in range(start, stop + 1) if num % 2 == 0]
    return even_numbers



if __name__ == "__main__":
    print(generate_even_numbers(1, 10))  # Output: [2, 4, 6, 8, 10]
    print(generate_even_numbers(5, 4))   # Output: []
    print(generate_even_numbers(0, 0))   # Output: [0]
