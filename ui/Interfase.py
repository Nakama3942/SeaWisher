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

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QSizePolicy, QPlainTextEdit, QLineEdit, QPushButton, QTableView, QSpacerItem, QLabel

class Interface(QMainWindow):
	def __init__(self):
		super(Interface, self).__init__()

		##############################
		#
		# Layout
		#
		##############################
		self.main_layout = QVBoxLayout()

		self.game_data_test = QPlainTextEdit()
		self.game_data_test.appendPlainText("Test")
		self.main_layout.addWidget(self.game_data_test)

		##############################
		#
		# Main window customization
		#
		##############################
		self.central_widget = QWidget()
		self.central_widget.setLayout(self.main_layout)
		self.setCentralWidget(self.central_widget)
		self.setWindowTitle("SeaWisher")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = Interface()
	ui.show()
	sys.exit(app.exec())
