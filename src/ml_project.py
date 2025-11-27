class EvenOddModel:
    def train(self):
        # Training not needed for even/odd
        return True

    def predict(self, number):
        if number % 2 == 0:
            return "even"
        else:
            return "odd"