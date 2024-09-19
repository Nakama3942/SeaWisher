# Copyright © 2024 Kalynovsky Valentin. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QPlainTextEdit, QLineEdit, QPushButton, QTableView, QSpacerItem, QLabel

from wisher.src.steamtest import get_app_details
from wisher.src.database import Database

class Interface(QMainWindow):
	def __init__(self):
		super(Interface, self).__init__()

		##############################
		#
		# Layout
		#
		##############################
		self.main_layout = QVBoxLayout()

		# self.game_data_test = QPlainTextEdit()
		# self.game_data_test.appendPlainText(get_app_details(648800)[str(648800)]['data']['name'])
		# self.main_layout.addWidget(self.game_data_test)

		self.db_test_butt = QPushButton("Test DB", self)
		self.db_test_butt.clicked.connect(self.main_layout_clicked)
		self.main_layout.addWidget(self.db_test_butt)

		##############################
		#
		# Main window customization
		#
		##############################
		self.central_widget = QWidget()
		self.central_widget.setLayout(self.main_layout)
		self.setCentralWidget(self.central_widget)
		self.setWindowTitle("SeaWisher")

	def main_layout_clicked(self):
		game_details = get_app_details(648800)

		if game_details and str(648800) in game_details and game_details[str(648800)]['success']:
			game_data = game_details[str(648800)]['data']

			# Имя игры
			title = game_data['name']
			# with Database() as db:
			# 	if not db.check_post(title):
			# 		return jsonify({'success': False, 'error_message': 'Пост із такою назвою вже існує'})

			# Ссылка на страницу игры
			game_link = f"https://store.steampowered.com/app/{648800}/"

			# Ссылка на заставку
			image_link = game_data['header_image']

			# Стоимость игры
			cost_info = game_data.get('price_overview', None)
			if cost_info:
				cost = cost_info['final_formatted']  # Цена в локальной валюте
			else:
				cost = "Игра недоступна для покупки"

			# Рецензии на игру
			reviews = game_data.get('recommendations', {}).get('total', 'Нет данных')

			# Дата релиза
			release_date = game_data['release_date']['date']

			# Платформы
			list_platforms = []
			if game_data['platforms']['windows']:
				list_platforms.append('Windows')
			if game_data['platforms']['mac']:
				list_platforms.append('MacOS')
			if game_data['platforms']['linux']:
				list_platforms.append('Linux')
			platforms = f"{', '.join(list_platforms)}"

			# Жанры
			steam_tags = f"{', '.join([genre['description'] for genre in game_data.get('genres', [])])}"

			# Симулирую ввод данных
			steamDB_game_link = "1"
			steamDB_rating_stats = "1"
			positive_reviews_stats = "1"
			negative_reviews_stats = "1"
			discount = "1"
			price = "1"
			max_discount = "1"
			min_price = "1"
			stability = "Constant"
			frequency = "Rare"
			user_tags = "1"
			added_date = "1"
			comment = "1"

			# Формуємо метаданні посту
			game_metadata = {
				'title': title,
				'game_link': game_link,
				'image_link': image_link,
				'cost': cost,
				'reviews': reviews,
				'release_date': release_date,
				'platforms': platforms,
				'steam_tags': steam_tags,
				'steamDB_game_link': steamDB_game_link,
				'steamDB_rating_stats': steamDB_rating_stats,
				'positive_reviews_stats': positive_reviews_stats,
				'negative_reviews_stats': negative_reviews_stats,
				'discount': discount,
				'price': price,
				'max_discount': max_discount,
				'min_price': min_price,
				'stability': stability,
				'frequency': frequency,
				'user_tags': user_tags,
				'added_date': added_date,
				'comment': comment
			}

			# Зберігаємо метадані в БД
			with Database() as db:
				db.add_game(game_metadata)

			# return jsonify({'success': True})

		else:
			print(f"Не удалось получить данные для приложения с ID {648800}")
