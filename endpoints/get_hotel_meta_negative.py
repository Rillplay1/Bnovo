import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
from config.logger import logger



class HotelMetaNegative(BaseEndpoint):
    @allure.step("Отправка запроса без uid - ожидаем 406")
    def get_hotel_meta_negative_406(self):
        logger.info("Отправка запроса без uid - ожидаем 406")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/accounts"
        )



    @allure.step("Проверка сообщения об ошибке при статусе 406")
    def check_hotel_meta_message_negative_is_406(self):
        logger.info("Проверка сообщения об ошибке при статусе 406")
        json_data = self.response.json()
        assert any(errors["message"] == "Не передан обязательный параметр uid"
                   for errors in json_data["errors"])



    @allure.step("Отправка запроса с несуществующим uid - ожидаем 404")
    def get_hotel_meta_negative_404(self):
        logger.info("Отправка запроса с несуществующим uid - ожидаем 404")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/accounts?uid=123"
        )






