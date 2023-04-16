import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

from string import punctuation
from heapq import nlargest

stop = set(stopwords.words('english'))
punct = punctuation + '\n'


def preprocessing(text):
    encoded_text = text.encode("utf-8")
    text = encoded_text.decode("utf-8")
    tokens = word_tokenize(text)

    return tokens


def word_frequency(processed_text):
    word_frequency_dictionary = {}
    for word in processed_text:
        word = word.lower()
        if word not in stop:
            if word not in punct:
                if word not in word_frequency_dictionary:
                    word_frequency_dictionary[word] = 1
                else:
                    word_frequency_dictionary[word] += 1

    return word_frequency_dictionary


def max_frequency(word_frequency_dictionary):
    max_freq = max(word_frequency_dictionary.values())
    
    return max_freq


def vectorizing(word_frequency_dictionary, max_freq):
    for word in word_frequency_dictionary:
        word_frequency_dictionary[word] = word_frequency_dictionary[word]/max_freq
        
    return word_frequency_dictionary



def sentence_score(word_frequency_dictionary, text):
    sentence_score_dictionary = {}
    encoded_text = text.encode("utf-8")
    text = encoded_text.decode("utf-8")
    sentences = sent_tokenize(text)
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            word = word.lower()
            if word in word_frequency_dictionary:
                if sentence not in sentence_score_dictionary:
                    sentence_score_dictionary[sentence] = word_frequency_dictionary[word]
                else:
                    sentence_score_dictionary[sentence] += word_frequency_dictionary[word]
                    
    return sentence_score_dictionary


def sentence_length(text):
    length = int(len(sent_tokenize(text))*0.3)
    
    return length


def get_summary(sl, sts):
    summary = nlargest(sl, sts)
    summary = ' '.join(summary)

    return summary

def main():

    text = """ It's a 5v5 multiplayer first-person shooter (FPS) where one team attacks and the other defends. The main game mode, Search and Destroy, is very similar to CS:GO. The attacking team's goal is to plant a bomb (called a spike) and have it detonate, while the defending team tries to avoid that. Regardless of whether the spike is planted or not, if a squad is wiped out before any other victory condition is met, the opposing squad will win.
    Matches are 25 rounds long, with each round lasting 100 seconds. The first team to win 13 rounds wins the match overall. At the beginning of the round, you'll have 30 seconds to buy weapons and gear for that round. If you die in a round, you'll have to wait until the next round to respawn. This main game mode can be played in either unrated or ranked matches.
    It sounds just like CS:GO's Defuse game mode, but Riot has a twist on the formula. In addition to buying weapons, you'll also choose an Agent at the beginning of each round. Each Agent has an ability, ranging from healing allies to making walls appear out of nowhere. Considering Valorant takes a MOBA-based approach to Agents, you'll likely need a good spread of abilities if you want to win a match. Note, however, that you'll need to buy some abilities at the beginning of a round.
    Since launch, Valorant has added the Spike Rush game mode. This is a quicker, best-of-seven-rounds mode where every attacker is equipped with a spike, and all players have the same weapon and all of their abilities; there is no buy round.
    Valorant's seasons will be known as Acts, each bringing new additions to the game including new Agents, maps, and modes """

    pt = preprocessing(text)
    wfd = word_frequency(pt)
    mf = max_frequency(wfd)
    vtr = vectorizing(wfd, mf)
    sts = sentence_score(wfd, text)
    sl = sentence_length(text)
    summary = get_summary(sl, sts)

    return summary


