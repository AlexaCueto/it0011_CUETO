#Display the number of vowels, consonants, spaces, and other characters given an input string

stringWord = input("Enter a word: ")
i = stringWord

print("The word you entered is: ", i)

vowels = "aeiou" 
consonants = "bcdfghjklmnpqrstvwxyz"
whitespace = " "

countVowels = 0
countConsonants = 0
countWhitespace = 0
countSymbols = 0

for i in range(0, len(stringWord)):
    if stringWord.lower()[i] in vowels:
        countVowels = countVowels + 1
    elif stringWord.lower()[i] in consonants:
        countConsonants = countConsonants + 1
    elif stringWord.lower()[i] in whitespace:
        countWhitespace = countWhitespace + 1
    else:
        countSymbols = countSymbols + 1

print("Number of Vowels: ", countVowels)
print("Number of Consonants: ", countConsonants)
print("Number of Whitespace: ", countWhitespace)
print("Number of Symbols: ", countSymbols)