import tkinter as tk
from PIL import Image, ImageTk
import random
from classificador import classificar_numeros


class NumberClassifierApp:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.carregar_widgets()

    def configurar_janela(self):
        self.root.title("Classificador de Números - Par e Ímpar")
        largura_janela = 819
        altura_janela = 819
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_central = int((largura_tela - largura_janela) / 2)
        y_central = int((altura_janela - altura_janela) / 2)
        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_central}+{y_central}")
        self.root.resizable(False, False)

        # Adicionando o background
        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    def carregar_widgets(self):
        # Botão com imagem para gerar números e classificar
        self.botao_imagem = ImageTk.PhotoImage(Image.open("assets/button_classify.png").resize((50, 50)))
        self.botao_classificar = tk.Button(
            self.root,
            image=self.botao_imagem,
            command=self.classificar_numeros,
            bg="#2b2b2b",
            bd=0,
            activebackground="#1E1E1E",
        )
        # Posicionar o botão no canto inferior direito
        self.botao_classificar.place(relx=0.95, rely=0.95, anchor="se")

        # Adicionar efeito de hover intermitente
        self.hover_state = False
        self.alternar_cor_hover()

    def alternar_cor_hover(self):
        """
        Alterna suavemente a cor do botão para criar um efeito de "hover intermitente".
        """
        if self.hover_state:
            self.botao_classificar.config(bg="#555555")  # Cor alternativa
        else:
            self.botao_classificar.config(bg="#2b2b2b")  # Cor original
        self.hover_state = not self.hover_state
        self.root.after(1500, self.alternar_cor_hover)

    def classificar_numeros(self):
        # Gerar uma lista aleatória de números
        numeros = [random.randint(1, 100) for _ in range(10)]
        pares, impares = classificar_numeros(numeros)

        # Exibir os números gerados e a classificação
        self.exibir_saida(numeros, pares, impares)

    def exibir_saida(self, numeros, pares, impares):
        # Criar a área de saída se ainda não existir
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()  # Remove a área existente

        self.output_frame = tk.Frame(
            self.root, bg="#333333", highlightthickness=2, highlightbackground="#FFD700", relief="raised"
        )
        self.output_frame.place(relx=0.5, rely=0.6, anchor="center", width=600, height=300)

        # Botão "close" dentro da área de saída
        self.close_icon = ImageTk.PhotoImage(Image.open("assets/close_icon.png").resize((20, 20)))
        self.close_button = tk.Button(
            self.output_frame,
            image=self.close_icon,
            bg="#333333",
            bd=0,
            activebackground="#444444",
            command=self.fechar_saida,
        )
        self.close_button.place(x=570, y=5)  # Ajuste fino para posicionar o ícone no canto superior direito

        # Área para exibir a sequência de entrada
        entrada_label = tk.Label(
            self.output_frame,
            text="🔢 Sequência Gerada:",
            bg="#333333",
            fg="#FFFFFF",
            font=("Helvetica", 12, "bold"),
        )
        entrada_label.place(x=10, y=10)

        entrada_texto = tk.Label(
            self.output_frame,
            text=", ".join(map(str, numeros)),
            bg="#333333",
            fg="#FFD700",
            font=("Courier", 12),
            wraplength=560,  # Quebra de linha se o texto for longo
            justify="left",
        )
        entrada_texto.place(x=10, y=40)

        # Ícones para pares e ímpares
        self.icon_par = ImageTk.PhotoImage(Image.open("assets/blue_circle.png").resize((20, 20)))
        self.icon_impar = ImageTk.PhotoImage(Image.open("assets/red_circle.png").resize((20, 20)))

        # Exibir números pares
        pares_label = tk.Label(
            self.output_frame,
            text="🔵 Números Pares:",
            bg="#333333",
            fg="#FFFFFF",
            font=("Helvetica", 12, "bold"),
        )
        pares_label.place(x=10, y=90)

        x_pos = 10
        for num in pares:
            tk.Label(self.output_frame, image=self.icon_par, bg="#333333").place(x=x_pos, y=120)
            tk.Label(self.output_frame, text=str(num), bg="#333333", fg="#FFFFFF", font=("Helvetica", 10)).place(
                x=x_pos + 25, y=120
            )
            x_pos += 50

        # Exibir números ímpares
        impares_label = tk.Label(
            self.output_frame,
            text="🔴 Números Ímpares:",
            bg="#333333",
            fg="#FFFFFF",
            font=("Helvetica", 12, "bold"),
        )
        impares_label.place(x=10, y=160)

        x_pos = 10
        for num in impares:
            tk.Label(self.output_frame, image=self.icon_impar, bg="#333333").place(x=x_pos, y=190)
            tk.Label(self.output_frame, text=str(num), bg="#333333", fg="#FFFFFF", font=("Helvetica", 10)).place(
                x=x_pos + 25, y=190
            )
            x_pos += 50

    def fechar_saida(self):
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()
            del self.output_frame


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberClassifierApp(root)
    root.mainloop()
