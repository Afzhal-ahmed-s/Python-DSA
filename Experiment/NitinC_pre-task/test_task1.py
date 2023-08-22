import pytest
import Library

def test_elementCheckInList():

    inputList = ["Orange", "Apple", "Jack Fruit", "Mango", "Lichi"]
    element = "Apple"
    obj = Library.Library()
    obj.checkIfelementIsPresentInTheList(element, inputList)


