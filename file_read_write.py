try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify content (uppercase + line numbers)
    lines = content.splitlines()
    modified = ""
    for i, line in enumerate(lines, start=1):
        modified += f"{i}. {line.upper()}\n"

    with open("output.txt", "w") as outfile:
        outfile.write("Modified Content:\n")
        outfile.write(modified)
        outfile.write(f"\nWord Count: {len(content.split())}\n")

    print("✅ File processed successfully! Check 'output.txt'.")

except FileNotFoundError:
    print("⚠️ Error: input.txt not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
