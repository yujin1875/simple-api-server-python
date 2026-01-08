import pytest

# ----------------------------
# Users API 테스트
# ----------------------------

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),     # 존재하는 유저
        (9999, 404),  # 없는 유저
    ]
)
def test_get_user_by_id(base_url, http_client, user_id, expected_status):
    """유저 단건 조회 API 테스트"""
    response = http_client.get(f"{base_url}/users/{user_id}")

    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert "id" in data
        assert "username" in data
        assert data["id"] == user_id
    else:
        data = response.json()
        assert data["message"] == "유저 없음"
        
def test_create_user(base_url, http_client):
    """회원 생성 API 테스트"""
    payload = {
        "username": "pytest_user",
        "password": "test1234"
    }

    response = http_client.post(
        f"{base_url}/users",
        json=payload
    )

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "회원가입 완료"