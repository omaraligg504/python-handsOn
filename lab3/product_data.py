import os
import json
from decorator import log_time
@log_time
def transform_product_data():
    filename = "product_data.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  
    else:
        data = []
    while True:
        products = input("Enter product names separated by commas: ").strip()
        if not products:
            print("No products entered. Please try again.")
            continue
        product_list = [p.strip() for p in products.split(',') if p.strip()]
        if not product_list:
            print("Enter valid product names. Please try again.")
            continue
        break

    while True:
        prices = input("Enter corresponding prices separated by commas: ").strip()
        if not prices:
            print("No prices entered. Please try again.")
            continue
        price_list = [price.strip() for price in prices.split(',') if price.strip()]
        if len(price_list) != len(product_list):
            print("The number of prices does not match the number of products. Please try again.")
            continue
        try:
            price_list = [float(price) for price in price_list]
            break
        except ValueError:
            print("Invalid price format. Please enter numeric values.")
            continue

    filtered = [{"Product": p, "Price": pr} for p, pr in zip(product_list, price_list) if pr >= 0]

    print("Preview of first 5 results:")
    for item in filtered[:5]:
        print(f"Product: {item['Product']}, Price: {item['Price']}\n")

    data.extend(filtered)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Filtered product data saved to {filename}.\n")
    
