import json


def template(hotel):
    name = hotel["name"]
    vacancy = hotel["vacancy"]
    link = hotel["link"]
    return f"[{name}]({link}) ({vacancy})"


if __name__ == "__main__":
    result = dict()
    with open("./result.jsonl") as fp:
        for line in fp:
            hotel = json.loads(line)
            name = hotel["name"]
            date = hotel["date"]
            vacancy = hotel["vacancy"]
            link = hotel["reservation_url"]
            if result.get(date) is None:
                result[date] = [{"name": name, "vacancy": vacancy, "link": link}]
            else:
                result[date].append({"name": name, "vacancy": vacancy, "link": link})

    for date, hotels in sorted(result.items()):
        print(date)
        print("\t".join([template(h) for h in hotels]))

        print()
