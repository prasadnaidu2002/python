# Word Counter Project


def count_words(text):
    if not text:
        return 0
    
    words = text.split()
    

    return len(words)

text = input("Enter a sentence or paragraph: ")

word_count = count_words(text)

print("Word count:", word_count)
