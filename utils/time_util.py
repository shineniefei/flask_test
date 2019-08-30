#!/usr/bin/env python3
# coding: utf-8

import time
from calendar import month
from datetime import datetime, timedelta


class TimeUtil():
    pass

    def now_timeStamp(self, ms=False):
        if not ms:
            return time.time()
        else:
            return int(round(time.time() * 1000))

    def to_timeStamp_s(self, timeStamp=None):
        if timeStamp is None:
            return int(time.time())
        else:
            return int(timeStamp / 1000)

    def to_timeStamp(self, date=None):
        if date is None:
            return int(time.time())
        else:
            return int(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))

    def to_localTime(self, timeStamp=None):
        if timeStamp is None:
            # return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # return datetime.now()
            return time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeStamp))

    def to_localTimeTZ(self, timeStamp=None):
        if timeStamp is None:
            return time.strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            return time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                 time.localtime(timeStamp))

    def time_format_ymd(self, date=None):
        if date is None:
            # return datetime.now().strftime('%Y-%m-%d')
            return time.strftime("%Y-%m-%d")
        else:
            pass

    def time_format_year(self, date=None):
        if date is None:
            # return datetime.now().year
            return time.strftime("%Y")
        else:
            pass

    def time_format_month(self, date=None):
        if date is None:
            # return datetime.now().month
            return time.strftime("%m")
        else:
            pass

    def time_format_day(self, date=None):
        if date is None:
            # return datetime.now().day
            return time.strftime("%d")
        else:
            pass

    def time_format_hour(self, date=None):
        if date is None:
            # return datetime.now().hour
            return time.strftime("%H")
        else:
            pass

    def time_format_minute(self, date=None):
        if date is None:
            # return datetime.now().minute
            return time.strftime("%M")
        else:
            pass

    def time_format_second(self, date=None):
        if date is None:
            # return datetime.now().second
            return time.strftime("%S")
        else:
            pass


# utcTime = time.strftime("%Y-%m-%d %H:%M:%S")
# print(time.gmtime(timeStamp))
# print(time.strptime(utcTime, "%Y-%m-%d %H:%M:%S"))
# print(month(2018, 2))
# print(timedelta(days=1))
# print(datetime.now().isoformat())

if __name__ == "__main__":
    TimeUtil = TimeUtil()
    print(TimeUtil.now_timeStamp())
    nowstamp = TimeUtil.now_timeStamp(True)
    print(nowstamp)
    nowstamp_s = TimeUtil.to_timeStamp_s(nowstamp)
    print(nowstamp_s)
    date = TimeUtil.to_localTime(nowstamp_s)
    print(date)
    print(TimeUtil.to_localTimeTZ(nowstamp_s))
    print(TimeUtil.to_timeStamp(date))
    print(TimeUtil.time_format_minute())
    print(TimeUtil.time_format_second(date))
