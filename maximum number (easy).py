def max_words_in_sentence(sentences):
    return max(len(sentence.split()) for sentence in sentences)

sentences = ["alice and bob love apple", "i think so too", "this is great thanks very much"]
print(max_words_in_sentence(sentences))  
