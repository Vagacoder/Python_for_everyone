## Ch08 P8.15


#  This program translates a single line of text from text messaging 
#  abbreviations to English.
#

def main() :
    transMap = buildMapping("abbrev.txt")
    
    print("Enter a message to be translated:")
    message = input("")
    words = message.split()
   
    translation = ""
    for word in words :
        translation = translation + translateAbbrv(transMap, word) + " "
      
    print("The translated text is:")
    print(translation)
      
## Extracts abbreviations and their corresponding English phrases from a 
#  file and builds a translation mapping.
#  @param filename name of the file containing the translations
#  @return a dictionary associating abbreviations with phrases
#
def buildMapping(filename) :
    transMap = {}
    infile = open(filename, "r")
    for line in infile :
        parts = line.split(":")
        transMap[parts[1].strip()] = parts[0].rstrip()
      
    infile.close()
    return transMap

## Translates a single abbreviation using the translation map. If the abbreviation 
#  ends with a punctuation mark, it remains part of the translation. 
#  @param transMap a dictionary containing the common translations
#  @param abbrv a string that contains the abbreviation to be translated
#  @return the word or phrase corresponding to the abbreviation. If the
#  abbreviation cannot be translated, it is returned unchanged 
#
def translateAbbrv(transMap, word) :
   # Determine if the word ends with a punctuation mark.

    lastChar = word[-1]
    if lastChar in ".?!,;:" :
        word = word.rstrip(lastChar)
    else :
        lastChar = ""

   # Translate the abbrv.
   
    for item in transMap:
        if item in word:
            word = replace(item, word, transMap)
      
   # Return the translated word and the original punctuation mark.
    return word + lastChar


def replace(item, word, transMap):
    if item in word:
        lowerWord = word.lower()
        startIndex = lowerWord.index(item)
        endIndex = startIndex + len(item)
        newWord = word[0:startIndex] + transMap[item]+word[endIndex:]
        newWord = replace(item, newWord, transMap)
        return newWord
    else:
        return word


# Start the program.
main()
