#Simulador_osi - Grupo 9 - CD
import tkinter as tk
from tkinter import messagebox
import time
import base64


class SimuladorOSI:

    def __init__(self, root):
        self.root = root
        self.root.title("SIMULADOR INTERACTIVO DEL MODELO OSI - UNEMI 2026")
        self.root.geometry("1200x820")
        self.root.configure(bg="#0b1f3a")

        self.capas = [
            "Aplicación", "Presentación", "Sesión",
            "Transporte", "Red", "Enlace", "Física"
        ]

        self.nombres = ["APL", "PRE", "SES", "TRA", "RED", "ENL", "FIS"]
        self.rects_a = []
        self.rects_b = []

        self.crear_interfaz()

    # ---------------------------------------------------------
    # Interfaz
    # ---------------------------------------------------------

    def crear_interfaz(self):

        tk.Label(
            self.root,
            text="SIMULADOR INTERACTIVO DEL MODELO OSI",
            font=("Arial", 18, "bold"),
            bg="#0b1f3a",
            fg="white"
        ).pack(pady=8)

        tk.Label(
            self.root,
            text="Encapsulamiento y desencapsulamiento de datos",
            font=("Arial", 11),
            bg="#0b1f3a",
            fg="#d9e2f3"
        ).pack()

        panel = tk.Frame(self.root, bg="#0b1f3a")
        panel.pack(pady=12)

        tk.Label(
            panel,
            text="Mensaje:",
            font=("Arial", 11, "bold"),
            bg="#0b1f3a",
            fg="white"
        ).pack(side=tk.LEFT)

        self.entrada = tk.Entry(panel, width=40, font=("Arial", 11))
        self.entrada.insert(0, "Hola desde PC-A")
        self.entrada.pack(side=tk.LEFT, padx=8)

        tk.Button(
            panel, text="ENVIAR", command=self.transmitir,
            bg="#28a745", fg="white", width=12
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            panel, text="REINICIAR", command=self.resetear,
            bg="#6c757d", fg="white", width=12
        ).pack(side=tk.LEFT, padx=4)

        principal = tk.Frame(self.root, bg="#0b1f3a")
        principal.pack(fill=tk.BOTH, expand=True, padx=20)

        principal.columnconfigure(0, weight=1)
        principal.columnconfigure(1, weight=0)
        principal.columnconfigure(2, weight=1)

        # PC-A
        frame_a = tk.Frame(principal, bg="#0b1f3a")
        frame_a.grid(row=0, column=0, sticky="nsew")

        tk.Label(
            frame_a,
            text="PC-A: ENCAPSULAMIENTO",
            font=("Arial", 12, "bold"),
            bg="#0b1f3a",
            fg="#ffcc00"
        ).pack()

        self.canvas_a = tk.Canvas(
            frame_a, width=490, height=110, bg="white"
        )
        self.canvas_a.pack(pady=5)

        self.consola_a = tk.Text(
            frame_a, width=58, height=24,
            bg="#151515", fg="#00ff66",
            font=("Consolas", 9)
        )
        self.consola_a.pack()

        # Canal
        frame_canal = tk.Frame(principal, bg="#0b1f3a")
        frame_canal.grid(row=0, column=1, padx=10)

        self.canvas_canal = tk.Canvas(
            frame_canal, width=100, height=110,
            bg="#0b1f3a", highlightthickness=0
        )
        self.canvas_canal.pack()

        self.flecha = self.canvas_canal.create_line(
            10, 55, 90, 55,
            arrow=tk.LAST, width=5, fill="#dddddd"
        )

        tk.Label(
            frame_canal,
            text="CANAL",
            font=("Arial", 9, "bold"),
            bg="#0b1f3a",
            fg="white"
        ).pack()

        # PC-B
        frame_b = tk.Frame(principal, bg="#0b1f3a")
        frame_b.grid(row=0, column=2, sticky="nsew")

        tk.Label(
            frame_b,
            text="PC-B: DESENCAPSULAMIENTO",
            font=("Arial", 12, "bold"),
            bg="#0b1f3a",
            fg="#ffcc00"
        ).pack()

        self.canvas_b = tk.Canvas(
            frame_b, width=490, height=110, bg="white"
        )
        self.canvas_b.pack(pady=5)

        self.consola_b = tk.Text(
            frame_b, width=58, height=24,
            bg="#151515", fg="#33ccff",
            font=("Consolas", 9)
        )
        self.consola_b.pack()

        self.dibujar_capas()

    # ---------------------------------------------------------
    # Las Capas
    # ---------------------------------------------------------

    def dibujar_capas(self):

        for i in range(7):
            x = 8 + i * 68

            r = self.canvas_a.create_rectangle(
                x, 25, x + 60, 85,
                fill="#f1f1f1",
                outline="#0b1f3a"
            )

            self.canvas_a.create_text(
                x + 30, 55,
                text=self.nombres[i],
                font=("Arial", 8, "bold")
            )

            self.rects_a.append(r)

        for i in range(7):
            x = 8 + i * 68

            r = self.canvas_b.create_rectangle(
                x, 25, x + 60, 85,
                fill="#f1f1f1",
                outline="#0b1f3a"
            )

            self.canvas_b.create_text(
                x + 30, 55,
                text=self.nombres[6 - i],
                font=("Arial", 8, "bold")
            )

            self.rects_b.append(r)

    def activar_a(self, posicion):
        self.canvas_a.itemconfig(
            self.rects_a[posicion], fill="#ffcc00"
        )
        self.root.update()
        time.sleep(0.4)
        self.canvas_a.itemconfig(
            self.rects_a[posicion], fill="#28a745"
        )

    def activar_b(self, posicion):
        self.canvas_b.itemconfig(
            self.rects_b[posicion], fill="#ffcc00"
        )
        self.root.update()
        time.sleep(0.4)
        self.canvas_b.itemconfig(
            self.rects_b[posicion], fill="#33ccff"
        )

    # ---------------------------------------------------------
    # Las Consolas
    # ---------------------------------------------------------

    def escribir_a(self, texto):
        self.consola_a.insert(tk.END, texto + "\n")
        self.consola_a.see(tk.END)
        self.root.update()

    def escribir_b(self, texto):
        self.consola_b.insert(tk.END, texto + "\n")
        self.consola_b.see(tk.END)
        self.root.update()

    # ---------------------------------------------------------
    # Para Reiniciar 
    # ---------------------------------------------------------

    def resetear(self):
        self.consola_a.delete("1.0", tk.END)
        self.consola_b.delete("1.0", tk.END)

        self.canvas_canal.itemconfig(
            self.flecha, fill="#dddddd"
        )

        for r in self.rects_a:
            self.canvas_a.itemconfig(r, fill="#f1f1f1")

        for r in self.rects_b:
            self.canvas_b.itemconfig(r, fill="#f1f1f1")

    # ---------------------------------------------------------
    # Encapsulamiento
    # ---------------------------------------------------------

    def encapsular(self, mensaje):

        datos = mensaje

        # Capa 7
        self.escribir_a(
            "[Capa 7 - Aplicación] Mensaje: " + datos
        )
        self.activar_a(0)

        # Capa 6
        datos = base64.b64encode(
            datos.encode("utf-8")
        ).decode("utf-8")

        self.escribir_a(
            "[Capa 6 - Presentación] Base64: " + datos
        )
        self.activar_a(1)

        # Capa 5
        datos = "SESION|" + datos

        self.escribir_a(
            "[Capa 5 - Sesión] Se agrega identificador de sesión."
        )
        self.activar_a(2)

        # Capa 4
        datos = "TCP|" + datos

        self.escribir_a(
            "[Capa 4 - Transporte] Se agrega información TCP simulada."
        )
        self.activar_a(3)

        # Capa 3
        datos = "IP|" + datos

        self.escribir_a(
            "[Capa 3 - Red] Se agrega direccionamiento IP simulado."
        )
        self.activar_a(4)

        # Capa 2
        datos = "MAC|" + datos + "|FCS"

        self.escribir_a(
            "[Capa 2 - Enlace] Se forma una trama con MAC y FCS."
        )
        self.activar_a(5)

        # Capa 1
        datos_bytes = datos.encode("utf-8")

        bits = "".join(
            format(byte, "08b")
            for byte in datos_bytes
        )

        self.escribir_a(
            "[Capa 1 - Física] Datos convertidos a bits."
        )

        self.escribir_a(
            "Bits transmitidos: " + bits[:120] + "..."
        )

        self.activar_a(6)

        return bits

    # ---------------------------------------------------------
    # Desencapsulamiento
    # ---------------------------------------------------------

    def desencapsular(self, bits):

        # Capa 1
        datos = bytes(
            int(bits[i:i + 8], 2)
            for i in range(0, len(bits), 8)
        ).decode("utf-8")

        self.escribir_b(
            "[Capa 1 - Física] Se reconstruyen los datos recibidos."
        )
        self.activar_b(6)

        # Capa 2
        if datos.startswith("MAC|") and datos.endswith("|FCS"):
            datos = datos[4:-4]

        self.escribir_b(
            "[Capa 2 - Enlace] Se retira MAC y FCS."
        )
        self.activar_b(5)

        # Capa 3
        if datos.startswith("IP|"):
            datos = datos[3:]

        self.escribir_b(
            "[Capa 3 - Red] Se retira el encabezado IP."
        )
        self.activar_b(4)

        # Capa 4
        if datos.startswith("TCP|"):
            datos = datos[4:]

        self.escribir_b(
            "[Capa 4 - Transporte] Se retira TCP."
        )
        self.activar_b(3)

        # Capa 5
        if datos.startswith("SESION|"):
            datos = datos[7:]

        self.escribir_b(
            "[Capa 5 - Sesión] Se retira la información de sesión."
        )
        self.activar_b(2)

        # Capa 6
        datos = base64.b64decode(
            datos.encode("utf-8")
        ).decode("utf-8")

        self.escribir_b(
            "[Capa 6 - Presentación] Se decodifica Base64."
        )
        self.activar_b(1)

        # Capa 7
        self.escribir_b(
            "[Capa 7 - Aplicación] Mensaje entregado."
        )
        self.activar_b(0)

        return datos

    # ---------------------------------------------------------
    # Transmision
    # ---------------------------------------------------------

    def transmitir(self):

        mensaje = self.entrada.get().strip()

        if not mensaje:
            messagebox.showwarning(
                "Mensaje vacío",
                "Ingrese un mensaje antes de transmitir."
            )
            return

        self.resetear()

        self.escribir_a(
            "========== INICIO DE TRANSMISIÓN =========="
        )

        self.escribir_a(
            "Mensaje original: " + mensaje
        )

        try:
            bits = self.encapsular(mensaje)

            self.canvas_canal.itemconfig(
                self.flecha, fill="#ffcc00"
            )

            self.escribir_a(
                ">>> CANAL: transmisión física en curso..."
            )

            time.sleep(1)

            self.canvas_canal.itemconfig(
                self.flecha, fill="#28a745"
            )

            self.escribir_b(
                ">>> CANAL: datos recibidos en PC-B."
            )

            mensaje_final = self.desencapsular(bits)

            self.escribir_b("")
            self.escribir_b(
                "=========================================="
            )
            self.escribir_b(
                "MENSAJE RECUPERADO: " + mensaje_final
            )
            self.escribir_b(
                "=========================================="
            )

            if mensaje_final == mensaje:

                self.escribir_b(
                    "RESULTADO: transmisión exitosa."
                )

                messagebox.showinfo(
                    "Simulación finalizada",
                    "El mensaje fue recuperado correctamente en PC-B."
                )

            else:

                self.escribir_b(
                    "RESULTADO: existe una diferencia en el mensaje."
                )

        except Exception as error:

            messagebox.showerror(
                "Error de simulación",
                f"Ocurrió un error durante la transmisión:\n{error}"
            )


if __name__ == "__main__":

    ventana = tk.Tk()
    simulador = SimuladorOSI(ventana)
    ventana.mainloop()