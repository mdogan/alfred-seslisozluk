#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, web, ICON_INFO, ICON_WEB

def get_key():
    return wf.get_password('seslisozluk')

def get_data(url):
    return web.get(url).json()

def add_items(wf, data, icn):
    for datum in data['translations']:
        wf.add_item(datum['translation'], icon=icn)

def main(wf):

    apikey = wf.cached_data('apikey', get_key, max_age=3600)

    query = None

    if len(wf.args) == 1:
        query = wf.args[0]
    else:
        raise Exception("Missing arguments!")

    url = 'http://api.seslisozluk.com/?key={0}&lang_from={1}&lang_to={2}&query={3}'
    url_tr_en = url.format(apikey, 'tr', 'en', query)
    url_en_tr = url.format(apikey, 'en', 'tr', query)

    data = get_data(url_tr_en)
    add_items(wf, data, 'icons/en.png');

    data = get_data(url_en_tr)
    add_items(wf, data, 'icons/tr.png');

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
