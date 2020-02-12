# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 07:58:48 2020

@author: raghed
"""
class cours(object):
    
    def __init__(self,code,intitule,niveau):
        self.code = code
        self.intitule = intitule
        self.set_niveau(niveau)
    
    def set_niveau(self, value):
      if value not in ('A', 'B', 'C'):
         raise ValueError()
      self.niveau = value
    
    def __repr__(self):
        return ("code:"+self.code+"\tintitule:"+self.intitule+"\tniveau: "+self.niveau)
