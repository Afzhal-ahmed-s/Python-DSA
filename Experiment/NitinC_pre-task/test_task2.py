import json
import requests
import Library
import jsonpath

obj = Library.Library()

def test_checkAPIStatus():
    expectedStatusCode = 200

    response = requests.get(obj.checkUrlStatusAPI())

    assert response.status_code == expectedStatusCode

def test_getProductById():
    productId = 1225
    expectedManufacturer = "Bosch"

    response = requests.get(obj.getProductByIdAPI(productId))
    jsonResponse = json.loads(response.text)
    manufacturer = jsonpath.jsonpath(jsonResponse, 'manufacturer')[0]
    print("Check test 2: ", response, manufacturer)

    assert response.status_code == 200
    assert manufacturer == expectedManufacturer

def test_create_cart():
    expectedCreatedResoponse = True

    response = requests.post(obj.createCartAPI())
    jsonResponse = json.loads(response.text)
    created = jsonpath.jsonpath(jsonResponse, 'created')[0]
    cartId = jsonpath.jsonpath(jsonResponse, 'cartId')[0]
    print("CartId: ", cartId)
    obj.setCartId(cartId)
    print("Assigned cartId: ", obj.getCartId())

    assert created == expectedCreatedResoponse

def test_add_items_to_cart():
    expectedStatusCodeResoponse = 200

    file = open("/home/afzhal-ahmed-s/PycharmProjects/pre-task2_testingData1.json",'r')
    jsonPayload = json.loads(file.read())
    print("JP: ", jsonPayload)
    print("cartId: ", obj.getCartId())
    temp = {
    "productId": 1225
    }
    response = requests.post(obj.addItemToCartAPI(obj.getCartId()), temp, headers= obj.headerWithAccessToken())

    print("Check4: ",response.text)

    assert response.status_code == 201

def test_create_new_order():
    # file = open("/home/afzhal-ahmed-s/PycharmProjects/pre-test2_data2.json",'r')
    # jsonPayload = json.loads(file.read())
    # jsonPayload["cartId"] = obj.getCartId()

    temp = {
            "cartId": obj.getCartId(),
            "customerName": "Afzhal Ahmed S"
            }
    print("cartId: ", obj.getCartId())

    response = requests.post("https://simple-grocery-store-api.glitch.me/orders", temp, headers= obj.headerWithAccessToken())
    print(response.text)

    assert response.status_code == 201

