import time

from usecase.csv import write_csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Rikunabi:
    company_name: str = ''
    job_title: str = ''
    job_description: str = ''
    target: str = ''
    location: str = ''
    nearest_station: str = ''
    salary: str = ''
    business_overview: str = ''

    def __init__(self):
        pass

    def get_job_list(self):
        print('start get_job_list_from_indeed')

        # ヘッドレスモード
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?leadtc=top_kvs_submit')

        time.sleep(5)

        # search_bar = driver.find_element_by_name('q')
        job_list = driver.find_elements(
            By.CSS_SELECTOR, '.rnn-jobOfferList__item')
        # up to 100
        job_list = job_list[:5]
        print('取得した求人リスト数：', len(job_list))

        dataList = [['会社名', '求人タイトル', '仕事内容',
                     '対象', '勤務地', '最寄り駅', '給与', '事業概要']]

        for job in job_list:

            job_title = job.find_element(
                By.CSS_SELECTOR, 'h2.js-abScreen__title > a.rnn-linkText')
            Rikunabi.job_title = job_title.text
            print('求人タイトル：', job_title.text)

            company_name = job.find_element(By.CSS_SELECTOR, '.rnn-linkText')
            Rikunabi.company_name = company_name.text
            print('会社名：', company_name.text)

            job_description = job.find_element(
                By.CSS_SELECTOR, '.rnn-offerCatch__contents__title')
            Rikunabi.job_description = job_description.text
            print('仕事内容：', job_description.text)

            descriptions = job.find_elements(
                By.CSS_SELECTOR, 'rnn-col-10 rnn-offerDetail__text')

            location = descriptions[0]
            Rikunabi.location = location.text
            print('勤務地：', location.text)

            salary = descriptions[1]
            Rikunabi.salary = salary.text
            print('給与：', salary.text)

            job_description = descriptions[2]
            Rikunabi.job_description = job_description.text
            print('仕事内容：', job_description.text)

            target = descriptions[3]
            Rikunabi.target = target.text
            print('対象：', target.text)

            data = [Rikunabi.job_title, Rikunabi.company_name, Rikunabi.job_description, Rikunabi.target,
                    Rikunabi.location, Rikunabi.nearest_station, Rikunabi.salary, Rikunabi.business_overview]

            dataList.append(data)

        write_csv('Rikunabi', dataList)

        # driver.get('https://www.google.co.jp')

        # search_bar = driver.find_element_by_name('q')
        # search_bar = driver.find_elements(By.NAME, 'q')
        # search_bar[0].clear()
        # search_bar[0].send_keys(company_name.text+'電話番号')
        # search_bar[0].submit()

        # search_bar[0].click()

        # for elem_h3 in driver.find_elements(By.XPATH, '//a/h3'):
        #     elem_a = elem_h3.find_elements(By.XPATH, '..')[0]
        #     print(elem_h3.text)
        #     print(elem_a.get_attribute('href'))
        #     if len(elem_h3) > 3:
        #         break

    def get_new_candidates(self, client_id, password):
        print('start get_new_candidates_from_indeed')

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

        # search_bar = driver.find_element_by_name('q')
        client_id_input = driver.find_element(By.CSS_SELECTOR, '.e1jgz0i3')
        client_id_input.clear()
        client_id_input.send_keys(client_id)
        client_id_input.submit()

        time.sleep(5)

        password_input = driver.find_element(By.CSS_SELECTOR, '.e1jgz0i3')
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

    def get_new_candidates_from_agent(self, client_id, login_id, password):
        print('start get_new_candidates_from_indeed')

        # ヘッドレスモード
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '../../driver/chromedriver',
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(
            'https://maps.Rikunabi.jp/maps/user/php/login.php?b=1&loc=progress.php')

        time.sleep(5)

        # search_bar = driver.find_element_by_name('q')
        client_id_input = driver.find_element(By.CSS_SELECTOR, '#WCLNO')
        client_id_input.clear()
        client_id_input.send_keys(client_id)
        client_id_input.submit()

        login_id_input = driver.find_element(By.CSS_SELECTOR, '#WLGID')
        login_id_input.clear()
        login_id_input.send_keys(login_id)
        login_id_input.submit()

        password_input = driver.find_element(By.CSS_SELECTOR, '#WCLPW')
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()

        button = driver.find_element(By.CSS_SELECTOR, '#login_btn')
        button.click()
