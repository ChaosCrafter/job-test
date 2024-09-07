import requests


def live(filter_string):
    data = requests.get(
        "http://frontendtest.jobs.fastmail.com.user.fm/data.json"
    ).json()
    filtered_data = filter(data["images"], filter_string)

    return extract_names(filtered_data)


def parse_filter(filter_string):
    return filter_string.strip().split()


def filter(src_data, filter_string):
    filter_items = parse_filter(filter_string)
    images = []
    for image in src_data:
        valid = True
        for colour in filter_items:
            if not colour in image["tags"]:
                valid = False
                break
        if valid:
            images.append(image)
    return images


def extract_names(src_data):
    return [image["name"] for image in src_data]


def main():
    print(live("red white"))
