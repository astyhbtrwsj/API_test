import pytest
from utils.request_handler import send_request
from utils.assertions import assert_success_response,assert_error_response



def test_health_API():
    res = send_request("get","/health")
    data = assert_success_response(res)
    assert res.status_code == 200
    assert data["服务状态"] == "正常"
    assert res.elapsed.total_seconds() < 1  #接口响应时间小于1秒(.elapsed.total_seconds() 固定格式，获取响应时间的秒数)

#05.08.01:57写
def test_v1_home_API():
    res = send_request("get","/v1/home")
    data = assert_success_response(res)
    assert res.status_code == 200
    assert res.elapsed.total_seconds() < 1  #接口响应时间小于1秒(.elapsed.total_seconds() 固定格式，获取响应时间的秒数)
    assert len(data["轮播图列表"]) == 4      #断言轮播图列表等于4个
    assert len(data["推荐商品列表"]) == 3    #断言推荐商品列表等于3个
    assert data["用户信息"]["用户编号"] == "u_001"  #断言用户编号等于u_001

#05.08.11:03写
def test_v1_products_API():
    res = send_request("get","/v1/products")
    data = assert_success_response(res)
    assert res.status_code == 200
    assert res.elapsed.total_seconds() < 1  #接口响应时间小于1秒
    assert len(data["商品列表"]) == 10     #断言商品列表等于10个
    assert data["商品数量"] == 10     #断言商品数量等于10个
    assert len(data["商品列表"]) == data["商品数量"]    #断言商品列表的长度等于商品数量
    assert len(data["分类列表"]) == 5      #断言分类列表等于5个

#05.08.12:20写
def test_v1_product_product_id_API():
    res = send_request("get","/v1/products/p_001")
    data = assert_success_response(res)
    assert res.status_code == 200
    assert res.elapsed.total_seconds() < 1  #接口响应时间小于1秒
    assert data["商品编号"] == "p_001"  #断言商品编号等于p_001
    assert len(data) == 13     #断言返回的商品详情字段数量等于13个
    assert data["规格选项"]["温度"] == ["热", "少冰", "冰"]

#测试/v1/coupons（优惠券列表）
#断言返回的优惠券数量等于4
#断言返回的优惠券列表长度等于4
#断言接口响应时间小于1秒

#测试/v1/user/profile（用户信息）
#断言返回的用户编号等于u_001
#断言返回的呢称等于"测试用户"
#断言接口响应时间小于1秒
#断言返回的数据字段长度等于8

#测试/v1/addresses（地址列表）
#断言返回的地址列表长度等于4
#断言返回数据的地址数量等于4
#断言返回的地址列表长度 == 返回数据的地址数量
#断言返回的地址列表中第一个地址的长度等于7
#断言接口响应时间小于1秒
# assert any(item["是否默认地址"] for item in data["地址列表"]) #断言地址列表中至少有一个默认地址，for item in data遍历列表，any（）函数判断是否至少有一个满足条件的元素，item["是否默认地址"]为True表示该地址是默认地址

#测试/v1/cart（购物车列表）
#断言返回的购物车商品列表长度等于3
#断言返回的商品总数量大于等于3

#测试/v1/orders（订单列表）
#断言返回的订单列表长度等于4
#断言返回数据的订单数量等于4
#断言返回的订单列表长度 == 返回数据的订单数量

#测试/v1/orders/<order_id>`（订单详情）
#断言返回的订单编号等于ORD_20260424_1002
#断言返回的订单详情字段数量等于11

#测试/v1/refunds（退款列表）
#断言返回的退款列表长度等于2
#断言返回数据的退款数量等于2
#断言返回的退款列表长度 == 返回数据的退款数量

#测试/v1/after-sales（售后列表）
#断言返回的售后列表长度等于2
#断言返回数据的售后数量等于2
#断言返回的售后列表长度 == 返回数据的售后数量

#-------------------------------------------------------------

# 上面是正向的用例，还有反向的用例
# 再写自动化脚本时，应该提前把测试用例写完：
#     {
#       覆盖正向和反向的场景，这样在写自动化脚本时就有明确的目标和预期结果，可以更高效地完成测试脚本的编写。
#       同时，提前规划好测试用例也有助于发现潜在的边界情况和异常场景，确保测试的全面性和有效性.
#     }


