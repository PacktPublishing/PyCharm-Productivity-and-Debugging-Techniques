import requests

SITES = [
    'http://youtube.com',
    'http://google.com',
    'http://python.org',
    'http://cnn.com'
]


def get_status(url):
    res = requests.get(url)
    return res.status_code

if __name__ =='__main__':
    get_status('http://python')
