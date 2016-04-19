# 获取股票信息
import json
import urllib.request


class Stock:
    _name = ""
    _code = ""

    def __init__(self, name, code):
        super().__init__()
        self._name = name
        self._code = code

    # 获取股票列表
    @staticmethod
    def get_stock_list():
        _url = "http://ctxalgo.com/api/stocks"
        content = json.loads(urllib.request.urlopen(_url).read().decode("utf-8"))
        stocks = {}
        for item in content:
            stock = Stock(item, content[item])
            stocks[item] = stock
        return stocks


test = Stock("", "")
print(test.get_stock_list())
