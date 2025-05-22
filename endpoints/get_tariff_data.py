import requests
from endpoints.base_endpoint import BaseEndpoint
import allure
from config.logger import logger



class GetTariffData(BaseEndpoint):
    @allure.step("Отправка запроса на получение данных о тарифах")
    def get_tariff_data(self, account_id):
        logger.info("Отправка запроса на получение данных о тарифах")
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/plans?account_id={account_id}"
        )
        self.response_json = self.response.json()



    @allure.step("Проверка, что description содержится в ответе")
    def check_response_is_description(self):
        logger.info("Проверка, что description содержится в ответе")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "description" in plan



    @allure.step("Проверка, что account_id содержится в ответе и имеет тип - целое число")
    def check_account_id_is_integer(self, random_account_id):
        logger.info("Проверка, что account_id содержится в ответе и имеет тип - целое число")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "account_id" in plan
            assert isinstance(plan["account_id"], int)



    @allure.step("Проверка, что name содержится в ответе и имеет тип - строка")
    def check_name_is_string(self, random_account_id):
        logger.info("Проверка, что name содержится в ответе и имеет тип - строка")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "name" in plan
            assert isinstance(plan["name"], str)



    @allure.step("Проверка, что booking_guarantee_sum содержится в ответе и имеет тип - строка")
    def check_booking_guarantee_sum(self):
        logger.info("Проверка, что booking_guarantee_sum содержится в ответе и имеет тип - строка")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "booking_guarantee_sum" in plan
            assert isinstance(plan["booking_guarantee_sum"],(str, type(None)))



    @allure.step("Проверка, что booking_guarantee_unit содержится в ответе, является строкой, а так же имеет значение percentage, absolute или None")
    def check_booking_guarantee_unit(self):
        logger.info("Проверка, что booking_guarantee_unit содержится в ответе, является строкой, а так же имеет значение percentage, absolute или None")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "booking_guarantee_unit" in plan
            assert isinstance(plan["booking_guarantee_unit"], (str, type(None)))
            assert plan["booking_guarantee_unit"] in ("percentage", "absolute", None)



    @allure.step("Проверка, что cancellation_rules есть в ответе и имеет тип строку либо пустое значение")
    def check_cancellation_rules(self):
        logger.info("Проверка, что cancellation_rules есть в ответе и имеет тип строку либо пустое значение")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "cancellation_rules" in plan
            assert isinstance(plan["cancellation_rules"], (str, type(None)))



    @allure.step("Проверка, что cancellation_deadline есть в ответе и имеет тип строку либо пустое значение")
    def check_cancellation_deadline(self):
        logger.info("Проверка, что cancellation_deadline есть в ответе и имеет тип строку либо пустое значение")
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "cancellation_deadline" in plan
            assert isinstance(plan["cancellation_deadline"], (str, type(None)))



