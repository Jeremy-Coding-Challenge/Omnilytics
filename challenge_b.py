def differentiate_types(item):
    if item.lstrip("-").isdigit():
        return "integer"
    elif item.isalpha():
        return "alphabetical strings"
    elif item.strip().isalnum():
        return "alphanumeric"
    else:
        return "real_numbers"


# open the file and read the entire line
file = open("output_a.txt", "r")
line = file.readline()
items = line.split(",")

# for each item, print their respective types
for item in items:
    print(f"{item.strip()} - {differentiate_types(item)}")

file.close()
