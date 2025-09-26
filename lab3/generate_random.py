import csv
import random

def random_data_generator():
    filename = "random_numbers.csv"

    while True:
        try:
            count = int(input("Enter how many random numbers to generate: ").strip())
            if count <= 0:
                print("cannot enter zero or negative numbers. Please try again with positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter positive number.")

    numbers = [random.randint(1, 100) for _ in range(count)]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"]) 
        for i, num in enumerate(numbers, start=1):
            writer.writerow([i, num])
    total = sum(numbers)
    average = total / len(numbers)

    print(f"\n {count} random numbers generated and saved to {filename}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}\n")
