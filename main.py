from config.config import get_env
from usecase.workport import Workport
from usecase.csv import write_csv
from usecase.doda import Doda
from usecase.indeed import Indeed

# doda = Doda()
# doda.get_job_list()
# print("end")
get_env()

workport = Workport()
workport.get_job_list()
print("end")

# indeed = Indeed()
# indeed.get_job_list()

# CareerCross	応募者記録	https://www.careercross.com/job-application	　
# リクルートダイレクトスカウト	会員管理	https://agt.directscout.recruit.co.jp/agent/applicants	　
# キャリアトレック	進捗管理	https://ag.careertrek.com/progress-management/?recruiterId=XXXX	最後のXXXXはアカウントによって変わります。
# 4桁～の数字。
# Daijob	応募者一覧
# https://companytools.daijob.com/company_profiles/[AgentID]/search/company_applicants
# [AgentID]はアカウントによって変わります。
# 4桁数字。
# doda	進捗管理一覧	https://maps.doda.jp/maps/user/php/progress.php	　
# イーキャリアFA	応募者管理	https://www.ecareerfa.jp/agent/mailbox/entry/history	　
# ミドル転職	エントリー管理	https://mid-tenshoku.com/company/entry/entry_list/?PK=YYYYYY	最後のYYYYYYアカウントによって変わります。
# 数字とローマ字混在。
# マイナビ転職エージェントサーチ	応募者情報一覧	https://mynavi.agentsearch.jp/client/applicationTop/	　
# RAN	エントリー者一覧	https://ran.next.rikunabi.com/rnc/docs/ca_f00010.jsp?tab_select_id=4&__u=ZZZZZZ	最後のZZZZはアカウントによって変わります。
# 長い数字。
# 「経験職種」など職種データは取得していません。
# 日経転職版	なし	なし	日経から直接応募者データをいただいていますので、
# ページのスクレイピングはしていません。
