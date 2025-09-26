
from math_report import append_to_report
from regex_log import check_valid_emails
from date_reminder import date_reminder
from product_data import transform_product_data
from os_file_manager import os_file_manage
from generate_random import random_data_generator
def main_menu():
    while True:
        print("=== The System ===\n")
        print("1. Math report")
        print("2. Regex log")
        print("3. Date reminder")
        print("4. Product data")
        print("5. OS file manager")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            append_to_report()
        elif choice == "2":
            check_valid_emails()
        elif choice == "3":
            date_reminder()
        elif choice == "4":
            transform_product_data()
        elif choice == "5":
            os_file_manage()
        elif choice == "6":
            random_data_generator()
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
