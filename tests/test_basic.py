def test_hello_api(base_url, http_client):
    """서버 기본 응답 확인 (/hello)"""
    response = http_client.get(f"{base_url}/hello")

    assert response.status_code == 200
    assert response.text == "Hello World"


def test_api_data(base_url, http_client):
    """단순 문자열 응답 API 확인 (/api/data)"""
    response = http_client.get(f"{base_url}/api/data")

    assert response.status_code == 200
    assert response.text == "data~"


def test_ping_api(base_url, http_client):
    """DB 연결 여부 확인용 헬스체크 API (/ping)"""
    response = http_client.get(f"{base_url}/ping")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data[0]["result"] == 1

def test_ping_multiple_requests(base_url, http_client):
    """
    동일 API를 여러 번 호출했을 때
    매번 정상 응답을 반환하는지 확인
    """
    for _ in range(3):
        response = http_client.get(f"{base_url}/ping")
        assert response.status_code == 200

