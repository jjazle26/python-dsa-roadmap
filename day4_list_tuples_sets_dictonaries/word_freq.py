text = "apple banana apple cherry banana apple"
words = text.split()

unique_words = set(words)

freq = {word: words.count(word) for word in unique_words}
print(freq)