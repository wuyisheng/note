#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "hello@yeshen.org"

import os,time,commands,datetime,argparse,sys
from datetime import datetime as dt
from datetime import timedelta as timedelta

_root=os.path.abspath(os.path.join(os.path.dirname(__file__),"daily"))
_now = datetime.datetime.now()
_daily_month_dir = os.path.join(_root,"%s/%s" %(_now.year,_now.month))
_daily_file = os.path.join(_daily_month_dir,"%s.md" % _now.day)
_my_birthday = "2022/12/9"


def bash(cmd):
  (status, output) = commands.getstatusoutput(cmd)
  if (status != 0):
    print output
    raise Exception('fail to exec command:\n%s\n%s' % (cmd,os.getcwd(),))
  else:
    return output


def getAliveDays():
  d1 = dt.strptime(_my_birthday, "%Y/%m/%d")
  diff = str(_now - d1)
  return diff[:diff.find(" day")]


def ensureMonthDir():
  if not os.path.exists(_daily_month_dir):
    os.makedirs(_daily_month_dir)


def getMetaDay():
  str_now = str(_now)
  str_now = str_now[:str_now.find(" ")]
  user_name = bash("git config user.name")
  return "%s write at %s, %s days alive" % (user_name,str_now,getAliveDays())


def writeDaily():
  ensureMonthDir()
  meta_day = getMetaDay()
  if not os.path.exists(_daily_file):
    with open(_daily_file,"aw") as f:
      f.writelines("%s\n---\n\n\n" % meta_day)


def backup():
  meta_day = getMetaDay()
  bash("git add ../ && git commit -m '%s' && git push origin master" % meta_day)
  print("archiving...")


# Usage : python note.py -b false
def main():
  arg_parser = argparse.ArgumentParser(
      description='A script of make a commitment to life')
  arg_parser.add_argument(
      '-b',
      '--backup',
      help='[true] [false], [true] for default',
      action='store',
      default='true')
  args = arg_parser.parse_args(sys.argv[1:])
  os.chdir(_root)

  writeDaily()

  if args.backup == "true":
    backup()

  bash("open %s" % _daily_file)
  print("--------")
  print("yeshen: make a commitment to life.")


if __name__ == "__main__":
  main()