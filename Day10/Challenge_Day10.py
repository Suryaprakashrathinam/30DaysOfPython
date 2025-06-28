try:
    with open("numbers.txt", "r") as file:
        for line in file:
            line = line.strip()
            try:
                number = float(line)  # or use int(line) if only whole numbers
                print(f"Number: {number}")
            except ValueError:
                print(f"Invalid data: '{line}' is not a number.")
except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
