from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Interfaz(QWidget):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.resize(330, 60)
        self.bt_no = QPushButton(self, text='NO')
        self.bt_ne = QPushButton(self, text='NE')
        self.bt_so = QPushButton(self, text='SO')
        self.bt_se = QPushButton(self, text='SE')
        self.bt_ctop = QPushButton(self, text='CENTRAR ARRIBA', width=80)
        self.bt_cbot = QPushButton(self, text='CENTRAR ABAJO', width=80)
        self.bt_c = QPushButton(self, text='CENTRAR', width=80)
        self.bt_ctop.move(6, 25)
        self.bt_c.move(106, 25)
        self.bt_cbot.move(190, 25)
        
        li = [self.bt_no, self.bt_ne, self.bt_so, self.bt_se]
        for x, bt in enumerate(li):
            bt.move((x*80)+4, 0)

        self.bt_ne.clicked.connect(self._mueve_a_ne)
        self.bt_no.clicked.connect(self._mueve_a_no)
        self.bt_se.clicked.connect(self._mueve_a_se)
        self.bt_so.clicked.connect(self._mueve_a_so)
        self.bt_ctop.clicked.connect(self._mueve_centrar_top)
        self.bt_cbot.clicked.connect(self._mueve_centrar_bot)
        self.bt_c.clicked.connect(self._centrar)

    def _obten_resolucion(self):
        gmp = QDesktopWidget().screenGeometry()
        return gmp.width(), gmp.height() - (30+30)

    def ubica_ventana(self, ub='ne'):
        wp, hp = self._obten_resolucion()
        gm = self.geometry()
        w, h = gm.width(), gm.height()
        if ub=='ne':
            x, y = wp-w, 0
        elif ub=='no':
            x, y = 0, 0
        elif ub=='se':
            x, y = wp-w, hp-h
        elif ub=='so':
            x, y = 0, hp-h
        elif ub=='ctop':
            x, y = wp//2-w//2, 0
        elif ub=='cbot':
            x, y = wp//2-w//2, hp-h
        elif ub=='centrar':
            x, y = wp//2-w//2 , hp//2-h//2
        self.move(x, y)

    def _mueve_a_ne(self):
        self.ubica_ventana('ne')

    def _mueve_a_no(self):
        self.ubica_ventana('no')

    def _mueve_a_se(self):
        self.ubica_ventana('se')

    def _mueve_a_so(self):
        self.ubica_ventana('so')

    def _mueve_centrar_top(self):
        self.ubica_ventana('ctop')

    def _mueve_centrar_bot(self):
        self.ubica_ventana('cbot')

    def _centrar(self):
        self.ubica_ventana('centrar')


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    vn = Interfaz()
    vn.show()
    sys.exit(app.exec_())