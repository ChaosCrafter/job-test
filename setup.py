from setuptools import setup, find_packages

setup(
    name="job_test",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "run_app= job_test.main:main",
            "run_tests= job_test.unit_tests:run_tests",
        ],
    },
    test_suite="nose.collector",
    tests_require=["nose"],
    install_requires=[],
)
