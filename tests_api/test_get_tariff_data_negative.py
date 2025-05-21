from endpoints.get_tariff_data_negative import GetTariffDataNegative

def test_get_tariff_data_negative_406():
    tariff_data_negative = GetTariffDataNegative()
    tariff_data_negative.get_tariff_data_negative_406()
    tariff_data_negative.check_response_is_406()
    tariff_data_negative.check_response_message_negative_is_406()


def test_check_get_tariff_data_negative_404():
    tariff_data_negative = GetTariffDataNegative()
    tariff_data_negative.get_tariff_data_negative_404()
    tariff_data_negative.check_response_is_404()
    tariff_data_negative.check_response_message_negative_is_404()


def test_check_get_tariff_data_negative_500():
    tariff_data_negative = GetTariffDataNegative()
    tariff_data_negative.get_room_category_data_500()
    tariff_data_negative.check_response_is_500()
    tariff_data_negative.check_response_message_negative_is_500()




