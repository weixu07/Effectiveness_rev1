import sys
import csv
import os.path
import pyqtgraph as pg
import numpy as np

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

from pyqtgraph import PlotWidget, plot

# chamber size data location
path = "chamber_data\\"


def polyfit(x, y, degree):
    #results = {}
    # polynomial coefficients
    m,b = np.polyfit(x, y, degree)
    # r-squared
    p = np.poly1d([m,b])
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    r = ssreg / sstot

    return r, m, b

def polyfit2(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()
    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results


class ThirdPage(QDialog):
	def __init__(self, chamber):
		super(ThirdPage, self).__init__()
		loadUi('ChamberForce.ui', self)
		self.setWindowTitle("Chamber Force")

        # pass chamber number
		self.chamber = chamber

		self.open_plotFile()
		self.open_plotFile2()

		self.label_2.setText(str(1))
		self.horizontalScrollBar.setMinimum(1)
		self.horizontalScrollBar.setMaximum(7)
		self.horizontalScrollBar.setValue(1)
		self.horizontalScrollBar.valueChanged.connect(self.changeOrder)
	
		self.label_6.setText(str(1))
		self.horizontalScrollBar_2.setMinimum(1)
		self.horizontalScrollBar_2.setMaximum(7)
		self.horizontalScrollBar_2.setValue(1)
		self.horizontalScrollBar_2.valueChanged.connect(self.changeOrder2)
		
		self.horizontalScrollBar.valueChanged.connect(self.open_plotFile3)
		self.horizontalScrollBar_2.valueChanged.connect(self.open_plotFile3)

	def plot(self, stroke, force, plotname, color):
		pen = pg.mkPen(color=color)
		self.graphWidget.plot(stroke, force, name=plotname, pen=pen)
		self.graphWidget.setLabel('left', 'Force (lbs)', color='white', size=30)
		self.graphWidget.setLabel('bottom', 'Stroke (inches)', color='white', size=30)

		self.graphWidget.setXRange(0.5, 3.5, padding=0)
		self.graphWidget.setYRange(0, 4500, padding=0)

	def plot2(self, pressure, force, plotname, color):
		pen = pg.mkPen(color=color)
		self.graphWidget_2.plot(pressure, force, name=plotname, pen=pen, symbol='+', symbolBrush=(color))
		
		self.graphWidget_2.setLabel('left', 'Force (lbs)', color='white', size=30)
		self.graphWidget_2.setLabel('bottom', 'Pressure (psi)', color='white', size=30)

		self.graphWidget_2.setXRange(0.5, 3.5, padding=0)
		self.graphWidget_2.setYRange(0, 4500, padding=0)	

	def plot3(self, x, y, color1, x_fit, y_fit, color2):
		self.graphWidget_3.clear()
		pen1 = pg.mkPen(color1)
		self.graphWidget_3.plot(x, y, pen=pen1, sysmbol='o', symbolBrush=(color1))
		pen2 = pg.mkPen(color = color2)
		self.graphWidget_3.plot(x_fit, y_fit, pen=pen2)
		self.graphWidget_3.setXRange(0.0, 3.5, padding=0)

	def plot4(self, x, y, color1, x_fit, y_fit, color2):
		self.graphWidget_4.clear()
		pen1 = pg.mkPen(color1)
		self.graphWidget_4.plot(x, y, pen=pen1, sysmbol='o', symbolBrush=(color1))
		pen2 = pg.mkPen(color = color2)
		self.graphWidget_4.plot(x_fit, y_fit, pen=pen2)
		self.graphWidget_4.setXRange(0.0, 3.5, padding=0)
		self.graphWidget_4.setLabel('bottom', 'Stroke (inches)', color='white', size=30)
	
	def changeOrder(self):
		order = self.horizontalScrollBar.value()
		self.label_2.setText(str(order))


	def changeOrder2(self):
		order = self.horizontalScrollBar_2.value()
		self.label_6.setText(str(order))


	def open_plotFile(self):

		data_file = self.chamber + ".csv"
		file_to_open = os.path.join(path + data_file)
		with open(file_to_open) as csv_file:
			self.tableWidget.setRowCount(0)
			self.tableWidget.setColumnCount(10)
			open_file = csv.reader(csv_file, delimiter=',', quotechar='|')
			strokes = []
			psi_10 = []
			psi_20 = []
			psi_30 = []
			psi_40 = []
			psi_50 = []
			psi_60 = []
			psi_70 = []
			psi_80 = []
			psi_90 = []
			psi_100 = []
			psi_110 = []

			for row_data in open_file:
				row = self.tableWidget.rowCount()
				self.tableWidget.insertRow(row)
				if len(row_data) > 10:
					self.tableWidget.setColumnCount(len(row_data))
				for column, stuff in enumerate(row_data):
					item = QTableWidgetItem(stuff)
					self.tableWidget.setItem(row, column, item)

				strokes.append(float(row_data[0]))
				psi_10.append(float(row_data[1]))
				psi_20.append(float(row_data[2]))
				psi_30.append(float(row_data[3]))
				psi_40.append(float(row_data[4]))
				psi_50.append(float(row_data[5]))
				psi_60.append(float(row_data[6]))
				psi_70.append(float(row_data[7]))
				psi_80.append(float(row_data[8]))
				psi_90.append(float(row_data[9]))
				psi_100.append(float(row_data[10]))
				psi_110.append(float(row_data[11]))

			self.tableWidget.setHorizontalHeaderLabels(['Stroke','10','20', '30','40','50','60','70','80','90','100','110','Normal','Legal'])
			self.tableWidget.resizeColumnsToContents()
			self.tableWidget.resizeRowsToContents()

			self.plot(strokes, psi_10, '10psi', 'r')
			self.plot(strokes, psi_20, '20psi', 'r')
			self.plot(strokes, psi_30, '30psi', 'r')
			self.plot(strokes, psi_40, '40psi', 'r')
			self.plot(strokes, psi_50, '50psi', 'r')
			self.plot(strokes, psi_60, '60psi', 'b')
			self.plot(strokes, psi_70, '70psi', 'b')
			self.plot(strokes, psi_80, '80psi', 'b')
			self.plot(strokes, psi_90, '90psi', 'g')
			self.plot(strokes, psi_100, '100psi', 'g')
			self.plot(strokes, psi_110, '110psi', 'g')

	def open_plotFile2(self):
		self.check_change = False
		data_file = self.chamber + ".csv"
		file_to_open = os.path.join(path + data_file)
		pressure = [10,20,30,40,50,60,70,80,90,100,110]
		with open(file_to_open) as csv_file:	
			self.tableWidget_2.setRowCount(10)
			self.tableWidget_2.setColumnCount(0)
			open_file = csv.reader(csv_file, delimiter=',', quotechar='|')
			matrix_data = []
			strokes = []
			psi_10 = []
			psi_20 = []
			psi_30 = []
			psi_40 = []
			psi_50 = []
			psi_60 = []
			psi_70 = []
			psi_80 = []
			psi_90 = []
			psi_100 = []
			psi_110 = []
			for row_data in open_file:
				strokes.append(float(row_data[0]))
				psi_10.append(float(row_data[1]))
				psi_20.append(float(row_data[2]))
				psi_30.append(float(row_data[3]))
				psi_40.append(float(row_data[4]))
				psi_50.append(float(row_data[5]))
				psi_60.append(float(row_data[6]))
				psi_70.append(float(row_data[7]))
				psi_80.append(float(row_data[8]))
				psi_90.append(float(row_data[9]))
				psi_100.append(float(row_data[10]))
				psi_110.append(float(row_data[11]))
			matrix_data = [strokes,psi_10,psi_20,psi_30,psi_40,psi_50,psi_60,psi_70,psi_80,psi_90,psi_100,psi_110]
			matrix_data_trans = np.transpose(matrix_data)
			list_data_trans = matrix_data_trans.tolist()

			#print(list_data_trans)	

			for column_data in list_data_trans:
				column = self.tableWidget_2.columnCount()
				self.tableWidget_2.insertColumn(column)
				if len(column_data) > 10:
					self.tableWidget_2.setRowCount(len(column_data))
				for row, stuff in enumerate(column_data):
					item = QTableWidgetItem(str(stuff))
					self.tableWidget_2.setItem(row, column, item)

			self.tableWidget_2.setVerticalHeaderLabels(['Stroke','10','20', '30','40','50','60','70','80','90','100','110'])
			self.tableWidget_2.resizeColumnsToContents()
			self.tableWidget_2.resizeRowsToContents()

		self.plot2(pressure, matrix_data_trans[0][1:len(matrix_data_trans)], "0.5", 'g')
		self.plot2(pressure, matrix_data_trans[1][1:len(matrix_data_trans)], "1", 'g')
		self.plot2(pressure, matrix_data_trans[2][1:len(matrix_data_trans)], "1.125", 'g')
		self.plot2(pressure, matrix_data_trans[3][1:len(matrix_data_trans)], "1.25", 'g')
		self.plot2(pressure, matrix_data_trans[4][1:len(matrix_data_trans)], "1.375", 'g')
		self.plot2(pressure, matrix_data_trans[5][1:len(matrix_data_trans)], "1.5", 'b')
		self.plot2(pressure, matrix_data_trans[6][1:len(matrix_data_trans)], "1.625", 'b')
		self.plot2(pressure, matrix_data_trans[7][1:len(matrix_data_trans)], "1.75", 'b')
		self.plot2(pressure, matrix_data_trans[8][1:len(matrix_data_trans)], "1.875", 'r')
		self.plot2(pressure, matrix_data_trans[9][1:len(matrix_data_trans)], "2", 'r')
		self.plot2(pressure, matrix_data_trans[10][1:len(matrix_data_trans)], "2.125", 'r')
		self.plot2(pressure, matrix_data_trans[11][1:len(matrix_data_trans)], "2.25", 'r')
		self.plot2(pressure, matrix_data_trans[12][1:len(matrix_data_trans)], "2.375", 'r')
		self.plot2(pressure, matrix_data_trans[13][1:len(matrix_data_trans)], "2.5", 'r')
		self.plot2(pressure, matrix_data_trans[14][1:len(matrix_data_trans)], "2.625", 'r')

			# linear fit 
		R = []; M = []; B = []
		for i in range(15):
			r, m,b = polyfit(pressure,matrix_data_trans[i][1:len(matrix_data_trans)], 1)
			R.append(round(r,3))
			M.append(round(m,3))
			B.append(round(b,3))

		linear_fit = [R, M, B]

		for row_data in linear_fit:
			row = self.tableWidget_3.rowCount()
			self.tableWidget_3.insertRow(row)
			if len(row_data) > 10:
				self.tableWidget_3.setColumnCount(len(row_data))
			for column, stuff in enumerate(row_data):
				item = QTableWidgetItem(str(stuff))
				self.tableWidget_3.setItem(row, column, item)
		self.tableWidget_3.setVerticalHeaderLabels(['R2','m','b'])
		self.tableWidget_3.resizeColumnsToContents()
		self.tableWidget_3.resizeRowsToContents()		

		self.check_change = True

	def open_plotFile3(self):
		self.check_change = False
		data_file = self.chamber + ".csv"
		file_to_open = os.path.join(path + data_file)
		pressure = [10,20,30,40,50,60,70,80,90,100,110]
		#Stroke = [0.5,1,1.125,1.25,1.375,1.5,1.625,1.75,1.875,2,2.125,2.25,2.375,2.5,2.625]
		
		with open(file_to_open) as csv_file:	
			open_file = csv.reader(csv_file, delimiter=',', quotechar='|')
			matrix_data = []
			strokes = []
			psi_10 = []
			psi_20 = []
			psi_30 = []
			psi_40 = []
			psi_50 = []
			psi_60 = []
			psi_70 = []
			psi_80 = []
			psi_90 = []
			psi_100 = []
			psi_110 = []
			for row_data in open_file:
				strokes.append(float(row_data[0]))
				psi_10.append(float(row_data[1]))
				psi_20.append(float(row_data[2]))
				psi_30.append(float(row_data[3]))
				psi_40.append(float(row_data[4]))
				psi_50.append(float(row_data[5]))
				psi_60.append(float(row_data[6]))
				psi_70.append(float(row_data[7]))
				psi_80.append(float(row_data[8]))
				psi_90.append(float(row_data[9]))
				psi_100.append(float(row_data[10]))
				psi_110.append(float(row_data[11]))
			matrix_data = [strokes,psi_10,psi_20,psi_30,psi_40,psi_50,psi_60,psi_70,psi_80,psi_90,psi_100,psi_110]
			matrix_data_trans = np.transpose(matrix_data)
			
			# linear fit 
		R = []; M = []; B = []
		for i in range(15):
			r, m,b = polyfit(pressure,matrix_data_trans[i][1:len(matrix_data_trans)], 1)
			R.append(round(r,4))
			M.append(round(m,4))
			B.append(round(b,4))

		# masked the zero 
		stroke_array = np.array(strokes)
		M_array = np.array(M)
		B_array = np.array(B)

		M = M_array[M_array !=0.0]
		B = B_array[B_array !=0.0]
		Stroke = stroke_array[:len(M)]

		 # Get order number from Scroll
		m_order = self.horizontalScrollBar.value()
		b_order = self.horizontalScrollBar_2.value()

		# Coefficients 
		M_coef = polyfit2(Stroke, M, m_order)
		B_coef = polyfit2(Stroke, B, b_order)

		# Polynomial
		M_poly = np.poly1d(M_coef['polynomial'])
		B_poly = np.poly1d(B_coef['polynomial'])

		new_stroke = np.arange(0.5, 3.6, 0.1)

		new_M = M_poly(new_stroke)
		new_B = B_poly(new_stroke)

		# Plot polynomial

		self.plot3(Stroke, M, 'r', new_stroke, new_M, 'w') 
		self.plot4(Stroke, B, 'r', new_stroke, new_B, 'w') 

		# Tabulate coefficients

		self.tableWidget_4.setColumnCount(1)
		self.tableWidget_4.setRowCount(len(M_coef['polynomial']))
		for i in range(len(M_coef['polynomial'])):
			item = QTableWidgetItem(str(round(M_coef['polynomial'][i],3)))
			self.tableWidget_4.setItem(i,0, item)
		self.tableWidget_4.setHorizontalHeaderLabels(['Coefficients'])
		self.tableWidget_4.resizeRowsToContents()
		self.label_4.setText(str(round(M_coef['determination'],3)))

		self.tableWidget_5.setColumnCount(1)
		self.tableWidget_5.setRowCount(len(B_coef['polynomial']))
		for j in range(len(B_coef['polynomial'])):
			item2 = QTableWidgetItem(str(round(B_coef['polynomial'][j],3)))
			self.tableWidget_5.setItem(j,0, item2)
		self.tableWidget_5.setHorizontalHeaderLabels(['Coefficients'])
		self.tableWidget_5.resizeRowsToContents()
		self.label_8.setText(str(round(B_coef['determination'],3)))


