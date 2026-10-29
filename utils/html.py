import json
import os
import frontmatter
from os.path import exists
from posix import listdir


def everything():
    data = {
        'articles': [],
        'issues': [],
        'columns': []
    }

    if exists('content/articles'):
        for a in listdir('content/articles'):
            with open('content/articles/' + a) as f:
                article = frontmatter.load(f)
                article.metadata['content'] = article.content
                data['articles'].append(article.metadata)


    if exists('content/issues'):
        for i in listdir('content/issues'):
            with open('content/issues/' + i) as f:
                issue = json.load(f)
                data['issues'].append(issue)
    return data
