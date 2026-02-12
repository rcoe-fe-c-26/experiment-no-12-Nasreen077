# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Nasreen
# Date:12/2/26

print("--- Extracting Words from Text File ---\n")



with open("story.txt","r") as file:
  content=file.read().split()
var = int(input("Enter Length of Words: "))
l = []

for i in content:
    i = i.lower().strip(".,!?")
    if len(i) == var:
        if i not in l:
            l.append(i)


print("words with length", var, "are:", l)
