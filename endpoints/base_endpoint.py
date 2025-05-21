class BaseEndpoint:
    response = None
    response_json = None




    def check_id_is_int(self, id):
        data = self.response_json
        assert id in data["account"]
        assert isinstance(data["account"][id], int)


    def check_response_message_negative_is_406(self):
        json_data = self.response.json()
        assert any(errors["message"] == "Не передан обязательный параметр account_id"
                   for errors in json_data["errors"])

    def check_response_message_negative_is_500(self):
        json_data = self.response.json()
        assert json_data.get("message") == "Internal error, our staff is notified"


    def check_response_is_406(self):
        assert self.response.status_code == 406


    def check_response_is_404(self):
        assert self.response.status_code == 404


    def check_response_is_500(self):
        assert self.response.status_code == 500

    def check_response_is_200(self):
        assert self.response.status_code == 200


    def check_response_message_negative_is_404(self):
        json_data = self.response.json()
        assert json_data["message"] == "Аккаунт не найден"











