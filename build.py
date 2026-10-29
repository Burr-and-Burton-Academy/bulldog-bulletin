from slugify import slugify
from utils import directus, html
from utils.gen import compile_template, write_sitemap

data = html.everything()

compile_template('index', '/', data)

tags_compiled = set()
for article in data['articles']:
    compile_template(
        'article',
        f'/articles/{article['id']}',
        data, article=article
    )

    for tag in article['categories']:
        if tag not in tags_compiled:
            tags_compiled.add(tag)
            compile_template('category', f'/c/{slugify(tag)}', data,
                             tag=tag,
                             filtered_articles=[
                                article for article in data['articles']
                                if tag in article['categories']
                             ]
                             )

for issue in data['issues']:
    issue_articles = [
        article for article in data['articles']
        if
        article['issue'] is not None
        and article['issue'] == issue['id']
    ]

    compile_template(
        'issue',
        f'/issues/{issue['id']}',
        data, issue=issue, issue_articles=issue_articles
    )

write_sitemap()
