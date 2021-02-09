# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:13:50 2021

@author: SHREYA
"""

class Vehicle:
    def __init__(self,vtype,comp,model,vnumber):
        self.vtype = vtype
        self.comp = comp
        self.model = model
        self.vnumber = vnumber
        
class NonCommercialVehicle(Vehicle):
    def __init__(self,details):
        super().__init__(details['vtype'],details['comp'],details['model'],details['vnumber'])
        self.suitableTerrain = details['suitableTerrain']
        self.seats = details['seats']
            
class CommercialVehicle(Vehicle):
     def __init__(self,details):
        super().__init__(details['vtype'],details['comp'],details['model'],details['vnumber'])
        self.loadingCapacity = details['loadingCapacity']
        self.covered = details['covered']
        
class Person:
    def __init__(self,userid,name,UID):
        self.userid = userid
        self.name = name
        self.UID = UID
        
class Customer(Person):
    def __init__(self,customerDetails):
        super().__init__(self,customerDetails['userid'],customerDetails['name'],customerDetails['UID'])
        self.phone = customerDetails['phone']
        self.email = customerDetails['email']
        self.needType = customerDetails['needType']
        
class Driver(Person):
    def __init__(self,driverDetails):
        super().__init__(self,driverDetails['userid'],driverDetails['name'],driverDetails['UID'])
        self.phone = driverDetails['phone']
        self.forType = customerDetails['forType']
        self.DLno = customerDetails['DLno']
        
        