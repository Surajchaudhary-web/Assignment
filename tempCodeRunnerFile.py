lower()
count = 0
for vowels in string:
    if vowels in "aeiou":
        count+=1
print(f"There are {count} vowels")