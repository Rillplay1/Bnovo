from conftest import random_account_id
from endpoints.get_room_category_data import GetRoomCategoryData

def test_get_hotel_room_category_positive(random_account_id):
    get_room_category_data = GetRoomCategoryData()
    get_room_category_data.room_category(random_account_id)
    get_room_category_data.check_response_is_200()
    get_room_category_data.check_response_id_description("id", "description")
    get_room_category_data.check_room_name_is_string("name")
    get_room_category_data.check_account_id_is_integer("account_id")
    get_room_category_data.check_response_adults_and_children()
    get_room_category_data.check_response_photos()
    get_room_category_data.check_response_localisation()