# def first_non_repe_string(word):
#     seen = set()
#     for char in seen:
#         if word.count(char)==1:
#             return char
#         seen.add(char)
#     return None
#
#
# print(first_non_repe_string("programming"))



def find_first_repetitive_char(s):
    seen = set()  # Set to store characters we've already seen
    for char in s:
        if char in seen:
            return char  # Return the first repetitive character
        seen.add(char)
    return None  # Return None if no repetitive character is found

# Example usage:
input_string = "programming"
result = find_first_repetitive_char(input_string)

if result:
    print(f"The first repetitive character is: {result}")
else:
    print("No repetitive characters found.")