class Basicword():

    def __init__(self,word, subwords):
        self.word = word
        self.subwords = subwords

    def check(self, ans):
        return ans in self.subwords


    def count(self):
        return len(self.subwords)
    #dfb

