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

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class GameDataFrame(QFrame):
	def __init__(self):
		super(GameDataFrame, self).__init__()

		self.main_layout = QHBoxLayout()
		self.main_layout.setContentsMargins(4, 4, 4, 4)
		self.main_layout.setSpacing(2)

		self.image_link = QLabel()
		self.image_link.setObjectName("image_link_field_in_frame")
		self.main_layout.addWidget(self.image_link)

		self.name_layout = QVBoxLayout()
		self.button_layout = QHBoxLayout()

		self.game_title = QLabel()
		self.game_title.setObjectName("game_title_field_in_frame")
		self.release_date = QLabel()
		self.release_date.setObjectName("release_date_field_in_frame")
		self.added_date = QLabel()
		self.added_date.setObjectName("added_date_field_in_frame")

		self.delete_game_butt = QPushButton()
		self.delete_game.setObjectName("delete_game_button_in_frame")
		self.buy_game_butt = QPushButton()
		self.buy_game.setObjectName("buy_game_button_in_frame")

		self.button_layout.addWidget(self.delete_game)
		self.button_layout.addWidget(self.buy_game)

		self.name_layout.addWidget(self.game_title)
		self.name_layout.addWidget(self.release_date)
		self.name_layout.addWidget(self.added_date)
		self.name_layout.addLayout(self.game_title)

		self.main_layout.addWidget(self.image_link)

		self.cost = QLabel()
		self.cost.setObjectName("cost_field_in_frame")
		self.main_layout.addWidget(self.cost)

		self.setLayout(self.main_layout)
		self.setObjectName("game_data_frame")

	# def console_input_return_pressed(self):
	# 	pass
