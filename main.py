from time import sleep

from selenium import webdriver

MYNAVI_URL = "https://tenshoku.mynavi.jp/list/"


def main():
    driver = webdriver.Chrome()
    # このままでは動きません。
    # 肉付けし、動かしましょう。
    driver.get(MYNAVI_URL)
    sleep(3)
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        sleep(1)
        driver.execute_script('document.querySelector(".karte-close").click()')
    except Exception:
        pass


if __name__ == "__main__":
    main()
