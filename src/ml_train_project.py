from ml_project import EvenOddModel

def main():
    model = EvenOddModel()
    model.train()  
    print("Model is ready!")

    print("2 ->", model.predict(2))
    print("3 ->", model.predict(3))

if __name__ == "__main__":
    main()