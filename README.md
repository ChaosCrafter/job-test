This repo will demonstrate each step of the filtering function requested by fastmail.
In an environment configured with Python () and Pip () it can be tested with the commands...

pip install -e .
run_app
run_test

Run_app uses the source data at http://frontendtest.jobs.fastmail.com.user.fm/data.json
Run_test uses local test data.

Copied from the request, the goal is to provide the following...

Instructions for your assessment
In the programming language of your choice, do the following steps. Each step should be a single commit in a git repository. Please send us a link to where we can find the repository.
Please document any assumptions you make regarding the requirements.
1. Create a function that fetches the data from http://frontendtest.jobs.fastmail.com.user.fm/data.json and outputs a list of the name properties of each object.
2. Add a search argument to the function. This is a string. If supplied, only output the name of objects with a colour matching the string.
3. Modify the function so the search argument can be a string with multiple colour names, e.g. "red white". An object must have all given colours to match.
4. Add support for "is:portrait" and "is:landscape" keywords, to only return the names of objects that represent portrait or landscape images respectively. These keywords can be used in combination with the colour names to filter, e.g. "red is:portrait".
5. Add support for the "OR" operator, e.g. "red OR white is:portrait" to return the names of objects that match any of the given conditions.
