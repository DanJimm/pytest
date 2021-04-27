import requests
import pytest

# class Test_Search:

@pytest.mark.parametrize('keyword', [
    'appium',
    'selenium',
    'Docker',
])
def test_search_result(keyword):
    url = 'https://ceshiren.com/search'
    params = {
        'q':keyword,
    }
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.68 Safari/537.36',
        'accept' : 'application/json',
    }

    r = requests.get(
        url = url,
        params = params,
        headers = headers,
    )

    assert r.status_code == 200
    assert keyword.lower() in str(r.json()['posts'][0]['blurb']).lower()
