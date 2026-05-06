import pytest
from utils.request_handler import send_request
from utils.assertions import assert_success_response,assert_error_response


def test_123():
    res = send_request("get","/health")
    data = assert_success_response(res)
    assert res.status_code == 200
    assert data["服务状态"] == "正常"
    assert res.elapsed.total_seconds() < 1  #接口响应时间小于1秒(.elapsed.total_seconds() 固定格式，获取响应时间的秒数)
