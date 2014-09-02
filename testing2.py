__author__ = 'zwhitman'

from Tkinter import *
import arcpy

master = Tk()

variable = StringVar(master)
variable.set("Choose Variable")

featureclass="C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Florida_03c6249c_ac3a_41df_b644_850fd218db39\\Florida_66254c14_0e61_441d_ad4a_d558090baa4e.shp"

field_names=[]

fieldList=arcpy.ListFields(featureclass)
for field in fieldList:
    field_names.append(field.name)
    field_names2 = field_names
print fieldList
print field_names
w = OptionMenu(master, variable, *field_names2)
w.pack()

def varOK():
    print variable.get()

button = Button(master, text="OK", command=varOK)
button.pack()

mainloop()



