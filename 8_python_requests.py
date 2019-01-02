import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# rate limit: api.github.com/rate_limit

# Make an API call and store response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)  # status code of 200 means succesful response

# Store response in a variable
response_dict = r.json()
print(response_dict.keys())
print("Total repositories: " + str(response_dict["total_count"]))

# Process results
repo_dicts = response_dict["items"]
print("Repositories returned: " + str(len(repo_dicts)))

# Storing info
names, stars = [], []
plot_dicts = []

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    # stars.append(repo_dict["stargazers_count"])
    # descriptions.append(repo_dict["description"])
    # plot_dicts.append({"value": repo_dict["stargazers_count"], "label": repo_dict["description"]})

    # Get project description if available
    description = repo_dict["description"]
    if not description:
        description = "No description provided"

    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": description,
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)

print(plot_dicts)
# Make visualization
my_style = LS("#333366", base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most Starred Python Projects on Github"
chart.x_labels = names
# chart.add("", stars)
chart.add("", plot_dicts)  # send a dictionary of values and descriptions to add custom tooltips
chart.render_to_file("python_repos.svg")

# Examine first repo
#repo_dict = repo_dicts[0]
#print("\nKeys: " + str(len(repo_dict)))
#for key in sorted(repo_dict.keys()):
#    print(key)

# Print info about each repo
#print("\nSelected info of each repo:")

#for repo_dict in repo_dicts:
#    print("Name: " + str(repo_dict["name"]))
#    print("Owner: " + str(repo_dict["owner"]["login"]))  # entire dictionary represents owner, so use login as second key to get login value
#    print("Stars: " + str(repo_dict["stargazers_count"]))
#    print("Repo: " + str(repo_dict["html_url"]))
#    print("Created: " + str(repo_dict["created_at"]))
#    print("Updated: " + str(repo_dict["updated_at"]))
#    print("Description: " + str(repo_dict["description"]))