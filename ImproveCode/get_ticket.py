import urllib
import urllib3
import requests


def show_ticket():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-16&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'

    response = requests.get(url)

    data = response.json()

    result = data['data']['result']

    return result


def get_image():
    url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=passenger&rand=randp&0.49825346980074925'

    # response = requests.get(url)
    # response = urllib.urlopen(url)

    # print(dir(response.content))
    # print(response.status_code)
    #
    # f = open('image.png', 'wb')
    # f.write(response.content)
    # f.close()

    response = urllib.request.urlopen(url)
    content = response.read()
    f = open('image.png', 'wb')
    f.write(content)
    f.close()


if __name__ == '__main__':
    result = show_ticket()

    index = 0
    for item in result:
        ticket_info = item.split('|')[1:]
        if ticket_info[29] not in ['', '无']:
            print(ticket_info[2], ticket_info[29], "二等座")

    # get_image()
