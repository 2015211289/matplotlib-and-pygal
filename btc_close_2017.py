import json
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
closes = []


for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))

import pygal
import math
from itertools import groupby
from datetime import datetime

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart =pygal.Line()
    line_chart.title = title
    line_chart.x_labels=x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

# datas = [datetime.strptime(_,'%Y-%m-%d') for _ in dates]
# idx_week = dates.index('2017-12-11')
# line_chart_month = draw_line([_.weekday() for _ in datas[1:idx_week]],closes[
#                                                               1:idx_week],
#                              'aveday_close_price_perWeekday','ave day close '
#                                                            'price')


with open('Dashboard_btc_close.html','w',encoding='utf-8') as html_file:
    html_file.write('<html><head><title>Dashboard of btc close</title><meta'
                    'charset="utf-8"></head><body>\n')
    for svg in ['close_price.svg','close_price_in_log.svg',
                'aveday_close_price_perMonth.svg',
                'aveday_close_price_perWeek.svg',
                'aveday_close_price_perWeekday.svg']:
        html_file.write('<object type="image/svg+xml" data="{0}" '
                        'height=500></object>\n'.format(svg))

    html_file.write('</body></html>')
