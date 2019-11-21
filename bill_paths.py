#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:45:35 2019

@author: Rajiv
"""

from os import listdir

def get_bill_file_paths(congress):
    """Finds all paths to bill files of a given congress

    Args:
        congress: The number of the congress for which bills are wanted

    Returns:
        A list of relative paths to files containing bills data
    """
    bill_files = []
    
    # Loop over bills of the House of Representatives
    for bill_dir in listdir('bills/' + str(congress) + '/hr'):
        bill_file = 'bills/' + str(congress) + '/hr/' + bill_dir + '/data.json'
        bill_files.append(bill_file)
    
    # Loop over bills of the Senate
    for bill_dir in listdir('bills/' + str(congress) + '/s'):
        bill_file = 'bills/' + str(congress) + '/s/' + bill_dir + '/data.json'
        bill_files.append(bill_file)
    
    return bill_files