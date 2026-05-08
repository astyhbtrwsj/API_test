# import pytest

# @pytest.fixture(scope="session", autouse=True)
# # @pytest.fixture
# # 表示：这是一个 fixture（测试前后处理函数）
# # 用来做：
# #   初始化环境
# #   准备数据
# #   登录获取token
# #   清理数据

# # scope参数表示为：控制“执行范围 / 生命周期”。可以理解为控制“执行多少次”
# # scope参数的值可以是：function（默认值，表示每个测试函数执行前后都会执行一次）
# #                     class（表示每个测试类执行前后都会执行一次）
# #                     module（表示每个测试文件执行前后都会执行一次）
# #                     session（表示整个测试会话执行前后都会执行一次，整个pytest运行期间，只执行一次）
# # autouse参数表示为：控制“是否自动执行”。可以理解为控制“要不要你手动调用”
# # autouse参数的值可以是：True（自动执行，不需要在测试函数里写参数引用，自动执行）
# #                       False（手动调用，需要手动在测试函数中使用）

# def setup_env():
# # 定义一个fixture函数
# # 名字叫 setup_env
# # 名字可以随便取（但要有语义）

#     print("测试环境初始化...")
# # 这里是：
# # 测试开始前执行的代码
# # 常见用途：
# # 初始化数据库
# # 创建测试数据
# # 登录系统
# # 获取token
# # 启动服务

#     yield
# # yield 之前的代码是：测试开始前执行的代码
# # yield 之后的代码是：测试结束后执行的代码

#     print("测试环境清理完成")
# # 这里是：
# # 测试结束后执行的代码
# # 常见用途：
# # 删除测试数据
# # 关闭数据库连接
# # 清理缓存
# # 退出登录

# # @pytest.fixture(scope="session",autouse=True)
# # def setup_test():
# #     print("测试前准备")
# #     yield
# #     print("测试后清理")


import pytest
import logging
from utils.request_handler import load_yaml, send_request
from pathlib import Path
from utils.logger import get_logger
from utils.assertions import assert_success_response, assert_error_response

logger = get_logger(__name__)

#登录token的fixture（多角色账号）
#对应需要登录的用例

#连接数据库的fixture

#创建订单的fixture
#对应必须要有订单的用例

#支付订单的fixture
#对应完成支付后操作的用例

#获取Redis数据的fixture
#对应需要验证Redis数据的用例（验证码登录、token校验、秒杀库存、登录状态）

#随机用户数据的fixture
#对应需要随机用户数据的用例（注册、登录、修改资料等）

#购物车数据的fixture
#对应需要购物车数据的用例（添加购物车、修改购物车、删除购物车等）

#上传文件的fixture
#对应需要上传文件的用例（头像上传、订单上传、上传咖啡商品图等）

#driver的fixture
#对应需要UI自动化的用例（登录（ui点击）、注册（UI输入）、修改资料（UI输入）、App自动化（点击控件）等）

#session的fixture
#对应长连接场景的用例（登录状态保持、WebSocket连接等）

#模拟接口的fixture
#对应需要模拟接口的用例（第三方支付、短信验证码等）

#业务流程的fixture
#对应需要完整业务流程的用例（注册-登录-下单-支付-查询订单等、查看退款状态、退款通知）

# 全局初始化fixture
#对应整个测试会话需要执行的初始化操作（如读取配置文件、设置环境变量等）

@pytest.fixture(scope="session", autouse=True)
def setup_env():
    logger.info("测试环境初始化...")
    yield
    logger.info("测试环境清理完成")

#5.8
#conftest.py文件读取yaml配置，是因为yaml配置有很多环境（不止一个基本url），
# 其他用例可能会用到其他的环境（比如：测试环境地址、预发布环境地址、服务器地址、重置数据地址）
@pytest.fixture(scope="session", autouse=True)
def api_config():
    """读取接口自动化配置。"""
    return load_yaml()

@pytest.fixture(scope="function", autouse=True)
def reset_mock_data():
    """每条用例执行前，通过 HTTP 接口重置测试数据。"""
    reset_response = send_request("post","/test/reset")
    assert_success_response(reset_response, "测试数据已重置")
    yield