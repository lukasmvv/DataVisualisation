import requests

from operator import itemgetter

# Make an api and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code: " + str(r.status_code))

# Process info about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate api call for each submission
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict["title"],
        "link": "http://news.ycombinator.coom/item?id=" + str(submission_id),
        "comments": response_dict.get("descendants", 0)  # when we are not sure if a key exists, we use the dict.get() method which returns value associated with key if it exists or value provided if it does not
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)  # sorting dicts by number of comments by using itemgetter

for submission_dict in submission_dicts:
    print("\nTitle: " + str(submission_dict["title"]))
    print("Discussion link: " + str(submission_dict["link"]))
    print("Comments: " + str(submission_dict["comments"]))