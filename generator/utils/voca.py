class Vocab(object):
    def __init__(self):
        self.id2word = []
        self.word2id = {}
        self.id2freq = []

    def add(self, word, freq):
        if word not in self.id2word:
            self.word2id[word] = len(self.id2word)
            self.id2word.append(word)
            self.id2freq.append(int(freq))
        
    def __len__(self):
        return len(self.id2word)

    def __getitem__(self, word):
        return self.word2id[word]

    def get_frequency(self, wordid):
        return self.id2freq[wordid]

    @classmethod
    def load(cls, vocab_path):
        v = Vocab()
        prog = 0
        with open(vocab_path) as f:
            for word in f:
                prog += 1
                recs = word.split("\t")
                v.add(recs[0], recs[1])
                if prog % 10000 == 0:
                    print("progress:{}".format(prog))
        return v
