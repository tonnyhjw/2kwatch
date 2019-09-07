
import requests
from bs4 import BeautifulSoup

from configs import *

def scrape():
    response = requests.request("GET", PS4_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    game_mode_table = soup.find('table', id="server-status-by-mode")
    # print(game_mode_table)
    for row in game_mode_table:
        print(row)
    return

if __name__ == '__main__':
    scrape()