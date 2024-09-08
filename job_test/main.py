import requests


def live(filter_string):
    data = requests.get(
        "http://frontendtest.jobs.fastmail.com.user.fm/data.json"
    ).json()
    filtered_data = filter(data["images"], filter_string)

    return extract_names(filtered_data)


def parse_filter(filter_string):
    filter_sets = filter_string.strip().lower().split(" or ")

    return [filter_set.strip().split() for filter_set in filter_sets]


def filter(src_data, filter_string):
    filter_sets = parse_filter(filter_string)
    print(filter_sets)
    images = []
    for image in src_data:
        for filter_set in filter_sets:
            valid = True
            for condition in filter_set:
                match condition:
                    case "is:landscape":
                        if image["width"] <= image["height"]:
                            valid = False
                            break
                    case "is:portrait":
                        if image["width"] >= image["height"]:
                            valid = False
                            break
                    case _:
                        if not condition in image["tags"]:
                            valid = False
                            break
            if valid:
                images.append(image)
                break
    return images


def extract_names(src_data):
    return [image["name"] for image in src_data]


def main():
    print(live("is:landscape yellow OR black OR is:portrait green white"))
