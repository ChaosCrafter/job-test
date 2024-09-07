import requests


def live():
    data = requests.get(
        "http://frontendtest.jobs.fastmail.com.user.fm/data.json"
    ).json()

    return extract_names(data)


def extract_names(src_data):
    return [image["name"] for image in src_data["images"]]


def main():
    print(live())
