import math
import os
import random
import re
import sys


n = int(input())
print('Weird') if n%2!=0 or (n%2==0 and n in range(6,21)) else print('Not Weird')