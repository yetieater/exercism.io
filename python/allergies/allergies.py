class Allergies(object):

    def __init__(self, score):
        if score > 255:
            self.score = score % 256
        else:
            self.score = score
        self.allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        self.l = []

    def is_allergic_to(self, item):
        if self.allergens.index(item) + 1 > len(bin(self.score)[2:]):
            return False
        elif bin(self.score)[-self.allergens.index(item)-1] == '1':
            return True
        return False

    @property
    def lst(self):
        print(self.score)
        b = bin(self.score)[2:]
        for i in range(len(bin(self.score)[2:])):
            if b[-i-1] == '1':
                print("Appending {}".format(self.allergens[i]))
                self.l.append(self.allergens[i])
        return self.l