# ################################################################################ #
# Copyright © 2024 Kalynovsky Valentin. All rights reserved.                       #
#                                                                                  #
# Licensed under the Apache License, Version 2.0 (the "License");                  #
# you may not use this file except in compliance with the License.                 #
# You may obtain a copy of the License at                                          #
#                                                                                  #
#     http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                                  #
# Unless required by applicable law or agreed to in writing, software              #
# distributed under the License is distributed on an "AS IS" BASIS,                #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.         #
# See the License for the specific language governing permissions and              #
# limitations under the License.                                                   #
# ################################################################################ #

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QMessageBox

from wisher.src.database import Database
from wisher.src.steam_api import get_game_details

class AddGameDialog(QDialog):
	def __init__(self):
		super(AddGameDialog, self).__init__()

		# Главный макет
		self.main_layout = QVBoxLayout()

		# Поле для ввода ID игры
		self.game_id_layout = QHBoxLayout()
		self.game_id_label = QLabel("Введи ID игры в Steam:", self)
		self.game_id_text = QTextEdit(self)
		self.game_id_layout.addWidget(self.game_id_label)
		self.game_id_layout.addWidget(self.game_id_text)
		self.main_layout.addLayout(self.game_id_layout)

		# Кнопка для подгрузки данных
		self.game_data_download_butt = QPushButton("Подгрузить данные со Steam", self)
		self.game_data_download_butt.clicked.connect(self.game_data_download_butt_clicked)
		self.main_layout.addWidget(self.game_data_download_butt)

		# Поле для ввода названия игры
		self.game_title_layout = QHBoxLayout()
		self.game_title_label = QLabel("Название игры:", self)
		self.game_title_text = QTextEdit(self)
		self.game_title_layout.addWidget(self.game_title_label)
		self.game_title_layout.addWidget(self.game_title_text)
		self.main_layout.addLayout(self.game_title_layout)

		# Поле для ввода ссылки на Стимовскую страницу игры
		self.page_link_layout = QHBoxLayout()
		self.page_link_label = QLabel("Ссылка на игру:", self)
		self.page_link_text = QTextEdit(self)
		self.page_link_layout.addWidget(self.page_link_label)
		self.page_link_layout.addWidget(self.page_link_text)
		self.main_layout.addLayout(self.page_link_layout)

		# Поле для ввода обложку игры
		self.image_link_layout = QHBoxLayout()
		self.image_link_label = QLabel("Ссылка на обложку:", self)
		self.image_link_text = QTextEdit(self)
		self.image_link_layout.addWidget(self.image_link_label)
		self.image_link_layout.addWidget(self.image_link_text)
		self.main_layout.addLayout(self.image_link_layout)

		# Поле для ввода краткого описания
		self.short_description_layout = QHBoxLayout()
		self.short_description_label = QLabel("Краткое описание:", self)
		self.short_description_text = QTextEdit(self)
		self.short_description_layout.addWidget(self.short_description_label)
		self.short_description_layout.addWidget(self.short_description_text)
		self.main_layout.addLayout(self.short_description_layout)

		# Поле для ввода ссылки на сайт игры
		self.website_layout = QHBoxLayout()
		self.website_label = QLabel("Ссылка на официальный сайт игры:", self)
		self.website_text = QTextEdit(self)
		self.website_layout.addWidget(self.website_label)
		self.website_layout.addWidget(self.website_text)
		self.main_layout.addLayout(self.website_layout)

		# Поле для ввода названий разработчиков
		self.developers_layout = QHBoxLayout()
		self.developers_label = QLabel("Разработчики:", self)
		self.developers_text = QTextEdit(self)
		self.developers_layout.addWidget(self.developers_label)
		self.developers_layout.addWidget(self.developers_text)
		self.main_layout.addLayout(self.developers_layout)

		# Поле для ввода названий издателей
		self.publishers_layout = QHBoxLayout()
		self.publishers_label = QLabel("Издатели:", self)
		self.publishers_text = QTextEdit(self)
		self.publishers_layout.addWidget(self.publishers_label)
		self.publishers_layout.addWidget(self.publishers_text)
		self.main_layout.addLayout(self.publishers_layout)

		# Поле для ввода coming_soon
		self.coming_soon_layout = QHBoxLayout()
		self.coming_soon_label = QLabel("coming_soon:", self)
		self.coming_soon_text = QTextEdit(self)
		self.coming_soon_layout.addWidget(self.coming_soon_label)
		self.coming_soon_layout.addWidget(self.coming_soon_text)
		self.main_layout.addLayout(self.coming_soon_layout)

		# Поле для ввода даты релиза игры
		self.release_date_layout = QHBoxLayout()
		self.release_date_label = QLabel("Дата релиза игры:", self)
		self.release_date_text = QTextEdit(self)
		self.release_date_layout.addWidget(self.release_date_label)
		self.release_date_layout.addWidget(self.release_date_text)
		self.main_layout.addLayout(self.release_date_layout)

		# Поле для ввода платформ
		self.platforms_layout = QHBoxLayout()
		self.platforms_label = QLabel("Платформы:", self)
		self.platforms_text = QTextEdit(self)
		self.platforms_layout.addWidget(self.platforms_label)
		self.platforms_layout.addWidget(self.platforms_text)
		self.main_layout.addLayout(self.platforms_layout)

		# Поле для ввода категорий
		self.steam_categories_layout = QHBoxLayout()
		self.steam_categories_label = QLabel("Категории:", self)
		self.steam_categories_text = QTextEdit(self)
		self.steam_categories_layout.addWidget(self.steam_categories_label)
		self.steam_categories_layout.addWidget(self.steam_categories_text)
		self.main_layout.addLayout(self.steam_categories_layout)

		# Поле для ввода жанров
		self.steam_tags_layout = QHBoxLayout()
		self.steam_tags_label = QLabel("Жанры:", self)
		self.steam_tags_text = QTextEdit(self)
		self.steam_tags_layout.addWidget(self.steam_tags_label)
		self.steam_tags_layout.addWidget(self.steam_tags_text)
		self.main_layout.addLayout(self.steam_tags_layout)

		# Поле для ввода стоимости игры
		self.cost_layout = QHBoxLayout()
		self.cost_label = QLabel("Стоимость:", self)
		self.cost_text = QTextEdit(self)
		self.cost_layout.addWidget(self.cost_label)
		self.cost_layout.addWidget(self.cost_text)
		self.main_layout.addLayout(self.cost_layout)

		# Поле для ввода категории по распределению в моей библиотеке
		self.category_layout = QHBoxLayout()
		self.category_label = QLabel("Категория (по библиотеке) куда я определяю игру:", self)
		self.category_text = QTextEdit(self)
		self.category_layout.addWidget(self.category_label)
		self.category_layout.addWidget(self.category_text)
		self.main_layout.addLayout(self.category_layout)

		# Поле для ввода ссылки на страницу игры в SteamDB
		self.steamDB_game_link_layout = QHBoxLayout()
		self.steamDB_game_link_label = QLabel("Ссылка на страницу игры в SteamDB:", self)
		self.steamDB_game_link_text = QTextEdit(self)
		self.steamDB_game_link_layout.addWidget(self.steamDB_game_link_label)
		self.steamDB_game_link_layout.addWidget(self.steamDB_game_link_text)
		self.main_layout.addLayout(self.steamDB_game_link_layout)

		# Поле для ввода рецензии
		self.steam_reviews_layout = QHBoxLayout()
		self.steam_reviews_label = QLabel("Рецензии:", self)
		self.steam_reviews_text = QTextEdit(self)
		self.steam_reviews_layout.addWidget(self.steam_reviews_label)
		self.steam_reviews_layout.addWidget(self.steam_reviews_text)
		self.main_layout.addLayout(self.steam_reviews_layout)

		# Поле для ввода процентного рейтинга
		self.steamDB_rating_stats_layout = QHBoxLayout()
		self.steamDB_rating_stats_label = QLabel("Процентный рейтинг игры:", self)
		self.steamDB_rating_stats_text = QTextEdit(self)
		self.steamDB_rating_stats_layout.addWidget(self.steamDB_rating_stats_label)
		self.steamDB_rating_stats_layout.addWidget(self.steamDB_rating_stats_text)
		self.main_layout.addLayout(self.steamDB_rating_stats_layout)

		# Поле для ввода количества позитивных отзывы
		self.positive_reviews_stats_layout = QHBoxLayout()
		self.positive_reviews_stats_label = QLabel("Количество позитивных отзывы:", self)
		self.positive_reviews_stats_text = QTextEdit(self)
		self.positive_reviews_stats_layout.addWidget(self.positive_reviews_stats_label)
		self.positive_reviews_stats_layout.addWidget(self.positive_reviews_stats_text)
		self.main_layout.addLayout(self.positive_reviews_stats_layout)

		# Поле для ввода количества негативных отзывы
		self.negative_reviews_stats_layout = QHBoxLayout()
		self.negative_reviews_stats_label = QLabel("Количество негативных отзывы:", self)
		self.negative_reviews_stats_text = QTextEdit(self)
		self.negative_reviews_stats_layout.addWidget(self.negative_reviews_stats_label)
		self.negative_reviews_stats_layout.addWidget(self.negative_reviews_stats_text)
		self.main_layout.addLayout(self.negative_reviews_stats_layout)

		# Поле для ввода ожидаемой скидки
		self.discount_layout = QHBoxLayout()
		self.discount_label = QLabel("Ожидаемая скидка:", self)
		self.discount_text = QTextEdit(self)
		self.discount_layout.addWidget(self.discount_label)
		self.discount_layout.addWidget(self.discount_text)
		self.main_layout.addLayout(self.discount_layout)

		# Поле для ввода цены по ожидаемой скидке
		self.price_layout = QHBoxLayout()
		self.price_label = QLabel("Цена по ожидаемой скидке:", self)
		self.price_text = QTextEdit(self)
		self.price_layout.addWidget(self.price_label)
		self.price_layout.addWidget(self.price_text)
		self.main_layout.addLayout(self.price_layout)

		# Поле для ввода максимальной скидки
		self.max_discount_layout = QHBoxLayout()
		self.max_discount_label = QLabel("Максимальная скидка:", self)
		self.max_discount_text = QTextEdit(self)
		self.max_discount_layout.addWidget(self.max_discount_label)
		self.max_discount_layout.addWidget(self.max_discount_text)
		self.main_layout.addLayout(self.max_discount_layout)

		# Поле для ввода цены по максимальной скидке
		self.min_price_layout = QHBoxLayout()
		self.min_price_label = QLabel("Цена по максимальной скидке (выбирать при минимальной стоимости игры):", self)
		self.min_price_text = QTextEdit(self)
		self.min_price_layout.addWidget(self.min_price_label)
		self.min_price_layout.addWidget(self.min_price_text)
		self.main_layout.addLayout(self.min_price_layout)

		# Поле для ввода стабильности скидки
		self.stability_layout = QHBoxLayout()
		self.stability_label = QLabel("Стабильность скидки:", self)
		self.stability_text = QTextEdit(self)
		self.stability_layout.addWidget(self.stability_label)
		self.stability_layout.addWidget(self.stability_text)
		self.main_layout.addLayout(self.stability_layout)

		# Поле для ввода частоты скидки
		self.frequency_layout = QHBoxLayout()
		self.frequency_label = QLabel("Частота скидки:", self)
		self.frequency_text = QTextEdit(self)
		self.frequency_layout.addWidget(self.frequency_label)
		self.frequency_layout.addWidget(self.frequency_text)
		self.main_layout.addLayout(self.frequency_layout)

		# Поле для ввода тегов игры
		self.user_tags_layout = QHBoxLayout()
		self.user_tags_label = QLabel("Теги:", self)
		self.user_tags_text = QTextEdit(self)
		self.user_tags_layout.addWidget(self.user_tags_label)
		self.user_tags_layout.addWidget(self.user_tags_text)
		self.main_layout.addLayout(self.user_tags_layout)

		# Поле для ввода даты добавления в список желаемого
		self.added_date_layout = QHBoxLayout()
		self.added_date_label = QLabel("Дата добавления в список желаемого:", self)
		self.added_date_text = QTextEdit(self)
		self.added_date_layout.addWidget(self.added_date_label)
		self.added_date_layout.addWidget(self.added_date_text)
		self.main_layout.addLayout(self.added_date_layout)

		# Поле для ввода комментария
		self.comment_layout = QHBoxLayout()
		self.comment_label = QLabel("Объяснение, почему я хочу купить игру:", self)
		self.comment_text = QTextEdit(self)
		self.comment_layout.addWidget(self.comment_label)
		self.comment_layout.addWidget(self.comment_text)
		self.main_layout.addLayout(self.comment_layout)

		self.add_game_butt = QPushButton("Добавить игру", self)
		self.add_game_butt.clicked.connect(self.add_game_butt_clicked)
		self.main_layout.addWidget(self.add_game_butt)

		# Dialog window customization
		self.setLayout(self.main_layout)
		self.setWindowTitle("Serial Monitor")
		self.setMinimumSize(600, 480)

	def game_data_download_butt_clicked(self):
		# id = 648800  # ID игры Raft
		game_id = self.game_id_text.toPlainText()
		# with Database() as db:
		# 	if not db.check_post(title):
		# 		return jsonify({'success': False, 'error_message': 'Пост із такою назвою вже існує'})

		game_details = get_game_details(game_id)

		# if game_details and str(648800) in game_details and game_details[str(648800)]['success']:
		if game_details[str(game_id)]['success']:
			game_data = game_details[str(game_id)]['data']

			list_platforms = []
			if game_data['platforms']['windows']:
				list_platforms.append('Windows')
			if game_data['platforms']['mac']:
				list_platforms.append('MacOS')
			if game_data['platforms']['linux']:
				list_platforms.append('Linux')

			self.game_title_text.setText(game_data['name'])
			self.page_link_text.setText(f"https://store.steampowered.com/app/{game_id}/")
			self.image_link_text.setText(game_data['header_image'])
			self.short_description_text.setText(game_data['short_description'])
			self.website_text.setText(game_data['website'])
			self.developers_text.setText(f"{', '.join(game_data['developers'])}")
			self.publishers_text.setText(f"{', '.join(game_data['publishers'])}")
			self.coming_soon_text.setText(str(game_data['release_date']['coming_soon']))
			self.release_date_text.setText(game_data['release_date']['date'])
			self.platforms_text.setText(f"{', '.join(list_platforms)}")
			self.steam_categories_text.setText(f"{', '.join([category['description'] for category in game_data.get('categories', [])])}")
			self.steam_tags_text.setText(f"{', '.join([genre['description'] for genre in game_data.get('genres', [])])}")
			self.cost_text.setText(game_data['price_overview']['final_formatted'])

			self.steamDB_game_link_text.setText(f"https://steamdb.info/app/{game_id}/")
		else:
			print(f"Не удалось получить данные для приложения с ID {game_id}")

	def add_game_butt_clicked(self):
		# Формуємо метаданні посту
		game_metadata = {
			"game_id": self.game_id_text.toPlainText(),
			'game_title': self.game_title_text.toPlainText(),
			'page_link': self.page_link_text.toPlainText(),
			'image_link': self.image_link_text.toPlainText(),
			"short_description": self.short_description_text.toPlainText(),
			"website": self.website_text.toPlainText(),
			"developers": self.developers_text.toPlainText(),
			"publishers": self.publishers_text.toPlainText(),
			"coming_soon": self.coming_soon_text.toPlainText(),
			'release_date': self.release_date_text.toPlainText(),
			'platforms': self.platforms_text.toPlainText(),
			"steam_categories": self.steam_categories_text.toPlainText(),
			'steam_tags': self.steam_tags_text.toPlainText(),
			'cost': self.cost_text.toPlainText(),
			'category': self.category_text.toPlainText(),
			'steamDB_game_link': self.steamDB_game_link_text.toPlainText(),
			"steam_reviews": self.steam_reviews_text.toPlainText(),
			'steamDB_rating_stats': self.steamDB_rating_stats_text.toPlainText(),
			'positive_reviews_stats': self.positive_reviews_stats_text.toPlainText(),
			'negative_reviews_stats': self.negative_reviews_stats_text.toPlainText(),
			'discount': self.discount_text.toPlainText(),
			'price': self.price_text.toPlainText(),
			'max_discount': self.max_discount_text.toPlainText(),
			'min_price': self.min_price_text.toPlainText(),
			'stability': self.stability_text.toPlainText(),
			'frequency': self.frequency_text.toPlainText(),
			'user_tags': self.user_tags_text.toPlainText(),
			'added_date': self.added_date_text.toPlainText(),
			'comment': self.comment_text.toPlainText()
		}

		# Зберігаємо метадані в БД
		with Database() as db:
			db.add_game(game_metadata)

		# return jsonify({'success': True})
