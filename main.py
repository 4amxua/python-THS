"""
关注公众号:投图匠
"""
import time
from API import *	
DCcookie1 = "东方财富cookie"
DCcookie2 = "东方财富cookie"


# THScookie1 = "同花顺cookie"
THScookie2 = "同花顺cookie"
THScookie3 = "同花顺cookie"

列表 = []
# 列表.append(THScookie1)
列表.append(THScookie2)
列表.append(THScookie3)
列表.append(DCcookie1)
列表.append(DCcookie2)

# t = 多账号登陆(列表)


class Strategy(Wencai):
    def __init__(self):
        super().__init__()
        self.api = 多账号登陆(列表)  #登陆多个交易账号
    def 止盈止损(self,stop_loss=-500,stop_profit=1500):
        while True:
            time.sleep(5) # 定时执行一次
            #self.选股()  #执行选股
            for i in self.api:
                print("="*43,"账号分割线")
                #print(i.qryChedan())  # 先全部撤单
                for pos in i.qryChicang(): # 循环执行多个合约
                    print("名称:  "+pos["证券名称"]+"   代码:  "+pos["证券代码"]+"  盈亏  :"+pos["浮动盈亏"])
                    if float(pos["浮动盈亏"]) <= float(stop_loss) or float(pos["浮动盈亏"]) > float(stop_profit):
                        #stock = i.sell(stock_no=pos["证券代码"], price=pos["市价"], amount=pos["可用余额"])
                        print("平仓")
    # def 止盈止损(self,stop_loss=-500,stop_profit=1500):
        # for i in self.api:
            # print("="*43,"账号分割线")
            # #print(i.qryChedan())  # 先全部撤单
            # for pos in i.qryChicang(): # 循环执行多个合约
                # print("名称:  "+pos["证券名称"]+"   代码:  "+pos["证券代码"]+"  盈亏  :"+pos["浮动盈亏"])
                # if float(pos["浮动盈亏"]) <= float(stop_loss) or float(pos["浮动盈亏"]) > float(stop_profit):
                    # #stock = i.sell(stock_no=pos["证券代码"], price=pos["市价"], amount=pos["可用余额"])
                    # print("平仓")
    def 下单(self,code):
        #i=0
        for i in self.api:
            #print(i.qryzijin()) # 查资金
            #print(i.qryChicang()) # 查持仓
            #print(i.qryChedan())  # 全部撤单
            #下单手数 = round(i.qryzijin()["可用资金"]/i.qrystock(code)["mrjw1"]/100)
            #print(i.buy(stock_no=code, price=0, amount=下单手数))
            print(i.buy(stock_no=code, price=0, amount=100))  
    def 选股(self):
        #条件 = '周rsi24上穿30，量比>1.5，涨幅<3%'
        #条件 = '资金流入大于1亿，dea>0，量比>1，涨幅<3%'
        #条件 = '连续三年净利润同比增长率大于50%,macd金叉，dea>0，量比>1，涨幅<3%'
        #条件 = '连续三年净利润同比增长率大于10%，连续三年毛利率同比增长率大于10%,连续三年净资产同比增长率大于10%,连续三年营业收入同比增长率大于10%'
        #条件 = '连续三年净资产同比增长率大于10%,连续三年营业收入同比增长率大于30%，上市天数>300天'
        条件 = "30日跌幅前十"
        for i in self.Xuangu(条件):
            code = i["代码"][:-3]
            print(code)
            #self.下单(code)
t=Strategy()
# t.选股()
t.止盈止损()  
