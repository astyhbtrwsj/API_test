import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler   #导入 RotatingFileHandler(日志文件切割器,当日志文件达到指定大小时自动切割)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    # 防止重复添加handler
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # =========================
        # 日志格式
        # =========================
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | "
            "%(filename)s:%(lineno)d | %(message)s"
        )
        # =========================
        # 控制台输出
        # =========================
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
        # =========================
        # 文件输出
        # =========================
        file_handler = RotatingFileHandler(
            filename=LOG_DIR / "test.log",
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        # 添加handler
        # logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger