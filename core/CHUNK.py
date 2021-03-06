#!/usr/bin/env python
# coding:utf-8
# build a chunk multiplication dictionary 
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import itertools
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, CHUNK_prefix, filextension
from lib.fun import finishprinter, finishcounter
from lib.fun import countchecker


# create the dictionary files
def get_chunk_dic(objflag, encodeflag, head, tail):
    countchecker(len(objflag))
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s%s" %
                             (CHUNK_prefix, get_buildtime(), encodeflag, filextension))
    with open(storepath, "w") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            if encodeflag == "":
                f.write(head + "".join(item) + tail + CRLF)
            else:
                f.write(operator.get(encodeflag)(head + "".join(item) + tail) + CRLF)
    finishprinter(finishcounter(storepath), storepath)
