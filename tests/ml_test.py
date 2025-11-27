from src.ml_project import EvenOddModel

def test_training():
    model = EvenOddModel()
    assert model.train() == True

def test_predict():
    model = EvenOddModel()
    assert model.predict(2) == "even"
    assert model.predict(3) == "odd"
