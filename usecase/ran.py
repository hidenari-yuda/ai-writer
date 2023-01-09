import time

from usecase.csv import write_csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Ran:
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
            'https://Ran.jp/RanFront/View/JobSearchList.action?sid=TopSearch&usrclk=&op=&k=WEB%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2&oc=&pr=&ha=')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        job_list = driver.find_elements(By.CSS_SELECTOR, ".modList02")
        # up to 100
        job_list = job_list[:10]
        print("取得した求人リスト数：", len(job_list))

        dataList = ['会社名', '求人タイトル', '仕事内容', '対象', '勤務地', '最寄り駅', '給与', '事業概要']

        for job in job_list:

            job_title = job.find_element(By.CSS_SELECTOR, ".job")
            Ran.job_title = job_title.text
            print("求人タイトル：", job_title.text)

            company_name = job.find_element(By.CSS_SELECTOR, ".company")
            Ran.company_name = company_name.text
            print("会社名：", company_name.text)

            descriptions = job.find_elements(
                By.CSS_SELECTOR, ".listJpbSpec02")

            for index, description in enumerate(descriptions):
                if index == 5:
                    break

                if "仕事内容" in description.text:
                    Ran.job_description = descriptions[index].text
                    print("仕事内容：", descriptions[index].text)

                elif "対象" in description.text:
                    Ran.target = descriptions[index].text
                    print("対象：", descriptions[index].text)

                elif "勤務地" in description.text:
                    Ran.location = descriptions[index].text
                    print("勤務地：", descriptions[index].text)

                elif "最寄り駅" in description.text:
                    Ran.nearest_station = descriptions[index].text
                    print("最寄り駅：", descriptions[index].text)

                elif "給与" in description.text:
                    Ran.salary = descriptions[index].text
                    print("給与：", descriptions[index].text)

                elif "事業概要" in description.text:
                    Ran.business_overview = descriptions[index].text
                    print("事業概要：", descriptions[index].text)
                else:
                    continue

                data = [Ran.job_title, Ran.company_name, Ran.job_description, Ran.target,
                        Ran.location, Ran.nearest_station, Ran.salary, Ran.business_overview]

                dataList.append(data)

        write_csv('Ran', dataList)

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
            'http://ran.next.rikunabi.com/rnc/docs/ca_s01000.jsp?__u=16731842261808094708518985156008')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        id_input = driver.find_element(By.NAME, "login_nm")
        id_input.clear()
        id_input.send_keys(id)
        id_input.submit()

        password_input = driver.find_element(By.NAME, "pswd")
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

        button = driver.find_element(By.CSS_SELECTOR, ".btn01")
        button.click()
