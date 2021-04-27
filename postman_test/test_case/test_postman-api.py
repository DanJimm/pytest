# -*- coding: utf-8 -*-

import requests
import pytest
import sys
sys.path.append("..")
from test_config import env_info as ei
from test_data import api_case_data as acd

'''
测试postman的pai
test_config中是测试环境信息，url等
test_data中是测试数据
'''

@pytest.mark.parametrize('keyword',acd.api_before.test_case
)
def test_get_befor(keyword):
    date1, date2 = keyword[0], keyword[1]
    params = {
        'timestamp':date1,
        'target':date2
    }
    r = requests.get(url=ei.test_before.api_url, params=params)
    try:
        result = r.json()['before']
    except:
        # print('there is no response!')
        assert r.status_code == 400
    else:
        assert r.status_code == 200
        assert result == keyword[2]



