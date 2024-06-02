import requests

def get_cat_breeds():
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_breed_description(breed_name, cat_breeds):
    for breed in cat_breeds:
        if breed['name'].lower() == breed_name.lower():
            return breed['description']
    return "Описание породы не найдено."

def main():
    cat_breeds = get_cat_breeds()

    if cat_breeds:
        breed_name = input("Введите название породы кошек: ")
        description = get_breed_description(breed_name, cat_breeds)
        print(description)
    else:
        print("Информация о породах кошек не найдена.")

if __name__ == "__main__":
    main()







