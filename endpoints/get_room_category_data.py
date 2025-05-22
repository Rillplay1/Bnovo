import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
from config.logger import logger



class GetRoomCategoryData(BaseEndpoint):
    @allure.step("Отправка запроса на получение данных о категориях номеров")
    def room_category(self, account_id):
        logger.info("Отправка запроса на получение данных о категориях номеров")
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id={account_id}"
        )
        self.response_json = self.response.json()



    @allure.step("Проверка, что id и description содержатся в ответе")
    def check_response_id_description(self, id, description):
        logger.info("Проверка, что id и description содержатся в ответе")
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert id in room
            assert description in room



    @allure.step("Проверка, что adults и children содержатся в ответе и имеют тип целое число")
    def check_response_adults_and_children(self):
        logger.info("Проверка что adults и children содержатся в ответе и имеют тип целое число")
        data = self.response_json
        rooms = data["rooms"]
        for room in rooms:
            assert "adults" in room and isinstance(room["adults"], int) and room["adults"] <= 15
            assert "children" in room and isinstance(room["adults"], int) and room["children"] <= 15



    @allure.step("Проверка, что в ответе есть photos, а так же оно имеет ключи id, name, create_data")
    def check_response_photos(self):
        logger.info("Проверка, что в ответе есть photos, а так же оно имеет ключи id, name, create_data")
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            photos = room.get("photos", [])
            if not photos:
                continue
            for photo in photos:
                assert "id" in photo
                assert "name" in photo
                assert "create_date" in photo



    @allure.step("Проверка, что в ответе есть name_ru, name_en и т.д")
    def check_response_localisation(self):
        logger.info("Проверка, что в ответе есть name_ru, name_en и т.д")
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            name_fields = [key for key in room.keys() if key.startswith("name_")]
            assert len(name_fields) > 0



    @allure.step("Проверка, что ключ name есть в ответе и имеет тип - строка")
    def check_room_name_is_string(self, name):
        logger.info("Проверка, что ключ name есть в ответе и имеет тип - строка")
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert name in room
            assert isinstance(room[name], str)



    @allure.step("Проверка, что ключ id есть в ответе и имеет тип - целое число")
    def check_account_id_is_integer(self, account_id):
        logger.info("Проверка, что ключ id есть в ответе и имеет тип - целое число")
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert account_id in room
            assert isinstance(room[account_id], int)





