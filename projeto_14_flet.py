import flet as ft
import random
import time

class BasqueteApp:
    def __init__(self):
        self.page = None
        self.pontuacao_jogo = 0
        self.tempo_restante = 30
        self.timer_ativo = False
        
    def main(self, page: ft.Page):
        self.page = page
        page.title = "NBA Pro - Basquete Profissional"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.bgcolor = "#1a1a1a"
        
        # Dados de exemplo mais detalhados
        self.noticias = [
            {
                "titulo": "Lakers vencem os Warriors em jogo emocionante",
                "imagem": "🏀", 
                "data": "15/12/2024",
                "conteudo": "Os Los Angeles Lakers venceram os Golden State Warriors por 112-108 em um jogo que foi decidido nos segundos finais. LeBron James liderou sua equipe com 32 pontos, 8 rebotes e 7 assistências, enquanto Stephen Curry marcou 28 pontos para os Warriors.",
                "destaque": "LeBron James com performance MVP",
                "comentarios": ["Jogo incrível!", "Lakers estão de volta!", "Curry foi brilhante"]
            },
            {
                "titulo": "Novo recorde de pontos na temporada",
                "imagem": "⭐", 
                "data": "14/12/2024",
                "conteudo": "Luka Doncic estabeleceu um novo recorde da temporada com 58 pontos na vitória do Dallas Mavericks sobre o Phoenix Suns. O esloveno fez 10 cestas de 3 pontos e completou um triple-double com 12 rebotes e 11 assistências.",
                "destaque": "Luka Doncic com 58 pontos",
                "comentarios": ["Luka é fenomenal!", "MVP da temporada?", "Performance histórica"]
            }
        ]
        
        self.produtos_loja = [
            {"nome": "Camiseta NBA", "preco": "R$ 199", "imagem": "👕", "categoria": "Vestuário"},
            {"nome": "Tênis de Basquete", "preco": "R$ 499", "imagem": "👟", "categoria": "Calçados"},
            {"nome": "Bola Oficial", "preco": "R$ 159", "imagem": "🏀", "categoria": "Equipamentos"},
            {"nome": "Boné NBA", "preco": "R$ 89", "imagem": "🧢", "categoria": "Acessórios"}
        ]
        
        # Tabela completa com todos os 30 times da NBA
        self.conferencia_leste = [
            {"time": "Boston Celtics", "vitorias": 22, "derrotas": 6, "conferencia": "Leste"},
            {"time": "Milwaukee Bucks", "vitorias": 21, "derrotas": 7, "conferencia": "Leste"},
            {"time": "Philadelphia 76ers", "vitorias": 20, "derrotas": 8, "conferencia": "Leste"},
            {"time": "Cleveland Cavaliers", "vitorias": 18, "derrotas": 10, "conferencia": "Leste"},
            {"time": "New York Knicks", "vitorias": 17, "derrotas": 11, "conferencia": "Leste"},
            {"time": "Miami Heat", "vitorias": 17, "derrotas": 12, "conferencia": "Leste"},
            {"time": "Indiana Pacers", "vitorias": 15, "derrotas": 13, "conferencia": "Leste"},
            {"time": "Orlando Magic", "vitorias": 16, "derrotas": 14, "conferencia": "Leste"},
            {"time": "Chicago Bulls", "vitorias": 14, "derrotas": 16, "conferencia": "Leste"},
            {"time": "Atlanta Hawks", "vitorias": 13, "derrotas": 17, "conferencia": "Leste"},
            {"time": "Brooklyn Nets", "vitorias": 13, "derrotas": 18, "conferencia": "Leste"},
            {"time": "Toronto Raptors", "vitorias": 12, "derrotas": 18, "conferencia": "Leste"},
            {"time": "Charlotte Hornets", "vitorias": 8, "derrotas": 22, "conferencia": "Leste"},
            {"time": "Washington Wizards", "vitorias": 6, "derrotas": 24, "conferencia": "Leste"},
            {"time": "Detroit Pistons", "vitorias": 3, "derrotas": 27, "conferencia": "Leste"}
        ]
        
        self.conferencia_oeste = [
            {"time": "Minnesota Timberwolves", "vitorias": 22, "derrotas": 6, "conferencia": "Oeste"},
            {"time": "Oklahoma City Thunder", "vitorias": 21, "derrotas": 9, "conferencia": "Oeste"},
            {"time": "Denver Nuggets", "vitorias": 21, "derrotas": 10, "conferencia": "Oeste"},
            {"time": "Los Angeles Clippers", "vitorias": 19, "derrotas": 12, "conferencia": "Oeste"},
            {"time": "Sacramento Kings", "vitorias": 18, "derrotas": 12, "conferencia": "Oeste"},
            {"time": "Dallas Mavericks", "vitorias": 18, "derrotas": 13, "conferencia": "Oeste"},
            {"time": "New Orleans Pelicans", "vitorias": 18, "derrotas": 14, "conferencia": "Oeste"},
            {"time": "Phoenix Suns", "vitorias": 16, "derrotas": 15, "conferencia": "Oeste"},
            {"time": "Los Angeles Lakers", "vitorias": 17, "derrotas": 16, "conferencia": "Oeste"},
            {"time": "Houston Rockets", "vitorias": 15, "derrotas": 15, "conferencia": "Oeste"},
            {"time": "Golden State Warriors", "vitorias": 15, "derrotas": 17, "conferencia": "Oeste"},
            {"time": "Utah Jazz", "vitorias": 14, "derrotas": 19, "conferencia": "Oeste"},
            {"time": "Memphis Grizzlies", "vitorias": 11, "derrotas": 20, "conferencia": "Oeste"},
            {"time": "Portland Trail Blazers", "vitorias": 9, "derrotas": 22, "conferencia": "Oeste"},
            {"time": "San Antonio Spurs", "vitorias": 5, "derrotas": 26, "conferencia": "Oeste"}
        ]

        # Prêmios da NBA corrigidos e completos
        self.premios = {
            "mvp": {
                "titulo": "🏆 MVP (Jogador Mais Valioso)",
                "candidatos": [
                    {"posicao": 1, "jogador": "Nikola Jokić", "time": "Denver Nuggets", "estatisticas": "29,6 PPG, 12,7 RPG, 10,2 APG"},
                    {"posicao": 2, "jogador": "Luka Dončić", "time": "Dallas Mavericks", "estatisticas": "34,2 PPG, 9,1 RPG, 9,8 APG"},
                    {"posicao": 3, "jogador": "Shai Gilgeous-Alexander", "time": "Oklahoma City Thunder", "estatisticas": "32,7 PPG, 5,0 RPG, 6,4 APG"},
                    {"posicao": 4, "jogador": "Giannis Antetokounmpo", "time": "Milwaukee Bucks", "estatisticas": "30,4 PPG, 11,9 RPG, 6,5 APG"},
                    {"posicao": 5, "jogador": "Anthony Edwards", "time": "Minnesota Timberwolves", "estatisticas": "27,6 PPG, 5,7 RPG, 4,5 APG, 1,2 SPG"}
                ]
            },
            "defensor": {
                "titulo": "🛡️ Defensor do Ano",
                "candidatos": [
                    {"posicao": 1, "jogador": "Jaren Jackson Jr.", "time": "Memphis Grizzlies", "estatisticas": "3,2 BLK, 1,1 SPG, 18,5 PPG"},
                    {"posicao": 2, "jogador": "Evan Mobley", "time": "Cleveland Cavaliers", "estatisticas": "2,3 BLK, 0,8 SPG, 18,5 PPG, 9,3 RPG"},
                    {"posicao": 3, "jogador": "Giannis Antetokounmpo", "time": "Milwaukee Bucks", "estatisticas": "1,8 BLK, 1,2 SPG, 11,9 RPG"},
                    {"posicao": 4, "jogador": "Brook Lopez", "time": "Milwaukee Bucks", "estatisticas": "2,7 BLK, 0,8 SPG, 12,8 PPG"},
                    {"posicao": 5, "jogador": "Anthony Davis", "time": "Los Angeles Lakers", "estatisticas": "2,3 BLK, 1,0 SPG, 12,5 RPG"}
                ]
            },
            "sexto_homem": {
                "titulo": "💺 Sexto Homem do Ano",
                "candidatos": [
                    {"posicao": 1, "jogador": "Malik Monk", "time": "Sacramento Kings", "estatisticas": "15,8 PPG, 5,2 APG, 44% 3PT"},
                    {"posicao": 2, "jogador": "Bobby Portis", "time": "Milwaukee Bucks", "estatisticas": "13,4 PPG, 7,1 RPG, 50% FG"},
                    {"posicao": 3, "jogador": "Norman Powell", "time": "Los Angeles Clippers", "estatisticas": "13,8 PPG, 41% 3PT, 88% FT"},
                    {"posicao": 4, "jogador": "Immanuel Quickley", "time": "Toronto Raptors", "estatisticas": "16,2 PPG, 4,8 APG, 39% 3PT"},
                    {"posicao": 5, "jogador": "Naz Reid", "time": "Minnesota Timberwolves", "estatisticas": "12,5 PPG, 5,8 RPG, 36% 3PT"}
                ]
            },
            "calouro": {
                "titulo": "🌟 Calouro do Ano",
                "candidatos": [
                    {"posicao": 1, "jogador": "Victor Wembanyama", "time": "San Antonio Spurs", "estatisticas": "21,8 PPG, 10,5 RPG, 3,4 BLK"},
                    {"posicao": 2, "jogador": "Chet Holmgren", "time": "Oklahoma City Thunder", "estatisticas": "18,2 PPG, 8,1 RPG, 2,5 BLK"},
                    {"posicao": 3, "jogador": "Brandon Miller", "time": "Charlotte Hornets", "estatisticas": "16,8 PPG, 4,2 RPG, 38% 3PT"},
                    {"posicao": 4, "jogador": "Scoot Henderson", "time": "Portland Trail Blazers", "estatisticas": "14,5 PPG, 5,2 APG, 1,1 SPG"},
                    {"posicao": 5, "jogador": "Amen Thompson", "time": "Houston Rockets", "estatisticas": "12,3 PPG, 7,8 RPG, 4,1 APG"}
                ]
            },
            "melhorado": {
                "titulo": "📈 Jogador Mais Melhorado",
                "candidatos": [
                    {"posicao": 1, "jogador": "Tyrese Maxey", "time": "Philadelphia 76ers", "estatisticas": "25,9 PPG, 6,8 APG, 44% 3PT"},
                    {"posicao": 2, "jogador": "Alperen Şengün", "time": "Houston Rockets", "estatisticas": "21,3 PPG, 9,5 RPG, 5,1 APG"},
                    {"posicao": 3, "jogador": "Jalen Williams", "time": "Oklahoma City Thunder", "estatisticas": "19,8 PPG, 4,6 RPG, 4,9 APG"},
                    {"posicao": 4, "jogador": "Coby White", "time": "Chicago Bulls", "estatisticas": "19,2 PPG, 5,3 APG, 39% 3PT"},
                    {"posicao": 5, "jogador": "Scottie Barnes", "time": "Toronto Raptors", "estatisticas": "20,1 PPG, 8,5 RPG, 6,1 APG"}
                ]
            },
            "treinador": {
                "titulo": "👔 Treinador do Ano",
                "candidatos": [
                    {"posicao": 1, "jogador": "Mark Daigneault", "time": "Oklahoma City Thunder", "estatisticas": "Liderou reconstrução bem-sucedida"},
                    {"posicao": 2, "jogador": "Chris Finch", "time": "Minnesota Timberwolves", "estatisticas": "Melhor campanha da Conferência Oeste"},
                    {"posicao": 3, "jogador": "Joe Mazzulla", "time": "Boston Celtics", "estatisticas": "Melhor campanha da NBA"},
                    {"posicao": 4, "jogador": "Jamahl Mosley", "time": "Orlando Magic", "estatisticas": "Surpresa positiva da temporada"},
                    {"posicao": 5, "jogador": "Tom Thibodeau", "time": "New York Knicks", "estatisticas": "Defesa consistentemente entre as melhores"}
                ]
            }
        }
        
        # Navegação
        self.nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
                ft.NavigationBarDestination(icon=ft.Icons.NEWSPAPER, label="Notícias"),
                ft.NavigationBarDestination(icon=ft.Icons.SPORTS_BASKETBALL, label="Jogos"),
                ft.NavigationBarDestination(icon=ft.Icons.STORE, label="Loja"),
                ft.NavigationBarDestination(icon=ft.Icons.LEADERBOARD, label="Classificação"),
                ft.NavigationBarDestination(icon=ft.Icons.EMOJI_EVENTS, label="Prêmios"),
            ],
            on_change=self.mudar_pagina,
            bgcolor="#2a2a2a"
        )
        
        # Conteúdo principal
        self.conteudo = ft.Container(expand=True)
        
        # Layout principal
        page.add(
            ft.Column([
                self.criar_header(),
                ft.Container(content=self.conteudo, expand=True),
                self.nav_bar
            ], expand=True)
        )
        
        # Carregar página inicial
        self.carregar_pagina_inicial()
    
    def criar_header(self):
        return ft.Container(
            content=ft.Row([
                ft.Text("NBA PRO", size=24, weight=ft.FontWeight.BOLD, color="#ff6b00"),
                ft.Icon(ft.Icons.SPORTS_BASKETBALL, color="#ff6b00")
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="#2a2a2a",
            padding=15,
            border_radius=ft.border_radius.only(bottom_left=10, bottom_right=10)
        )
    
    def mudar_pagina(self, e):
        index = e.control.selected_index
        if index == 0:
            self.carregar_pagina_inicial()
        elif index == 1:
            self.carregar_noticias()
        elif index == 2:
            self.carregar_mini_games()
        elif index == 3:
            self.carregar_loja()
        elif index == 4:
            self.carregar_classificacao()
        elif index == 5:
            self.carregar_premios()
        self.page.update()
    
    def carregar_pagina_inicial(self):
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Bem-vindo ao NBA Pro!", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("Seu app completo de basquete", size=16, color="grey"),
                    
                    ft.Row([
                        self.criar_card("📊", "Estatísticas", "Veja as estatísticas dos jogadores"),
                        self.criar_card("🏆", "Prêmios", "Corrida por prêmios"),
                    ]),
                    
                    ft.Row([
                        self.criar_card("📰", "Notícias", "Últimas do basquete"),
                        self.criar_card("🛒", "Loja", "Produtos oficiais"),
                    ]),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Jogo em Destaque", size=20, weight=ft.FontWeight.BOLD),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.Row([
                                            ft.Text("Lakers", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("112", size=24, weight=ft.FontWeight.BOLD, color="#ff6b00"),
                                            ft.Text("-"),
                                            ft.Text("108", size=24, weight=ft.FontWeight.BOLD, color="#ff6b00"),
                                            ft.Text("Warriors", size=18, weight=ft.FontWeight.BOLD),
                                        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                                    ]),
                                    padding=20
                                )
                            )
                        ]),
                        margin=ft.margin.only(top=20)
                    )
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content
    
    def criar_card(self, emoji, titulo, subtitulo):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(emoji, size=30),
                    ft.Text(titulo, weight=ft.FontWeight.BOLD),
                    ft.Text(subtitulo, size=12, color="grey")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=15,
                width=150,
                height=100,
                on_click=self.ao_clicar_card
            ),
            elevation=5
        )
    
    def ao_clicar_card(self, e):
        self.page.show_snack_bar(ft.SnackBar(ft.Text("Navegando para a funcionalidade...")))
    
    def carregar_noticias(self):
        noticias_widgets = []
        for noticia in self.noticias:
            noticias_widgets.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text(noticia["imagem"], size=24),
                                ft.Column([
                                    ft.Text(noticia["titulo"], weight=ft.FontWeight.BOLD),
                                    ft.Text(noticia["data"], size=12, color="grey")
                                ], expand=True)
                            ]),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text(noticia["conteudo"], size=14),
                                    ft.Container(
                                        content=ft.Text(f"🏅 {noticia['destaque']}", color="#ff6b00", weight=ft.FontWeight.BOLD),
                                        margin=ft.margin.only(top=10)
                                    )
                                ]),
                                padding=10,
                                bgcolor="#2a2a2a",
                                border_radius=10
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("💬 Discussões:", weight=ft.FontWeight.BOLD),
                                    *[ft.Text(f"• {comentario}", size=12) for comentario in noticia["comentarios"]]
                                ]),
                                padding=10,
                                bgcolor="#1a1a1a",
                                border_radius=10,
                                margin=ft.margin.only(top=10)
                            )
                        ]),
                        padding=15
                    )
                )
            )
        
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Últimas Notícias", size=24, weight=ft.FontWeight.BOLD),
                    *noticias_widgets
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content
    
    def iniciar_timer(self):
        if self.tempo_restante > 0 and self.timer_ativo:
            self.tempo_restante -= 1
            self.carregar_mini_games()
            if self.tempo_restante > 0:
                self.page.run_task(self.iniciar_timer)
            else:
                self.timer_ativo = False
                self.page.show_snack_bar(ft.SnackBar(ft.Text("⏰ Tempo esgotado! Jogo finalizado.")))
    
    def carregar_mini_games(self):
        game1 = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("🏀 Arremesso de 3 Pontos", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Pontuação: {self.pontuacao_jogo}", size=16),
                    ft.Text(f"Tempo: {self.tempo_restante}s", size=16, color="#ff6b00" if self.tempo_restante < 10 else "white"),
                    
                    ft.Row([
                        ft.ElevatedButton(
                            "Arremesso!",
                            on_click=self.fazer_arremesso,
                            bgcolor="#ff6b00",
                            color="white"
                        ),
                        ft.ElevatedButton(
                            "Iniciar Timer",
                            on_click=self.iniciar_jogo
                        ),
                        ft.ElevatedButton(
                            "Reiniciar",
                            on_click=self.reiniciar_jogo
                        )
                    ])
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            )
        )
        
        game2 = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("🧠 Quiz NBA", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Teste seu conhecimento sobre basquete!", size=14),
                    ft.ElevatedButton(
                        "Iniciar Quiz",
                        on_click=self.iniciar_quiz
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            )
        )
        
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Mini Games", size=24, weight=ft.FontWeight.BOLD),
                    game1,
                    game2
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content
    
    def iniciar_jogo(self, e):
        if not self.timer_ativo:
            self.timer_ativo = True
            self.tempo_restante = 30
            self.pontuacao_jogo = 0
            self.page.show_snack_bar(ft.SnackBar(ft.Text("🎮 Jogo iniciado! Você tem 30 segundos.")))
            self.iniciar_timer()
    
    def fazer_arremesso(self, e):
        if self.tempo_restante > 0:
            resultado = random.random()
            if resultado < 0.3:
                pontos = 0
                mensagem = "Arremesso errado! 😅"
            elif resultado < 0.7:
                pontos = 2
                mensagem = "Cesta de 2 pontos! 🎯"
            else:
                pontos = 3
                mensagem = "Cesta de 3 pontos! 🔥"
            
            self.pontuacao_jogo += pontos
            self.page.show_snack_bar(ft.SnackBar(ft.Text(mensagem)))
            self.carregar_mini_games()
        else:
            self.page.show_snack_bar(ft.SnackBar(ft.Text("⏰ Tempo esgotado! Reinicie o jogo.")))
    
    def reiniciar_jogo(self, e):
        self.pontuacao_jogo = 0
        self.tempo_restante = 30
        self.timer_ativo = False
        self.carregar_mini_games()
        self.page.show_snack_bar(ft.SnackBar(ft.Text("🔄 Jogo reiniciado!")))
    
    def iniciar_quiz(self, e):
        self.page.show_snack_bar(ft.SnackBar(ft.Text("📝 Quiz em desenvolvimento em breve!")))
    
    def carregar_loja(self):
        produtos_widgets = []
        for produto in self.produtos_loja:
            produtos_widgets.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text(produto["imagem"], size=30),
                                ft.Column([
                                    ft.Text(produto["nome"], weight=ft.FontWeight.BOLD),
                                    ft.Text(produto["preco"], color="#ff6b00"),
                                    ft.Text(produto["categoria"], size=12, color="grey")
                                ], expand=True)
                            ]),
                            ft.ElevatedButton(
                                "🛒 Comprar", 
                                on_click=lambda e, p=produto: self.comprar_produto(p),
                                bgcolor="#ff6b00",
                                color="white"
                            )
                        ]),
                        padding=15
                    )
                )
            )
        
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Loja NBA", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Produtos oficiais da NBA", size=16, color="grey"),
                    *produtos_widgets
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content
    
    def comprar_produto(self, produto):
        self.page.show_snack_bar(ft.SnackBar(ft.Text(f"🛒 {produto['nome']} adicionado ao carrinho!")))
    
    def criar_tabela_classificacao(self, times, titulo):
        header = ft.Container(
            content=ft.Row([
                ft.Text("#", width=30, weight=ft.FontWeight.BOLD),
                ft.Text("Time", expand=1, weight=ft.FontWeight.BOLD),
                ft.Text("V", width=30, weight=ft.FontWeight.BOLD),
                ft.Text("D", width=30, weight=ft.FontWeight.BOLD),
                ft.Text("%", width=50, weight=ft.FontWeight.BOLD),
            ]),
            padding=10,
            bgcolor="#ff6b00",
            border_radius=5
        )
        
        linhas = [header]
        for i, time in enumerate(times, 1):
            porcentagem = time["vitorias"] / (time["vitorias"] + time["derrotas"])
            cor_fundo = "#2a2a2a" if i % 2 == 0 else "#1a1a1a"
            
            linha = ft.Container(
                content=ft.Row([
                    ft.Text(f"{i}°", width=30),
                    ft.Text(time["time"], expand=1),
                    ft.Text(str(time["vitorias"]), width=30),
                    ft.Text(str(time["derrotas"]), width=30),
                    ft.Text(f"{porcentagem:.3f}", width=50),
                ]),
                padding=10,
                bgcolor=cor_fundo,
                border_radius=5
            )
            linhas.append(linha)
        
        return ft.Column([
            ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Column(linhas),
                margin=ft.margin.only(bottom=20)
            )
        ])
    
    def carregar_classificacao(self):
        tabela_leste = self.criar_tabela_classificacao(self.conferencia_leste, "🏀 Conferência Leste")
        tabela_oeste = self.criar_tabela_classificacao(self.conferencia_oeste, "🏀 Conferência Oeste")
        
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Classificação da NBA", size=24, weight=ft.FontWeight.BOLD),
                    tabela_leste,
                    tabela_oeste,
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content

    def criar_tabela_premio(self, premio_data):
        header = ft.Container(
            content=ft.Row([
                ft.Text("#", width=40, weight=ft.FontWeight.BOLD),
                ft.Text("Jogador", expand=2, weight=ft.FontWeight.BOLD),
                ft.Text("Time", expand=1, weight=ft.FontWeight.BOLD),
                ft.Text("Estatísticas", expand=3, weight=ft.FontWeight.BOLD),
            ]),
            padding=12,
            bgcolor="#ff6b00",
            border_radius=5
        )
        
        linhas = [header]
        for candidato in premio_data["candidatos"]:
            cor_fundo = "#2a2a2a" if candidato["posicao"] % 2 == 0 else "#1a1a1a"
            
            linha = ft.Container(
                content=ft.Row([
                    ft.Text(f"{candidato['posicao']}°", width=40, weight=ft.FontWeight.BOLD),
                    ft.Text(candidato["jogador"], expand=2, weight=ft.FontWeight.BOLD),
                    ft.Text(candidato["time"], expand=1),
                    ft.Text(candidato["estatisticas"], expand=3, size=12),
                ]),
                padding=10,
                bgcolor=cor_fundo,
                border_radius=5
            )
            linhas.append(linha)
        
        return ft.Column([
            ft.Text(premio_data["titulo"], size=18, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Column(linhas),
                margin=ft.margin.only(bottom=20)
            )
        ])

    def carregar_premios(self):
        premios_widgets = []
        
        for premio_key, premio_data in self.premios.items():
            premios_widgets.append(self.criar_tabela_premio(premio_data))
        
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("🏆 Prêmios da NBA 2024-25", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("Candidatos e estatísticas para os principais prêmios", size=16, color="grey"),
                    *premios_widgets
                ]),
                padding=20
            )
        ], scroll=ft.ScrollMode.ADAPTIVE)
        
        self.conteudo.content = content

# Executar o app
if __name__ == "__main__":
    ft.app(target=BasqueteApp().main)