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

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum, Boolean, ForeignKey, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Games(Base):
	__tablename__ = "games"
	id = Column(Integer, primary_key=True)

	# ############################################################
	# Стимовская информация
	# Скачивается автоматически при добавлении игры
	# ############################################################
	game_id = Column(String, nullable=False)  # ID игры
	game_title = Column(String, nullable=False)  # Название игры (Базовый)
	page_link = Column(String, nullable=False)  # Ссылка на игру в Стиме (Базовый)
	image_link = Column(String, nullable=False)  # Ссылка на обложку игры (Базовый)
	short_description = Column(String, nullable=False)  # Краткое описание
	website = Column(String, nullable=False)  # Ссылка на сайт игры
	developers = Column(String, nullable=False)  # Разработчики
	publishers = Column(String, nullable=False)  # Издатели
	coming_soon = Column(String, nullable=False)  #
	release_date = Column(String, nullable=False)  # Дата релиза игры (Базовый)
	platforms = Column(String, nullable=False)  # Платформы, на которые вышла игра (Базовый)
	steam_categories = Column(String, nullable=False)  # Стимовские категории
	steam_tags = Column(String, nullable=False)  # Жанры игры (Базовый)
	cost = Column(String, nullable=False)  # Стоимость игры (Базовый)

	# ############################################################
	# Информация со SteamDB
	# Вводится вручную при добавлении игры
	# ############################################################
	category = Column(String, nullable=False)  # Категория (по библиотеке) куда я определяю игру
	steamDB_game_link = Column(String, nullable=False)  # Ссылка на игру в SteamDB
	steam_reviews = Column(Enum('Mostly positive', 'Very happy'), nullable=False)  # Рецензии
	steamDB_rating_stats = Column(String, nullable=False)  # Рейтинг игры по SteamDB
	positive_reviews_stats = Column(String, nullable=False)  # Количество позитивных отзывов по SteamDB
	negative_reviews_stats = Column(String, nullable=False)  # Количество негативных отзывов по SteamDB
	discount = Column(String, nullable=False)  # Ожидаемая скидка (которая в среднем чаще всего даётся)
	price = Column(String, nullable=False)  # Цена по ожидаемой скидке
	max_discount = Column(String, nullable=False)  # Максимальная скидка, которая когда-либо была на игру
	min_price = Column(String, nullable=False)  # Цена по максимальной скидке (выбирать при минимальной стоимости игры)
	stability = Column(Enum('Constant', 'Not constant'), nullable=False)  # Стабильность скидки
	frequency = Column(Enum('Frequent', 'Rare'), nullable=False)  # Частота скидки
	user_tags = Column(String, nullable=False)  # Теги

	# ############################################################
	# Информация от себя
	# Вводится вручную при добавлении игры
	# ############################################################
	added_date = Column(String, nullable=False)  # Дата добавления в список желаемого
	comment = Column(String, nullable=False)  # Объяснение, почему я хочу купить игру

	# ############################################################
	# Информация о покупке - чек
	# Вводится вручную после покупки игры
	# ############################################################
	purchase_date = Column(String)  # Дата покупки
	purchase_time = Column(String)  # Время покупки
	total_discount = Column(String)  # Скидка на момент покупки
	total_price = Column(String)  # Сколько я заплатил

	# ############################################################
	# Впечатления об игре
	# Вводится вручную после написания отзыва на игру в Стиме
	# ############################################################
	played_steam_time = Column(String)  # Наиграно времени (по Стимовскому стандарту) в момент написания отзыва
	played_standard_time = Column(String)  # Наиграно времени (в переводе в обычное время) в момент написания отзыва
	grade = Column(String)  # Объективная оценка (со Стим отзыва)
	review_link = Column(String)  # Ссылка на Стим отзыв
	impressions = Column(String)  # Субъективная оценка
	impressions_comment = Column(String)  # Краткое объяснение субъективной оценки

	# ############################################################
	# Техническая информация
	# Флаги для программы
	# ############################################################
	hidden = Column(Boolean, nullable=False)  # Указывает, удалена ли игра со списка желаемого
	bought = Column(Boolean, nullable=False)  # Указывает, куплена ли игра

	# todo: удалить
	# description = Column(String, nullable=False)
	# tags = Column(String, nullable=False)
	# importance = Column(Enum('Normal', 'Rare', 'Elite', 'Super Rare', 'Ultra Rare'), nullable=False)
	# created_at = Column(DateTime, nullable=False)
	# published_at = Column(DateTime)
	# last_changed_at = Column(DateTime)

class Database:
	def __init__(self):
		super(Database, self).__init__()

		self.engine = create_engine("sqlite:///game_database.db")
		Base.metadata.create_all(self.engine)
		self.Session = sessionmaker(bind=self.engine)
		self.session = self.Session()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

	def close(self):
		self.session.close()

	def add_game(self, game_data):
		adding_game = Games(**game_data)
		self.session.add(adding_game)
		self.session.commit()

	######################### BLOG #########################

	# def get_post(self, title):
	# 	return self.session.query(Posts).filter_by(title=title).first()
	#
	# def get_all_posts(self, limit):
	# 	if limit == 0:
	# 		return self.session.query(Posts).order_by(desc(Posts.created_at)).all()
	# 	else:
	# 		return self.session.query(Posts).order_by(desc(Posts.created_at)).limit(limit).all()
	#
	# def check_post(self, title):
	# 	return self.session.query(Posts.title).filter_by(title=title).scalar() is None
	#
	# def search_post(self, column, text):  # Метод для поиска постов
	# 	if text:
	# 		# Создаем динамическое условие для поиска в указанной колонке
	# 		search_condition = getattr(Posts, column).ilike(f'%{text}%')
	# 		# Выполняем запрос к БД с использованием условия
	# 		result = self.session.query(Posts).filter(search_condition).all()
	# 	else:
	# 		result = []
	#
	# 	return result
	#
	# def create_post(self, title, post_data):
	# 	new_post = Posts(title=title, **post_data)
	# 	self.session.add(new_post)
	# 	self.session.commit()
	#
	# def update_post(self, title, new_post_data):
	# 	post = self.get_post(title)
	# 	if post:
	# 		# Оновлюємо поля посту
	# 		for key, value in new_post_data.items():
	# 			setattr(post, key, value)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	#
	# def remove_post(self, title):
	# 	post = self.session.query(Posts).filter_by(title=title).first()
	# 	if post:
	# 		self.session.delete(post)
	# 		self.session.commit()

	######################### FTES #########################

	# def get_user(self, username):
	# 	return self.session.query(User).filter_by(username=username).first()
	#
	# def get_all_users(self):
	# 	return self.session.query(User).all()
	#
	# def check_username(self, username):
	# 	existing_user = self.session.query(User.username).filter_by(username=username).scalar()
	# 	return existing_user is None
	#
	# def create_user(self, username, user_data):
	# 	new_user = User(username=username, **user_data)
	# 	self.session.add(new_user)
	# 	self.session.commit()
	# 	self.new.emit(new_user)
	#
	# def set_user_status(self, username, online: bool):
	# 	user = self.get_user(username)
	# 	if user:
	# 		# Оновлюємо статус користувача
	# 		setattr(user, "online", online)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	# 		self.dirty.emit(user)
	#
	# def update_user(self, username, new_data):
	# 	user = self.get_user(username)
	# 	if user:
	# 		# Оновлюємо поля користувача
	# 		for key, value in new_data.items():
	# 			setattr(user, key, value)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	# 		self.dirty.emit(user)
	#
	# def silent_spy_update(self, username, new_data):
	# 	user = self.get_user(username)
	# 	if user:
	# 		for key, value in new_data.items():
	# 			# Створюємо об'єкт запиту для оновлення поля
	# 			update_query = update(User).where(User.username == username)
	# 			# Оновлюємо поле, додаючи нове значення
	# 			update_query = update_query.values({key: User.__dict__[key] + value})
	# 			# Виконуємо запит
	# 			self.session.execute(update_query)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	#
	# def number_recalculate(self, username, new_data):
	# 	user = self.get_user(username)
	# 	if user:
	# 		# Оновлюємо поля користувача
	# 		for key, value in new_data.items():
	# 			setattr(user, key, getattr(user, key) + value)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	#
	# def set_user_date(self, username, new_data):
	# 	user = self.get_user(username)
	# 	if user:
	# 		# Оновлюємо поля користувача
	# 		for key, value in new_data.items():
	# 			setattr(user, key, value)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	#
	# def set_user_time(self, username, new_data):
	# 	user = self.get_user(username)
	# 	if user:
	# 		# Оновлюємо поля користувача
	# 		for key, value in new_data.items():
	# 			tim = value - getattr(user, "last_login_date")
	# 			setattr(user, key, tim)
	#
	# 		# Фіксуємо значення в БД
	# 		self.session.commit()
	#
	# def remove_user(self, username):
	# 	user = self.session.query(User).filter_by(username=username).first()
	# 	if user:
	# 		self.session.delete(user)
	# 		self.deleted.emit(username)
	# 		self.session.commit()
	#
	# def close(self):
	# 	self.session.close()
