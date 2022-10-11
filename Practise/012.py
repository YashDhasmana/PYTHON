# Reverse words in a given String

def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


if __name__ == "__main__":
    inp = 'Python Awesome'
    print(rev_sentence(inp))

