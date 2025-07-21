import customtkinter as ctk
import tkinter.messagebox as messagebox
from googletrans import Translator

# Diccionario de idiomas
IDIOMAS_NOMBRES = {
    "Detectar idioma": "auto",
    "Afrikáans": "af",
    "Alemán": "de",
    "Árabe": "ar",
    "Bengalí": "bn",
    "Chino (simplificado)": "zh-cn",
    "Coreano": "ko",
    "Español": "es",
    "Francés": "fr",
    "Griego": "el",
    "Hebreo": "iw",
    "Hindi": "hi",
    "Húngaro": "hu",
    "Inglés": "en",
    "Italiano": "it",
    "Japonés": "ja",
    "Neerlandés": "nl",
    "Noruego": "no",
    "Portugués": "pt",
    "Ruso": "ru",
    "Sueco": "sv",
    "Turco": "tr",
    "Ucraniano": "uk",
    "Urdu": "ur",
    "Vietnamita": "vi"
}

# Apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Función de traducción
def traducir(texto, idioma_destino):
    translator = Translator()
    try:
        resultado = translator.translate(texto, dest=idioma_destino)
        return resultado.text
    except Exception as e:
        return f"Error al traducir: {str(e)}"

# Iniciar interfaz
def iniciar_interfaz():
    class TraductorApp(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title("Traductor estilo Google")
            self.geometry("1000x550")
            self.timer = None

            self.idioma_origen = ctk.StringVar(value="Detectar idioma")
            self.idioma_destino = ctk.StringVar(value="Español")

            self.crear_widgets()

        def crear_widgets(self):
            # Frame superior con selectores y botón de intercambio
            frame_top = ctk.CTkFrame(self, fg_color="transparent")
            frame_top.place(relx=0.5, y=20, anchor="n")

            self.selector_origen = ctk.CTkOptionMenu(
                frame_top, values=list(IDIOMAS_NOMBRES.keys()),
                variable=self.idioma_origen,
                command=lambda _: self.traducir()
            )
            self.selector_origen.grid(row=0, column=0, padx=(0, 10))

            self.boton_intercambiar = ctk.CTkButton(
                frame_top, text="↔", width=40,
                command=self.intercambiar_idiomas
            )
            self.boton_intercambiar.grid(row=0, column=1, padx=10)

            self.selector_destino = ctk.CTkOptionMenu(
                frame_top, values=list(IDIOMAS_NOMBRES.keys()),
                variable=self.idioma_destino,
                command=lambda _: self.traducir()
            )
            self.selector_destino.grid(row=0, column=2, padx=(10, 0))

            # Cuadros de texto
            self.frame_textos = ctk.CTkFrame(self, fg_color="transparent")
            self.frame_textos.place(x=50, y=70)

            self.entrada = ctk.CTkTextbox(self.frame_textos, width=400, height=250)
            self.entrada.grid(row=0, column=0, padx=(0, 40))
            self.entrada.bind("<KeyRelease>", self.on_input_change)

            self.salida = ctk.CTkTextbox(self.frame_textos, width=400, height=250)
            self.salida.grid(row=0, column=1, padx=(0, 0))

            # Botones Copiar y Limpiar centrados abajo
            frame_botones = ctk.CTkFrame(self, fg_color="transparent")
            frame_botones.place(relx=0.5, rely=0.85, anchor="center")

            self.boton_copiar = ctk.CTkButton(
                frame_botones, text="📋 Copiar", command=self.copiar
            )
            self.boton_copiar.grid(row=0, column=0, padx=10)

            self.boton_limpiar = ctk.CTkButton(
                frame_botones, text="🧹 Limpiar", command=self.limpiar
            )
            self.boton_limpiar.grid(row=0, column=1, padx=10)

        def traducir(self):
            texto = self.entrada.get("1.0", "end").strip()
            if not texto:
                self.salida.delete("1.0", "end")
                return

            idioma = IDIOMAS_NOMBRES.get(self.idioma_destino.get(), "es")
            resultado = traducir(texto, idioma)
            self.salida.delete("1.0", "end")
            self.salida.insert("end", resultado)

        def intercambiar_idiomas(self):
            origen = self.idioma_origen.get()
            destino = self.idioma_destino.get()
            self.idioma_origen.set(destino)
            self.idioma_destino.set(origen)
            self.traducir()

        def copiar(self):
            texto = self.salida.get("1.0", "end").strip()
            if texto:
                self.clipboard_clear()
                self.clipboard_append(texto)
                messagebox.showinfo("Copiado", "Traducción copiada al portapapeles.")

        def limpiar(self):
            self.entrada.delete("1.0", "end")
            self.salida.delete("1.0", "end")

        def on_input_change(self, event=None):
            if self.timer:
                self.after_cancel(self.timer)
            self.timer = self.after(1000, self.traducir)

    app = TraductorApp()
    app.mainloop()

