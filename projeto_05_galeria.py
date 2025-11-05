import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "🎓 Galeria de Alunos - SENAI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.bgcolor = ft.Colors.BLUE_GREY_50
    
    # Dados dos alunos (nome, curso, imagem)
    alunos = [
        {
            "nome": "Ana Silva",
            "curso": "Python para Iniciantes",
            "imagem": "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024001"
        },
        {
            "nome": "Carlos Santos",
            "curso": "Desenvolvimento Web",
            "imagem": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024002"
        },
        {
            "nome": "Mariana Oliveira",
            "curso": "Data Science",
            "imagem": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024003"
        },
        {
            "nome": "João Pereira",
            "curso": "Machine Learning",
            "imagem": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024004"
        },
        {
            "nome": "Juliana Costa",
            "curso": "Python Avançado",
            "imagem": "https://images.unsplash.com/photo-1544725176-7c40e5a71c5e?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024005"
        },
        {
            "nome": "Ricardo Lima",
            "curso": "Desenvolvimento Web",
            "imagem": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024006"
        },
        {
            "nome": "Fernanda Souza",
            "curso": "Data Science",
            "imagem": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024007"
        },
        {
            "nome": "Lucas Almeida",
            "curso": "Python para Iniciantes",
            "imagem": "https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=150&h=150&fit=crop&crop=face",
            "matricula": "2024008"
        }
    ]

    # Cabeçalho
    header = ft.Container(
        content=ft.Column([
            ft.Text(
                "🎓 Galeria de Alunos",
                size=32,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Curso de Desenvolvimento com Python - SENAI",
                size=18,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Text(
                f"Total de alunos: {len(alunos)}",
                size=16,
                color=ft.Colors.GREY_700,
                weight=ft.FontWeight.W_500,
                text_align=ft.TextAlign.CENTER
            )
        ]),
        padding=20,
        margin=ft.margin.only(bottom=20),
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLACK12,
        )
    )

    # Função para criar cartão de aluno
    def criar_cartao_aluno(aluno):
        return ft.Container(
            content=ft.Column([
                # Imagem do aluno
                ft.Container(
                    content=ft.CircleAvatar(
                        foreground_image_src=aluno["imagem"],
                        radius=60,
                        tooltip=f"Foto de {aluno['nome']}"
                    ),
                    alignment=ft.alignment.center,
                    padding=10
                ),
                
                # Nome do aluno
                ft.Text(
                    aluno["nome"],
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                
                # Curso
                ft.Container(
                    content=ft.Text(
                        aluno["curso"],
                        size=14,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.W_500,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.Colors.BLUE_600,
                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                    border_radius=20
                ),
                
                # Matrícula
                ft.Text(
                    f"Matrícula: {aluno['matricula']}",
                    size=12,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER
                ),
                
                # Ícone de estudante
                ft.Icon(
                    name=ft.Icons.SCHOOL_OUTLINED,
                    color=ft.Colors.BLUE_400,
                    size=20
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
            ),
            width=200,
            padding=20,
            margin=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.BLACK12,
            ),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            # Efeito hover
            on_hover=lambda e: hover_effect(e),
        )

    # Efeito hover nos cartões
    def hover_effect(e):
        if e.data == "true":
            e.control.bgcolor = ft.Colors.BLUE_50
            e.control.scale = ft.transform.Scale(1.05)
        else:
            e.control.bgcolor = ft.Colors.WHITE
            e.control.scale = ft.transform.Scale(1.0)
        e.control.update()

    # Criar grid de cartões
    cartoes_alunos = []
    for aluno in alunos:
        cartoes_alunos.append(criar_cartao_aluno(aluno))

    # Layout responsivo em grid
    grid_alunos = ft.ResponsiveRow(
        controls=cartoes_alunos,
        run_spacing=20,
        spacing=20,
    )

    # Filtros por curso
    cursos = list(set(aluno["curso"] for aluno in alunos))
    cursos.insert(0, "Todos os Cursos")
    
    dropdown_filtro = ft.Dropdown(
        label="Filtrar por curso",
        options=[ft.dropdown.Option(curso) for curso in cursos],
        value="Todos os Cursos",
        width=300,
        on_change=lambda e: filtrar_alunos(e.control.value)
    )

    def filtrar_alunos(curso_selecionado):
        if curso_selecionado == "Todos os Cursos":
            cartoes_filtrados = [criar_cartao_aluno(aluno) for aluno in alunos]
        else:
            alunos_filtrados = [aluno for aluno in alunos if aluno["curso"] == curso_selecionado]
            cartoes_filtrados = [criar_cartao_aluno(aluno) for aluno in alunos_filtrados]
        
        grid_alunos.controls = cartoes_filtrados
        page.update()

    # Barra de filtros
    barra_filtros = ft.Container(
        content=ft.Row([
            dropdown_filtro,
            ft.IconButton(
                icon=ft.Icons.REFRESH,
                tooltip="Recarregar galeria",
                on_click=lambda e: filtrar_alunos("Todos os Cursos")
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20,
        margin=ft.margin.only(bottom=20)
    )

    # Adicionar tudo à página
    page.add(
        header,
        barra_filtros,
        grid_alunos
    )

# Executar a aplicação
if __name__ == "__main__":
    ft.app(target=main)