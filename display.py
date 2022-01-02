from github import Github
import pygal
import itertools 
import collections
import sys

# Get the Github username and their repositories
username = input("Enter a Github Username: ")

try:
    token = input("Enter your personal access token: ")
    git = Github(token)
    user = git.get_user(username)
    print("Valid token")
except:
    git = Github()
    user = git.get_user(username)
    print("Invalid token")

repositories = user.get_repos()

languages, months = {}, [0] * 12
name_of_months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for repo in repositories:

    language = repo.language
    if language in languages:
        languages[language] = languages[language] + 1
    else:
        languages[language] = 1

    month = int(repo.created_at.strftime("%m"))
    months[month-1] = months[month-1] + 1

config = pygal.Config()
config.show_legend = True
config.title_font_size = 65
config.label_font_size = 25
config.show_y_guides = False
config.width = 1400

pie_chart = pygal.Pie(config, inner_radius=.4)
pie_chart.title = f"Favurite languages by {user.login}"
for language in languages:
    pie_chart.add(language, languages[language])
pie_chart.render_in_browser()
pie_chart.render_to_file("Favourite_languages.svg")

tree_map = pygal.Treemap(config)
tree_map.title = f"Most starred repositories by {user.login}"
for repo in repositories:
    tree_map.add(repo.name, repo.stargazers_count)
tree_map.render
tree_map.render_in_browser()
tree_map.render_to_file("Most_Starred_Repos.svg")

bar_chart = pygal.Bar(config)
bar_chart.title = f"How many repositories did {user.login} create in each month"
bar_chart.x_labels = name_of_months
bar_chart.add('', months)
bar_chart.render
bar_chart.render_in_browser()
bar_chart.render_to_file("Repositories_Made_Each_Month.svg")