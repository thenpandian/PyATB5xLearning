# Frequency of char in string
# Write a program to count the frequency of each character in a given string.

string = "automation"
# str = input("Enter the input e.g automation : \n")
# Expected Output -> {a:2 ,u:1,t:2,o:2,m:1,i:1,n:1}

char_count= {}    # Output
# Logic building Formula
# i/p- String
# o/P - Dict #  {a:2 ,u:1,t:2,o:2,m:1,i:1,n:1}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)



# Different way for the same Question

# Using a dictionary (dict)

string = "automation"
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)


# 2. Using a list of tuples

string = "automation"
char_list = []

for char in string:
    found = False
    for i, (ch, count) in enumerate(char_list):
        if ch == char:
            char_list[i] = (ch, count + 1)
            found = True
            break
    if not found:
        char_list.append((char, 1))

print(char_list)


# 3. Using collections.Counter

from collections import Counter

string = "automation"
char_count = Counter(string)

print(char_count)

# 4. Using set and list comprehension


string = "automation"
char_set = set(string)
char_count = [(char, string.count(char)) for char in char_set]

print(char_count)


# 5. Using defaultdict from collections

from collections import defaultdict

string = "automation"
char_count = defaultdict(int)

for char in string:
    char_count[char] += 1

print(dict(char_count))  # converting defaultdict to regular dict for display



# 6. Using sorted and groupby from itertools

from itertools import groupby

string = "automation"
sorted_string = sorted(string)
char_count = [(char, len(list(group))) for char, group in groupby(sorted_string)]

print(char_count)


# Summary:
# Dictionary (dict): Most straightforward and commonly used approach.
# List of Tuples: Uses basic list but can be less efficient for large strings.
# collections.Counter: Most convenient for counting with a built-in method.
# Set and List Comprehension: Functional approach but with a bit more complexity.
# collections.defaultdict: Similar to a dictionary but with a default value for keys.
# itertools.groupby: Functional approach that involves sorting and grouping.