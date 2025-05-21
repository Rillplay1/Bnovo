from endpoints.get_tariff_data import GetTariffData
from conftest import random_account_id

def test_get_tariff_data(random_account_id):
    tariff_data = GetTariffData()
    tariff_data.get_tariff_data(random_account_id)
    tariff_data.check_response_is_200()
    tariff_data.check_response_is_description()
    tariff_data.check_account_id_is_integer(random_account_id)
    tariff_data.check_name_is_string(random_account_id)
    tariff_data.check_booking_guarantee_sum()
    tariff_data.check_booking_guarantee_unit()
    tariff_data.check_cancellation_rules()
    tariff_data.check_cancellation_deadline()