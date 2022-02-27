greet = "hello"
print(greet)

# pet_shop = {
#             "pets": [
#                 {
#                     "name": "Sir Percy",
#                     "pet_type": "cat",
#                     "breed": "British Shorthair",
#                     "price": 500
#                 },
#                 {
#                     "name": "King Bagdemagus",
#                     "pet_type": "cat",
#                     "breed": "British Shorthair",
#                     "price": 500
#                 },
#                 {
#                     "name": "Sir Lancelot",
#                     "pet_type": "dog",
#                     "breed": "Pomsky",
#                     "price": 1000,
#                 },
#                 {
#                     "name": "Arthur",
#                     "pet_type": "dog",
#                     "breed": "Husky",
#                     "price": 900,
#                 },
#                 {
#                     "name": "Tristan",
#                     "pet_type": "cat",
#                     "breed": "Basset Hound",
#                     "price": 800,
#                 },
#                 {
#                     "name": "Merlin",
#                     "pet_type": "cat",
#                     "breed": "Egyptian Mau",
#                     "price": 1500,
#                 }
#             ],
#             "admin": {
#                 "total_cash": 1000,
#                 "pets_sold": 0,
#             },
#             "name": "Camelot of Pets"
#         }
print("before_funct")

def remove_pet_by_name(name):
    print("before_model")
    pet_shop = {
    
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

    
    not_removed_name = []
    for deleted_name in pet_shop["pets"]:
        if deleted_name["name"] != name:
            print(deleted_name)
            not_removed_name.append(deleted_name)
    pet_shop += not_removed_name
    print(pet_shop)
    return not_removed_name

remove_pet_by_name("Arthur")