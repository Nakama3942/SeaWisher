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

import requests
import json

def get_game_details(game_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP ошибки
        # print(f"Response content: {json.dumps(response.json(), indent=4)}")  # Для отладки
        # with open("steam test dump.txt", "w") as dump:
        #     dump.write(json.dumps(response.json(), indent=4))
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode failed: {e}")
        return None
