import requests
import json

def get_app_details(app_id3):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id3}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP ошибки
        print(f"Response content: {json.dumps(response.json(), indent=4)}")  # Для отладки
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode failed: {e}")
        return None

def start(app_id2):
    # Получение информации о приложении
    app_details = get_app_details(app_id2)

    if app_details and str(app_id) in app_details and app_details[str(app_id)]['success']:
        app_data = app_details[str(app_id)]['data']

        # 1) Ссылка на заставку
        header_image = app_data['header_image']
        print(f"Ссылка на заставку: {header_image}")

        # 2) Заголовок (Название игры)
        game_title = app_data['name']
        print(f"Заголовок: {game_title}")

        # 3) Цена (если игра доступна для покупки)
        price_info = app_data.get('price_overview', None)
        if price_info:
            price = price_info['final_formatted']  # Цена в локальной валюте
            print(f"Цена: {price}")
        else:
            print("Цена: Игра недоступна для покупки")

        # 5) Ссылка на игру (опционально)
        game_link = f"https://store.steampowered.com/app/{app_id}/"
        print(f"Ссылка на игру: {game_link}")

        # 7) Рецензии
        reviews = app_data.get('recommendations', {}).get('total', 'Нет данных')
        print(f"Рецензии: {reviews} отзывов")

        # 8) Релиз
        release_date = app_data['release_date']['date']
        print(f"Релиз: {release_date}")

        # 9) Платформы
        platforms = []
        if app_data['platforms']['windows']:
            platforms.append('Windows')
        if app_data['platforms']['mac']:
            platforms.append('MacOS')
        if app_data['platforms']['linux']:
            platforms.append('Linux')
        print(f"Платформы: {', '.join(platforms)}")

        # 10) Теги
        tags = app_data.get('genres', [])
        tags_list = ', '.join([tag['description'] for tag in tags])
        print(f"Теги: {tags_list}")

    else:
        print(f"Не удалось получить данные для приложения с ID {app_id}")

if __name__ == '__main__':
    # ID игры
    app_id1 = 648800  # ID игры Raft

    start(app_id1)
