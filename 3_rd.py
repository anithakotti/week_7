
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

for word in set(words):
    print(word, ":", words.count(word))
