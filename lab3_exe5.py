#print characters of the str in reverse order.


# first method: using a for loop
str = "This sentence has 27 chars." [::-1]

# first method 
for i in str:
    print(i, end = "")

#second method: using a functio
def reverse (i):
    return i[::-1]

str = reverse ("This sentence has 27 chars.")
print(f"{str}")

#third method: negative indexing
str = "This sentence has 27 chars."
print (str [::-1])

#fifth method: using the .join method
str = "This sentence has 27 chars."
reversedstr = "".join(reversed(str))
print(reversedstr)
