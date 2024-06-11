import pytest
from make_requests import make_request
from config import API_KEY

class TestClass:

    def test_search_asteroids_with_success(self):
        # Act:
        response = make_request(API_KEY)
        # Assertion:
        assert response.status_code == 200  # Validation of status code
        data = response.json()
        # Assertion of body response content:
        assert 'element_count' in data
        assert data["element_count"] > 0

    def test_search_without_any_query_parameter(self):
        response = make_request("") #empty query parameter
        assert response.status_code == 403

    def test_search_with_Start_date_only(self):
        # setting the start day as today
        response = make_request(f"{API_KEY}&start_date=2024-06-11")
        assert response.status_code == 200
        data = response.json()
        assert 'element_count' in data
        assert data["element_count"] > 0

    def test_search_with_end_date_only(self):
        # For example, let's set the end date to be 7 days from today
        response = make_request(f"{API_KEY}&end_date=2024-06-18")
        assert response.status_code == 200
        data = response.json()
        assert 'element_count' in data
        assert data["element_count"] > 0

    def test_search_in_valid_date_range(self):
        # Let's set a valid date range, for example, the last week
        response = make_request(f"{API_KEY}&start_date=2024-06-04&end_date=2024-06-11")
        assert response.status_code == 200
        data = response.json()
        assert all(field != "" for field in data.values())

    def test_search_start_date_bigger_than_end_date(self):
        # Providing start date bigger than end date should still return 200, if the API doesn't handle this case properly
        response = make_request(f"{API_KEY}&start_date=2024-06-12&end_date=2024-06-11")
        assert response.status_code == 200

    def test_search_with_invalid_api_token(self):
        # Using an invalid API token should return 403
        response = make_request("3H2cWYv2OnvDbzhE33TEQqT7xMsOf77dje6azmLUUUUUUUUUhgghyhtththththth876thtttu")
        assert response.status_code == 403



