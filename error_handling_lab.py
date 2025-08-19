filename = input("Enter the filename: ")

try:
    with open(filename, "r") as f:
        print("✅ File opened successfully!\n")
        print(f.read())

except FileNotFoundError:
    print("⚠️ Error: The file does not exist.")
except PermissionError:
    print("⚠️ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
