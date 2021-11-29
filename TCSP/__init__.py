def read_stopwords_list():
    stop_words = []

    # reading the custom stopwords text file
    with open("stopwords-zht.txt", "r" ) as f :
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.rstrip('\n'))
    return stop_words
