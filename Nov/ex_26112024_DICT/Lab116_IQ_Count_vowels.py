# count the vowel in the String

# input String = "Hello,World"


string = "automation"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
char_count = 0

for char in string:
    if char in vowels:
        vowel_count = vowel_count + 1
      else:
        consonant_count = consonant_count + 1

print(vowel_count)

print(consonant_count)
