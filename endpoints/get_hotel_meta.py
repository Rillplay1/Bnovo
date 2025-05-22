import requests
from endpoints.base_endpoint import BaseEndpoint
from config.logger import logger
import allure



class HotelMeta(BaseEndpoint):
    @allure.step("Отправка запроса на получение мета-информации об отеле")
    def get_hotel_meta(self):
        logger.info("Отправка запроса на получение мета-информации об отеле")
        uid = "d7494710-8c8c-4c4c-bba4-f71caf96fece"
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/accounts?uid={uid}"
        )
        self.response_json = self.response.json()



    @allure.step("Проверка, что uid содержится в ответе и является строкой")
    def check_response_uid_is_string(self, uid):
        logger.info("Проверка, что uid содержится в ответе и является строкой")
        data = self.response_json
        assert uid in data["account"]
        assert isinstance(data["account"][uid], str)



    @allure.step("Проверка типа отеля")
    def check_hotel_type(self):
        logger.info("Проверка типа отеля")
        allowed_types = [
            "hotel", "apartments", "hostel", "pension", "recreational center", "sanatorium", "apart_hotel", "glamping",
            "country_hotel", "mote", "children_health_camp", "other"
        ]
        account = self.response_json.get("account", {})
        assert "hotel_type" in account
        assert account["hotel_type"] in allowed_types



    @allure.step("Проверка, что phone, email, address - строки")
    def check_response_phone_email_address_is_string(self):
        logger.info("Проверка, что phone, email, address - строки")
        data = self.response_json
        account = data.get("account", {})
        for key in ["phone", "email", "address"]:
            value = account.get(key)
            assert isinstance(value, str)



    @allure.step("Проверка, что имя является строкой")
    def check_name_is_string(self, name):
        logger.info("Проверка, что имя является строкой")
        data = self.response_json
        assert name in data["account"]
        assert isinstance(data["account"][name], str)




