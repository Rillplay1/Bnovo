import requests
from endpoints.base_endpoint import BaseEndpoint
from config.logger import logger
import allure



class GetRoomCategoryDataNegative(BaseEndpoint):
    @allure.step("Отправка запроса с неверным account_id - ожидаем 500")
    def get_room_category_data_500(self):
        logger.info("Отправка запроса с неверным account_id - ожидаем 500")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id=aaa"
        )



    @allure.step("Отправка запроса без account_id - ожидаем 406")
    def get_room_category_data_406(self):
        logger.info("Отправка запроса без account_id - ожидаем 406")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes"
        )



    @allure.step("Отправка запроса с несуществующим account_id - ожидаем 404")
    def get_room_category_data_404(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id=184"
        )
