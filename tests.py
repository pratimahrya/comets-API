import pytest
from make_requests import make_request


class TestClass:

    def test_search_asteroids_with_success(self):
        # Arrange:
        api_key = "3H2cWYv2OnvDbzhE33TEQqT7xMsOf77dje6azmLU"
        # Act:
        response = make_request(api_key)
        # Assertion:
        assert response.status_code == 200  # Validation of status code
        data = response.json()
        # Assertion of body response content:
        assert 'element_count' in data
        assert data["element_count"] > 0
