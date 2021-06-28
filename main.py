import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore,QtWidgets,QtGui
from read_data import song_import
from shazamgui import Ui_MainWindow
#from mel_spec import  my_songs
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.song_hashes=[]
        self.songs_number=1
        self.table_data=0
        self.ui.actionfile.triggered.connect(self.open_newwindow)
        self.ui.actionsingle_song.triggered.connect(lambda :self.get_data(1))
        self.ui.action2_songs.triggered.connect(lambda :self.get_data(2))
        self.ui.horizontalSlider.sliderReleased.connect(lambda :self.check_songs_number(2))
    def check_songs_number(self,number):
        try:
            if number == 2:
                data_mixed =self.ui.horizontalSlider.value()/100*self.song_hashes[0]+((100-self.ui.horizontalSlider.value())/100)*self.song_hashes[1]
            else:
                data_mixed =self.song_hashes[0]
            self.get_similarity_index(data_mixed)
        except Exception:
            pass
    def get_data(self,data_number):
        self.song_hashes=[]
        self.songs_number=data_number
        for i in range(self.songs_number):
            self.song_hashes.append(song_import().get_song())
        try:
            self.check_songs_number(data_number)
        except Exception:
            pass
    def get_similarity_index(self,data_mixed):
        songs_list,similarity_list=song_import().similarity_iteration(data_mixed)
        for i in range(len(songs_list)):
            for j in range(2):
                self.table_data = 0
                if j == 0:
                    self.table_data=songs_list[i]
                else:
                    self.table_data=similarity_list[i]
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(self.table_data)))
    def open_newwindow(self):
        self.new_instance = MainWindow()
        self.new_instance.show()
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    mw = MainWindow()
    sys.exit(app.exec_())
