#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:58:14 2017

@author: aliakbar
"""
class DBScan(object):
    def __init__(self,  epsilon, minpts, data, distance_metric):
        self.data = data
        self.epsilon = epsilon
        self.minpts = minpts
        self.distance_metric = distance_metric
    
    