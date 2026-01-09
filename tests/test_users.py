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

def test_get_user_invalid_id_format(base_url, http_client):
    """
    숫자가 아닌 user_id 요청 시
    서버가 예외적으로 처리되는지 확인
    """
    response = http_client.get(f"{base_url}/users/abc")
    assert response.status_code in [400, 404]

@pytest.mark.parametrize(
    "payload",
    [
        {"username": "only_name"},
        {"password": "only_pw"},
        {},
    ]
)
def test_create_user_invalid_payload(base_url, http_client, payload):
    """
    필수 필드 누락 시
    회원가입 요청이 정상 처리되지 않는지 검증
    """
    response = http_client.post(
        f"{base_url}/users",
        json=payload
    )

    assert response.status_code in [400, 500]

def test_users_response_schema(base_url, http_client):
    """
    /users 응답이 리스트 형태이며
    각 요소가 동일한 구조를 가지는지 검증
    """
    response = http_client.get(f"{base_url}/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)

    for user in users:
        assert "id" in user
        assert "username" in user
