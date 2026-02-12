# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Nasreen
# Date:12/2/26

print("--- Extracting Words from Text File ---\n")



with open("story.txt", "r") as f:
    words = f.read().split()

n = int(input())

result = []

for word in words:
    word = word.lower().strip(".,!?")
    if len(word) == n and word not in result:
        result.append(word)

result.sort()

print(result)

