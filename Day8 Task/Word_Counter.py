""" Write a Python program that: 
 Opens and reads the file 
 Counts the number of words, lines, and characters in the file 
 Displays the results.
"""


# Word Counter Program
# Opens article.txt, counts words, lines, characters

# Create article.txt - Run once
with open("article.txt", "w") as f:
    f.write("Python is easy to learn\n")
    f.write("File handling is very useful\n")

# Main Progam
with open("article.txt", "r") as f:
    # Read full file
    data = f.read()
    #Split into lines
    lines = data.splitlines()
    # Split into words
    words = data.split()

    print("--- Articles ---")
    print(data)
    print("\nTotal Lines     :",len(lines))
    print("Total Words       :",len(words))
    print("Total Characters :",len(data))
    
