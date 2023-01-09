import time
from usecase.csv import write_csv
import config.config
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Doda:
    company_name = ""
    job_title = ""
    job_description = ""
    target = ""
    location = ""
    nearest_station = ""
    salary = ""
    business_overview = ""

    def __init__(self):
        pass

    def get_job_list(self):
        print("start get_job_list_from_indeed")

        # ヘッドレスモード
        options = Options()

        # iPhoneXをエミュレートした画面で実行する
        # mobile_emulation = {"deviceName": "iPhone X"}
        # options.add_experimental_option("mobileEmulation", mobile_emulation)

        # ポート9222でデバッグ通信を待ち受けているChromeを操作する
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--remote-debugging-address=127.0.0.1")

        # プロファイルの保存先を指定
        options.add_argument(
            "--user-data-dir=" + config.config.USER_DATA_DIR)
        # 使用するプロファイルを指定
        options.add_argument('--profile-directory=Default')

        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://doda.jp/DodaFront/View/JobSearchList.action?sid=TopSearch&usrclk=&op=&k=WEB%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2&oc=&pr=&ha=')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        job_list = driver.find_elements(By.CSS_SELECTOR, ".modList02")
        # up to 100
        job_list = job_list[:10]
        print("取得した求人リスト数：", len(job_list))

        dataList = [['会社名', '求人タイトル', '仕事内容',
                     '対象', '勤務地', '最寄り駅', '給与', '事業概要']]

        for job in job_list:

            job_title = job.find_element(By.CSS_SELECTOR, ".job")
            Doda.job_title = job_title.text
            print("求人タイトル：", job_title.text)

            company_name = job.find_element(By.CSS_SELECTOR, ".company")
            Doda.company_name = company_name.text
            print("会社名：", company_name.text)

            descriptions = job.find_elements(
                By.CSS_SELECTOR, ".listJpbSpec02")

            for index, description in enumerate(descriptions):
                if index == 5:
                    break

                if "仕事内容" in description.text:
                    Doda.job_description = descriptions[index].text
                    print("仕事内容：", descriptions[index].text)

                elif "対象" in description.text:
                    Doda.target = descriptions[index].text
                    print("対象：", descriptions[index].text)

                elif "勤務地" in description.text:
                    Doda.location = descriptions[index].text
                    print("勤務地：", descriptions[index].text)

                elif "最寄り駅" in description.text:
                    Doda.nearest_station = descriptions[index].text
                    print("最寄り駅：", descriptions[index].text)

                elif "給与" in description.text:
                    Doda.salary = descriptions[index].text
                    print("給与：", descriptions[index].text)

                elif "事業概要" in description.text:
                    Doda.business_overview = descriptions[index].text
                    print("事業概要：", descriptions[index].text)
                else:
                    continue

                data = [Doda.job_title, Doda.company_name, Doda.job_description, Doda.target,
                        Doda.location, Doda.nearest_station, Doda.salary, Doda.business_overview]

                dataList.append(data)

        write_csv('doda', dataList)

        # driver.get('https://www.google.co.jp')

        # search_bar = driver.find_element_by_name("q")
        # search_bar = driver.find_elements(By.NAME, "q")
        # search_bar[0].clear()
        # search_bar[0].send_keys(company_name.text+"電話番号")
        # search_bar[0].submit()

        # search_bar[0].click()

        # for elem_h3 in driver.find_elements(By.XPATH, '//a/h3'):
        #     elem_a = elem_h3.find_elements(By.XPATH, '..')[0]
        #     print(elem_h3.text)
        #     print(elem_a.get_attribute('href'))
        #     if len(elem_h3) > 3:
        #         break

    def get_new_candidates(self, client_id, password):
        print("start get_new_candidates_from_indeed")

        # ヘッドレスモード
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://secure.indeed.com/auth?continue=https%3A%2F%2Femployers.indeed.com%2Fjobs%3Ffrom%3Dgnav-empcenter%26from%3Dgnav-util-one-host&hl=ja&co=JP&userType=employer')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        client_id_input = driver.find_element(By.CSS_SELECTOR, ".e1jgz0i3")
        client_id_input.clear()
        client_id_input.send_keys(client_id)
        client_id_input.submit()

        time.sleep(5)

        password_input = driver.find_element(By.CSS_SELECTOR, ".e1jgz0i3")
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

    def get_new_candidates_from_agent(self, client_id, login_id, password):
        print("start get_new_candidates_from_indeed")

        # ヘッドレスモード
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://maps.doda.jp/maps/user/php/login.php?b=1&loc=progress.php')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        client_id_input = driver.find_element(By.CSS_SELECTOR, "#WCLNO")
        client_id_input.clear()
        client_id_input.send_keys(client_id)
        client_id_input.submit()

        login_id_input = driver.find_element(By.CSS_SELECTOR, "#WLGID")
        login_id_input.clear()
        login_id_input.send_keys(login_id)
        login_id_input.submit()

        password_input = driver.find_element(By.CSS_SELECTOR, "#WCLPW")
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

        button = driver.find_element(By.CSS_SELECTOR, "#login_btn")
        button.click()
