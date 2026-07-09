sentence = "apple banana apple cherry banana apple"
words = sentence.split()

unique_words = set(words)
print("Unique words:", unique_words)

word_counts = {word: words.count(word) for word in unique_words}
print("Word counts:", word_counts)