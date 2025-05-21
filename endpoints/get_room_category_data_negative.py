import requests
from endpoints.base_endpoint import BaseEndpoint


class GetRoomCategoryDataNegative(BaseEndpoint):
    def get_room_category_data_500(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id=aaa"
        )


    def get_room_category_data_406(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes"
        )


    def get_room_category_data_404(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id=184"
        )
