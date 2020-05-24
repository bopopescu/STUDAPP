# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STUD.ui'
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from tkinter import messagebox as tkMessageBox



from PyQt5 import QtCore, QtGui, QtWidgets
try: 
    mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
    mycursor=mydb.cursor()        
except Exception:
    tkMessageBox.showerror('connection failed ') 


class Ui_Form(object):
    
    def male(self):
        self.sex='male'

    def female(self):
        self.sex='female'
    
    def showdetails(self):
        mycursor.execute('select * from student')
        dbresponse=mycursor.fetchall()
        rows=''
        self.listWidget.clear()
        for a in dbresponse:
            for j in a:
                temp2=str(j)
                rows=rows+temp2+' ,'
            rows=rows.rstrip(' ,')
            rows='('+rows+')'
            self.listWidget.addItem(rows)
            rows=''
    
    def Addstudent(self):
        name=self.txtname.text()
        rollno=self.txtroll.text()
        marks=self.txtmarks.text()
        sex=self.sex
        age=self.spinBox.value()
        print(name)
        print(name)
        insquery='insert into student values(%s,%s,%s,%s,%s)'
        values=(name,rollno,marks,age,sex)
        mycursor.execute(insquery,values)
        mydb.commit()
        result='student '+ name + ' is successfully added to DB'
        self.listWidget.clear()
        self.listWidget.addItem(result)
        query='select * from student where roll={}'.format(rollno) 
        mycursor.execute(query)
        dbresponse=mycursor.fetchall()
        result=''
        for a in dbresponse:
            for j in a:
                temp2=str(j)
                result=result+temp2+' ,'
            result=result.rstrip(' ,')
            result='('+result+')'
    
        self.listWidget.addItem(result)

    def delstudent(self):
        rollno=self.txtroll.text()
        delquery='delete from student where roll={}'.format(rollno)
        mycursor.execute(delquery)
        mydb.commit()
        rollno=str(rollno)
        result='student with rollno '+ rollno +' is successfully removed from DB'
        self.listWidget.clear()
        self.listWidget.addItem(result)

    def Modifystudent(self):
        query='select * from student where roll={}'.format(self.txtroll.text())
        mycursor.execute(query)
        dbresponse=mycursor.fetchall()
        for a in dbresponse:
            print('')
        name=self.txtname.text()
        rollno=self.txtroll.text()
        marks=self.txtmarks.text()
        sex=a[4]
        age=self.spinBox.value()
        if name=='':
            name=a[0]
            print(name)
        if marks=='':
            marks=a[2]
        if age==0:
            age=a[3]
        modquery='update student set stud_name="{}" ,roll={}, marks={}, age={}, sex="{}" where roll={}'.format(name,rollno,marks,age,sex,rollno)
        mycursor.execute(modquery)
        mydb.commit()
        result='student '+ name + ' is successfully modified in DB'
        self.listWidget.clear()
        self.listWidget.addItem(result)
        query='select * from student where roll={}'.format(rollno) 
        mycursor.execute(query)
        dbresponse=mycursor.fetchall()
        result=''
        for a in dbresponse:
            for j in a:
                temp2=str(j)
                result=result+temp2+' ,'
            result=result.rstrip(' ,')
            result='('+result+')'
    
        self.listWidget.addItem(result)
        

    

    def delstudent(self):
        rollno=self.txtroll.text()
        delquery='delete from student where roll={}'.format(rollno)
        mycursor.execute(delquery)
        mydb.commit()
        rollno=str(rollno)
        result='student with rollno '+ rollno +' is successfully removed from DB'
        self.listWidget.clear()
        self.listWidget.addItem(result)
        
        
       


    
        

    def setupUi(self, Form):
           

        Form.setObjectName("Form")
        Form.resize(610, 460)
        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(0, 0, 611, 521))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.frame = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame.setGeometry(QtCore.QRect(140, 30, 341, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(30, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.rollno = QtWidgets.QLabel(self.frame)
        self.rollno.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rollno.setFont(font)
        self.rollno.setObjectName("rollno")
        self.marks = QtWidgets.QLabel(self.frame)
        self.marks.setGeometry(QtCore.QRect(30, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.marks.setFont(font)
        self.marks.setObjectName("marks")
        self.sex = QtWidgets.QLabel(self.frame)
        self.sex.setGeometry(QtCore.QRect(30, 120, 58, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")
        self.age = QtWidgets.QLabel(self.frame)
        self.age.setGeometry(QtCore.QRect(30, 160, 58, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.txtname = QtWidgets.QLineEdit(self.frame)
        self.txtname.setGeometry(QtCore.QRect(140, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txtname.setFont(font)
        self.txtname.setObjectName("txtname")
        self.txtroll = QtWidgets.QLineEdit(self.frame)
        self.txtroll.setGeometry(QtCore.QRect(140, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txtroll.setFont(font)
        self.txtroll.setObjectName("txtroll")
        self.txtmarks = QtWidgets.QLineEdit(self.frame)
        self.txtmarks.setGeometry(QtCore.QRect(140, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txtmarks.setFont(font)
        self.txtmarks.setObjectName("txtmarks")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(139, 110, 181, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.male)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 10, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.female)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(141, 160, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.btnShow = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnShow.setGeometry(QtCore.QRect(140, 240, 71, 31))
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.showdetails)
        self.btnAdd = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnAdd.setGeometry(QtCore.QRect(230, 240, 71, 31))
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.Addstudent)
        self.btnModify = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnModify.setGeometry(QtCore.QRect(381, 240, 101, 31))
        self.btnModify.setObjectName("btnModify")
        self.btnModify.clicked.connect(self.Modifystudent)
        self.btDelete = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btDelete.setGeometry(QtCore.QRect(310, 240, 71, 31))
        self.btDelete.setObjectName("btDelete")
        self.btDelete.clicked.connect(self.delstudent)
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(140, 281, 341, 151))
        self.listWidget.setObjectName("listWidget")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "NAME:"))
        self.rollno.setText(_translate("Form", "ROLL NO:"))
        self.marks.setText(_translate("Form", "MARKS:"))
        self.sex.setText(_translate("Form", "SEX:"))
        self.age.setText(_translate("Form", "AGE:"))
        self.radioButton.setText(_translate("Form", "MALE"))
        self.radioButton_2.setText(_translate("Form", "FEMALE"))
        self.btnShow.setText(_translate("Form", "SHOW"))
        self.btnAdd.setText(_translate("Form", "ADD"))
        self.btnModify.setText(_translate("Form", "MODIFY"))
        self.btDelete.setText(_translate("Form", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



