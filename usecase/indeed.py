import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Indeed:

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
            'https://jp.indeed.com/jobs?q=web%E5%88%B6%E4%BD%9C&l=&from=searchOnHP&vjk=e0b43d814dd088f1')

        time.sleep(5)

        # search_bar = driver.find_element_by_name("q")
        job_list = driver.find_elements(By.CSS_SELECTOR, ".job_seen_beacon")
        print("求人リストを取得", len(job_list))

        for job in job_list:

            job_title = job.find_element(By.CSS_SELECTOR, ".jobTitle")
            print("求人タイトル", job_title.text)

            company_name = job.find_element(By.CSS_SELECTOR, ".companyName")
            print("会社名", company_name.text)

            company_location = job.find_element(
                By.CSS_SELECTOR, ".companyLocation")

            print("会社の場所", company_location.text)
            if len(job.find_elements(By.CSS_SELECTOR, ".attribute_snippet")) > 0:
                attribute = job.find_element(
                    By.CSS_SELECTOR, ".attribute_snippet")
                print("給与", attribute.text)
            else:
                print("給与の記載なし")

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

    def get_new_candidates(self, email, password):
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
        email_input = driver.find_element(By.CSS_SELECTOR, ".e1jgz0i3")
        email_input.clear()
        email_input.send_keys(email)
        email_input.submit()

        time.sleep(5)

        password_input = driver.find_element(By.CSS_SELECTOR, ".e1jgz0i3")
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

        for job in job_list:

            job_title = job.find_element(By.CSS_SELECTOR, ".jobTitle")
