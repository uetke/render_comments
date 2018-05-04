import datetime
import os

import yaml as yaml
from os.path import isfile, join
from jinja2 import Environment, FileSystemLoader, select_autoescape
from os import listdir
import markdown

commentsPath = 'comments_yml'
output_path = 'comments'
commentsYML = [f for f in listdir(commentsPath) if isfile(join(commentsPath, f))]

comments = {}
for c in commentsYML:
    c = join(commentsPath, c)
    with open(c, 'r') as f:
        data = yaml.load(f)
        if not data['url'] in comments:
            comments[data['url']] = []

        comments[data['url']].append({
            'name': data['name'],
            'website': data['website'] if 'website' in data else None,
            'message': markdown.markdown(data['message']),
            'date': data['date'],
            'avatar': 'https://www.gravatar.com/avatar/'+data['email']+'?s=64',
        })


env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)
FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')).list_templates()

def datetimeformat(value, format='%d-%m-%Y at %H:%M'):
    value =  datetime.datetime.fromtimestamp(int(value))
    return value.strftime(format)

env.filters['datetimeformat'] = datetimeformat

def main():
    for entry in comments:
        comment = comments[entry]
        template = env.get_template('comment_template.html')
        rendered_template = template.render(comments=comment)
        entry_out = os.path.join(output_path, entry)
        if not os.path.exists(entry_out):
            os.makedirs(entry_out)

        with open(os.path.join(entry_out, 'comments.html'), 'w') as f:
            f.write(rendered_template)

