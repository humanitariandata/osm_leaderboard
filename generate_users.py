#!/usr/bin/python

import sys, os, argparse
import pandas as pd

# take inputs from command line
parser = argparse.ArgumentParser(description='Generate user list based on changeset')
parser.add_argument('file', help='path to xxxx.json.new')

df = pd.read_json("data/benin/benin_2424.json.new")
list = pd.unique(df.user.ravel())
print list
