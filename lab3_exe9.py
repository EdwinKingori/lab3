# A program that reads a sentence from the user and prints it out word by word,
# prints the length of each word,
# And should be in a separate line.

def phrase():
    
    sentence = input("Enter your phrase:")
    words = sentence.split()
   
    for i in words:
        print(f"{i} =>", {len(i)})

phrase()


