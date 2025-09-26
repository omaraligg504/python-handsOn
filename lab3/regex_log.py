import math 
import os
import re
from decorator import log_time
@log_time
def check_valid_emails():
    filename = "access.log"
    
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("access_log\n")
            f.write("===========\n\n")
    else:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                print(f"{filename} is empty. Please add log entries.")
                return
        valid_email_path="valid_emails.txt"
        if not os.path.exists(valid_email_path):
            with open(valid_email_path, 'w') as f:
                f.write("Valid Emails\n")
                f.write("============\n\n")
        for line in lines:
            email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
            if email_match:
                email = email_match.group(0)
                with open(valid_email_path, 'a') as f:
                    f.write(email + "\n")
        print(f"Valid emails extracted and saved to {valid_email_path}.\n")
    