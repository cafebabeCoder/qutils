# -*- coding: utf-8 -*-
# @Time   : 2021/3/7
# @Author : lorineluo 
import redis
import time
import datetime

en_ch_dict={
    'code': '代码',
    'stock_name': '股票',
    'qty': '持仓',
    'pl_ratio_trans': '盈亏比例',
    'pl_val': '盈亏金额',
    'price': '价格',
    'trd_side':'方向',
    'qty':'数量',
    'status':'订单状态',
    'pl_ratio_trans':'盈亏比例',
    'pl_val':'盈亏金额',
}

def ts_to_date(ts, sformat='%Y%m%d'):
    try:
        return datetime.datetime.timestamp(datetime.datetime.strptime(ts, sformat))
    except:
        return None

def date_to_ts(d, sformat='%Y%m%d'):
    try:
        return datetime.datetime.timestamp(datetime.datetime.strptime(d, sformat))
    except:
        return None 

def safe_to_int(v, default):
    if v is None or v == 'N/A':
        return default
    else:
        return int(v)

def safe_to_float(v, default):
    if v is None or v == 'N/A':
        return default
    else:
        return float(v)

# 把datafram转成json
def dataframe_to_str(data, columns=None, keepdim=3):
    columns = columns if columns else data.columns
    data = data[columns]
    float_columns = data.select_dtypes(include='float').columns
    for column in float_columns:
        data[column] = data[column].map(lambda x: str(round(x, 3)))
    msg_json = data.rename(columns = en_ch_dict).to_json(orient = "records", force_ascii=False, indent=4) 
    return msg_json

def get_n_days(current_day, n, sformat="%Y%m%d", before_flag=True):
    """
    获取n天前的时间戳
    :param current_day: yyyyMMdd
    :param n:
    :param before_flag: 默认获取n_days前的时间戳
    :return: yyyyMMdd
    """
    t = time.strptime(current_day, sformat)
    y, m, d = t[0:3]
    current_date = datetime.datetime(y, m, d)
    if before_flag:
        result_date = current_date + datetime.timedelta(-n)
    else:
        result_date = current_date + datetime.timedelta(n)
    return result_date.strftime(sformat)

def get_date(sformat='%Y%m%d'):
    return datetime.datetime.fromtimestamp(time.time()).strftime(sformat)

def parse_strike_timestamp(code, typ='C'):
    index = code.rfind(typ)
    strike_time = '20' + code[index-6:index]
    strike_ts = date_to_ts(strike_time)
    return strike_ts


if __name__ == '__main__':
    print(get_n_days('20210801', 7))
    print(get_date())
    code = 'US.AAPL210910C152500'
    print(parse_strike_timestamp(code))
