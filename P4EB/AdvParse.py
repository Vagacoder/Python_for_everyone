## Advanced string parse
# stirng.punctuation = "!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

import string

filename = "romeo.txt"

try:
    inputFile = open(filename, "r")

except:
    print("File not found!")
    exit()
    
counts = dict()
for line in inputFile:
    line = line.strip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] =1
        else:
            counts[word] +=1

print(counts)