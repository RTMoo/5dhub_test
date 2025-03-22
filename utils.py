from hashlib import md5

MAX_URL_SIZE = 8


def url_shorter(url):
    short_url = md5(url.encode()).hexdigest()[:MAX_URL_SIZE]
    return short_url
