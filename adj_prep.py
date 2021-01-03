import re


def preprocessing(text):
    user_input = text
    print(user_input)
    data = []
    # prepare text for splitting into sentences
    user_input = re.sub(r'\n', ' ', user_input)
    user_input = re.sub(r'\s\s', ' ', user_input)
    user_input = re.sub(r'\s\:', ':', user_input)
    user_input = re.sub(r'\s\;', ';', user_input)
    user_input = re.sub(r'\s\,', ',', user_input)
    user_input = re.sub(r'\.\s', '.\n', user_input)
    user_input = re.sub(r'\?\s', '?\n', user_input)
    user_input = re.sub(r'!\s', '!\n', user_input)
    sentences = user_input.split('\n')
    # tagging sentences
    for sentence in sentences:
        print(sentence)
        sentence_data = []
        if sentence != '':
            sentence_data.append(sentence)
            tags = 'pos_tags'
            sp = []
            sentence_data.append(tags)
        data.append(sentence_data)
    clean_data = []
    for sentence in data:
        if sentence != []:
            clean_data.append(sentence)
    data = clean_data
    # print(data)
    # sent[0] - plaintext sentence, sent[1] - tagged sentence
    print(data)
    return data


def adj_prep(data):

    with open('adj.txt', 'r', encoding='utf-8') as file:
        raw = file.read()
        adj_phrase = raw.split('\n')
    adjs = []
    for phrase in adj_phrase:
        words = phrase.split(' ')
        adj = words[0]
        if adj not in adjs:
            adjs.append(adj)

    with open('prep.txt', 'r', encoding='utf-8') as file:
        raw = file.read()
        prepositions = raw.split('\n')

    for sent in data:
        text = sent[0]
        for adj in adjs:
            if adj in text:
                for prep in prepositions:
                    pattern = (adj + ' ' + prep)
                    if pattern not in adj_phrase:
                        mis = re.search(pattern, text)
                        if mis:
                            sent.append([pattern, 'You might want to use a different preposition with this adjective.'])
    return data


def main():
    text = 'Be aware about this. He is hopeless in reading. I am grateful for your help.'
    data = preprocessing(text)
    adj_prep(data)
    print(data)


if __name__ == '__main__':
    main()