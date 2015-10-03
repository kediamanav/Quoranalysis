from __future__ import print_function
from bs4 import BeautifulSoup
import os

num = 0

for filename in os.listdir('../Quora_user_logs/'):
    num += 1
    print('processing file num ' + str(num) + ': ' + filename)

    html_doc = open('../Quora_user_logs/' + filename)
    html = html_doc.read()
    out_file = open('../answer_links/' + filename, 'w')

    soup = BeautifulSoup(html, 'html.parser')

    for item in soup.findAll('div', {'class': 'feed_item_activity'}):
        if item.text == 'Answer added.':
            print('https://www.quora.com' + item.parent.parent.strong.span.a['href'] + '/answer/' + filename.split('.')[0], file=out_file)

    out_file.close()
    html_doc.close()
