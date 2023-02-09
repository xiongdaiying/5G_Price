import pandas as pd
from pywebio.pin import *

# 价格计算

# 人联卡相关信息
def Cal_RenLian(RenLian):
    #[ '数量', '单位', '税率', '产品标准资费', '折扣率', '折后资费',
                  # '折后月资费小计', '折后年资费合计', '一次性服务费/调试费', '一次性成本合计', '报价合计']
    # （名称 类型 备注） 一般是选择 （税率 单位） 为固定值 其余为输入
    # 数量
    num1 = ''
    # 产品标准资费
    charge1 = ''
    # 折扣率
    discount1 = ''
    # 折后资费
    discountFee1 = ''
    # 折后月资费小计
    discountMonthFee1 = ''
    # 折后年资费合计
    discountYearFee1 = ''
    # 一次性服务费/调试费
    oneTimeFee1 = ''
    # 一次性服务费合计
    oneTimeFeeSum1 = ''
    # 报价合计
    sum1 = ''
    # 人联卡的产品标准资费
    if (pin.select1 != None):
        charge1 = "%d" % int(RenLian[RenLian['月流量/通话'] == pin.select1].loc[:, '月资费'].values[0])
    if (pin.Discount1 != None):
        # 人联卡的折后资费
        discount1 = pin.Discount1
        discountFee1 = "%d" % (int(charge1) * int(pin.Discount1) * 0.01)
        # 人联卡的折后月资费小计
        if (pin.Num1 != None):
            num1 = pin.Num1
            discountMonthFee1 = "%d" % (int(charge1) * int(pin.Discount1) * 0.01 * int(pin.Num1))
            # 人联卡的折后年资费合计
            discountYearFee1 = "%d" % (int(discountMonthFee1) * 12)
    if (pin.Num1 != None and pin.Fee1 != None and pin.Discount1 != None):
        # 人联卡的一次性成本合计
        oneTimeFee1 = pin.Fee1
        oneTimeFeeSum1 = "%d" % (int(pin.Num1) * int(pin.Fee1)* int(pin.Discount1)* 0.01)
    if(discountYearFee1!= '' and oneTimeFeeSum1 != ''):
        sum1 = "%d" % (int(discountYearFee1) + int(oneTimeFeeSum1))
    a1 = [num1,charge1,discount1,discountFee1,discountMonthFee1,discountYearFee1,oneTimeFee1,oneTimeFeeSum1,sum1]
    return a1

# 物联卡相关信息
def Cal_WuLian(WuLian_Month,WuLian_Year):
    # 数量
    num2 = ''
    # 产品标准资费
    charge2 = ''
    # 折扣率
    discount2 = ''
    # 折后资费
    discountFee2 = ''
    # 折后月资费小计
    discountMonthFee2 = ''
    # 折后年资费合计
    discountYearFee2 = ''
    # 一次性服务费/调试费
    oneTimeFee2 = ''
    # 一次性服务费合计
    oneTimeFeeSum2 = ''
    # 报价合计
    sum2 = ''
    # 物联卡的产品标准资费
    if(pin.select2 == '月包(通用)'):
        charge2 = WuLian_Month[WuLian_Month['国内流量'] == pin.select3].loc[:, '通用流量'].values[0]
    elif(pin.select2 == '月包(定向)'):
        charge2 = WuLian_Month[WuLian_Month['国内流量'] == pin.select3].loc[:, '定向流量'].values[0]
    elif (pin.select2 == '年包(通用)'):
        charge2 = WuLian_Year[WuLian_Year['国内流量'] == pin.select3].loc[:, '通用流量'].values[0]
    elif (pin.select2 == '年包(定向)'):
        charge2 = WuLian_Year[WuLian_Year['国内流量'] == pin.select3].loc[:, '定向流量'].values[0]
    # 判断charge2是否为空
    if (pd.isna(charge2) != True):
        charge2 = "%d" % int(charge2)
    else:
        charge2 = ' '

    if (pin.Discount2 != None and charge2 != ' '):
        # 物联卡的折后资费
        discount2 = pin.Discount2
        discountFee2 = "%d" % (int(charge2) * int(pin.Discount2) * 0.01)
        # 物联卡的折后月资费小计
        if (pin.Num2 != None):
            num2 = pin.Num2
            discountMonthFee2 = "%d" % (int(charge2) * int(pin.Discount2) * 0.01 * int(pin.Num2))
            # 人联卡的折后年资费合计
            discountYearFee2 = "%d" % (int(discountMonthFee2) * 12)
    if (pin.Num2 != None and pin.Fee2 != None and pin.Discount2 != None):
        # 物联卡的一次性成本合计
        oneTimeFee2 = pin.Fee2
        oneTimeFeeSum2 = "%d" % (int(pin.Num2) * int(pin.Fee2) * int(pin.Discount2)* 0.01)
    if (discountYearFee2 != '' and oneTimeFeeSum2 != ''):
        sum2 = "%d" % (int(discountYearFee2) + int(oneTimeFeeSum2))
    a2 = [num2,charge2,discount2,discountFee2,discountMonthFee2,discountYearFee2,oneTimeFee2,oneTimeFeeSum2,sum2]
    return a2

# 流量池相关计算
def Cal_LiuLiangChi(LiuLiangChi):
    # 数量
    num3 = ''
    # 产品标准资费
    charge3 = ''
    # 折扣率
    discount3 = ''
    # 折后资费
    discountFee3 = ''
    # 折后月资费小计
    discountMonthFee3 = ''
    # 折后年资费合计
    discountYearFee3 = ''
    # 一次性服务费/调试费
    oneTimeFee3 = ''
    # 一次性服务费合计
    oneTimeFeeSum3 = ''
    # 报价合计
    sum3 = ''
    # 流量池的产品标准资费
    if (pin.select4 != None):
        charge3 = LiuLiangChi[LiuLiangChi['流量类型'] == pin.select4].loc[:, '月资费'].values[0]
    if (pin.Discount3 != None):
        # 流量池的折后资费
        discount3 = pin.Discount3
        discountFee3 = "%d" % (int(charge3) * int(pin.Discount3) * 0.01)
        # 流量池的折后月资费小计
        if (pin.Num3 != None):
            num3 = pin.Num3
            discountMonthFee3 = "%d" % (int(charge3) * int(pin.Discount3) * 0.01 * int(pin.Num3))
            # 流量池的折后年资费合计
            discountYearFee3 = "%d" % (int(discountMonthFee3) * 12)
    if (pin.Num3 != None and pin.Fee3 != None and pin.Discount3 != None):
        # 流量池的一次性成本合计
        oneTimeFee3 = pin.Fee3
        oneTimeFeeSum3 = "%d" % (int(pin.Num3) * int(pin.Fee3) * int(pin.Discount3)* 0.01)
    if (discountYearFee3 != '' and oneTimeFeeSum3 != ''):
        sum3 = "%d" % (int(discountYearFee3) + int(oneTimeFeeSum3))
    a3 = [num3, charge3, discount3, discountFee3, discountMonthFee3, discountYearFee3, oneTimeFee3, oneTimeFeeSum3,sum3]
    return a3

# 流量包相关计算
def Cal_LiuLiangBao(LiuLiangChi):
    # 数量
    num4 = ''
    # 产品标准资费
    charge4 = ''
    # 折扣率
    discount4 = ''
    # 折后资费
    discountFee4 = ''
    # 折后月资费小计
    discountMonthFee4 = ''
    # 折后年资费合计
    discountYearFee4 = ''
    # 一次性服务费/调试费
    oneTimeFee4 = ''
    # 一次性服务费合计
    oneTimeFeeSum4 = ''
    # 报价合计
    sum4 = ''
    # 流量包的产品标准资费
    charge4 = LiuLiangChi.iloc[2,1]
    if (pin.Discount4 != None):
        # 流量包的折后资费
        discount4 = pin.Discount4
        discountFee4 = "%d" % (int(charge4) * int(pin.Discount4) * 0.01)
        # 流量包的折后月资费小计
        if (pin.Num4 != None):
            num4 = pin.Num4
            discountMonthFee4 = "%d" % (int(charge4) * int(pin.Discount4) * 0.01 * int(pin.Num4))
            # 流量包的折后年资费合计
            discountYearFee4 = "%d" % (int(discountMonthFee4) * 12)
    if (pin.Num4 != None and pin.Fee4 != None and pin.Discount4 != None):
        # 流量包的一次性成本合计
        oneTimeFee4 = pin.Fee4
        oneTimeFeeSum4 = "%d" % (int(pin.Num4) * int(pin.Fee4) * int(pin.Discount4)* 0.01)
    if (discountYearFee4 != '' and oneTimeFeeSum4 != ''):
        sum4 = "%d" % (int(discountYearFee4) + int(oneTimeFeeSum4))
    a4 = [num4, charge4, discount4, discountFee4, discountMonthFee4, discountYearFee4, oneTimeFee4, oneTimeFeeSum4,sum4]
    return a4


# 定制号卡相关计算
def Cal_HaoKa(HaoKa):
    # 数量
    num5 = ''
    # 折扣率
    discount5 = ''
    # 一次性服务费/调试费
    oneTimeFee5 = ''
    # 一次性服务费合计
    oneTimeFeeSum5 = ''
    # 报价合计
    sum5 = ''
    # 流量包的一次性成本合计
    if (pin.select5 != None):
        oneTimeFee5 = HaoKa[HaoKa['卡品'] == pin.select5].loc[:, '价格'].values[0]
    if (pin.Discount5 != None):
        discount5 = pin.Discount5
    if (pin.Num5 != None):
        num5 = pin.Num5
    if (pin.Num5 != None and  pin.Discount5 != None and pin.select5 != None):
        oneTimeFeeSum5 = "%d" % (int(pin.Num5) * int(oneTimeFee5) * int(pin.Discount5)* 0.01)
    if (oneTimeFeeSum5 != ''):
        sum5 = "%d" % (int(oneTimeFeeSum5))
    a5 = [num5, discount5,oneTimeFee5, oneTimeFeeSum5,sum5]
    return a5

# 定制DNN相关计算
def Cal_DNN(YeWuGeLi):
    # 数量
    num6 = ''
    # 产品标准资费
    charge6 = ''
    # 折扣率
    discount6 = ''
    # 折后资费
    discountFee6 = ''
    # 折后月资费小计
    discountMonthFee6 = ''
    # 折后年资费合计
    discountYearFee6 = ''
    # 一次性服务费/调试费
    oneTimeFee6 = ''
    # 一次性服务费合计
    oneTimeFeeSum6 = ''
    # 报价合计
    sum6 = ''
    # 定制DNN的产品标准资费
    charge6 = YeWuGeLi.iloc[0, 1]
    if (pin.Discount6 != None):
        # 定制DNN的折后资费
        discount6 = pin.Discount6
        discountFee6 = "%d" % (int(charge6) * int(pin.Discount6) * 0.01)
        # 定制DNN的折后月资费小计
        if (pin.Num6 != None):
            num6 = pin.Num6
            discountMonthFee6 = "%d" % (int(charge6) * int(pin.Discount6) * 0.01 * int(pin.Num6))
            # 定制DNN的折后年资费合计
            discountYearFee6 = "%d" % (int(discountMonthFee6) * 12)
    if (pin.Num6 != None and pin.Fee6 != None and pin.Discount6 != None):
        # 定制DNN的一次性成本合计
        oneTimeFee6 = pin.Fee6
        oneTimeFeeSum6 = "%d" % (int(pin.Num6) * int(pin.Fee6)* int(pin.Discount6)* 0.01)
    if (discountYearFee6 != '' and oneTimeFeeSum6 != ''):
        sum6 = "%d" % (int(discountYearFee6) + int(oneTimeFeeSum6))
    a6 = [num6, charge6, discount6, discountFee6, discountMonthFee6, discountYearFee6, oneTimeFee6, oneTimeFeeSum6,sum6]
    return a6


# 无线 VPDN 群相关计算
def Cal_VPDN(YeWuGeLi):
    # 数量
    num7 = ''
    # 产品标准资费
    charge7 = ''
    # 折扣率
    discount7 = ''
    # 折后资费
    discountFee7 = ''
    # 折后月资费小计
    discountMonthFee7 = ''
    # 折后年资费合计
    discountYearFee7 = ''
    # 一次性服务费/调试费
    oneTimeFee7 = ''
    # 一次性服务费合计
    oneTimeFeeSum7 = ''
    # 报价合计
    sum7 = ''
    # 无线 VPDN 群的产品标准资费
    charge7 = YeWuGeLi.iloc[1,1]
    if (pin.Discount7 != None):
        # 无线 VPDN 群的折后资费
        discount7 = pin.Discount7
        discountFee7 = "%d" % (int(charge7) * int(pin.Discount7) * 0.01)
        # 无线 VPDN 的折后月资费小计
        if (pin.Num7 != None):
            num7 = pin.Num7
            discountMonthFee7 = "%d" % (int(charge7) * int(pin.Discount7) * 0.01 * int(pin.Num7))
            # 定制DNN的折后年资费合计
            discountYearFee7 = "%d" % (int(discountMonthFee7) * 12)
    if (pin.Num7 != None and pin.Fee7 != None and pin.Discount7 != None):
        # 无线 VPDN 的一次性成本合计
        oneTimeFee7 = pin.Fee7
        oneTimeFeeSum7 = "%d" % (int(pin.Num7) * int(pin.Fee7) * int(pin.Discount7)* 0.01)
    if (discountYearFee7 != '' and oneTimeFeeSum7 != ''):
        sum7 = "%d" % (int(discountYearFee7) + int(oneTimeFeeSum7))
    a7 = [num7, charge7, discount7, discountFee7, discountMonthFee7, discountYearFee7, oneTimeFee7, oneTimeFeeSum7,sum7]
    return a7

# 网元定制(UPF)相关计算
def Cal_WangYuan1(WangYuan):
    # 数量
    num81 = ''
    # 产品标准资费
    charge81 = ''
    # 折扣率
    discount81 = ''
    # 折后资费
    discountFee81 = ''
    # 折后月资费小计
    discountMonthFee81 = ''
    # 折后年资费合计
    discountYearFee81 = ''
    # 一次性服务费/调试费
    oneTimeFee81 = ''
    # 一次性服务费合计
    oneTimeFeeSum81 = ''
    # 报价合计
    sum81 = ''
    # 网元定制的产品标准资费
    if (pin.select6 != None):
        # 方案几
        schemeNum = WangYuan[WangYuan['方案说明'] == pin.select6].index
        if(pin.select7 != None):
            if(pin.select7 == '一年一付'):
                col = schemeNum * 2 + 1
            elif(pin.select7 == '一次性付清'):
                col = schemeNum * 2 + 2
    if(pin.select8 != None):
        line = WangYuan[WangYuan['协议期'] == pin.select8].index
        charge81 = WangYuan.iloc[line,col].values[0][0]
        if(pd.isna(charge81) != True):
            charge81 = "%d" % int(charge81)
        else:
            charge81 = ''
    if (pin.Discount8 != None and charge81 != ''):
        # 网元定制的折后资费
        discount81 = pin.Discount8
        discountFee81 = "%d" % (int(charge81) * int(pin.Discount8) * 0.01)
        # 网元定制的折后月资费小计
        if (pin.Num8 != None):
            num81 = pin.Num8
            discountMonthFee81 = "%d" % (int(charge81) * int(pin.Discount8) * 0.01 * int(pin.Num8))
            # 定制DNN的折后年资费合计
            discountYearFee81 = "%d" % (int(discountMonthFee81) * 12)
    if (pin.Num8 != None and pin.Fee8 != None and pin.Discount8 != None):
        # 网元定制的一次性成本合计
        oneTimeFee81 = pin.Fee8
        oneTimeFeeSum81 = "%d" % (int(pin.Num8) * int(pin.Fee8) * int(pin.Discount8)* 0.01)
    if (discountYearFee81 != '' and oneTimeFeeSum81 != ''):
        sum81 = "%d" % (int(discountYearFee81) + int(oneTimeFeeSum81))
    a81 = [num81, charge81, discount81, discountFee81, discountMonthFee81, discountYearFee81, oneTimeFee81, oneTimeFeeSum81,sum81]
    return a81

# 网元定制(专网)
def Cal_WangYuan2(RuWangZhuanXian):
    # 数量
    num82 = ''
    # 产品标准资费
    charge82 = ''
    # 折扣率
    discount82 = ''
    # 折后资费
    discountFee82 = ''
    # 折后月资费小计
    discountMonthFee82 = ''
    # 折后年资费合计
    discountYearFee82 = ''
    # 一次性服务费/调试费
    oneTimeFee82 = ''
    # 一次性服务费合计
    oneTimeFeeSum82 = ''
    # 报价合计
    sum82 = ''
    # 网元定制的产品标准资费
    if (pin.select9 != None):
        charge82 = RuWangZhuanXian[RuWangZhuanXian['5G云网UPF带宽'] == pin.select9].iloc[:,1].values[0]
    if (pin.Discount8 != None):
        # 网元定制的折后资费
        discount82 = pin.Discount8
        discountFee82 = "%d" % (int(charge82) * int(pin.Discount8) * 0.01)
        # 网元定制的折后月资费小计
        if (pin.Num8 != None):
            num82 = pin.Num8
            discountMonthFee82 = "%d" % (int(charge82) * int(pin.Discount8) * 0.01 * int(pin.Num8))
            # 网元定制的折后年资费合计
            discountYearFee82 = "%d" % (int(discountMonthFee82) * 12)
    if (pin.Num8 != None and pin.Fee8 != None and pin.Discount8 != None):
        # 网元定制的一次性成本合计
        oneTimeFee82 = pin.Fee8
        oneTimeFeeSum82 = "%d" % (int(pin.Num8) * int(pin.Fee8) * int(pin.Discount8) * 0.01)
    if (discountYearFee82 != '' and oneTimeFeeSum82 != ''):
        sum82 = "%d" % (int(discountYearFee82) + int(oneTimeFeeSum82))
    a82 = [num82, charge82, discount82, discountFee82, discountMonthFee82, discountYearFee82, oneTimeFee82, oneTimeFeeSum82,
          sum82]
    return a82

# 固定入网专线STN专线
def Cal_STNZhuanXian(RuWangZhuanXian):
    # 数量
    num10 = ''
    # 产品标准资费
    charge10 = ''
    # 折扣率
    discount10 = ''
    # 折后资费
    discountFee10 = ''
    # 折后月资费小计
    discountMonthFee10 = ''
    # 折后年资费合计
    discountYearFee10 = ''
    # 一次性服务费/调试费
    oneTimeFee10 = ''
    # 一次性服务费合计
    oneTimeFeeSum10 = ''
    # 报价合计
    sum10 = ''
    # 网元定制的产品标准资费
    if (pin.select10 != None):
        charge10 = RuWangZhuanXian[RuWangZhuanXian['5G定制网STN带宽'] == pin.select10].iloc[:, 3].values[0]
    if (pin.Discount10 != None):
        # 网元定制的折后资费
        discount10 = pin.Discount10
        discountFee10 = "%d" % (int(charge10) * int(pin.Discount10) * 0.01)
        # 网元定制的折后月资费小计
        if (pin.Num10 != None):
            num10 = pin.Num10
            discountMonthFee10 = "%d" % (int(charge10) * int(pin.Discount10) * 0.01 * int(pin.Num10))
            # 网元定制的折后年资费合计
            discountYearFee10 = "%d" % (int(discountMonthFee10) * 12)
    if (pin.Num10 != None and pin.Fee10 != None and pin.Discount10 != None):
        # 网元定制的一次性成本合计
        oneTimeFee10 = pin.Fee10
        oneTimeFeeSum10 = "%d" % (int(pin.Num10) * int(pin.Fee10) * int(pin.Discount10) * 0.01)
    if (discountYearFee10 != '' and oneTimeFeeSum10 != ''):
        sum10 = "%d" % (int(discountYearFee10) + int(oneTimeFeeSum10))
    a10 = [num10, charge10, discount10, discountFee10, discountMonthFee10, discountYearFee10, oneTimeFee10,
           oneTimeFeeSum10,sum10]
    return a10

# IPRAN相关信息
def cal_IPRAN(IPRAN):
    # 数量
    num11 = ''
    # 产品标准资费
    charge11 = ''
    # 折扣率
    discount11 = ''
    # 折后资费
    discountFee11 = ''
    # 折后月资费小计
    discountMonthFee11 = ''
    # 折后年资费合计
    discountYearFee11 = ''
    # 一次性服务费/调试费
    oneTimeFee11 = ''
    # 一次性服务费合计
    oneTimeFeeSum11 = ''
    # 报价合计
    sum11 = ''
    # 网元定制的产品标准资费
    if (pin.select11 != None):
        charge11 = IPRAN[IPRAN['网络参考费'] == pin.select11].iloc[:, 1].values[0]
    if (pin.Discount11 != None):
        # 网元定制的折后资费
        discount11 = pin.Discount11
        discountFee11 = "%d" % (int(charge11) * int(pin.Discount11) * 0.01)
        # 网元定制的折后月资费小计
        if (pin.Num11 != None):
            num11 = pin.Num11
            discountMonthFee11 = "%d" % (int(charge11) * int(pin.Discount11) * 0.01 * int(pin.Num11))
            # 网元定制的折后年资费合计
            discountYearFee11 = "%d" % (int(discountMonthFee11) * 12)
    if (pin.Num11 != None and pin.Fee11 != None and pin.Discount11 != None):
        # 网元定制的一次性成本合计
        oneTimeFee11 = pin.Fee11
        oneTimeFeeSum11 = "%d" % (int(pin.Num11) * int(pin.Fee11) * int(pin.Discount11) * 0.01)
    if (discountYearFee11 != '' and oneTimeFeeSum11 != ''):
        sum11 = "%d" % (int(discountYearFee11) + int(oneTimeFeeSum11))
    a11 = [num11, charge11, discount11, discountFee11, discountMonthFee11, discountYearFee11, oneTimeFee11,
           oneTimeFeeSum11,
           sum11]
    return a11

# 功能费相关信息
def cal_GonNeng(IPRAN):
    # 数量
    num12 = ''
    # 产品标准资费
    charge12 = ''
    # 折扣率
    discount12 = ''
    # 折后资费
    discountFee12 = ''
    # 折后月资费小计
    discountMonthFee12 = ''
    # 折后年资费合计
    discountYearFee12 = ''
    # 一次性服务费/调试费
    oneTimeFee12 = ''
    # 一次性服务费合计
    oneTimeFeeSum12 = ''
    # 报价合计
    sum12 = ''
    # 功能费的产品标准资费
    charge12 = IPRAN.iloc[:, 5].values[1]
    if (pin.Discount12 != None):
        # 功能费的折后资费
        discount12 = pin.Discount12
        discountFee12 = "%d" % (int(charge12) * int(pin.Discount12) * 0.01)
        # 功能费的折后月资费小计
        if (pin.Num12 != None):
            num12 = pin.Num12
            discountMonthFee12 = "%d" % (int(charge12) * int(pin.Discount12) * 0.01 * int(pin.Num12))
            # 功能费的折后年资费合计
            discountYearFee12 = "%d" % (int(discountMonthFee12) * 12)
    if (pin.Num12 != None and pin.Fee12 != None and pin.Discount12 != None):
        # 功能费的一次性成本合计
        oneTimeFee12 = pin.Fee12
        oneTimeFeeSum12 = "%d" % (int(pin.Num12) * int(pin.Fee12) * int(pin.Discount12) * 0.01)
    if (discountYearFee12 != '' and oneTimeFeeSum12 != ''):
        sum12 = "%d" % (int(discountYearFee12) + int(oneTimeFeeSum12))
    a12 = [num12, charge12, discount12, discountFee12, discountMonthFee12, discountYearFee12, oneTimeFee12,
           oneTimeFeeSum12,sum12]
    return a12


# 计算总价
def totalSum(list):
    sum1 = 0
    for x in list:
        if (x != ''):
            sum1 += int(x)
    return sum1