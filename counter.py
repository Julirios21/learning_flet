import flet as ft

def main(page: ft.Page):
    
    page.add(
        ft.Row(
             [
                ft.IconButton(ft.Icons.REMOVE),
                ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100),
                ft.IconButton(ft.Icons.ADD),
            ],
        )
    )
    
ft.app(main)