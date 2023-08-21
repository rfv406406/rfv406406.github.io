import urllib.request as request
import json
import csv

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]

# 將行政區資訊寫入 CSV 檔案
with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    districts = ["中正區", "萬華區", "中山區", "大同區", "大安區", "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]

    for sightspot in clist:
        address = sightspot["address"]
        stitle = sightspot["stitle"]
        longitude = sightspot["longitude"]
        latitude = sightspot["latitude"]

        splitfile = sightspot["file"].split("https")
        finalfile = "https" + splitfile[1]

        for district in districts:
            if district in address:
                district_name = district[:3]
                writer.writerow([stitle, district_name, longitude, latitude, finalfile])

# 將捷運站的景點資訊合併並寫入 CSV 檔案
    mrt_data = {}

    for sightspot in clist:
        MRT = sightspot["MRT"]
        stitle = sightspot["stitle"]
        
        if MRT and MRT.strip():
            if MRT in mrt_data:
                mrt_data[MRT] += "," + stitle
            else:
                mrt_data[MRT] = stitle

with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([])  # 空行，分隔行政區資訊和捷運站景點資訊

    for MRT, stitles in mrt_data.items():
        writer.writerow([MRT, stitles])