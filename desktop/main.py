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

    page.scroll = "adaptative"
    page.padding = 50

    def add_note(e):
        new_note = crear_nota("nueva nota")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def crear_nota(text):
        note_content = f.TextField(value=text, multiline=True)

        note = f.Container(
            content=f.Column([note_content, f.IconButton(
                icon=f.icons.DELETE,
                on_click=lambda _: delete_note(note)
                )]),
                width=200,
                height=200,
                bgcolor="#070017",
                border_radius=10,
                padding=10
        )
        return note

    grid = f.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10
    )
    notas = [
    ] 

    for note in notas:
        grid.controls.append(crear_nota(note))


    page.add(f.Row([
        f.Text("Mis notas", size=24, weight="bold"),
        f.IconButton(icon = f.Icons.ADD, on_click=add_note)], 
        alignment=f.MainAxisAlignment.SPACE_BETWEEN),
        grid
        )
f.app(main)