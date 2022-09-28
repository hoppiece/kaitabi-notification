import json

if __name__ == "__main__":
    with open("./result.json") as fp:
        result = json.load(fp)
    for hotel in result:
        name = hotel["name"]
        date = hotel["date"]
        num_vacancy = hotel["vacancy"]
        link = hotel["reservation_url"]
        ret = f"【{name}】  {date}  空き:{num_vacancy}  [予約]({link})"
        print(ret)
