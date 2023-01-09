import time

from usecase.csv import write_csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Mynavi:
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
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://tenshoku.mynavi.jp/list/?jobsearchType=4&searchType=8')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        # scrape job list from indeed upto 100

        job_list = driver.find_elements(
            By.CSS_SELECTOR, ".cassetteRecruitRecommend")
        # up to 100
        job_list = job_list[:10]
        print("取得した求人リスト数：", len(job_list))

        dataList = ['会社名', '求人タイトル', '仕事内容', '対象', '勤務地', '最寄り駅', '給与', '事業概要']

        for job in job_list:

            job_title = job.find_element(
                By.CSS_SELECTOR, ".cassetteRecruitRecommend__copy")
            Mynavi.job_title = job_title.text
            print("求人タイトル：", job_title.text)

            company_name = job.find_element(
                By.CSS_SELECTOR, ".cassetteRecruitRecommend__name")
            Mynavi.company_name = company_name.text
            print("会社名：", company_name.text)

            attributes = job.find_elements(
                By.CSS_SELECTOR, "li.cassetteRecruit__attributeLabel > span.labelCondition")
            for attribute in attributes:
                print("特徴",attribute.text)

            detail_url = job.find_element(
                By.CSS_SELECTOR, ".linkArrowS").get_attribute("href")
            print("詳細URL：", detail_url)

            descriptions = job.find_elements(
                By.CSS_SELECTOR, ".tableCondition__body")

            Mynavi.job_description = descriptions[0].text
            print("仕事内容：", Mynavi.job_description)

            Mynavi.target = descriptions[1].text
            print("対象：", Mynavi.target)

            Mynavi.location = descriptions[2].text
            print("勤務地：", Mynavi.location)

            Mynavi.salary = descriptions[3].text
            print("給与：", Mynavi.salary)

            print("初年度年収：", descriptions[4].text)

            data = [Mynavi.job_title, Mynavi.company_name, Mynavi.job_description, Mynavi.target,
                    Mynavi.location, Mynavi.nearest_station, Mynavi.salary, Mynavi.business_overview]

            dataList.append(data)

        write_csv('Mynavi', dataList)

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

    def get_new_candidates(self, id, password):
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
            'https://mynavi.agentsearch.jp/client/')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        id_input = driver.find_element(
            By.CSS_SELECTOR, "#clientMailAddress")
        id_input.clear()
        id_input.send_keys(id)
        id_input.submit()

        time.sleep(5)

        password_input = driver.find_element(
            By.CSS_SELECTOR, "#clientPassword")
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

        button = driver.find_element(By.CSS_SELECTOR, ".js-recaptcha")
        button.click()
