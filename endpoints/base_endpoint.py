import allure
from config.logger import logger


class BaseEndpoint:
    response = None
    response_json = None



    @allure.step("Проверка, что id является целым числом")
    def check_id_is_int(self, id):
        data = self.response_json
        logger.info("Проверка, что id есть в data['account'] ")
        assert id in data["account"]
        logger.info("Проверка, что id это целое число")
        assert isinstance(data["account"][id], int)



    @allure.step("Проверка сообщения ошибки при статусе 406")
    def check_response_message_negative_is_406(self):
        json_data = self.response.json()
        logger.info("Проверка текста сообщения ошибки при статусе 406")
        assert any(errors["message"] == "Не передан обязательный параметр account_id"
                   for errors in json_data["errors"])



    @allure.step("Проверка сообщения ошибки при статусе 500")
    def check_response_message_negative_is_500(self):
        json_data = self.response.json()
        logger.info("Проверка текста сообщения ошибки при статусе 500")
        assert json_data.get("message") == "Internal error, our staff is notified"



    @allure.step("Проверка что статус ответа - 406")
    def check_response_is_406(self):
        logger.info("Проверка что статус ответа 406")
        assert self.response.status_code == 406



    @allure.step("Проверка что статус ответа - 404")
    def check_response_is_404(self):
        logger.info("Проверка что статус ответа 404")
        assert self.response.status_code == 404



    @allure.step("Проверка что статус ответа - 500")
    def check_response_is_500(self):
        logger.info("Проверка что статус ответа 500")
        assert self.response.status_code == 500



    @allure.step("Проверка что статус ответа - 200")
    def check_response_is_200(self):
        logger.info("Проверка что статус ответа 200")
        assert self.response.status_code == 200



    @allure.step("Проверка сообщения ошибки при статусе 404")
    def check_response_message_negative_is_404(self):
        logger.info("Проверка текста сообщения ошибки при статусе 404")
        json_data = self.response.json()
        assert json_data["message"] == "Аккаунт не найден"













