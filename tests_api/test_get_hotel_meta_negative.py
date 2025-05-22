from endpoints.get_hotel_meta_negative import HotelMetaNegative

def test_get_hotel_meta_negative_is_406():
    hotel_meta_negative = HotelMetaNegative()
    hotel_meta_negative.get_hotel_meta_negative_406()
    hotel_meta_negative.check_response_is_406()
    hotel_meta_negative.check_hotel_meta_message_negative_is_406()

def test_get_hotel_meta_negative_is_404():
    hotel_meta_negative = HotelMetaNegative()
    hotel_meta_negative.get_hotel_meta_negative_404()
    hotel_meta_negative.check_response_is_404()
    hotel_meta_negative.check_response_message_negative_is_404()



