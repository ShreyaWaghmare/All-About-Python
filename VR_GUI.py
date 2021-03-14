# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:04:28 2021

@author: SHREYA
"""

#basic
import tkinter as tk # thin layer tcl/tk
from tkinter import Menu
from tkinter import ttk
from functools import partial  
import json

#import VehicleRental

global vehicle_data
vehicle_data = {0: {'vtype': 'a', 'vprice': 's', 'vmodel': 'd', 'vnumber': 'f'},1: {'vtype': 'w', 'vprice': 'w', 'vmodel': 'd', 'vnumber': 'f'}}

def dump_data(v_data):
   fp = open('data.json','w')
   json.dump(v_data,fp)
   
def read_data():
    with open('data.json') as fp:
        v_data = json.load(fp)
    return v_data


#basic
win = tk.Tk()

#basic
win.title('Vehicle Rental')

def _quit():
    win.quit()
    win.destroy()
    exit()
    
def get_current_size():
    win.update()
    print('width ',win.winfo_width())
    print('height ',win.winfo_height())
    win.minsize(width=300,height=300) #1 is default ie 200
    win.update()
    print('width ',win.winfo_width())
    print('height ',win.winfo_height())
    win.resizable(0,0)
    
def register_vehicle(details):
    print('!!!!!!!!to register!!!')
    vehicle_data = read_data()
    vehicle = {}
    vehicle['vtype'] = details[0].get()
    vehicle['vprice'] = details[1].get()
    vehicle['vmodel'] = details[2].get()
    vehicle['vnumber'] = details[3].get()
    vehicle_data[len(vehicle_data)] = vehicle
    print(vehicle_data)
    dump_data(vehicle_data)

#setting tab 2
def rent_vehicle():
    def action(event):
        select = selectVehicle.get()
        #print ('selected vtype :', select)
        details = [list(v.values()) for v in read_data().values() if v['vtype'] == select][0]
        #print(details)
        ttk.Label(rent_frame,text="Price:").grid(column=0,row=1,sticky="E")
        ttk.Label(rent_frame,text=details[1],width=12).grid(column=1,row=1,sticky="W")
        
        ttk.Label(rent_frame,text="Model:").grid(column=0,row=2,sticky="E")
        ttk.Label(rent_frame,text=details[2]).grid(column=1,row=2,sticky="W")
    
        ttk.Label(rent_frame,text="Vehicle Number:").grid(column=0,row=3,sticky="E")
        ttk.Label(rent_frame,text=details[3]).grid(column=1,row=3,sticky="W")
    
    rent_frame = ttk.LabelFrame(tab2,text="Pick a vehicle to rent")
    rent_frame.grid(column=0,row=0,padx=8,pady=4)
    
    ttk.Label(rent_frame,text="Vehicle Type:").grid(column=0,row=0,sticky="E")
    vehicle = tk.StringVar()
    selectVehicle = ttk.Combobox(rent_frame,width=12,textvariable=vehicle)
    selectVehicle.bind('<<ComboboxSelected>>', action)
    print('--->',read_data())
    selectVehicle['values'] = [v['vtype'] for v in read_data().values()]
    selectVehicle.grid(column=1,row=0)
    selectVehicle.current(0)
    max_width = max(len(v) for v in selectVehicle['values'])
    selectVehicle.config(width=max_width)
    
    #looping and adding padding
    for child in rent_frame.winfo_children():
        child.grid_configure(padx=4,pady=4)
 
#menu
menuBar = Menu()
win.config(menu = menuBar)

#cascading menu
fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Create")
fileMenu.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="User Account",menu=fileMenu)

#setting up tab control
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text="Register")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text="Rent")
tabControl.pack(expand=1,fill="both")

#setting tab 1
register_frame = ttk.LabelFrame(tab1,text="Register your vehicle here for renting")
register_frame.grid(column=0,row=0,padx=8,pady=4)

vtype = tk.StringVar()
ttk.Label(register_frame,text="Vehicle Type:").grid(column=0,row=0,sticky="E")
entry_vtype = tk.Entry(register_frame, textvariable=vtype).grid(column=1,row=0)  

vprice = tk.StringVar()  
ttk.Label(register_frame,text="Price:").grid(column=0,row=1,sticky="E")
entry_vprice = tk.Entry(register_frame, textvariable=vprice).grid(column=1,row=1) 

vmodel = tk.StringVar()
ttk.Label(register_frame,text="Model:").grid(column=0,row=2,sticky="E") 
entry_vmodel = tk.Entry(register_frame, textvariable=vmodel).grid(column=1,row=2)

vnumber = tk.StringVar()
ttk.Label(register_frame,text="Vehicle Number:").grid(column=0,row=3,sticky="E")
entry_vmodel = tk.Entry(register_frame, textvariable=vnumber).grid(column=1,row=3)

register_vehicle = partial(register_vehicle, [vtype,vprice,vmodel,vnumber])  
buttonReg = tk.Button(register_frame, text="Register", command=register_vehicle).grid(column=0,row=4) 

rent_vehicle = partial(rent_vehicle)  
buttonRent = tk.Button(register_frame, text="Rent", command=rent_vehicle).grid(column=1,row=4) 

#looping and adding padding
for child in register_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)







get_current_size()

#basic
win.mainloop()
