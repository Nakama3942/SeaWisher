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

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QPlainTextEdit, QLineEdit, QPushButton, QTableView, QSpacerItem, QLabel

from wisher.ui.add_game_dialog import AddGameDialog

class SeaWisher(QMainWindow):
	def __init__(self):
		super(SeaWisher, self).__init__()

		###################
		# Initialization
		###################
		# Initialization of dialog windows
		self.add_game_dialog = AddGameDialog()

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
		self.db_test_butt.clicked.connect(self.db_test_butt_clicked)
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

	def db_test_butt_clicked(self):
		self.add_game_dialog.show()
