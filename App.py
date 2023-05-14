import tkinter as tk
import numpy

from ChartView import ChartView
from EmployeeView import EmployeeView
from ProductsView import ProductsView

class App:
    def __init__(self, manage):
        self.manage = manage

    def button_clicked(self):
        pass

    def show(self):
        root = tk.Tk()
        root.title('Manage app')
        root.geometry("1280x960")

        employee_view = EmployeeView(root,self.manage,6)
        employee_view.show()
        products_view = ProductsView(root,self.manage,6)
        products_view.show()
        chart_view = ChartView(self.manage,root,6)
        chart_view.show()




        root.mainloop()



