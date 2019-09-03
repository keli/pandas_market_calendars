from datetime import time, timedelta
from functools import partial

from dateutil.relativedelta import MO
from pandas import DateOffset, Timestamp
from pandas.tseries.holiday import Holiday, next_monday, sunday_to_monday
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.holidays.us import USNewYearsDay

from pandas_market_calendars.market_calendar import MarketCalendar
from pandas_market_calendars.holidays.cn import *
from .sse import SSEExchangeCalendar


class DCEExchangeCalendar(SSEExchangeCalendar):
    """
    Exchange calendar for Dalian Commodity Exchange

    Day Session:
        Open Time: 9:00 AM, Asia/Shanghai
        1st BREAK: 10:15 AM - 10:30 AM, Asia/Shanghai
        2nd BREAK: 11:30 AM - 1:30 PM Asia/Shanghai
        Close Time: 3:15 PM, Asia/Shanghai
    """

    aliases = ['DCE']

    tea_break_start = time(10, 15)
    tea_break_end = time(10, 30)
    break_start = time(11, 30)
    break_end = time(13, 30)

    regular_market_times = {
        "market_open": ((None, time(9, 0)), ),
        "tea_break_start": ((None, tea_break_start), ),
        "tea_break_end": ((None, tea_break_end), ),
        "break_start": ((None, break_start), ),
        "break_end": ((None, break_end), ),
        "market_close": ((None, time(15, 15)), ),
    }

    @property
    def name(self):
        return "DCE"

    @property
    def tz(self):
        return timezone('Asia/Shanghai')

    # def open_at_time(self, schedule, timestamp, include_close=False, only_rth=False):
    #     tm = timestamp.time()
    #     if DCEExchangeCalendar.tea_break_start < tm < DCEExchangeCalendar.tea_break_end:
    #         return False
    #     return super().open_at_time(schedule, timestamp, include_close, only_rth)
