import requests
from endpoints.base_endpoint import BaseEndpoint
class GetTariffDataNegative(BaseEndpoint):
    def get_tariff_data_negative_406(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans"
        )
        self.response_json = self.response.json()


    def get_tariff_data_negative_404(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans?account_id=184"
        )
        self.response_json = self.response.json()

    def get_room_category_data_500(self):
        self.response = requests.get(
            "https://public-api.reservationsteps.ru/v1/api/plans?account_id=asas"
        )



