import json

if __name__ == "__main__":
    result = []
    with open("./result.jsonl") as fp:
        for line in fp:
            result.append(json.loads(line))
    for hotel in result:
        name = hotel["name"]
        date = hotel["date"]
        num_vacancy = hotel["vacancy"]
        link = hotel["reservation_url"]
        ret = f"【{name}】  {date}  空き:{num_vacancy}  [予約]({link})"
        print(ret)
