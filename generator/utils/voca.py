class Vocab(object):
    def __init__(self):
        self.id2word = []
        self.word2id = {}
        self.id2freq = []

    def add(self, word):
        if word not in self.id2word:
            self.word2id[word] = len(self.id2word)
            self.id2word.append(word)
            self.id2freq.append(1)
        else:
            self.id2freq[self.word2id[word]] += 1

    def __len__(self):
        return len(self.id2word)

    def __getitem__(self, word):
        return self.word2id[word]

    def exist(self, word):
        return word in self.id2word

    def get_frequency(self, word):
        return self.id2freq[self.word2id[word]]
