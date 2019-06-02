#!/usr/bin/env python
"""mapper.py"""

import sys
import re
import time
import datetime

for line in sys.stdin:
	line = line.rstrip()
	words = line.split('[')
	words = re.split(r' -0800| -0700',words[1])
	time = datetime.datetime.strptime(words[0], "%d/%b/%Y:%H:%M:%S")
	print(time.strftime('%Y-%m')+"\t1")
