import requests


def post_tests_reponses():

    url = "http://127.0.0.1:8000/get_form"

    print("Первый запрос. Форма 'Сontractor':")
    data = {
        "email": "test@example.com",
        "name_contractor": "Vasia",
    }

    response = requests.post(url, data=data)

    print(f"Статус-код: {response.status_code}")
    print(f"Данные: {response.json()}")


    print("Второй запрос. Форма: 'Employee data'")
    data = {
        "email": "test@example.com",
        "phone_number": "+79819667977",
        "birthday": "01.01.1970",
    }

    response = requests.post(url, data=data)

    print(f"Статус-код: {response.status_code}")
    print(f"Данные: {response.json()}")    


    print("Третий запрос. Форма не существует.")
    data = {
    "addres": "ул. Марата, д. 1",
    "name": " Vasia",
    "delivery date": "01.01.2025",
}

    response = requests.post(url, data=data)

    print(f"Статус-код: {response.status_code}")
    print(f"Данные: {response.json()}")

if __name__ == "__main__":
    post_tests_reponses()