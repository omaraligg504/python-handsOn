import os
import shutil

def os_file_manage():
    while True:
        dir_path = input("Enter a directory path: ").strip()
        dir_path = os.path.expanduser(dir_path)

        if not os.path.isdir(dir_path):
            print(f"'{dir_path}' is not a valid directory. Please try again.")
            continue
        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        copied_files = []
        for file in os.listdir(dir_path):
            if file.endswith(".txt"):
                src = os.path.join(dir_path, file)
                dest = os.path.join(backup_path, file)
                shutil.copy2(src, dest)  
                copied_files.append(file)

        print(f"{len(copied_files)} .txt files copied to {backup_path}")
        if copied_files:
            print("Copied files:", ", ".join(copied_files))
        break



