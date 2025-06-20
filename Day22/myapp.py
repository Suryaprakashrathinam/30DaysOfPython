import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI app that greets the user.")

    # Positional argument
    parser.add_argument("name", help="Your name")

    # Optional argument with a flag
    parser.add_argument("--age", type=int, help="Your age", default=18)

    # Boolean flag
    parser.add_argument("--shout", action="store_true", help="Shout the greeting")

    args = parser.parse_args()

    greeting = f"Hello, {args.name}! You are {args.age} years old."
    if args.shout:
        greeting = greeting.upper()

    print(greeting)


if __name__ == "__main__":
    main()
