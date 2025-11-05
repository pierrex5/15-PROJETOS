import flet as ft
import math

class CalculadoraAvancada:
    def __init__(self):
        self.expressao = ""
        self.memoria = 0
        self.historico = []
        
    def main(self, page: ft.Page):
        self.page = page
        page.title = "Calculadora Avançada"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = "#f5f5f5"
        page.padding = 20
        
        # Display principal
        self.display = ft.TextField(
            value="0",
            text_align=ft.TextAlign.RIGHT,
            read_only=True,
            border=ft.InputBorder.NONE,
            text_style=ft.TextStyle(size=32, weight=ft.FontWeight.BOLD),
            bgcolor="white",
            color="black"
        )
        
        # Display do histórico
        self.display_historico = ft.Text(
            value="",
            text_align=ft.TextAlign.RIGHT,
            size=14,
            color="gray"
        )
        
        # Botões da calculadora
        botoes_basicos = self.criar_botoes_basicos()
        botoes_cientificos = self.criar_botoes_cientificos()
        
        page.add(
            ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.Text("Calculadora Avançada", size=20, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.Icons.HISTORY,
                            on_click=self.mostrar_historico
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    margin=ft.margin.only(bottom=10)
                ),
                
                # Displays
                ft.Container(
                    content=ft.Column([
                        self.display_historico,
                        self.display
                    ]),
                    bgcolor="white",
                    padding=15,
                    border_radius=10,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Corpo da calculadora
                ft.Row([
                    # Calculadora básica
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Básica", size=16, weight=ft.FontWeight.BOLD),
                            botoes_basicos
                        ]),
                        expand=2
                    ),
                    
                    # Calculadora científica
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Científica", size=16, weight=ft.FontWeight.BOLD),
                            botoes_cientificos
                        ]),
                        expand=1
                    )
                ])
            ])
        )
    
    def criar_botoes_basicos(self):
        botoes = [
            ["MC", "MR", "M+", "M-", "C"],
            ["7", "8", "9", "/", "√"],
            ["4", "5", "6", "*", "x²"],
            ["1", "2", "3", "-", "1/x"],
            ["0", ".", "=", "+", "±"]
        ]
        
        grid_botoes = []
        for linha in botoes:
            row_botoes = []
            for texto in linha:
                cor = self.obter_cor_botao(texto)
                row_botoes.append(
                    ft.ElevatedButton(
                        text=texto,
                        on_click=lambda e, t=texto: self.processar_botao(t),
                        bgcolor=cor,
                        color="white" if cor != "#e0e0e0" else "black",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=15
                        ),
                        expand=1
                    )
                )
            grid_botoes.append(
                ft.Row(row_botoes, spacing=5)
            )
        
        return ft.Column(grid_botoes, spacing=5)
    
    def criar_botoes_cientificos(self):
        botoes = [
            ["sin", "cos", "tan", "π"],
            ["log", "ln", "e", "x^y"],
            ["(", ")", "!", "mod"],
            ["rad", "deg", "rand", "AC"]
        ]
        
        grid_botoes = []
        for linha in botoes:
            row_botoes = []
            for texto in linha:
                row_botoes.append(
                    ft.ElevatedButton(
                        text=texto,
                        on_click=lambda e, t=texto: self.processar_botao(t),
                        bgcolor="#4a6572",
                        color="white",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=12
                        ),
                        expand=1
                    )
                )
            grid_botoes.append(
                ft.Row(row_botoes, spacing=5)
            )
        
        return ft.Column(grid_botoes, spacing=5)
    
    def obter_cor_botao(self, texto):
        if texto in ["=", "C", "AC"]:
            return "#ff6b00"
        elif texto in ["+", "-", "*", "/"]:
            return "#4a6572"
        elif texto in ["MC", "MR", "M+", "M-"]:
            return "#344955"
        else:
            return "#e0e0e0"
    
    def processar_botao(self, texto):
        try:
            if texto.isdigit() or texto == ".":
                self.adicionar_numero(texto)
            elif texto in ["+", "-", "*", "/"]:
                self.adicionar_operador(texto)
            elif texto == "=":
                self.calcular()
            elif texto == "C":
                self.limpar()
            elif texto == "AC":
                self.limpar_tudo()
            elif texto == "±":
                self.trocar_sinal()
            elif texto == "√":
                self.raiz_quadrada()
            elif texto == "x²":
                self.quadrado()
            elif texto == "1/x":
                self.inverso()
            elif texto == "sin":
                self.seno()
            elif texto == "cos":
                self.cosseno()
            elif texto == "tan":
                self.tangente()
            elif texto == "π":
                self.adicionar_pi()
            elif texto == "e":
                self.adicionar_e()
            elif texto == "log":
                self.logaritmo10()
            elif texto == "ln":
                self.logaritmo_natural()
            elif texto == "x^y":
                self.adicionar_operador("^")
            elif texto == "!":
                self.fatorial()
            elif texto == "mod":
                self.adicionar_operador("%")
            elif texto == "(":
                self.adicionar_parentese("(")
            elif texto == ")":
                self.adicionar_parentese(")")
            elif texto == "rad":
                self.modo_radianos = True
                self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Modo: Radianos")))
            elif texto == "deg":
                self.modo_radianos = False
                self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Modo: Graus")))
            elif texto == "rand":
                self.numero_aleatorio()
            elif texto == "MC":
                self.memoria_clear()
            elif texto == "MR":
                self.memoria_recall()
            elif texto == "M+":
                self.memoria_add()
            elif texto == "M-":
                self.memoria_subtract()
            
            self.page.update()
            
        except Exception as e:
            self.display.value = "Erro"
            self.page.update()
    
    def adicionar_numero(self, numero):
        if self.display.value == "0" or self.display.value == "Erro":
            self.display.value = numero
        else:
            self.display.value += numero
    
    def adicionar_operador(self, operador):
        if self.display.value == "Erro":
            self.display.value = "0"
        
        ultimo_caracter = self.display.value[-1] if self.display.value else ""
        if ultimo_caracter in ["+", "-", "*", "/", "^", "%"]:
            self.display.value = self.display.value[:-1] + operador
        else:
            self.display.value += operador
    
    def adicionar_parentese(self, parentese):
        if self.display.value == "0" or self.display.value == "Erro":
            self.display.value = parentese
        else:
            self.display.value += parentese
    
    def calcular(self):
        try:
            if self.display.value == "Erro":
                return
            
            expressao = self.display.value
            
            # Substituir símbolos especiais
            expressao = expressao.replace("^", "**")
            expressao = expressao.replace("π", str(math.pi))
            expressao = expressao.replace("e", str(math.e))
            
            # Calcular resultado
            resultado = eval(expressao)
            
            # Adicionar ao histórico
            self.historico.append(f"{expressao} = {resultado}")
            if len(self.historico) > 10:
                self.historico.pop(0)
            
            self.display_historico.value = expressao
            self.display.value = str(resultado)
            
        except ZeroDivisionError:
            self.display.value = "Erro: Divisão por zero"
        except:
            self.display.value = "Erro"
    
    def limpar(self):
        if self.display.value == "Erro":
            self.display.value = "0"
        elif len(self.display.value) > 1:
            self.display.value = self.display.value[:-1]
        else:
            self.display.value = "0"
    
    def limpar_tudo(self):
        self.display.value = "0"
        self.display_historico.value = ""
    
    def trocar_sinal(self):
        try:
            if self.display.value != "0" and self.display.value != "Erro":
                if self.display.value[0] == "-":
                    self.display.value = self.display.value[1:]
                else:
                    self.display.value = "-" + self.display.value
        except:
            pass
    
    def raiz_quadrada(self):
        try:
            valor = float(self.display.value)
            if valor >= 0:
                resultado = math.sqrt(valor)
                self.display.value = str(resultado)
                self.historico.append(f"√{valor} = {resultado}")
            else:
                self.display.value = "Erro: Número negativo"
        except:
            self.display.value = "Erro"
    
    def quadrado(self):
        try:
            valor = float(self.display.value)
            resultado = valor ** 2
            self.display.value = str(resultado)
            self.historico.append(f"{valor}² = {resultado}")
        except:
            self.display.value = "Erro"
    
    def inverso(self):
        try:
            valor = float(self.display.value)
            if valor != 0:
                resultado = 1 / valor
                self.display.value = str(resultado)
                self.historico.append(f"1/{valor} = {resultado}")
            else:
                self.display.value = "Erro: Divisão por zero"
        except:
            self.display.value = "Erro"
    
    def seno(self):
        try:
            valor = float(self.display.value)
            if hasattr(self, 'modo_radianos') and not self.modo_radianos:
                valor = math.radians(valor)
            resultado = math.sin(valor)
            self.display.value = str(resultado)
            self.historico.append(f"sin({valor}) = {resultado}")
        except:
            self.display.value = "Erro"
    
    def cosseno(self):
        try:
            valor = float(self.display.value)
            if hasattr(self, 'modo_radianos') and not self.modo_radianos:
                valor = math.radians(valor)
            resultado = math.cos(valor)
            self.display.value = str(resultado)
            self.historico.append(f"cos({valor}) = {resultado}")
        except:
            self.display.value = "Erro"
    
    def tangente(self):
        try:
            valor = float(self.display.value)
            if hasattr(self, 'modo_radianos') and not self.modo_radianos:
                valor = math.radians(valor)
            resultado = math.tan(valor)
            self.display.value = str(resultado)
            self.historico.append(f"tan({valor}) = {resultado}")
        except:
            self.display.value = "Erro"
    
    def adicionar_pi(self):
        if self.display.value == "0" or self.display.value == "Erro":
            self.display.value = str(math.pi)
        else:
            self.display.value += str(math.pi)
    
    def adicionar_e(self):
        if self.display.value == "0" or self.display.value == "Erro":
            self.display.value = str(math.e)
        else:
            self.display.value += str(math.e)
    
    def logaritmo10(self):
        try:
            valor = float(self.display.value)
            if valor > 0:
                resultado = math.log10(valor)
                self.display.value = str(resultado)
                self.historico.append(f"log({valor}) = {resultado}")
            else:
                self.display.value = "Erro: Número inválido"
        except:
            self.display.value = "Erro"
    
    def logaritmo_natural(self):
        try:
            valor = float(self.display.value)
            if valor > 0:
                resultado = math.log(valor)
                self.display.value = str(resultado)
                self.historico.append(f"ln({valor}) = {resultado}")
            else:
                self.display.value = "Erro: Número inválido"
        except:
            self.display.value = "Erro"
    
    def fatorial(self):
        try:
            valor = int(float(self.display.value))
            if valor >= 0:
                resultado = math.factorial(valor)
                self.display.value = str(resultado)
                self.historico.append(f"{valor}! = {resultado}")
            else:
                self.display.value = "Erro: Número negativo"
        except:
            self.display.value = "Erro"
    
    def numero_aleatorio(self):
        import random
        resultado = random.random()
        self.display.value = str(resultado)
    
    def memoria_clear(self):
        self.memoria = 0
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Memória limpa")))
    
    def memoria_recall(self):
        self.display.value = str(self.memoria)
    
    def memoria_add(self):
        try:
            valor = float(self.display.value)
            self.memoria += valor
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Adicionado à memória: {valor}")))
        except:
            self.display.value = "Erro"
    
    def memoria_subtract(self):
        try:
            valor = float(self.display.value)
            self.memoria -= valor
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Subtraído da memória: {valor}")))
        except:
            self.display.value = "Erro"
    
    def mostrar_historico(self, e):
        if self.historico:
            historico_texto = "\n".join(self.historico)
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Histórico de Cálculos"),
                    content=ft.Text(historico_texto),
                    actions=[
                        ft.TextButton("Fechar", on_click=lambda e: self.page.close_dialog())
                    ]
                )
            )
        else:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Nenhum cálculo no histórico")))

# Executar a calculadora
if __name__ == "__main__":
    ft.app(target=CalculadoraAvancada().main)