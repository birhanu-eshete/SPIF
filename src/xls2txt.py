#! /usr/bin/python
# -*- $Id -*-  
# -*- coding: gbk -*-
# author: dengzhifeng

import math
import sys,os
from sys import exit


def main():


        if len(sys.argv) < 2:
                return 1

        table = sys.argv[1]

        if table == "skilllv":
                cmd = "python tools/gen.py tools/skilllv.xls -m -i > skilllv.txt"
        elif table in ["tech", "jobs", "jobsancestry", "skill", "skillexp"]:
                cmd = "python tools/gen.py tools/job.xls -s %s > %s.txt" % (table, table)
        elif table in ["enemy", "enemyai", "enemybase", "enemytalk", "group"]:
                cmd = "python tools/gen.py tools/enemy.xls -s %s > %s.txt" % (table, table)
        elif table in ["itemset", "itemauto", "itemmaterial", "itemrecipe"]:
                cmd = "python tools/gen.py tools/item.xls -s %s > %s.txt" % (table, table)
        elif table in ["msg", "titlename"]:
                cmd = "python tools/gen.py tools/msg.xls -s %s > %s.txt" % (table, table)
        elif table in ["npc", "techarea"]:
                cmd = "python tools/gen.py tools/map.xls -s %s > %s.txt" % (table, table)
        else:
                cmd = "python tools/gen.py tools/other.xls -s %s > %s.txt" % (table, table)

        os.system(cmd)

if __name__=="__main__":
        main()


