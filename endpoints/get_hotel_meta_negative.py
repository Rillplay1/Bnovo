import requests
from endpoints.base_endpoint import BaseEndpoint

class HotelMetaNegative(BaseEndpoint):
    def get_hotel_meta_negative_406(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/accounts"
        )

    def check_hotel_meta_message_negative_is_406(self):
        json_data = self.response.json()
        assert any(errors["message"] == "Не передан обязательный параметр uid"
                   for errors in json_data["errors"])

    def get_hotel_meta_negative_404(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/accounts?uid=123"
        )






