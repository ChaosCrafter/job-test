from unittest import TestCase
from .main import filter, extract_names


class TestMain(TestCase):
    def test_extract_names_step1(self, data):
        result = extract_names(data["images"])
        self.assertEqual(
            result,
            [
                "norway-1.jpg",
                "norway-2.jpg",
                "norway-3.jpg",
                "norway-4.jpg",
                "norway-5.jpg",
                "norway-6.jpg",
                "norway-7.jpg",
                "norway-8.jpg",
                "norway-9.jpg",
                "norway-10.jpg",
                "norway-11.jpg",
                "norway-12.jpg",
                "norway-13.jpg",
                "norway-14.jpg",
                "norway-15.jpg",
                "norway-16.jpg",
                "norway-17.jpg",
                "norway-18.jpg",
                "norway-19.jpg",
                "norway-20.jpg",
                "norway-21.jpg",
                "norway-22.jpg",
            ],
        )
        self.assertEqual(len(result), 22)

    def test_filter_step2(self, data):
        filtered_data = filter(data["images"], "yellow")
        result = extract_names(filtered_data)
        self.assertEqual(
            result,
            [
                "norway-2.jpg",
                "norway-3.jpg",
                "norway-4.jpg",
                "norway-5.jpg",
                "norway-18.jpg",
            ],
        )
        self.assertEqual(len(result), 5)

    def test_filter_step3(self, data):
        filtered_data = filter(data, "red white")
        result = extract_names(filtered_data)
        self.assertEqual(
            result,
            [
                "norway-3.jpg",
                "norway-15.jpg",
                "norway-16.jpg",
                "norway-17.jpg",
                "norway-22.jpg",
            ],
        )
        self.assertEqual(len(result), 5)

    def test_filter_step4_portrait(self, data):
        filtered_data = filter(data, "is:portrait")
        result = extract_names(filtered_data)
        self.assertEqual(result[0], "norway-7.jpg")
        self.assertEqual(len(result), 5)

    def test_filter_step4_portrait_colour(self, data):
        filtered_data = filter(data, "is:portrait green white")
        result = extract_names(filtered_data)
        self.assertEqual(result, ["norway-9.jpg"])
        self.assertEqual(len(result), 1)

    def test_filter_step4_landscape(self, data):
        filtered_data = filter(data, "is:landscape")
        result = extract_names(filtered_data)
        self.assertEqual(
            result,
            [
                "norway-1.jpg",
                "norway-2.jpg",
                "norway-3.jpg",
                "norway-4.jpg",
                "norway-5.jpg",
                "norway-6.jpg",
                "norway-10.jpg",
                "norway-11.jpg",
                "norway-13.jpg",
                "norway-14.jpg",
                "norway-15.jpg",
                "norway-16.jpg",
                "norway-17.jpg",
                "norway-19.jpg",
                "norway-20.jpg",
                "norway-21.jpg",
                "norway-22.jpg",
            ],
        )
        self.assertEqual(len(result), 17)

    def test_filter_step4_landscape_colour(self, data):
        filtered_data = filter(data, "is:landscape yellow")
        result = extract_names(filtered_data)
        self.assertEqual(
            result,
            [
                "norway-2.jpg",
                "norway-3.jpg",
                "norway-4.jpg",
                "norway-5.jpg",
            ],
        )
        self.assertEqual(len(result), 4)

    def test_filter_step5(self, data):
        filtered_data = filter(
            data, "is:landscape yellow OR black OR is:portrait green white"
        )
        result = extract_names(filtered_data)
        self.assertEqual(
            result,
            [
                "norway-2.jpg",
                "norway-3.jpg",
                "norway-4.jpg",
                "norway-5.jpg",
                "norway-8.jpg",
                "norway-9.jpg",
                "norway-19.jpg",
                "norway-22.jpg",
            ],
        )
        self.assertEqual(len(result), 8)


def run_tests():
    sample_data = {
        "imagePath": "http://frontendtest.jobs.fastmail.com.user.fm/images/",
        "images": [
            {
                "name": "norway-1.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["pink", "purple"],
            },
            {
                "name": "norway-2.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["green", "brown", "yellow", "red", "grey"],
            },
            {
                "name": "norway-3.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["red", "brown", "white", "blue", "green", "yellow", "grey"],
            },
            {
                "name": "norway-4.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["blue", "yellow", "green", "black"],
            },
            {
                "name": "norway-5.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["blue", "yellow", "red"],
            },
            {
                "name": "norway-6.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["green", "white", "brown"],
            },
            {
                "name": "norway-7.jpg",
                "width": 682,
                "height": 1024,
                "tags": ["white"],
            },
            {
                "name": "norway-8.jpg",
                "width": 682,
                "height": 1024,
                "tags": ["grey", "black"],
            },
            {
                "name": "norway-9.jpg",
                "width": 682,
                "height": 1024,
                "tags": ["white", "green"],
            },
            {
                "name": "norway-10.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["grey", "green", "brown"],
            },
            {
                "name": "norway-11.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["white", "blue", "green", "grey"],
            },
            {
                "name": "norway-12.jpg",
                "width": 682,
                "height": 1024,
                "tags": ["purple", "green", "brown"],
            },
            {
                "name": "norway-13.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["purple", "green", "brown"],
            },
            {
                "name": "norway-14.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["white", "brown", "green"],
            },
            {
                "name": "norway-15.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["red", "green", "white"],
            },
            {
                "name": "norway-16.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["red", "green", "white", "brown"],
            },
            {
                "name": "norway-17.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["red", "green", "white"],
            },
            {
                "name": "norway-18.jpg",
                "width": 682,
                "height": 1024,
                "tags": ["yellow", "red", "green"],
            },
            {
                "name": "norway-19.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["white", "black", "grey"],
            },
            {
                "name": "norway-20.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["green", "white", "brown"],
            },
            {
                "name": "norway-21.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["brown", "green", "white", "black"],
            },
            {
                "name": "norway-22.jpg",
                "width": 1024,
                "height": 683,
                "tags": ["orange", "green", "red", "white", "black", "pink"],
            },
        ],
    }

    TestMain().test_extract_names_step1(sample_data)
    TestMain().test_filter_step2(sample_data)
    # TestMain().test_filter_step3(sample_data)
    # TestMain().test_filter_step4_portrait(sample_data)
    # TestMain().test_filter_step4_portrait_colour(sample_data)
    # TestMain().test_filter_step4_landscape(sample_data)
    # TestMain().test_filter_step4_landscape_colour(sample_data)
    # TestMain().test_filter_step5(sample_data)
    print("Test completed")
