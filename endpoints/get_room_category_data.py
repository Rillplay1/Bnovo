import requests
from endpoints.base_endpoint import BaseEndpoint


class GetRoomCategoryData(BaseEndpoint):
    def room_category(self, account_id):
        self.response = requests.get(
            f"https://public-api.reservationsteps.ru/v1/api/roomtypes?account_id={account_id}"
        )
        self.response_json = self.response.json()


    def check_response_id_description(self, id, description):
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert id in room
            assert description in room


    def check_response_adults_and_children(self):
        data = self.response_json
        rooms = data["rooms"]
        for room in rooms:
            assert "adults" in room and isinstance(room["adults"], int) and room["adults"] <= 15
            assert "children" in room and isinstance(room["adults"], int) and room["children"] <= 15


    def check_response_photos(self):
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            photos = room.get("photos", [])
            if not photos:
                continue
            for photo in photos:
                assert "id" in photo
                assert "name" in photo
                assert "create_date" in photo


    def check_response_locations(self):
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            name_fields = [key for key in room.keys() if key.startswith("name_")]
            assert len(name_fields) > 0


    def check_room_name_is_string(self, name):
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert name in room
            assert isinstance(room[name], str)


    def check_account_id_is_integer(self, account_id):
        data = self.response_json
        rooms = data.get("rooms", [])
        for room in rooms:
            assert account_id in room
            assert isinstance(room[account_id], int)





