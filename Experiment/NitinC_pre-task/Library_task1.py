
class LibraryTask1:

    def __init__(self):
        print("LibraryTask1 object created.")
    def checkIfelementIsPresentInTheList(self, myElement, inputList):
        assert myElement in inputList, f"{myElement} not found in {inputList}"
