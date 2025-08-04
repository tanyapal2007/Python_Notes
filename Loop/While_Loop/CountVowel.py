s = "education"
i = 0
count = 0
while i < len(s):
    if s[i] in 'aeiouAEIOU':
        count += 1
    i += 1
print("Vowel count:" , count)