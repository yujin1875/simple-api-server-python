import pytest
import requests

# ----------------------------
# 공통 테스트 설정 (fixtures)
# ----------------------------

@pytest.fixture(scope="session")
def base_url():
    """
    테스트 대상 서버의 기본 URL
    session scope로 설정해 테스트 전체에서 재사용
    """
    return "http://localhost:4444"


@pytest.fixture(scope="session")
def http_client():
    """
    requests.Session 사용
    - TCP 재사용
    """
    with requests.Session() as session:
        yield session
