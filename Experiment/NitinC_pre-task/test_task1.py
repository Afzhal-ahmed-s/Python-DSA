import pytest
import Library_task1

def test_elementCheckInList():

    inputList = ["Orange", "Apple", "Jack Fruit", "Mango", "Lichi"]
    element = "Apple"
    obj = Library_task1.LibraryTask1()
    obj.checkIfelementIsPresentInTheList(element, inputList)

