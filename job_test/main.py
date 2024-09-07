import requests

def live(filter_string):
    
    data = requests.get(
        "http://frontendtest.jobs.fastmail.com.user.fm/data.json"
    ).json()
    filtered_data = filter(data["images"], filter_string)

    return extract_names(filtered_data)


def filter(src_data, filter_string):
    images = []
    for image in src_data:
        if filter_string in image["tags"]:
            images.append(image)
    return images


def extract_names(src_data):
    return [image["name"] for image in src_data]

def main():
    print(live("red"))
