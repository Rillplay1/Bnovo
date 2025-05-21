import requests
from endpoints.base_endpoint import BaseEndpoint


class HotelMeta(BaseEndpoint):
    def get_hotel_meta(self):
        uid = "d7494710-8c8c-4c4c-bba4-f71caf96fece"
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/accounts?uid={uid}"
        )
        self.response_json = self.response.json()


    def check_response_uid(self, uid):
        data = self.response_json
        assert uid in data["account"]
        assert isinstance(data["account"][uid], str)


    def check_hotel_type(self):
        allowed_types = [
            "hotel", "apartments", "hostel", "pension", "recreational center", "sanatorium", "apart_hotel", "glamping",
            "country_hotel", "mote", "children_health_camp", "other"
        ]
        account = self.response_json.get("account", {})

        assert "hotel_type" in account
        assert account["hotel_type"] in allowed_types


    def check_response_phone_email_address_is_string(self):
        data = self.response_json
        account = data.get("account", {})
        for key in ["phone", "email", "address"]:
            value = account.get(key)
            assert isinstance(value, str)


    def check_name_is_string(self, name):
        data = self.response_json
        assert name in data["account"]
        assert isinstance(data["account"][name], str)




