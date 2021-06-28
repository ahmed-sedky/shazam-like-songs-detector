from PyQt5 import QtCore, QtGui, QtWidgets
import logging
class error():
    def error_if_not_equal(self,path):
        logging.basicConfig(filename="errors.log",format='%(asctime)s %(message)s',filemode='w')
        logger=logging.getLogger()
        #Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)
        if path == 0:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('no path found')
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()
            logger.error("no path found")
            raise "no path found"
        #if  path1_length==0 or path2_length==0:
        #    error_dialog = QtWidgets.QErrorMessage()
        #    error_dialog.showMessage('no path found')
        #    error_dialog.setWindowTitle("Error")
        #    error_dialog.exec_()
        #    logger.error("no path found")
        #    raise "no path found"
        #elif  not (len(data1) or len(data2)):
        #    error_dialog = QtWidgets.QErrorMessage()
        #    error_dialog.showMessage('no data found')
        #    error_dialog.setWindowTitle("Error")
        #    error_dialog.exec_()
        #    logger.error("empty data error")
        #    raise "empty arrays"
        #elif  len(data1.reshape(-1))!=len(data2.reshape(-1)):
        #    error_dialog = QtWidgets.QErrorMessage()
        #    error_dialog.showMessage('the 2 images does not have the same length')
        #    error_dialog.setWindowTitle("Error")
        #    error_dialog.exec_()
        #    logger.error("data not matching")
        #    raise "not equall sizes"
        
        
