import tkinter as tk
from posicion_ventana import PosicionVentana


class VentanaSimple(tk.Tk):
    def __init__(self):
        super(VentanaSimple, self).__init__()
        ancho, alto = 320, 80
        self.geometry(f"{ancho}x{alto}")
        posv = PosicionVentana(self, ancho, alto)
        # BOTONES
        self.bt_no = tk.Button(self, text='ARRIBA IZQ', width=12, command=posv.arriba.izquierda)
        self.bt_no.grid(row=0, column=0)
        self.bt_ct = tk.Button(self, text='ARRIBA CENTRAR', width=16, command=posv.arriba.centrar)
        self.bt_ct.grid(row=0, column=1)
        self.bt_ne = tk.Button(self, text='ARRIBA DER', width=12, command=posv.arriba.derecha)
        self.bt_ne.grid(row=0, column=2)
        self.bt_so = tk.Button(self, text='ABAJO IZQ', width=12, command=posv.abajo.izquierda)
        self.bt_so.grid(row=2, column=0)
        self.bt_cb = tk.Button(self, text='ABAJO CENTRAR', width=16, command=posv.abajo.centrar)
        self.bt_cb.grid(row=2, column=1)
        self.bt_se = tk.Button(self, text='ABAJO DER', width=12, command=posv.abajo.derecha)
        self.bt_se.grid(row=2, column=2)
        self.bt_c = tk.Button(self, text='CENTRAR', width=12, command=posv.centrar)
        self.bt_c.grid(row=1, column=1)



miv = VentanaSimple()
miv.mainloop()