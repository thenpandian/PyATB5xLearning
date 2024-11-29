# Find the first non repetive character in String using Sets
# swiss     -> -x, w - Answer

def first_non_repetitive_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    # return None

print(first_non_repetitive_char("Swiss"))
print(first_non_repetitive_char("swiss"))
print(first_non_repetitive_char("pepper"))
print(first_non_repetitive_char("DADA"))