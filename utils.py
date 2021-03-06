import datetime
import logging
import time


def formatTime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return "%d:%02d:%02d" % (h, m, s)


def getLogger(_name, _level=logging.DEBUG, _format=None):
    if _format is None:
        _format = '[%(asctime)s] %(name)s: %(levelname)s: %(message)s'

    # logger.debug("debug")
    # logger.info("info")
    # logger.warning("warning")
    # logger.error("error")
    # logger.critical("critical")

    # 使用一個名字為 Crescent 的 logger
    logger = logging.getLogger(_name)

    # 避免重複輸出 log
    if not logger.handlers:
        # 設置 logger 的 level
        logger.setLevel(_level)

        # 創建一個輸出日誌到控制台的 StreamHandler
        hdr = logging.StreamHandler()

        # 設置 logger 的格式
        formatter = logging.Formatter(_format)

        # 將格式添加給 StreamHandler
        hdr.setFormatter(formatter)

        # 將 handler 添加給 logger
        logger.addHandler(hdr)

    return logger


def processTime(func):
    def f(*args):
        # logger = getLogger(func.__name__)
        start = datetime.datetime.now()
#        logger.debug("@{} [{}] start".format(time.strftime("%X", time.localtime()), func.__name__))
        result = func(*args)
#        logger.debug("@{} [{}]  end".format(time.strftime("%X", time.localtime()), func.__name__))
        end = datetime.datetime.now()
        message = "@{} taken for {}".format(str(end - start), func.__name__)
        # logger.debug(message)
        print(message)
        return result
    return f


def voidFuncTime(func):
    """[計算程式運算時間]
    利用裝飾器的形式，計算無回傳值函式的運算時間

    Args:
        func: 被計算運算時間的程式

    Returns:
        沒有回傳值
    """

    def f(*args):
        """[承接 func 參數]
        func 參數可能有0個到N個，用這個來承接參數，再傳給 func

        Args:
            *args: func 所需參數

        Returns:
            沒有回傳值
        """
        start = time.time()
        func(*args)
        print("@{:.10f}s taken for {}".format(time.time() - start, func.__name__))

    return f


if __name__ == "__main__":
    print(formatTime(35400))  # 9:50:00

