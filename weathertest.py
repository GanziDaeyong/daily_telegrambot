import requests
import json
import datetime


def get_raw_weather(key):
    url_wo_date = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={key}&numOfRows=1000&dataType=JSON&pageNo=1&base_time=0500&nx=61&ny=125"
    date = str(datetime.date.today()).replace("-", "").strip()
    url = url_wo_date + "&base_date=" + date

    raw = ((requests.get(url)).content).decode()
    raw_dict = json.loads(raw)

    body_dict = raw_dict["response"]["body"]["items"]["item"]

    return body_dict


def process_weather(raw_weather):

    ## get today's
    date = str(datetime.date.today()).replace("-", "").strip()
    raw_weather = [v for v in raw_weather if v["fcstDate"] == date]

    temp_li = [item for item in raw_weather if item["category"] == "TMP"]
    rain_percentage_li = [item for item in raw_weather if item["category"] == "POP"]
    rain_type_li = [item for item in raw_weather if item["category"] == "PTY"]
    sky_li = [item for item in raw_weather if item["category"] == "SKY"]

    fcst_res = ""

    for _, (temp, sky, rainp, raint) in enumerate(
        zip(temp_li, sky_li, rain_percentage_li, rain_type_li)
    ):

        sky_s = "맑음" if int(sky["fcstValue"]) <= 3 else "안맑음"
        v = int(raint["fcstValue"])
        raint_s = (
            "비 안올듯"
            if v == 0
            else "비"
            if v == 1
            else "비/눈"
            if v == 2
            else "눈"
            if v == 3
            else "소나기"
        )

        fcst_res += f"[{temp['fcstTime']}] {raint_s}({rainp['fcstValue']}%), {temp['fcstValue']}도, 하늘은{sky_s}\n"

    return fcst_res
