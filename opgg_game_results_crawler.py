import os
import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

PATH = 'data'

# TODO 1: 각 랭킹 페이지에 대응할 수 있도록 수정
# TODO 2: 게임 종류 솔로 랭크 여부 확인 코드 추가
class GetGameInfo:
    def __init__(self):
        self.__base_url = 'http://www.op.gg/ranking/ladder/page=1'

    @staticmethod
    def text2time(timestamp):
        timestamp = timestamp[:-1]
        time_split = timestamp.split('m ')

        time_converted = float(time_split[0]) + (float(time_split[-1]) / 60)
        return round(time_converted, 2)

    def _get_highest_summoner_urls(self):
        res = requests.get(self.__base_url)
        contents = BeautifulSoup(res.content, 'html.parser')
        rank_highest_list = contents.find('ul', 'ranking-highest__list')
        rank_highest_items = rank_highest_list.find_all('li')
        highest_summoner_urls = ['https://' + item.a['href'][2:] for item in rank_highest_items]
        return highest_summoner_urls

    def _get_summoner_urls(self):
        res = requests.get(self.__base_url)
        contents = BeautifulSoup(res.content, 'html.parser')
        rank_table = contents.find('table', 'ranking-table')
        rank_body = rank_table.find('tbody')
        rank_items = rank_body.find_all('tr')
        summoner_urls = ['https://' + item.a['href'][2:] for item in rank_items]
        return summoner_urls

    def get_summoner_urls(self):
        highest_summoner_urls = self._get_highest_summoner_urls()
        summoner_urls = self._get_summoner_urls()
        return highest_summoner_urls + summoner_urls

    def get_game_stats(self, url):

        game_df = pd.DataFrame(columns=['result', 'time', 'kill',
                                        'death', 'assist', 'kda',
                                        'p_kill', 'wards', 'cs', 'cs/m'])
        res = requests.get(url_1)
        contents = BeautifulSoup(res.content, 'html.parser')
        game_info_list = contents.find_all('div', 'GameItemWrap')

        for info in game_info_list:

            try:
                stats = {
                    'result': re.sub('\s', '', info.find('div', 'GameResult').text),
                    'time': text2time(info.find('div', 'GameLength').text),
                    'kill': info.find('span', 'Kill').text,
                    'death': info.find('span', 'Death').text,
                    'assist': info.find('span', 'Assist').text,
                    'kda': info.find('span', 'KDARatio').text[:-2],
                    'p_kill': float(re.findall('[0-9]{2}', info.find('div', 'CKRate').text)[0]) / 100,
                    'wards': info.find('span', 'wards vision').text,
                    'cs': info.find('span', 'CS tip').text.split()[0],
                    'cs/m': info.find('span', 'CS tip').text.split()[1][1:-1],
                }
            except AttributeError:
                stats = {
                    'result': re.sub('\s', '', info.find('div', 'GameResult').text),
                    'time': text2time(info.find('div', 'GameLength').text),
                    'kill': info.find('span', 'Kill').text,
                    'death': info.find('span', 'Death').text,
                    'assist': info.find('span', 'Assist').text,
                    'kda': info.find('span', 'KDARatio').text[:-2],
                    'p_kill': float(re.findall('[0-9]{2}', info.find('div', 'CKRate').text)[0]) / 100,
                    'wards': 0,
                    'cs': info.find('span', 'CS tip').text.split()[0],
                    'cs/m': info.find('span', 'CS tip').text.split()[1][1:-1],
                }

            if stats['kda'] == 'Perfe':
                stats['kda'] = np.inf

            game_df.loc[len(game_df)] = {
                'result': stats['result'],
                'time': stats['time'],
                'kill': stats['kill'],
                'death': stats['death'],
                'assist': stats['assist'],
                'kda': stats['kda'],
                'p_kill': stats['p_kill'],
                'wards': stats['wards'],
                'cs': stats['cs'],
                'cs/m': stats['cs/m'],
            }
        game_df.iloc[:, 1:] = game_df.iloc[:, 1:].astype(float)

        return game_df

    def get_game_stats_df(self):

        summoner_urls = self.get_summoner_urls()

        df_list = []
        for url in tqdm(summoner_urls):
            df = self.get_game_stats(url)
            df_list.append(df)

            df_concat = pd.concat(df_list)
        return df_concat


def main():
    if not os.path.exists(os.path.join(PATH)):
        os.makedirs(PATH)
    get_game_info = GetGameInfo()
    game_df = get_game_info.get_game_stats_df()
    game_df.to_csv(os.path.join(PATH, 'game_results.csv'), index=False)


if __name__ == 'main':
    main()