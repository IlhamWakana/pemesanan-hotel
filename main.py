

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 708)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 54, 14))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 380, 101, 16))
        self.label_8.setObjectName("label_8")
        self.IsiID = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiID.setGeometry(QtCore.QRect(160, 340, 551, 31))
        self.IsiID.setObjectName("IsiID")
        self.IsiKode = QtWidgets.QLineEdit(self.centralwidget)
        self.IsiKode.setGeometry(QtCore.QRect(160, 440, 113, 20))
        self.IsiKode.setObjectName("IsiKode")
        self.IsiNama = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiNama.setGeometry(QtCore.QRect(160, 260, 551, 31))
        self.IsiNama.setObjectName("IsiNama")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 101, 16))
        self.label_9.setObjectName("label_9")
        self.IsiNoTelp = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiNoTelp.setGeometry(QtCore.QRect(160, 300, 551, 31))
        self.IsiNoTelp.setObjectName("IsiNoTelp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 101, 16))
        self.label_3.setObjectName("label_3")
        self.Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.Simpan.setGeometry(QtCore.QRect(720, 510, 85, 26))
        self.Simpan.setObjectName("Simpan")
        self.Batal = QtWidgets.QPushButton(self.centralwidget)
        self.Batal.setGeometry(QtCore.QRect(820, 510, 85, 26))
        self.Batal.setObjectName("Batal")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 291, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 139))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 291, 141))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.JUDUL = QtWidgets.QComboBox(self.centralwidget)
        self.JUDUL.setGeometry(QtCore.QRect(160, 410, 181, 22))
        self.JUDUL.setObjectName("JUDUL")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.IsiLama = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiLama.setGeometry(QtCore.QRect(160, 380, 111, 21))
        self.IsiLama.setObjectName("IsiLama")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionlogin = QtWidgets.QAction(MainWindow)
        self.actionlogin.setObjectName("actionlogin")

        self.retranslateUi(MainWindow)
        self.Batal.clicked.connect(MainWindow.close)
        self.Simpan.clicked.connect(self.on_Simpan_clicked)
        self.IsiNoTelp.textChanged.connect(self.update_buttons)
        self.IsiID.textChanged.connect(self.update_buttons)
        self.IsiKode.textChanged['QString'].connect(self.update_buttons)
        self.IsiNama.textChanged.connect(self.update_buttons)
        self.JUDUL.activated['QString'].connect(self.update_buttons)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "NAMA"))
        self.label_7.setText(_translate("MainWindow", "LAMA"))
        self.label_6.setText(_translate("MainWindow", "NO.TELP"))
        self.label_5.setText(_translate("MainWindow", "JUDUL"))
        self.label.setText(_translate("MainWindow", "PEMINJAMAN BUKU PERPUSTAKAAN"))
        self.label_8.setText(_translate("MainWindow", "HARI"))
        self.label_9.setText(_translate("MainWindow", "ID CARD"))
        self.label_3.setText(_translate("MainWindow", "KODE BUKU"))
        self.Simpan.setText(_translate("MainWindow", "Simpan"))
        self.Batal.setText(_translate("MainWindow", "Batal"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "1. Air Mata Terakhir Bunda"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "2. Perestroika"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "3. Madilog"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "4. Mein Kampf"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "5. Bocchi The Rock"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "6. A Silent Voice"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "7. Jujur Kasian"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "8. Six day War"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "9. A Man Called Ahok"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "10. Art of War"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "11. Kono Hatsukoi wa Fiction Desu"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "12. Comic Girls"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "13. Holocaust"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "14. Santa Cruz 1991"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "15. Unai Emery: El Maestro"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.JUDUL.setItemText(0, _translate("MainWindow", "1. Air Mata Terakhir Bunda"))
        self.JUDUL.setItemText(1, _translate("MainWindow", "2. Perestroika"))
        self.JUDUL.setItemText(2, _translate("MainWindow", "3. Madilog"))
        self.JUDUL.setItemText(3, _translate("MainWindow", "4. Mein Kampf"))
        self.JUDUL.setItemText(4, _translate("MainWindow", "5. Bocchi the Rock"))
        self.JUDUL.setItemText(5, _translate("MainWindow", "6. A Silent Voice"))
        self.JUDUL.setItemText(6, _translate("MainWindow", "7. Jujur Kasian"))
        self.JUDUL.setItemText(7, _translate("MainWindow", "8. Six Day War"))
        self.JUDUL.setItemText(8, _translate("MainWindow", "9. A Man Called Ahok"))
        self.JUDUL.setItemText(9, _translate("MainWindow", "10. Art of War"))
        self.JUDUL.setItemText(10, _translate("MainWindow", "11. Kono Hatsukoi wa Fiction Desu"))
        self.JUDUL.setItemText(11, _translate("MainWindow", "12. Comic Girls"))
        self.JUDUL.setItemText(12, _translate("MainWindow", "13. Holocaust"))
        self.JUDUL.setItemText(13, _translate("MainWindow", "14. Santa Cruz 1991"))
        self.JUDUL.setItemText(14, _translate("MainWindow", "15. Unai Emery: El Maestro"))
        self.actionlogin.setText(_translate("MainWindow", "login"))

    def update_buttons(self):
        is_all_filled = all(
            [
                self.IsiNama.toPlainText(),
                self.IsiNoTelp.toPlainText(),
                self.IsiID.toPlainText(),
                self.IsiKode.text(),
                self.JUDUL.currentText()
            ]
        )
        self.Simpan.setEnabled(is_all_filled)

        pass

    def on_Simpan_clicked(self):
        nama = self.IsiNama.toPlainText()
        no_telp = self.IsiNoTelp.toPlainText()
        id_card = self.IsiID.toPlainText()
        kode_buku = self.IsiKode.text()
        judul_buku = self.JUDUL.currentText()

        data_to_save = f"NAMA: {nama}\nNO.TELP: {no_telp}\nID CARD: {id_card}\nKODE BUKU: {kode_buku}\nJUDUL BUKU: {judul_buku}"

        with open("output.txt", "w") as file:
            file.write(data_to_save)

        QtWidgets.QMessageBox.information(None, "Informasi", "Data berhasil disimpan!")
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())