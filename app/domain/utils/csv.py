import csv
import datetime


def write_csv(service_name, data):
    # print now time
    datetime_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = './tmp/'+service_name+datetime_now+'.csv'
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
