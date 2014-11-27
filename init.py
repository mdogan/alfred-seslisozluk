#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow


def main(wf):

    apikey = None

    if len(wf.args):
        apikey = wf.args[0]

    if apikey:
        wf.save_password('seslisozluk', apikey)
    else:
        try:
            wf.delete_password('seslisozluk')
        except:
            print "N/A "    

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
