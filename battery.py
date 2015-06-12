#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# TOCOS TWE-lite DIP monitor
#
#    battery.py num
#     num is number of Tag unit
#
__author__ = 'yo'

import sys
import sqlite3

DBNAME = "/var/log/twelite/twelite.db

def getvolt(num):
    con = sqlite3.connect(DBNAME, isolation_level=None)
    c = con.execute("""SELECT batt FROM data ORDER BY id ASC;""")
    r = c.fetchall()
    con.close()

    if (num > len(r)):
        return 0
    return r.pop(num)[0]

def main(args):
    if len(args) > 0:
        num = int(args[0])
        print("volt{0:02d}.value {1}".format(num, getvolt(num)))


if __name__ == '__main__':
    main(sys.argv)
    exit(0)
