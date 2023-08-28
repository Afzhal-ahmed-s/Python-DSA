import json

import pytest
import requests
import Library
from Experiment.Exceptions.AddItemsToCartError import AddItemsToCartError
import jsonpath
from faker import Faker
import SqlLibrary

obj = Library.Library()
sqlGateway = SqlLibrary.Sql("localhost", "root", "new_password", "db1")

@pytest.mark.automate
@pytest.mark.parametrize(
    "productId", ["1225", "3674", "2585", "8739", "4643"]
)
@pytest.mark.run(order=5)
def test_automate_add_items_to_a_single_cart(productId):
    print("automated addition for cartId: ", obj.getCartId())
    if not add_items_to_cart(productId):
        # pytest.skip("Skipping further parameterizations due to add_items_to_cart returning False")
        raise AddItemsToCartError(f"Error occurred in add_items_to_cart with prodcutId: {productId}")

@pytest.mark.automate
@pytest.mark.run(order=7)
def test_automate_create_cart_add_items_to_cart_create_an_order():
    count = 1

    while count <= 5:
        test_create_cart()
        productIds = ["1225", "3674", "2585", "8739", "4643"]

        for i in range(0, len(productIds)):
            test_automate_add_items_to_a_single_cart(productIds[i])

        test_create_new_order()
        print(f"End to end automation testing {count}")
        print("============================================================")
        count += 1

@pytest.mark.run(order=1)
def test_checkAPIStatus():
    expectedStatusCode = 200
    response = requests.get(obj.checkUrlStatusAPI())

    assert response.status_code == expectedStatusCode


@pytest.mark.run(order=2)
def test_getProductById():
    productId = 1225
    expectedManufacturer = "Bosch"
    response = requests.get(obj.getProductByIdAPI(productId))
    jsonResponse = json.loads(response.text)
    manufacturer = jsonResponse['manufacturer']

    assert response.status_code == 200
    assert manufacturer == expectedManufacturer


@pytest.mark.run(order=3)
def test_create_cart():
    expectedCreatedResoponse = True

    response = requests.post(obj.createCartAPI())
    jsonResponse = json.loads(response.text)
    created = jsonResponse['created']
    cartId = jsonResponse['cartId']
    print("Cart created with cartId: ", cartId)
    obj.setCartId(cartId)
    print("Check: ", response.text)

    # DB
    sqlGateway.add_TableOne_Info(cartId)

    assert created == expectedCreatedResoponse


@pytest.mark.run(order=4)
def test_add_items_to_cart():
    expectedStatusCodeResponse = 201
    productId = 1225

    url = obj.addItemToCartAPI(obj.getCartId())
    jsonPayload = dynamic_add_items_to_cart_file_handling(productId)
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)
    print("Current Check: ", response.text)

    # DB
    sqlGateway.add_TableTwo_Info(str(productId), obj.getCartId())
    print(f"CartId: {obj.getCartId()} with productId: {productId} persisted to tableTwo.")

    assert response.status_code == expectedStatusCodeResponse


# @pytest.mark.parametrize(
#     productId=["1225", "3674", "2585", "8739", "4643", "4646"],
#     customerName=["Afzhal", "Nitin Chawala", "Shubham", "Mriganka", "Gaurav"]
# )
# def test_exp_automation_method(productId, customerName):


@pytest.mark.run(order=6)
def test_create_new_order():
    url = obj.createNewOrderAPI()
    jsonPayload = dynamic_create_order_file_handling()
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)

    pythonResponseFormat = json.loads(response.text)
    orderId = pythonResponseFormat["orderId"]
    pythonFormatJsonPayload = json.loads(jsonPayload)
    cartId = pythonFormatJsonPayload["cartId"]
    customerName = pythonFormatJsonPayload["customerName"]

    #DB
    sqlGateway.add_TableThree_Info(orderId, cartId, customerName)
    print(f"OrderId: {orderId} with cartId: {cartId} with customer name: {customerName}")
    assert response.status_code == 201

    print("New Order created: ", response.text)


def dynamic_add_items_to_cart_file_handling(productId):
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["productId"] = str(productId)
    jsonPayload = json.dumps(jsonPayload)
    return jsonPayload


def dynamic_create_order_file_handling():
    file = open("/home/afzhal-ahmed-s/PycharmProjects/create_order_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["cartId"] = obj.getCartId()
    jsonPayload["customerName"] = obj.generate_random_name()

    jsonPayload = json.dumps(jsonPayload)

    return jsonPayload


def add_items_to_cart(productId):
    url = obj.addItemToCartAPI(obj.getCartId())
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["productId"] = str(productId)
    jsonPayload = json.dumps(jsonPayload)

    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)
    jsonResponse = json.loads(response.text)
    print(response.text)

    #DB
    sqlGateway.add_TableTwo_Info(productId, obj.getCartId())
    print(f"CartId: {obj.getCartId()} with productId: {productId} persisted to tableTwo.")

    if "created" in jsonResponse:
        return True





