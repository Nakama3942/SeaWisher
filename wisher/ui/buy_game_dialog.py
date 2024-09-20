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

class BuyGameDialog(QDialog):
	def __init__(self):
		super(BuyGameDialog, self).__init__()

		# Главный макет
		self.main_layout = QVBoxLayout()

		# # Поле для ввода ID игры
		# self.game_id_layout = QHBoxLayout()
		# self.game_id_label = QLabel("Введи ID игры в Steam:", self)
		# self.game_id_text = QTextEdit(self)
		# self.game_id_layout.addWidget(self.game_id_label)
		# self.game_id_layout.addWidget(self.game_id_text)
		# self.main_layout.addLayout(self.game_id_layout)
		#
		# # Кнопка для подгрузки данных
		# self.game_data_download_butt = QPushButton("Подгрузить данные со Steam", self)
		# self.game_data_download_butt.clicked.connect(self.game_data_download_butt_clicked)
		# self.main_layout.addWidget(self.game_data_download_butt)
		#
		# # Поле для ввода названия игры
		# self.game_title_layout = QHBoxLayout()
		# self.game_title_label = QLabel("Название игры:", self)
		# self.game_title_text = QTextEdit(self)
		# self.game_title_layout.addWidget(self.game_title_label)
		# self.game_title_layout.addWidget(self.game_title_text)
		# self.main_layout.addLayout(self.game_title_layout)
		#
		# # Поле для ввода ссылки на Стимовскую страницу игры
		# self.page_link_layout = QHBoxLayout()
		# self.page_link_label = QLabel("Ссылка на игру:", self)
		# self.page_link_text = QTextEdit(self)
		# self.page_link_layout.addWidget(self.page_link_label)
		# self.page_link_layout.addWidget(self.page_link_text)
		# self.main_layout.addLayout(self.page_link_layout)
		#
		# # Поле для ввода обложку игры
		# self.image_link_layout = QHBoxLayout()
		# self.image_link_label = QLabel("Ссылка на обложку:", self)
		# self.image_link_text = QTextEdit(self)
		# self.image_link_layout.addWidget(self.image_link_label)
		# self.image_link_layout.addWidget(self.image_link_text)
		# self.main_layout.addLayout(self.image_link_layout)
		#
		# # Поле для ввода краткого описания
		# self.short_description_layout = QHBoxLayout()
		# self.short_description_label = QLabel("Краткое описание:", self)
		# self.short_description_text = QTextEdit(self)
		# self.short_description_layout.addWidget(self.short_description_label)
		# self.short_description_layout.addWidget(self.short_description_text)
		# self.main_layout.addLayout(self.short_description_layout)
