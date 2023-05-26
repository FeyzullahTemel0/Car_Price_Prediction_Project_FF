# -*- coding: utf-8 -*-

### Program için yazılan kodların çalışması için gerekli kütüphanelerin içe aktarılması
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc
import sys
from datetime import datetime
from PyQt5.QtCore import QTimer,QTime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import webbrowser
import pandas as pd

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1258, 608)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 1221, 541))
        self.label.setStyleSheet("background-color:rgb(0, 0, 0,10);\n"
"border-radius:15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 1221, 41))
        self.label_2.setStyleSheet("background-color:rgb(0, 170, 255);\n"
"border-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.exit_button_function)
        self.pushButton.setGeometry(QtCore.QRect(1208, 30, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 0, 0);\n"
"color:black;\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(31, 25, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        self.timer.start(1000)
        self.lcd_number()
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 1221, 531))
        self.label_3.setStyleSheet("background-color:rgb(0, 170, 255);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 291, 41))
        self.lineEdit_2.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 140, 291, 41))
        self.lineEdit_3.setStyleSheet("\n"
"border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 190, 291, 41))
        self.lineEdit_4.setStyleSheet("\n"
"border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 240, 291, 41))
        self.lineEdit_5.setStyleSheet("\n"
"border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 290, 291, 41))
        self.lineEdit_6.setStyleSheet("\n"
"border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 340, 291, 41))
        self.lineEdit_7.setStyleSheet("\n"
"border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 90, 291, 41))
        self.lineEdit_8.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 140, 291, 41))
        self.lineEdit_9.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 190, 291, 41))
        self.lineEdit_10.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(470, 240, 291, 41))
        self.lineEdit_11.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(470, 290, 291, 41))
        self.lineEdit_12.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(470, 340, 291, 41))
        self.lineEdit_13.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(830, 90, 291, 41))
        self.lineEdit_14.setStyleSheet("border-radius:20px;\n"
"border-bottom: 2px solid rgb(0, 0, 0);\n"
"border-left: 2px solid rgb(0, 0, 0);\n"
"border-right: 2px solid rgb(0, 0, 0);\n"
"border-top: 2px solid rgb(0, 0, 0);\n"
"")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 1171, 20))
        self.label_4.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(830, 430, 381, 129))
        self.label_6.setStyleSheet("border-radius:15px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 490, 371, 61))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.araba_fiyat_tahmin_fonksiyonu)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 420, 371, 61))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.write_to_data_in_araba_verileri)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 430, 751, 51))
        self.label_7.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(71, 506, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_5:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.instagram_yonlendirmesi)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(72, 511, 31, 31))
        self.label_5.setStyleSheet("border-image: url(:/images/instagram.svg);\n"
"border-radius:15px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(251, 505, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_6:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.mail_yonlendirmesi)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(261, 509, 34, 31))
        self.label_8.setStyleSheet("border-image:  url(:/images/mail (3).svg);\n"
"border-radius:15px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(439, 505, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_7:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_7:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.linkedin_yonlendirmesi)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(448, 510, 31, 31))
        self.label_9.setStyleSheet("border-image:url(:/images/linkedin.svg);\n"
"border-radius:15px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(250, 27, 861, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1176, 30, 21, 21))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 0);\n"
"border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(629, 505, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"border:none;\n"
"border-radius:15px;\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-top:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-left:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_8:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_8:pressed{\n"
"border-bottom-color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.github_yonlendirmesi)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(640, 510, 31, 31))
        self.label_12.setStyleSheet("border-image:url(:/images/githubicon.png);\n"
"border-radius:15px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(800, 160, 401, 221))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "X"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "İlan Tarihi"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Marka"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Araç Tip Grubu"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Model - Yıl"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Yakıt Türü"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Vites"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "CCM Beygir Gücü"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "Renk"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "Kasa Tipi"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "Kimden"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "Durum"))
        self.lineEdit_13.setPlaceholderText(_translate("Form", "KM"))
        self.lineEdit_14.setPlaceholderText(_translate("Form", "Fiyat"))
        self.pushButton_3.setText(_translate("Form", "Bilgilere Göre Tahmin Yap"))
        self.pushButton_4.setText(_translate("Form", "Bilgileri Kaydet"))
        self.label_7.setText(_translate("Form", "Yapay Zekanın Araç Fiyat Tahmini"))
        self.pushButton_5.setText(_translate("Form", "İnstagram"))
        self.pushButton_6.setText(_translate("Form", "E-Mail"))
        self.pushButton_7.setText(_translate("Form", "Linkedin"))
        self.label_10.setText(_translate("Form", "ARAÇ KAYIT VE FİYAT TAHMİN PROGRAMI             | FF TEKNOLOJİ | "))
        self.pushButton_2.setText(_translate("Form", "_"))
        self.pushButton_8.setText(_translate("Form", "GitHub"))
        self.plainTextEdit.setPlainText(_translate("Form", "BİLGİLENDİRME MENTİNLERİNİ OKUMADAN PROGRAMI KULLANMAYINIZ!!!\n"
"\n"
"- Fiyatı bilinmeyen bir araç için önce bilgiler girilmeli daha sonrasında tahmin yaptırılmalıdır!\n"
"\n"
" - Eğer verilerinize yeni araç kaydı yapmak istiyorsanız bilgileri kaydet butonu ile kısaca yapabilirsiniz.\n"
"\n"
"-Ekranın sol üst köşesinde anlık saati görebilirsiniz.\n"
"\n"
"-Program tarafından yapılan tahminleri \"Yapay Zekanın Araç Fiyat Tahmini\" kısmında görebilirsiniz.\n"
"\n"
"- Ekranın alt kısmında bulunan butonlar aracılığıyla hangi platformdan isterseniz bana ulaşabilirsiniz.."))


### Saat Fonksiyonu

    def lcd_number(self):
        time = datetime.now()
        formatted_time = time.strftime("%H:%M")
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.display(formatted_time)

### Kırmızı çıkış butonu için yazılmış olan çıkış fonksyionu

    def exit_button_function(self):
        exit()

### Kullanıcı tarafından girilen verilerin bir değişkene atanması ve araba_verileri.csv dosyasına kayıt edilmesi için yazılan fonksyion

    def write_to_data_in_araba_verileri(self):
        csv_file = "araba_verileri.csv"
        '''
        # İlan Tarihi,Marka,Arac Tip Grubu,Arac Tip,Model Yıl,
        ## Yakıt Turu,Vites,CCM Beygir Gucu,Renk,Kasa Tipi,Kimden,
        ### Durum,Km,Fiyat
        '''
        ilanTarihi      = self.lineEdit_2.text()
        marka           = self.lineEdit_3.text()
        arac_tip_grup   = self.lineEdit_4.text()
        model_yil       = self.lineEdit_5.text()
        yakit           = self.lineEdit_6.text()
        vites           = self.lineEdit_7.text()
        ccm_BeygirGucu  = self.lineEdit_8.text()
        renk            = self.lineEdit_9.text()
        kasa_tipi       = self.lineEdit_10.text()
        kimden          = self.lineEdit_11.text()
        durum           = self.lineEdit_12.text()
        km              = self.lineEdit_13.text()
        fiyat           = self.lineEdit_14.text()

        # Verilerin kaydı için bir dataFrame oluşturup ardından csv dosyasına yazıp güncelliyorum.

        data  =  pd.DataFrame({
             "İlan Tarihi":[ilanTarihi],
             "Marka":[marka],
             "Arac Tip Grubu":[arac_tip_grup],
             "Model Yıl":[model_yil],
             "Yakıt Turu":[yakit],
             "Vites":[vites],
             "CCM Beygir Gucu":[ccm_BeygirGucu],
             "Renk":[renk],
             "Kasa Tipi": [kasa_tipi],
             "Kimden":[kimden],
             "Durum":[durum],
             "Km":[km],
             "Fiyat":[fiyat]
        })

        df = pd.read_csv(csv_file,encoding="utf-8")
        df = pd.concat([df,data],ignore_index=True)
        df.to_csv(csv_file,index=True)

    def araba_fiyat_tahmin_fonksiyonu(self):
         
        veri_seti = pd.read_csv("araba_verileri.csv",encoding="utf-8")
        ozellikler = veri_seti[['İlan Tarihi','Marka','Arac Tip Grubu','Model Yıl','Yakıt Turu','Vites','CCM Beygir Gucu','Renk','Kasa Tipi','Kimden','Durum','Km','Fiyat']]
        fiyatlar = veri_seti['Fiyat']

        #Kategorik Özelliklerin sayısallaştırılması. Makine öğrenimi için gerekli kısımdır.
        ozellikler_encoded = pd.get_dummies(ozellikler,drop_first=True)

        #Veri setini eğitim ve test kümelerine ayrılması kısmı.
        X_train, X_test, y_train, y_test = train_test_split(ozellikler_encoded,fiyatlar,test_size=0.2,random_state=42)

        #Random Forest Regression kullanarak bir makine öğrenmesi modeli oluşturalım ve eğitelim.
        model = RandomForestRegressor(n_estimators=100,random_state=42)
        model.fit(X_train,y_train)

        #Tahminler ayapalım ve tahmminleri değerlendirelim
        y_pred = model.predict(X_test)
        en_iyi_tahmin = y_pred[0]
        formatted_tahmin = "{:,.2f} TL".format(en_iyi_tahmin)

        # Tahmin farklarına bakarak programa yorum yaptıralım ve yorumunu ekranda gösterelim.
        farklar = (y_test - y_pred)

        for fark in farklar:
                if fark > 0:
                        formatted_tahmin = str(formatted_tahmin)
                        self.label_7.setText(formatted_tahmin + " Programın bu araç için tahmini aracın gerçek fiyatından düşüktür.")
                elif fark < 0:
                        self.label_7.setText(formatted_tahmin + " Programın bu araç için tahmini aracın gerçek fiyatından yüksektir." )
                else:
                     self.label_7.setText(formatted_tahmin + " Programın bu araç için tahmini aracın gerçek fiyatıyla aynıdır.")


    def instagram_yonlendirmesi(self):
        url = "https://www.instagram.com/feyzullahc4/"
        webbrowser.open(url)

    def mail_yonlendirmesi(self):
        url = "mailto:feyzullaht421@gmail.com"
        webbrowser.open(url)
    
    def linkedin_yonlendirmesi(self):
        url = "https://www.linkedin.com/in/feyzullahtemel/"
        webbrowser.open(url)
    
    def github_yonlendirmesi(self):
        url = "https://github.com/FeyzullahTemel0"
        webbrowser.open(url)

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())


