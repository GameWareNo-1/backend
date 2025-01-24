from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Level

class LevelAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Sample data for testing
        self.valid_level_data = {
            "name": "Test Level 1",
            "time": 300,
            "materials": [1, 2, 3],
            "target": {"1": 2, "2": 1, "3": 1},  # Sum is 4
        }
        self.invalid_target_data = {
            "name": "Invalid Target",
            "time": 300,
            "materials": [1, 2, 3],
            "target": {"1": 3, "2": 1, "3": 1},  # Sum is 5
        }
        self.invalid_materials_data = {
            "name": "Invalid Materials",
            "time": 300,
            "materials": "not_a_list",  # Invalid type
            "target": {"1": 2, "2": 1, "3": 1},  # Sum is 4
        }

    # Test creating a level successfully
    def test_create_level_success(self):
        response = self.client.post('/levels/', self.valid_level_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_level_data['name'])

    # Test creating a level with invalid target (sum != 4)
    def test_create_level_invalid_target(self):
        response = self.client.post('/levels/', self.invalid_target_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("target", response.data)
        self.assertIn("Sum of target values must equal 4.", response.data['target'][0])

    # Test creating a level with invalid materials field
    def test_create_level_invalid_materials(self):
        response = self.client.post('/levels/', self.invalid_materials_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("materials", response.data)

    # Test retrieving all levels
    def test_get_all_levels(self):
        Level.objects.create(**self.valid_level_data)
        response = self.client.get('/levels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.valid_level_data['name'])

    # Test retrieving a single level by ID
    def test_get_single_level(self):
        level = Level.objects.create(**self.valid_level_data)
        response = self.client.get(f'/levels/{level.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.valid_level_data['name'])

    # Test retrieving a non-existent level
    def test_get_non_existent_level(self):
        response = self.client.get('/levels/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test deleting a level successfully
    def test_delete_level(self):
        level = Level.objects.create(**self.valid_level_data)
        response = self.client.delete(f'/levels/{level.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Level.objects.filter(id=level.id).exists())

    # Test deleting a non-existent level
    def test_delete_non_existent_level(self):
        response = self.client.delete('/levels/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test that duplicate names are not allowed (if enforced)
    def test_create_duplicate_name(self):
        Level.objects.create(**self.valid_level_data)
        response = self.client.post('/levels/', self.valid_level_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

