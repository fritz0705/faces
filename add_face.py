#!/usr/bin/env python3
# coding: utf-8

import pymongo
import argparse
import subprocess

argparser = argparse.ArgumentParser()
argparser.add_argument('files', nargs='*')
argparser.add_argument('--tag', '-t', action='append')

db = pymongo.Connection().clintonfaces

if __name__ == '__main__':
	args = argparser.parse_args()

	for file in args.files:
		number = 1
		while True:
			if db.faces.find({"number": number}).count() == 0:
				break
			number = number + 1
		obj = { "number": number, "tags": args.tag or [] }
		db.faces.save(obj)
		
		# build image
		subprocess.call(['convert', file, '-resize', '460x460^', '-gravity', 'center', '-extent', '460x460', 'faces/{0}.jpg'.format(number)])
		subprocess.call(['convert', 'faces/{0}.jpg'.format(number), '-resize', '150x150', 'thumbs/{0}.jpg'.format(number)])
