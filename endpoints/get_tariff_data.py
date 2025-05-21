import requests
from endpoints.base_endpoint import BaseEndpoint

class GetTariffData(BaseEndpoint):
    def get_tariff_data(self, account_id):
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/plans?account_id={account_id}"
        )
        self.response_json = self.response.json()

    def check_response_is_description(self):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "description" in plan


    def check_account_id_is_integer(self, random_account_id):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "account_id" in plan
            assert isinstance(plan["account_id"], int)

    def check_name_is_string(self, random_account_id):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "name" in plan
            assert isinstance(plan["name"], str)

    def check_booking_guarantee_sum(self):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "booking_guarantee_sum" in plan
            assert isinstance(plan["booking_guarantee_sum"],(str, type(None)))

    def check_booking_guarantee_unit(self):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "booking_guarantee_unit" in plan
            assert plan["booking_guarantee_unit"] in ("percentage", "absolute", None)

    def check_cancellation_rules(self):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "cancellation_rules" in plan
            assert isinstance(plan["cancellation_rules"], (str, type(None)))

    def check_cancellation_deadline(self):
        data = self.response_json
        plans = data.get("plans", [])
        for plan in plans:
            assert "cancellation_deadline" in plan
            assert isinstance(plan["cancellation_deadline"], (str, type(None)))



