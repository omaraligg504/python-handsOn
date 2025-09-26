import os
import math

def append_to_report():
    filename = "math_report.txt"

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Math Report\n")
            f.write("============\n\n")

    while True:
        elements = input("Enter numbers separated by commas: ").strip()
        listelements = elements.split(',')

        try:
            nums = [float(num.strip()) for num in listelements]
            break 
        except ValueError:
            print("Invalid input. Please enter numbers only separated by commas.")

    report_lines = []
    for num in nums:
        line = (
            f"Number: {num} , "
            f"Ceil: {math.ceil(num)} , "
            f"Floor: {math.floor(num)} , "
            f"Square Root: {num ** 0.5:.2f} , "
            f"Area of Circle (r={num}): {3.14 * num ** 2:.2f}\n"
        )
        report_lines.append(line)

    finalstr = "".join(report_lines)

    with open(filename, 'a') as f:
        f.write(finalstr)

    print(f"Report updated and saved to {filename}.\n")
