import os

import pytest

def test_dict_connection():

    dict_a = {
        "a":1,
        "b":2,
        "c":1
    }

    dict_b = {
        "c":3
    }

    dict_c = {
        "a":1,
        "b":2,
        "c":3
    }

    # python <= 3.8
    dict_c_38 = dict_a.copy()
    dict_c_38.update(dict_b)

    # python 3.9
    dict_c_39 = dict_a | dict_b

    assert dict_c == dict_c_39 == dict_c_38

def test_removeprefix():

    str_a = "PYbbbbPYccc"
    correct = "bbbbPYccc"

    # python 3.8
    str_38 = str_a.replace("PY", "", 1)

    # python 3.9
    str_39 = str_a.removeprefix("PY")

    assert correct == str_38 == str_39

def test_removesuffix():

    str_a = "bbbbPYcccPY"
    correct = "bbbbPYccc"

    # python <= 3.8
    if str_a.endswith("PY"):
        str_38 = str_a[:len(str_a)-len("PY")]

    # python 3.9
    str_39 = str_a.removesuffix("PY")

    assert correct == str_38 == str_39

from datetime import datetime
from zoneinfo import ZoneInfo # python 3.9

def test_timezone():
    
    tokyo = ZoneInfo("Asia/Tokyo") # タイムゾーン情報を取得
    jst_now = datetime(2021, 4, 10, 0, 0, 0, tzinfo=tokyo) # Asia/Tokyoタイムゾーンでの現在時刻を取得

    correct = "2021-04-10T00:00:00+09:00"
    assert correct == jst_now.isoformat()

    utc = ZoneInfo("UTC")
    utc_now = jst_now.astimezone(utc)
    correct = "2021-04-09T15:00:00+00:00"
    assert correct == utc_now.isoformat()

    pst = ZoneInfo("America/Los_Angeles")
    pst_now = jst_now.astimezone(pst)
    correct = "2021-04-09T08:00:00-07:00"
    assert correct == pst_now.isoformat()
