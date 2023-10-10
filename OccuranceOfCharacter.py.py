str_input = input("Please Enter a String : ")

char_counts = {}

for char in str_input:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)
