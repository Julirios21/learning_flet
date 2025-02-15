import flet as f

def main(page: f.Page):
    dispositivo = page.platform

    if dispositivo in ["android", "ios"]:
        page.window_width = 400
        page.window_height = 700
    else:
        page.window_width = 1024
        page.window_height = 768
        page.window_maximized = True  # Maximiza en escritorio

    fila = f.ResponsiveRow(
        controls=[
            f.Container(f.Text("Elemento 1"), bgcolor="blue", padding=20, col={"sm": 12, "md": 6, "lg": 4}),
            f.Container(f.Text("Elemento 2"), bgcolor="green", padding=20, col={"sm": 12, "md": 6, "lg": 4}),
            f.Container(f.Text("Elemento 3"), bgcolor="red", padding=20, col={"sm": 12, "md": 6, "lg": 4}),
        ]
    )

    page.add(fila)
f.app(main)