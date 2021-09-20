import os
import time
from selenium import webdriver
import io
import requests
import hashlib
import chromedriver_binary


def great_img(word,add_word):
    # クリックなど動作後に待つ時間(秒)
    sleep_between_interactions = 2
    # ダウンロードする枚数
    download_num = 3


    # 検索ワード
    query = word + " " + add_word
    # 画像検索用のurl
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # サムネイル画像のURL取得
    wd = webdriver.Chrome()
    wd.get(search_url.format(q=query))
    # サムネイル画像のリンクを取得(ここでコケる場合はセレクタを実際に確認して変更する)
    thumbnail_results = wd.find_elements_by_css_selector("img.rg_i")

    # サムネイルをクリックして、各画像URLを取得
    image_urls = set()
    for img in thumbnail_results[:download_num]:
        try:
            img.click()
            time.sleep(sleep_between_interactions)
        except Exception:
            continue
        # 一発でurlを取得できないので、候補を出してから絞り込む(やり方あれば教えて下さい)
        # 'n3VNCb'は変更されることあるので、クリックした画像のエレメントをみて適宜変更する
        url_candidates = wd.find_elements_by_class_name('n3VNCb')
        for candidate in url_candidates:
            url = candidate.get_attribute('src')

            if url and 'https' in url:
                print(url)
                image_urls.add(url)
                
    # 少し待たないと正常終了しなかったので3秒追加
    time.sleep(sleep_between_interactions+3)
    wd.quit()
    url_list = list(image_urls)
    print(url_list[0])
    a = url_list[0]
    return  a
