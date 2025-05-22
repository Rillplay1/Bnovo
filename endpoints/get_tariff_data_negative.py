import requests
from endpoints.base_endpoint import BaseEndpoint
import allure
from config.logger import logger



class GetTariffDataNegative(BaseEndpoint):
    @allure.step("Отправка запроса без account_id - ожидаем 406")
    def get_tariff_data_negative_406(self):
        logger.info("Отправка запроса без account_id - ожидаем 406")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans"
        )
        self.response_json = self.response.json()



    @allure.step("Отправка запроса с несуществующим account_id - ожидаем 404")
    def get_tariff_data_negative_404(self):
        logger.info("Отправка запроса с несуществующим account_id - ожидаем 404")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans?account_id=184"
        )
        self.response_json = self.response.json()



    @allure.step("Отправка запроса с неверным account_id - ожидаем 500")
    def get_room_category_data_500(self):
        logger.info("Отправка запроса с неверным account_id - ожидаем 500")
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans?account_id=asas"
        )



