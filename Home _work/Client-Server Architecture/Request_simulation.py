import time
ALLOWED_METHODS = "GET", "POST", "PUT", "DELETE"
request_dict = {"DATA": {"email": "user_email", "password": "admin"},
                "GOODS": {
                    "JEANS": {"price": 130},
                    "T-SHIRT": {"price": 60},
                    "SHOES": {"price": 100}
                }}


def decorator_costumer(func):
    def wrapper(request):
        print("Registration")
        if request not in ALLOWED_METHODS:
            return print(ValueError("Not correct HTTP method"))
        if request != "POST":
            return print(ValueError("HTTP method is not supported"))
        time.sleep(2)
        func(request)
        print("Registration done")
    return wrapper


@decorator_costumer
def register_costumer(request: str):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    request_dict["DATA"] = {"email": email, "password": password}
    print("User data successfully registered: ", request_dict["DATA"])


def decorator_goods(func):
    def wrapper(request):
        print("Loading...")
        if request not in ALLOWED_METHODS:
            return print(ValueError("Not correct HTTP method"))
        if request != "GET":
            return print(ValueError("HTTP method is not supported"))
        time.sleep(2)
        func(request)
    return wrapper


@decorator_goods
def show_available_goods(request: str):
    return print(f"Available goods : \n {request_dict["GOODS"]}")


def decorator_add_goods(func):
    def wrapper(request):
        print("Loading...")
        if request not in ALLOWED_METHODS:
            return print(ValueError("Not correct HTTP method"))
        if request != "PUT":
            return print(ValueError("HTTP method is not supported"))
        time.sleep(2)
        func(request)
    return wrapper


@decorator_add_goods
def add_goods(request: str):
    new_stuff = input("Stuff name: ").upper()
    stuff_price = input("Stuff price: ")
    request_dict["GOODS"][new_stuff] = {"price": stuff_price}
    print(f"Goods was update by {new_stuff}.")


def decorator_delete_goods(func):
    def wrapper(request):
        print("Сhecking basket. Please wait.... ")
        if request not in ALLOWED_METHODS:
            return print(ValueError("Not correct HTTP method"))
        if request != "DELETE":
            return print(ValueError("HTTP method is not supported"))
        time.sleep(2)
        func(request)
    return wrapper


@decorator_delete_goods
def delete_goods(request: str):
    stuff_name = input("Enter stuff name to remove from goods basket: ").upper()
    if stuff_name in request_dict["GOODS"]:
        del request_dict["GOODS"][stuff_name]
        print(f'Stuff {stuff_name} was deleted.')
    else:
        print(f'Stuff {stuff_name} not in goods basket.')


while True:
    request = input("REQUEST: ").strip().upper()

    if request == "POST":
        register_costumer(request)
    elif request == "GET":
        show_available_goods(request)
    elif request == "PUT":
        add_goods(request)
    elif request == "DELETE":
        delete_goods(request)
    elif request == "EXIT":
        print("Exit from the shop")
        break
    else:
        print("HTTP method not correct")



