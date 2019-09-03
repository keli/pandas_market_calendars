from datetime import time, timedelta
from functools import partial

from dateutil.relativedelta import MO
from pandas import DateOffset, Timestamp
from pandas.tseries.holiday import Holiday, next_monday, sunday_to_monday
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.holidays_us import USNewYearsDay

from pandas_market_calendars import MarketCalendar
from .exchange_calendar_sse import SSEExchangeCalendar
from .holidays_cn import *


class DCENightExchangeCalendar(SSEExchangeCalendar):
    """
    Exchange calendar for Dalian Commodity Exchange

    Night Session:
        Open Time: 9:00 PM, Asia/Shanghai
        Close Time: 11:00 PM, Asia/Shanghai
    """

    aliases = ['DCE_night']

    @property
    def name(self):
        return "DCE"

    @property
    def tz(self):
        return timezone('Asia/Shanghai')

    @property
    def open_time_default(self):
        return time(21, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(23, tzinfo=self.tz)
