# # WRITE YOUR FUNCTIONS HERE
from ctypes import cdll


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, added_value):
    pet_shop["admin"]["total_cash"] += added_value
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_added_value):
    pet_shop["admin"]["pets_sold"] += new_added_value
    return pet_shop["admin"]["pets_sold"]


def get_stock_count(pet_shop):
    len_1 = len(pet_shop ["pets"])
    return len_1


def get_pets_by_breed(pet_shop, breed):
    pelo_corto = []
    for corto in pet_shop["pets"]:
        if corto["breed"] == breed:
            pelo_corto.append(corto)
    
    return pelo_corto

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet ["name"] == name:
            pet_shop ["pets"].remove(pet)
            return pet_shop

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append("Bors the Younger")
    return pet_shop

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return customer
    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):    
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def update_pet_sold(pet_shop):
    pet_shop["admin"]["pets_sold"] += 1


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None:
        can_afford_pet = customer_can_afford_pet(customer, pet)
        if(can_afford_pet == True):
            add_pet_to_customer(customer, pet) 
            update_pet_sold(pet_shop)
            cash = pet['price']
            remove_customer_cash(customer, cash)
            add_or_remove_cash(pet_shop, cash)





    





