class Vocab(object):
    def __init__(self):
        self.id2word = []
        self.word2id = {}

    def add(self, word, freq):
        if word not in self.word2id:
            self.word2id[word] = len(self.id2word)
            self.id2word.append((word, int(freq)))
        
    def __len__(self):
        return len(self.id2word)

    def __getitem__(self, word):
        return self.word2id[word]

    def get_frequency(self, wordid):
        return self.id2word[wordid][1]

    @classmethod
    def load(cls, vocab_path):
        v = Vocab()
        with open(vocab_path) as f:
            for word in f:
                # prog += 1
                recs = word.split("\t")
                v.add(recs[0], recs[1])
        return v
