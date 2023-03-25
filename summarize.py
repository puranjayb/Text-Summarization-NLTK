import spacy

nlp = spacy.load('en_core_web_sm')

def summarize_text(text):
    doc = nlp(text)

    word_dictionary = {}
    for word in doc:
        word = word.text.lower()
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sentences = []
    score = 0

    for i,sentence in enumerate(doc.sents):
        for word in sentence:
            word = word.text.lower()
            score = word_dictionary[word]
        sentences.append((i, sentence.text.replace("\n", " "), score/len(sentence)))

    sorted_sentence_score = sorted(sentences, key=lambda x: -x[2])
    top_three = sorted(sentences[0:3], key=lambda x: x[0])
    summary = ""

    for sentence in top_three:
        summary = summary + sentence[1] + " "
    
    return summary