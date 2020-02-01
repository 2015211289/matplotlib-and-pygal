import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print("Status code:",r.status_code)

reponse_dict = r.json()
print('Total repositories:',reponse_dict['total_count'])
print('incomplete_results:',reponse_dict['incomplete_results'])

repo_dicts = reponse_dict['items']

names, plot_dicts =[],[]

for repo_dict in repo_dicts:

    # print('\nName:',repo_dict['name'])
    # print('Owner:',repo_dict['owner']['login'])
    # print('Stars:',repo_dict['stargazers_count'])
    # print('Repository:',repo_dict['html_url'])
    # print('Created:',repo_dict['created_at'])
    # print('Updated:',repo_dict['updated_at'])
    # print('Description:',repo_dict['description'])

    names.append(repo_dict['name'])
    value = lambda x: x if x else 0
    label = lambda x: x if x else ''

    plot_dict = {
        'value': value(repo_dict['stargazers_count']),
        'label': label(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.force_uri_protocol = 'http'
my_config.x_label_rotation = 45
my_config.show_legend=False
my_config.title_font_size =24
my_config.label_font_size = 14
my_config.major_label_font_size =18
my_config.truncate_label =15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title='Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
