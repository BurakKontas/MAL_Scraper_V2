from bs4 import BeautifulSoup


def scrap_producers(soup: BeautifulSoup) -> str:
    producers = []
    producers_div = soup.select_one(
        '#content > table > tbody > tr > td.borderClass > div > div:nth-child(21)')
    if "Producers" not in str(producers_div):
        return None
    producers_a = producers_div.find_all('a')
    for producer_a in producers_a:
        producers.append(producer_a.text)
    return producers
