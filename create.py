#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# File for creating a ramdom, proper, test file.

with open('test.log', 'w') as f:
    for x in range(100000):
        if x != 5:
            f.write("{0}\n".format(x))

