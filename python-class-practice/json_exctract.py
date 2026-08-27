import json
with open("product.json","r") as file:
    python_data=json.load(file)
    print(python_data["products"][0]["id"])
    print(python_data["products"][0]["title"])
    print(python_data["products"][0]["description"])
    print(python_data["products"][0]["stock"])
    print(python_data["products"][0]["category"])
    print(python_data["products"][0]["rating"])
    print(python_data["products"][0]["price"])
    print(python_data["products"][0]["tags"])
    print(python_data["products"][0]["discountPercentage"])
    r=file.read()

   

    #clean_json.txt
