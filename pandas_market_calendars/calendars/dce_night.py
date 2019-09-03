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


class DCENightExchangeCalendar(SSEExchangeCalendar):
    """
    Exchange calendar for Dalian Commodity Exchange

    Night Session:
        Open Time: 9:00 PM, Asia/Shanghai
        Close Time: 11:00 PM, Asia/Shanghai
    """

    aliases = ['DCE_night']
    regular_market_times = {
        "market_open": ((None, time(21, 0)), ),
        "market_close": ((None, time(2, 30), 1), ),
    }

    @property
    def name(self):
        return "DCE_night"

    @property
    def tz(self):
        return timezone('Asia/Shanghai')
