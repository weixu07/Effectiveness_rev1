import sys
import pandas as pd
import pyqtgraph as pg


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from pyqtgraph import PlotWidget, plot


cutInPressure_Type30 = 80 
nomForce_Type30 = 2268

def eff_Type_30(ST):
	m = -1.7223*ST**4+6.3876*ST**3-7.1615*ST**2+2.1847*ST+29.465
	b = -147.65*ST**4+779.8*ST**3-1466.6*ST**2+1110.9*ST-319.58
	F = m*cutInPressure_Type30+b
	if F < 0:
		f_cal = 0
	elif F > nomForce_Type30:
		f_cal = nomForce_Type30
	else:
		f_cal = F

	EFF = f_cal / nomForce_Type30
	return EFF

class SecondPage(QDialog):
	def __init__(self, slackData, degreeData):
		super(SecondPage, self).__init__()
		loadUi('BrakePerform.ui', self)
		self.setWindowTitle("Brake Performance")

		self.slackData = slackData
		self.degreeData = degreeData

		# Display Stroke
		self.pushButton_1.setText(str(self.Stroke(slackData, degreeData)[0][0]))
		self.pushButton_2.setText(str(self.Stroke(slackData, degreeData)[0][1]))
		self.pushButton_3.setText(str(self.Stroke(slackData, degreeData)[0][2]))
		self.pushButton_4.setText(str(self.Stroke(slackData, degreeData)[0][3]))
		self.pushButton_5.setText(str(self.Stroke(slackData, degreeData)[0][4]))
		self.pushButton_6.setText(str(self.Stroke(slackData, degreeData)[0][5]))
		self.pushButton_7.setText(str(self.Stroke(slackData, degreeData)[0][6]))
		self.pushButton_8.setText(str(self.Stroke(slackData, degreeData)[0][7]))
		self.pushButton_9.setText(str(self.Stroke(slackData, degreeData)[0][8]))
		self.pushButton_10.setText(str(self.Stroke(slackData, degreeData)[0][9]))
		# Display Stroke Chart

		self.pushButton_10.clicked.connect(self.PlotStroke_59)
		self.pushButton_9.clicked.connect(self.PlotStroke_57)


		# Display Effectiveness
		self.label_1.setText(str(self.Stroke(slackData, degreeData)[1][0]))
		self.label_2.setText(str(self.Stroke(slackData, degreeData)[1][1]))
		self.label_3.setText(str(self.Stroke(slackData, degreeData)[1][2]))
		self.label_4.setText(str(self.Stroke(slackData, degreeData)[1][3]))
		self.label_5.setText(str(self.Stroke(slackData, degreeData)[1][4]))
		self.label_6.setText(str(self.Stroke(slackData, degreeData)[1][5]))
		self.label_7.setText(str(self.Stroke(slackData, degreeData)[1][6]))
		self.label_8.setText(str(self.Stroke(slackData, degreeData)[1][7]))
		self.label_9.setText(str(self.Stroke(slackData, degreeData)[1][8]))
		self.label_10.setText(str(self.Stroke(slackData, degreeData)[1][9]))

	def Stroke(self, slackData, degreeData):
		if slackData[0] == "":
			stroke_17 = 'NA'
			effectiveness_17 = 'NA'
		else:
			stroke_17 = round(float(slackData[0]) * degreeData[0].max(axis=1).max(), 3)
			effectiveness_17 = str(round(eff_Type_30(stroke_17)*100, 2))+'%'
		if slackData[1] == "":
			stroke_19 = 'NA'
			effectiveness_19 = 'NA'
		else:
			stroke_19 = round(float(slackData[1]) * degreeData[1].max(axis=1).max(), 3) 
			effectiveness_19 = str(round(eff_Type_30(stroke_19)*100, 2))+'%'
		if slackData[2]  == "":
			stroke_27 = 'NA'
			effectiveness_27 = 'NA'
		else:
			stroke_27 = round(float(slackData[2]) * degreeData[2].max(axis=1).max(), 3)
			effectiveness_27 = str(round(eff_Type_30(stroke_27)*100, 2))+'%'
		if slackData[3] == "":
			stroke_29 = 'NA'
			effectiveness_29 = 'NA'
		else:
			stroke_29 = round(float(slackData[3]) * degreeData[3].max(axis=1).max(), 3) 
			effectiveness_29 = str(round(eff_Type_30(stroke_29)*100, 2))+'%'
		if slackData[4] == "":
			stroke_37 = 'NA'
			effectiveness_37 = 'NA'
		else:	
			stroke_37 = round(float(slackData[4]) * degreeData[4].max(axis=1).max(), 3)
			effectiveness_37 = str(round(eff_Type_30(stroke_37)*100, 2))+'%'
		if slackData[5] == "":
			stroke_39 = 'NA'
			effectiveness_39 = 'NA'
		else:
			stroke_39 = round(float(slackData[5]) * degreeData[5].max(axis=1).max(), 3) 
			effectiveness_39 = str(round(eff_Type_30(stroke_39)*100, 2))+'%'
		if slackData[6] == "":
			stroke_47 = 'NA'
			effectiveness_47 = 'NA'
		else:
			stroke_47 = round(float(slackData[6]) * degreeData[6].max(axis=1).max(), 3)
			effectiveness_47 = str(round(eff_Type_30(stroke_47)*100, 2))+'%'
		if slackData[7] == "":
			stroke_49 = 'NA'
			effectiveness_49 = 'NA'
		else:
			stroke_49 = round(float(slackData[7]) * degreeData[7].max(axis=1).max(), 3)
			effectiveness_49 = str(round(eff_Type_30(stroke_49)*100, 2))+'%'
		if slackData[8] == "":
			stroke_57 = 'NA'
			effectiveness_57 = 'NA'
		else:
			stroke_57 = round(float(slackData[8]) * degreeData[8].max(axis=1).max(), 3)
			effectiveness_57 = str(round(eff_Type_30(stroke_57)*100, 2))+'%'
		if slackData[9] == "":
			stroke_59 = 'NA'
			effectiveness_59 = 'NA'
		else:
			stroke_59 = round(float(slackData[9]) * degreeData[9].max(axis=1).max(),3) 
			effectiveness_59 = str(round(eff_Type_30(stroke_59)*100, 2))+'%'
		
		strokeData = [stroke_17,stroke_19,stroke_27,stroke_29,stroke_37,stroke_39,stroke_47,stroke_49,stroke_57,stroke_59]
		effectivenessData = [effectiveness_17,effectiveness_19,effectiveness_27,effectiveness_29,effectiveness_37,effectiveness_39,effectiveness_47,effectiveness_49,effectiveness_57,effectiveness_59]
		
		Data = [strokeData,effectivenessData]
		
		return Data

	def PlotStroke_59(self):
		slackData = self.slackData
		degreeData = self.degreeData
		distance_59 = round(float(slackData[9]) * degreeData[9],3) 
		pen = pg.mkPen(color=(255, 0, 0))
		self.graphWidget.plot(list(range(0, len(distance_59))), distance_59.iloc[:,0], name="stroke_59", pen=pen)
		self.graphWidget.setLabel('left', 'Stroke (inches)', color='white', size=35)
		self.graphWidget.setYRange(0, 5, padding=0)

		self.label_11.setStyleSheet('background-color: rgb(255, 0, 0)')

	def PlotStroke_57(self):
		slackData = self.slackData
		degreeData = self.degreeData
		distance_57 = round(float(slackData[8]) * degreeData[8],3) 
		pen = pg.mkPen(color=(0, 0, 255))
		self.graphWidget.plot(list(range(0, len(distance_57))), distance_57.iloc[:,0], name="stroke_57", pen=pen)
		self.graphWidget.setLabel('left', 'Stroke (inches)', color='white', size=35)
		self.graphWidget.setYRange(0, 5, padding=0)

		self.label_12.setStyleSheet('background-color: rgb(0, 0, 255)')





# import wheelNum

# app = QApplication(sys.argv)
# widget = SecondPage()
# widget.setWindowTitle('Brake Performance')
# widget.show()
# sys.exit(app.exec_())