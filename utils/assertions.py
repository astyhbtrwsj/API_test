#封装断言

#把响应体解析成json格式（字典）的函数
def get_response_body(response):
    return response.json()

#断言成功响应的函数（正向用例）
def assert_success_response(response, expected_message=None):
    body = get_response_body(response)
    assert response.status_code == 200,"HTTP状态码不为200"
    assert body["状态码"] == 200,"业务状态码不为200"
    if expected_message is not None:
        assert body["消息"] == expected_message
    assert "数据" in body,"响应缺少数据字段"
    return body["数据"]

#断言失败响应的函数（反向用例）
def assert_error_response(response, expected_status_code, expected_message):
    body = get_response_body(response)
    assert response.status_code == expected_status_code
    assert body["状态码"] == expected_status_code
    assert body["消息"] == expected_message
    return body