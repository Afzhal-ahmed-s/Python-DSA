
class Library:

    def __init__(self):
        global baseUrl
        self.cartId = 0
        baseUrl = "https://simple-grocery-store-api.glitch.me"
        print("Library object created.")

    def checkIfelementIsPresentInTheList(self, myElement, inputList):
        assert myElement in inputList, f"{myElement} not found in {inputList}"

    def getBaseUrl(self):
        return baseUrl

    def checkUrlStatusAPI(self):
        endpoint = "/status"
        return self.getBaseUrl() + endpoint

    def getProductByIdAPI(self, productId):
        endpoint = "/products/" + str(productId)
        return self.getBaseUrl() + endpoint

    def createCartAPI(self):
        endpoint = "/carts"
        return self.getBaseUrl() + endpoint

    def setCartId(self, inputCartId):
        self.cartId = inputCartId

    def getCartId(self):
        return str(self.cartId)

    def addItemToCartAPI(self, cartId):
        endpoint = ""

        if cartId != None:
            endpoint = "/carts/"+str(cartId)+"/items"
        else:
            endpoint = "/carts/" + str(self.cartId) + "/items"

        return self.getBaseUrl() + endpoint

    def headerWithAccessToken(self):
        return {"Authorization": "Bearer 3da66c8dc837414e2ba267151263f10147559f49a22e9e4b7f9314fec51d2541"}