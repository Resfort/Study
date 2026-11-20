def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1.0,
        "centimeters": 100.0,
        "millimeters": 1000.0,
        "kilometers": 0.001,
    }

    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    return value / conversion_factors[from_unit] * conversion_factors[to_unit]


def main():
    units = "meters, centimeters, millimeters, kilometers"
    print(f"Available units: {units}")

    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Convert from: ")
        to_unit = input("Convert to: ")
        result = convert_length(value, from_unit, to_unit)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"{value:g} {from_unit} = {result:g} {to_unit}")


if __name__ == "__main__":
    main()
