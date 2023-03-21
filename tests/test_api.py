from requests import Session


def test_get_category_list():
    with Session() as session:
        response = session.get('http://localhost:8000/api/v1/category')
        assert response.status_code == 200
