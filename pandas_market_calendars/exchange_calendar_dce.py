from datetime import time, timedelta
from functools import partial

from dateutil.relativedelta import MO
from pandas import DateOffset, Timestamp
from pandas.tseries.holiday import Holiday, next_monday, sunday_to_monday
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.holidays_us import USNewYearsDay

from .market_calendar import MarketCalendar
from .exchange_calendar_sse import SSEExchangeCalendar
from .holidays_cn import *


class DCEExchangeCalendar(SSEExchangeCalendar):
    """
    Exchange calendar for Dalian Commodity Exchange

    Day Session:
        Open Time: 9:00 AM, Asia/Shanghai
        1st BREAK: 10:15 AM - 10:30 AM, Asia/Shanghai
        2nd BREAK: 11:30 AM - 1:30 PM Asia/Shanghai
        Close Time: 3:00 PM, Asia/Shanghai
    """

    aliases = ['DCE']

    break1_start = time(10, 15)
    break1_end = time(10, 30)
    break2_start = time(11, 30)
    break2_end = time(13, 30)

    @property
    def name(self):
        return "DCE"

    @property
    def tz(self):
        return timezone('Asia/Shanghai')

    @property
    def open_time_default(self):
        return time(9, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(15, 15, tzinfo=self.tz)

    @staticmethod
    def open_at_time(schedule, timestamp, include_close=False):
        tm = timestamp.time()
        if DCEExchangeCalendar.break1_start < tm < DCEExchangeCalendar.break1_end or \
            DCEExchangeCalendar.break2_start < tm < DCEExchangeCalendar.break2_end:
            return False
        return MarketCalendar.open_at_time(schedule, timestamp, include_close)
