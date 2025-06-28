import argparse

def convert_temp (value , from_unit , to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == to_unit:
        return value

    #by default we will 1st convert into degree celcius
    if from_unit == 'fahrenheit':
        value = (value-32) * 5/9
    elif from_unit == 'kelvin':
        value = value - 273.15
    elif from_unit != 'celsius':
        raise ValueError ("Invalid from_unit. Choose from (celsius, fahrenheit, kelvin)")

    #then we will change into target unit
    if to_unit == 'fahrenheit':
        return value * 9/5 +32
    elif to_unit == 'kelvin':
        return value + 273.15
    elif to_unit == 'celsius':
        return value
    else:
        raise ValueError ("Invalid to_unit. Choose from (celsius, fahrenheit, kelvin)")

def main():
    parser = argparse.ArgumentParser(description="Simple Temperature converter CLI tool")
    parser.add_argument('--from-unit', required=True, help="Unit to convert from (celsius, fahrenheit, kelvin)")
    parser.add_argument('--to-unit', required=True, help="Unit to convert to (celsius, fahrenheit, kelvin)")
    parser.add_argument('--value', type=float, required=True, help="Temperature value to convert is")
    args = parser.parse_args()
    try:
        result = convert_temp(args.value, args.from_unit, args.to_unit)
        print(f"{args.value} {args.from_unit} = {result:.2f} {args.to_unit}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()