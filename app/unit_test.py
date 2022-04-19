import unittest
from main import app
import random


class ApiTestCase(unittest.TestCase):
    building_names = ["Pegasus", "Elixir", "Moon Tiger Enterprise"]
    sensor_names = ["temperature_sensor", "humidity_sensor", "light_sensor"]
    tester = app.test_client()
    fake_data = {
        "name": "Icarus",
        "geo_latitude": 0.9916226046594874,
        "geo_longitude": 0.36899048255865285
    }
    fake_data_update = {
        "name": "Pluto",
        "geo_latitude": 0.9916226046594874,
        "geo_longitude": 0.36899048255865285
    }
    id = 2

    # Test api
    def test_1_index(self):
        response = self.tester.get("/api/")
        self.assertEqual(response.status_code, 200)

    def test_2_index_content(self):
        response = self.tester.get("/api/buildings")
        self.assertEqual(response.content_type, "application/json")

    def test_3_index_data(self):
        response = self.tester.get("/api/")
        self.assertTrue(b'info' in response.data, "Should be info")

    # Test buildings
    def test_4_get_all_buildings(self):
        response = self.tester.get("/api/buildings")
        self.assertEqual(response.status_code, 200)

    def test_5_get_one_building(self):
        ran = random.randrange(0, len(self.building_names))
        response = self.tester.get("/api/buildings/" + self.building_names[ran])
        self.assertEqual(response.status_code, 200, "Should work if db was seeded")

    def test_6_add_building(self):
        response = self.tester.post("/api/buildings", json=self.fake_data)
        self.assertEqual(response.status_code, 201)

    def test_7_get_new_building(self):
        response = self.tester.get("api/buildings/" + self.fake_data["name"])
        self.assertEqual(response.status_code, 200)

    def test_8_update_building(self):
        response = self.tester.put("api/buildings/" + str(self.id), json=self.fake_data_update)
        self.assertEqual(response.status_code, 201)

    def test_9_delete_building(self):
        response = self.tester.delete("api/buildings/" + self.fake_data_update["name"])
        self.assertEqual(response.status_code, 200)

    # tests readings
    def test_10_get_readings(self):
        ran = random.randrange(0, len(self.sensor_names))
        response = self.tester.get("api/readings/" + self.sensor_names[ran])
        self.assertEqual(response.status_code, 200, "Should work if db was seeded")

    def test_11_get_readings_from_building(self):
        ran = random.randrange(0, len(self.sensor_names))
        response = self.tester.get("api/readings/" + self.building_names[ran] + "/" + self.sensor_names[ran])
        self.assertEqual(response.status_code, 200, "Should work if db was seeded")


if __name__ == "__main__":
    unittest.main() 