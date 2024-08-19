from collections import Counter

import pandas as pd
import requests
import pandas as dp


NEWS_API = "https://belarusbank.by/api/news_info"


def format_news(news_list: list[dict]) -> list[dict]:
    new_list = []
    for item in news_list:
        new_item = {"name_ru": item["name_ru"],
                    "start_date": item["start_date"]}
        new_list.append(new_item)
    return new_list


def get_news(url: str):
    response = requests.get(url)
    if not str(response.status_code).startswith("2"):
        return "Invalid response.status_code. Not equal 2XX"
    fresh_news = response.json()[:20]
    return fresh_news


def exclude_even_date(news_list: list[dict]) -> list[dict]:
    new = []
    for item in news_list:
        if item['start_date'][-1] not in "02468":
            new.append(item)
    return new



news = get_news(url=NEWS_API)
f_news = format_news(news_list=news)
# print(f_news, len(f_news))
odd_news = exclude_even_date(news_list=f_news)
# print(odd_news, len(odd_news))


def get_longest_title(news_list: list[dict]) -> str:
    return max(news_list, key=lambda item: len(item["name_ru"]))['name_ru']


print(get_longest_title(odd_news))


def get_longest_word(news_list: list[dict]) -> str:
    return max(news_list, key=lambda item: len(item["name_ru"].split()))['name_ru']


print(get_longest_word(odd_news))
print(get_longest_title(odd_news))


def most_common_letter(new_list: list[dict]) -> str:
    all_titles = ''
    for item in new_list:
        all_titles += item['name_ru'].replace(" ", '')
    letter, count = Counter(all_titles).most_common(1)[0]
    return letter


print(most_common_letter(odd_news))


print(odd_news)


df = pd.DataFrame(odd_news)
df.to_excel('./odd_news.xlsx')