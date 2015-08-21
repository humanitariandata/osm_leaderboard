#!/usr/bin/python

import sys, os, argparse
import pandas as pd

# take inputs from command line
parser = argparse.ArgumentParser(description='Generate user list based on changeset')
parser.add_argument('file', help='path to xxxx.json.new')

args = parser.parse_args()

file = args.file

df = pd.read_json(file)
list = pd.unique(df.user.ravel())
print list
