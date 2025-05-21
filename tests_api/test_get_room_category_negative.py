from endpoints.get_room_category_data_negative import GetRoomCategoryDataNegative


def test_get_room_category_negative_500():
    room_category_negative = GetRoomCategoryDataNegative()
    room_category_negative.get_room_category_data_500()
    room_category_negative.check_response_is_500()
    room_category_negative.check_response_message_negative_is_500()


def test_get_room_category_negative_406():
    room_category_negative = GetRoomCategoryDataNegative()
    room_category_negative.get_room_category_data_406()
    room_category_negative.check_response_is_406()
    room_category_negative.check_response_message_negative_is_406()


def test_get_room_category_negative_404():
    room_category_negative = GetRoomCategoryDataNegative()
    room_category_negative.get_room_category_data_404()
    room_category_negative.check_response_is_404()
    room_category_negative.check_response_message_negative_is_404()
