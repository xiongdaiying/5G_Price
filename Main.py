from pywebio import start_server
from pywebio.output import *
from pywebio.session import go_app

from pywebio1.UPF import *
from pywebio1.VPDN import VPDNBaoBiao, VPDNPrice
from pywebio1.ZhuanWang import ZhuanWangBaoBiao, ZhuanWangPrice


def index():
    with use_scope('Title'):
        put_text('报表类型').style('font-size:20px')
        with use_scope('sub'):
            put_button('独享 UPF', onclick=lambda: go_app('upfBaoBiao', new_window=False))
            put_button('本地专网', onclick=lambda: go_app('ZhuanWangBaoBiao', new_window=False))
            put_button('5G VPDN', onclick=lambda: go_app('VPDNBaoBiao', new_window=False))


start_server([index,upfPrice,upfBaoBiao,ZhuanWangBaoBiao,ZhuanWangPrice,VPDNBaoBiao,VPDNPrice], port=8898, debug=True)