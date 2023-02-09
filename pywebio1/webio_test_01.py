from pandas import options
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

def main():
    # 数据导入
    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
    # xlsx表格数据导入
    RenLian = pd.read_excel('人联卡.xlsx')
    WuLian_Month = pd.read_excel('物联卡(月包).xlsx')
    WuLian_Year = pd.read_excel('物联卡(年包).xlsx')
    LiuLiangChi = pd.read_excel('流量池.xlsx')
    HaoKa = pd.read_excel('定制号卡.xlsx')
    YeWuGeLi = pd.read_excel('业务隔离.xlsx')
    RuWangZhuanXian = pd.read_excel('固定入网专线.xlsx')
    WangYuan = pd.read_excel('网元定制.xlsx')
    IPRAN = pd.read_excel('IPRAN专线参考资费.xlsx')
    # 数据获取
    # b左侧类型 p右侧具体费用
    b1 = np.array(RenLian['月流量/通话'])
    p1 = np.array(RenLian['月资费'])
    b2 = np.array(WuLian_Month['国内流量'])
    b3 = np.array(WuLian_Year['国内流量'])
    b5 = np.array(HaoKa['卡品'])
    b71 = np.array(RuWangZhuanXian['5G云网UPF带宽'])
    b72 = np.array(RuWangZhuanXian['5G定制网STN带宽'])
    b81 = np.array(WangYuan['方案说明'])
    b82 = np.array(WangYuan['协议期'])


    p21 = np.array(WuLian_Month['通用流量'])
    p22 = np.array(WuLian_Month['定向流量'])
    p31 = np.array(WuLian_Year['通用流量'])
    p32 = np.array(WuLian_Year['定向流量'])
    p41 = np.array(LiuLiangChi['通用流量'])
    p42 = np.array(LiuLiangChi['定向流量'])
    p43 = np.array(LiuLiangChi['园区流量包'])
    p51 = np.array(HaoKa['价格'])
    b1 = list(b1)
    b2 = list(b2)
    b3 = list(b3)
    b5 = list(b5)
    b81 = list(b81)
    b82 = list(b82)

    option_list1 = b1
    option_list2 = b2
    option_list5 = b5
    option_list81 = b81
    option_list82 = b82
    # 如果输入的个数为0，在输出的excel中就不再出现这一条

    # put_table(
    #     [['名称','类型','备注','数量','单位','税率','产品标准资费', '折扣率','折后资费',
    #       '折后月资费小计','折后年资费合计','一次性服务费/调试费','一次性成本合计','报价合计'],
    #     ['人联卡','5G畅享套餐',put_select('select1', options=option_list1),put_input('Num1',type=NUMBER),'张',
    #      put_input('Tax1', type=NUMBER),'',put_input('Discount1', type=NUMBER),'','','',
    #      put_input('Fee1', type=NUMBER),'',''],
    #     ['物联卡',put_select('select2', options=['月包(通用)','月包(定向)','年包(通用)','年包(定向)']),put_select('select3', options=option_list2),put_input('Num2',type=NUMBER),'张',
    #      put_input('Tax2', type=NUMBER),'',put_input('Discount2', type=NUMBER),'','','',
    #      put_input('Fee2', type=NUMBER),'',''],
    #     ['流量池', '', put_select('select4', options=['定向流量', '通用流量']),put_input('Num3', type=NUMBER),'GB',
    #      put_input('Tax3', type=NUMBER), '',put_input('Discount3', type=NUMBER),'','','',
    #      put_input('Fee3', type=NUMBER),'',''],
    #     ['园区流量包', '', '',put_input('Num4', type=NUMBER), '',
    #      put_input('Tax4', type=NUMBER), '',put_input('Discount4', type=NUMBER),'','','',
    #      put_input('Fee4', type=NUMBER),'',''],
    # ])

    # 需要输入信息的表格
    put_table(
        [['', '名称', '类型', '规格', '数量', '税率', '折扣率', '一次性服务费'],
         [span('定制流量', row=6)],
         ['人联卡', '5G畅享套餐', put_select('select1', options=option_list1).style('width:150px'),
          put_input('Num1', type=NUMBER),
          '6%', put_input('Discount1', type=NUMBER),
          put_input('Fee1', type=NUMBER)],
         ['物联卡', put_select('select2', options=['月包(通用)', '月包(定向)', '年包(通用)', '年包(定向)']),
          put_select('select3', options=option_list2), put_input('Num2', type=NUMBER),
          '6%', put_input('Discount2', type=NUMBER),
          put_input('Fee2', type=NUMBER)],
         ['流量池', put_select('select4', options=['定向流量', '通用流量']), '-', put_input('Num3', type=NUMBER),
          '6%', put_input('Discount3', type=NUMBER),
          put_input('Fee3', type=NUMBER)],
         ['园区流量包', '-', '-', put_input('Num4', type=NUMBER),
          '6%', put_input('Discount4', type=NUMBER),
          put_input('Fee4', type=NUMBER)],
         ['定制号卡', put_select('select5', options=option_list5), '-', put_input('Num5', type=NUMBER),
          '一半6%,一半13%', put_input('Discount5', type=NUMBER),
          put_input('Fee5', type=NUMBER)],
         [span('业务隔离', row=3)],
         ['定制DNN', '专网加密隧道服务', '-', put_input('Num6', type=NUMBER),
          '6%', put_input('Discount6', type=NUMBER),
          put_input('Fee6', type=NUMBER)],
         ['无线VPDN群', '-', '-', put_input('Num7', type=NUMBER),
          '6%', put_input('Discount7', type=NUMBER),
          put_input('Fee7', type=NUMBER)],
         [span('网元定制', row=2)],
         [put_select('select6', options=option_list81).style('width:150px'),
          put_select('select7', options=['一年一付', '一次性付清']), put_select('select8', options=option_list82),
          put_input('Num8', type=NUMBER),
          '6%', put_input('Discount8', type=NUMBER),
          put_input('Fee8', type=NUMBER)]
         ]).style('text-align:center;text-align-last:center;table-layout:fixed;word-wrap:break-word')

    # 输出有用信息的表
    with use_scope('scope1'):  # open and enter a new output: 'scope1'
        put_table(
            [['', '名称', '类型', '备注', '数量', '单位', '税率', '产品标准资费', '折扣率', '折后资费',
              '折后月资费小计', '折后年资费合计', '一次性服务费/调试费', '一次性成本合计', '报价合计'],
             [span('定制流量', row=6)],
             ['人联卡', '5G畅享套餐', put_text(" %s " % (pin.select1)), '0', '张',
              '6%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             ['物联卡', put_text(" %s " % (pin.select2)), put_text(" %s " % (pin.select3)), '0', '张',
              '6%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             ['流量池', '-', put_text(" %s " % (pin.select4)), '0', 'GB',
              '6%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             ['园区流量包', '-', '-', '0', '户',
              '6%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             ['定制号卡', put_text(" %s " % (pin.select5)), '0', '张',
              '一半6%,一半13%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             [span('业务隔离', row=3)],
             ['定制DNN', '专网加密隧道服务', '-', '0',
              '6%', '0', '100%', '0', '0', '0', '0', '0', '0'],
             ['无线VPDN群', '-', '-', '0',
              '6%', '6%', '0', '100%', '0', '0', '0', '0', '0', '0']
             ])

    # 更新表格
    while True:
        pin_wait_change('select1','Num1','Discount1','Fee1',
                        'select2','Num2','Discount2','Fee2',
                        'select4','Num3','Discount3','Fee3',
                        'Num4', 'Discount4', 'Fee4',
                        'select5','Num5','Discount5','Fee5',
                        'Num6','Discount6','Fee6',
                        'Num7','Discount7','Fee7')
        # 更新下拉选框
        if (pin.select2 == '月包(通用)' or pin.select2 == '月包(定向)'):
            option_list2 = b2
        else:
            option_list2 = b3
        pin_update('select3', options=option_list2)
        # 查数据表，得到产品标准资费
        # 人联卡的产品标准资费
        with use_scope('scope1', clear=True): # 删除scope1中的所有信息，重新建立表格
            # 人联卡相关信息计算
            a1 = Cal_RenLian(RenLian)
            r1 = a1[0]
            d1 = a1[1]
            dm1 = a1[2]
            dy1 = a1[3]
            fy1 = a1[4]
            sum1 = a1[5]


            # 物联卡相关信息计算
            a2 = Cal_WuLian(WuLian_Month,WuLian_Year)
            r2 = a2[0]
            d2 = a2[1]
            dm2 = a2[2]
            dy2 = a2[3]
            fy2 = a2[4]
            sum2 = a2[5]


            put_table(
                [['','名称', '类型', '备注', '数量', '单位', '税率', '产品标准资费', '折扣率', '折后资费',
                  '折后月资费小计', '折后年资费合计', '一次性服务费/调试费', '一次性成本合计', '报价合计'],
                 [span('定制流量', row=6)],
                 ['人联卡', '5G畅享套餐', put_text(" %s " % (pin.select1)), put_text(" %s " % (pin.Num1)), '张',
                  '6%',put_text(" %s " % (r1)),put_text(" %s " % (pin.Discount1)), put_text(" %s " % (d1)), put_text(" %s " % (dm1)), put_text(" %s " % (dy1)),
                  put_text(" %s " % (pin.Fee1)), put_text(" %s " % (fy1)), sum1],
                 ['物联卡', put_text(" %s " % (pin.select2)), put_text(" %s " % (pin.select3)), put_text(" %s " % (pin.Num2)), '张',
                  '6%', put_text(" %s " % (r2)), put_text(" %s " % (pin.Discount2)), put_text(" %s " % (d2)),
                  put_text(" %s " % (dm2)), put_text(" %s " % (dy2)),
                  put_text(" %s " % (pin.Fee2)), put_text(" %s " % (fy2)), sum2]
                 # ['物联卡', put_select('select2', options=['月包(通用)', '月包(定向)', '年包(通用)', '年包(定向)']),
                 #  put_select('select3', options=option_list2), put_input('Num2', type=NUMBER), '张',
                 #  put_input('Tax2', type=NUMBER), '', put_input('Discount2', type=NUMBER), '', '', '',
                 #  put_input('Fee2', type=NUMBER), '', ''],
                 # ['流量池', '', put_select('select4', options=['定向流量', '通用流量']), put_input('Num3', type=NUMBER),
                 #  'GB',
                 #  put_input('Tax3', type=NUMBER), '', put_input('Discount3', type=NUMBER), '', '', '',
                 #  put_input('Fee3', type=NUMBER), '', ''],
                 # ['园区流量包', '', '', put_input('Num4', type=NUMBER), '',
                 #  put_input('Tax4', type=NUMBER), '', put_input('Discount4', type=NUMBER), '', '', '',
                 #  put_input('Fee4', type=NUMBER), '', ''],
                 # [span('业务隔离', row=3)],
                 ])

            # put_text(" %s " % (pin.select1))
            # put_text("a + b = %s" % (pin.a + pin.b))



    # [put_text('名称'), put_text('类型'), put_text('备注'),put_text('数量'),put_text('税率'),put_text('折扣率'),put_text('一次性费用')],
    # put_select('select', options=['月流量30GB，通话500分钟', '月流量40GB，通话800分钟', '月流量60GB，通话1000分钟',
    #                               '月流量80GB，通话1000分钟'])
    # select('Which gift you want?', ['keyboard', 'ipad'])
    #
    # put_grid([
    #     # [put_text('名称'), put_text('类型'), put_text('备注'),put_text('数量'),put_text('税率'),put_text('折扣率'),put_text('一次性费用')],
    #     [put_text('名称'), put_text('类型')],
    #     [put_text('人联卡'), put_text('gift = %r' % gift)],
    # ], cell_width='100px', cell_height='100px')

def check_num(num):
    if(num > 100 or num < 0):
        return 'Invalid Input'

def Cal_RenLian(RenLian):
    r1 = 0
    d1 = 0
    dm1 = 0
    dy1 = 0
    fy1 = 0
    sum1 = 0
    # 人联卡的产品标准资费
    if (pin.select1 != None):
        r1 = RenLian[RenLian['月流量/通话'] == pin.select1].loc[:, '月资费'].values[0]
    if (pin.Discount1 != None):
        # 人联卡的折后资费
        d1 = int(r1) * int(pin.Discount1) * 0.01
        # 人联卡的折后月资费小计
        if (pin.Num1 != None):
            dm1 = d1 * int(pin.Num1)
            # 人联卡的折后年资费合计
            dy1 = dm1 * 12
    if (pin.Num1 != None and pin.Fee1 != None and pin.Discount1 != None):
        # 人联卡的一次性成本合计
        fy1 = int(pin.Num1) * int(pin.Fee1)
    sum1 = dy1 + fy1
    a1 = [r1,d1,dm1,dy1,fy1,sum1]
    return a1




def Cal_WuLian(WuLian_Month,WuLian_Year):
    r2 = 0
    d2 = 0
    dm2 = 0
    dy2 = 0
    fy2 = 0
    sum2 = 0
    # 物联卡的产品标准资费
    if(pin.select2 == '月包(通用)'):
        r2 = WuLian_Month[WuLian_Month['国内流量'] == pin.select3].loc[:, '通用流量'].values[0]
    elif(pin.select2 == '月包(定向)'):
        r2 = WuLian_Month[WuLian_Month['国内流量'] == pin.select3].loc[:, '定向流量'].values[0]
    elif (pin.select2 == '年包(通用)'):
        r2 = WuLian_Year[WuLian_Month['国内流量'] == pin.select3].loc[:, '通用流量'].values[0]
    elif (pin.select2 == '年包(定向)'):
        r2 = WuLian_Year[WuLian_Month['国内流量'] == pin.select3].loc[:, '定向流量'].values[0]

    if (pin.Discount2 != None):
        # 物联卡的折后资费
        d1 = int(r2) * int(pin.Discount2) * 0.01
        # 物联卡的折后月资费小计
        if (pin.Num2 != None):
            dm2 = d2 * int(pin.Num2)
            # 物联卡的折后年资费合计
            dy2 = dm2 * 12
    if (pin.Num2 != None and pin.Fee2 != None and pin.Discount2 != None):
        # 人联卡的一次性成本合计
        fy2 = int(pin.Num2) * int(pin.Fee2)
    sum2 = dy2 + fy2
    a2 = [r2, d2, dm2, dy2, fy2, sum2]
    return a2


start_server(main, port=8080, debug=True)


