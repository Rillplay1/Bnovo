from endpoints.get_hotel_meta import HotelMeta

def test_get_hotel_meta():
    hotel_meta = HotelMeta()
    hotel_meta.get_hotel_meta()
    hotel_meta.check_response_is_200()
    hotel_meta.check_response_uid("uid")
    hotel_meta.check_name_is_string("name")
    hotel_meta.check_id_is_int("id")
    hotel_meta.check_response_phone_email_address_is_string()
    hotel_meta.check_hotel_type()



