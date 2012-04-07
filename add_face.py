#!/usr/bin/env python3
# coding: utf-8

import pymongo
import argparse
import subprocess

argparser = argparse.ArgumentParser()
argparser.add_argument('file')
argparser.add_argument('--tag', '-t', action='append')

db = pymongo.Connection().clintonfaces

if __name__ == '__main__':
	args = argparser.parse_args()

	number = 1
	while True:
		if db.faces.find({"number": number}).count() == 0:
			break
		number = number + 1
	obj = { "number": number, "tags": args.tag or [] }
	db.faces.save(obj)
	
	# build image
	subprocess.call(['convert', args.file, '-resize', '600x600^', '-gravity', 'center', '-extent', '600x600', 'faces/{0}.jpg'.format(number)])
	subprocess.call(['convert', 'faces/{0}.jpg'.format(number), '-size', '150x150', 'thumbs/{0}.jpg'.format(number)])
