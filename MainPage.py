import sys
import pandas as pd
import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi

from SecondPage import SecondPage
from ThirdPage import ThirdPage


### Brake Constants ###
chamberSize = ["9","12","16","16LS","20","20LS","24","24L","24LS","30","30LS","36"]
slackAdjuster = ["5","5.5","6","6.5","7"]

### DAQ Constants ###
ServiceOff_V = 2.3

ch_17 = 2                                   #channel number for degree_ST_17
ch_19 = 2                                   #channel number for degree_ST_19
ch_27 = 2                                   #channel number for degree_ST_27
ch_29 = 2                                   #channel number for degree_ST_29
ch_37 = 2                                   #channel number for degree_ST_37
ch_39 = 2                                   #channel number for degree_ST_39
ch_47 = 2                                   #channel number for degree_ST_47
ch_49 = 2                                   #channel number for degree_ST_49
ch_57 = 2                                   #channel number for degree_ST_57
ch_59 = 3                                   #channel number for degree_ST_59


class MainPage(QDialog):
	def __init__(self):
		super(MainPage, self).__init__()
		loadUi('BrakeChar.ui', self)


        # initiate Chamber size & Slack adjuster
		self.checkBox_1.stateChanged.connect(self.change_state_1)
		self.checkBox_2.stateChanged.connect(self.change_state_2)
		self.checkBox_3.stateChanged.connect(self.change_state_3)
		self.checkBox_4.stateChanged.connect(self.change_state_4)
		self.checkBox_5.stateChanged.connect(self.change_state_5)
		self.checkBox_6.stateChanged.connect(self.change_state_6)
		self.checkBox_7.stateChanged.connect(self.change_state_7)
		self.checkBox_8.stateChanged.connect(self.change_state_8)
		self.checkBox_9.stateChanged.connect(self.change_state_9)
		self.checkBox_10.stateChanged.connect(self.change_state_10)
		
		# calcuate
		self.pushButton.setEnabled(False)
		self.pushButton.clicked.connect(self.saveCalculate)

		# import CSV button
		self.pushButton_3.clicked.connect(self.getCSV)
		self.df = pd.DataFrame()

		#show chamber force data
		self.comboBox.addItems(chamberSize)
		self.pushButton_2.clicked.connect(self.showChamberForceData)
	
	def getCSV(self):
		filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV", "encoder_data","CSV(*.csv)")
		if filePath:
			self.df = pd.read_csv(str(filePath))
			self.pushButton.setEnabled(True)
		
	def showChamberForceData(self, chamber):
		chamber = self.comboBox.currentText()
		theclass = ThirdPage(chamber)
		theclass.exec_()

	def saveCalculate(self, slackData):
		# Pop BrakePerform UI & calculate Stroke
		
		slackData_17 = self.comboBox_2.currentText()   # slack adjuster length
		slackData_19 = self.comboBox_4.currentText()
		slackData_27 = self.comboBox_6.currentText()
		slackData_29 = self.comboBox_8.currentText()
		slackData_37 = self.comboBox_10.currentText()
		slackData_39 = self.comboBox_12.currentText()
		slackData_47 = self.comboBox_14.currentText()
		slackData_49 = self.comboBox_16.currentText()
		slackData_57 = self.comboBox_18.currentText()
		slackData_59 = self.comboBox_20.currentText()

		degree_ST_17 = (abs((self.df.iloc[:,[ch_17]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_19 = (abs((self.df.iloc[:,[ch_19]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_27 = (abs((self.df.iloc[:,[ch_27]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_29 = (abs((self.df.iloc[:,[ch_29]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_37 = (abs((self.df.iloc[:,[ch_37]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_39 = (abs((self.df.iloc[:,[ch_39]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_47 = (abs((self.df.iloc[:,[ch_47]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_49 = (abs((self.df.iloc[:,[ch_49]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_57 = (abs((self.df.iloc[:,[ch_57]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel x for encoder_data
		degree_ST_59 = (abs((self.df.iloc[:,[ch_59]] - ServiceOff_V) *36/180*math.pi)).astype(float)  # Channel 2 for encoder_data, only current one

		degreeData = [degree_ST_17,degree_ST_19,degree_ST_27,degree_ST_29,degree_ST_37,degree_ST_39,degree_ST_47,degree_ST_49,degree_ST_57,degree_ST_59]
		slackData = [slackData_17,slackData_19,slackData_27,slackData_29,slackData_37,slackData_39,slackData_47,slackData_49,slackData_57,slackData_59]

		theclass = SecondPage(slackData,degreeData)
		theclass.exec_()
		
	def change_state_1(self, state):
		if state == Qt.Checked:
			self.comboBox_1.addItems(chamberSize)
			self.comboBox_2.addItems(slackAdjuster)
		else:
			self.comboBox_1.clear()
			self.comboBox_2.clear()
	def change_state_2(self, state):
		if state == Qt.Checked:
			self.comboBox_3.addItems(chamberSize)
			self.comboBox_4.addItems(slackAdjuster)
		else:
			self.comboBox_3.clear()
			self.comboBox_4.clear()
	def change_state_3(self, state):
		if state == Qt.Checked:
			self.comboBox_5.addItems(chamberSize)
			self.comboBox_6.addItems(slackAdjuster)
		else:
			self.comboBox_5.clear()
			self.comboBox_6.clear()
	def change_state_4(self, state):
		if state == Qt.Checked:
			self.comboBox_7.addItems(chamberSize)
			self.comboBox_8.addItems(slackAdjuster)
		else:
			self.comboBox_7.clear()
			self.comboBox_8.clear()
	def change_state_5(self, state):
		if state == Qt.Checked:
			self.comboBox_9.addItems(chamberSize)
			self.comboBox_10.addItems(slackAdjuster)
		else:
			self.comboBox_9.clear()
			self.comboBox_10.clear()
	def change_state_6(self, state):
		if state == Qt.Checked:
			self.comboBox_11.addItems(chamberSize)
			self.comboBox_12.addItems(slackAdjuster)
		else:
			self.comboBox_11.clear()
			self.comboBox_12.clear()
	def change_state_7(self, state):
		if state == Qt.Checked:
			self.comboBox_13.addItems(chamberSize)
			self.comboBox_14.addItems(slackAdjuster)
		else:
			self.comboBox_13.clear()
			self.comboBox_14.clear()
	def change_state_8(self, state):
		if state == Qt.Checked:
			self.comboBox_15.addItems(chamberSize)
			self.comboBox_16.addItems(slackAdjuster)
		else:
			self.comboBox_15.clear()
			self.comboBox_16.clear()
	def change_state_9(self, state):
		if state == Qt.Checked:
			self.comboBox_17.addItems(chamberSize)
			self.comboBox_18.addItems(slackAdjuster)
		else:
			self.comboBox_17.clear()
			self.comboBox_18.clear()
	def change_state_10(self, state):
		if state == Qt.Checked:
			self.comboBox_19.addItems(chamberSize)
			self.comboBox_20.addItems(slackAdjuster)
		else:
			self.comboBox_19.clear()
			self.comboBox_20.clear()

import wheelNum

app = QApplication(sys.argv)
widget = MainPage()
widget.setWindowTitle('Brake Configurations')
widget.show()
sys.exit(app.exec_())