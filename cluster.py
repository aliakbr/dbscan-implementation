#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:33:13 2017

@author: aliakbar
"""

class Cluster(object):
    def __init__(self,  cluster_id):
        self.cluster_id = cluster_id
        self.members = []
    
    def add_objects(self, obj):
        self.members.append(obj)
        
    def get_members(self):
        return self.members
    
    def erase(self):
        self.members = []
    
        return None
    
    def has(self, obj):
        return obj in self.points
            
    def __str__(self):
        return "%s: %d points" % (str(self.cluster_id), len(self.members))