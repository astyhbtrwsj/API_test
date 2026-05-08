# import requests
# import yaml
# # yaml：用来读取配置文件（.yaml）

# def load_yaml():
#     with open('./config/config.yaml', encoding="utf-8") as f:
#         config = yaml.safe_load(f)
#         print(type(config))
# # 它是用来把 YAML 格式的配置文件解析成 Python 的字典或列表结构。
# # safe_load 是安全解析方法，不会执行任意代码，适合在项目中读取配置，比如 base_url、账号信息等
# # safe_load() 做的是：
# # 根据 YAML 的结构 → 自动映射到 Python 最接近的数据结构

#     return config
# #这个函数主要是把yaml文件里的内容读取出来，返回一个字典对象，方便后续使用。


# config = load_yaml()
# BASE_URL = config["base_url"]

# def send_request(method, endpoint, **kwargs):
# # 定义叫发送请求的函数，接收三个参数：
# # method（HTTP方法，如GET、POST等）
# # endpoint（API的具体路径）
# # **kwargs（可选的其他参数，如请求体、查询参数等）。

#     headers = kwargs.pop("headers", {})
# # 为什么用 kwargs + pop？
# # 你可以这样答：
# # kwargs 用来接收不固定参数，使请求函数更加通用。
# # 使用 pop 是为了在提取 headers 的同时从 kwargs 中删除，避免在调用 requests.request 时出现参数重复冲突。

#     # headers["Authorization"] = f"Bearer {TOKEN}"
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.request(method, url, headers=headers, **kwargs)
# #requests.request=requests.get/post/put/delete等方法的通用接口，可以根据 method 参数动态调用对应的 HTTP 方法。

#     return response
# #这个函数的作用是根据传入的 HTTP 方法和 API 路径，构造完整的 URL，并发送 HTTP 请求，最后返回响应对象。




import requests
import yaml
from pathlib import Path
import logging
from utils.logger import get_logger

logger = get_logger(__name__)

config_path = Path(__file__).resolve().parents[1]/"config"/"config.yaml"
#Path(__file__).resolve()获取当前文件的绝对路径
#Path(__file__).resolve().parent获取当前文件的所在目录
#parents[1]获取当前文件的上一个目录

def load_yaml():
    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

config = load_yaml()
BASE_URL = config["base_url"]

def send_request(method, endpoint, **kwargs):
    logger.info(f"请求方法：%s",method)
    logger.info(f"请求路径：%s",endpoint)
    logger.info(f"请求参数：%s",kwargs)
    headers = kwargs.pop("headers", {})
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, headers=headers, **kwargs)
    return response

# response = send_request("get","/health")
# print(response.elapsed.total_seconds())