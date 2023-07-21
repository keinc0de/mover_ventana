from PyQt5.QtWidgets import *
from vn_qt5 import Ui_Form
from posicion_ventana import PosicionVentana

class VentanaQt5(QWidget, Ui_Form):
    def __init__(self):
        super(VentanaQt5, self).__init__()
        self.setupUi(self)
        self.mueveVentana()

    def mueveVentana(self):
        gm = self.geometry()
        ancho, alto = gm.width(), gm.height()
        pv = PosicionVentana(self, w=ancho, h=alto)
        self.bt_no.clicked.connect(lambda:pv.arriba.izquierda())
        self.bt_ne.clicked.connect(lambda:pv.arriba.derecha())
        self.bt_so.clicked.connect(lambda:pv.abajo.izquierda())
        self.bt_se.clicked.connect(lambda:pv.abajo.derecha())
        self.bt_ctop.clicked.connect(lambda:pv.arriba.centrar())
        self.bt_cbot.clicked.connect(lambda:pv.abajo.centrar())
        self.bt_c.clicked.connect(lambda:pv.centrar())
        

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    vn = VentanaQt5()
    vn.show()
    sys.exit(app.exec_())