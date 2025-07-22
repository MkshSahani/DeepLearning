import string 

class TextVectorization:

    def standardize(self, text):
        text = text.lower()
        return "".join(x for x in text if x not in string.punctuation)

    def tokenize(self, text):
        text = self.standardize(text)
        return text.split(" ")

    def make_vocabulary(self, dataset):
        self.vocab = {"[MASK]": 0, "[UNK]": 1}
        for text in dataset:
            tokens = self.tokenize(text)
            for token in tokens:
                if token not in self.vocab:
                    self.vocab[token] = len(self.vocab)
        self.inv_vocb = dict((v, k) for k, v in self.vocab.items())
        return self.vocab
    

    def encode(self, text):
        tokens = self.tokenize(text)
        print(tokens)
        return [self.vocab.get(token, 1) for token in tokens]

    def decode(self, int_sequence):
        return " ".join(self.inv_vocb.get(i, "[UNK]") for i in int_sequence)


text_vectorization = TextVectorization()
dataset = [
    "I write, erase, rewrite",
    "Erase again, and then",
    "A popp  blooms.",
]
text_vectorization.make_vocabulary(dataset)
test_sentence = "I write, rewrite, and still rewrite again"
encoded_sequence = text_vectorization.encode(test_sentence)
print(encoded_sequence)
decode_text = text_vectorization.decode(encoded_sequence)
print(decode_text)
