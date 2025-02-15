import flet as f

def main(page: f.Page):
    
    page.title = "Lista de tareeas"
    page.horizontal_alignment = f.CrossAxisAlignment.CENTER

    def agregar_tarea(e):
       if textfield.value.strip():  # Evita agregar tareas vacías
            lista_tareas.controls.append(f.Text(value=textfield.value))
            textfield.value = ""  # Limpia el campo
            page.update()  # Actualiza la interfaz


    textfield1 = f.Text(
        value="TASK-LIST",
        text_align=f.TextAlign.CENTER,  # Centrar texto
        color="white",  # Color del texto
        weight=f.FontWeight.BOLD,  # Texto en negrita
        size=20,  # Tamaño de la fuente
        width=200,  # Ancho del texto
        height=50,  # Altura
    )
    textfield = f.TextField(
        hint_text="Ingrese una tarea...",  # Cambié 'value' por 'hint_text' para mayor claridad
        text_align="center",
        bgcolor="#00782f",
    )
    lista_tareas = f.Column()

    page.add(textfield1, textfield)
    page.add(
        f.ElevatedButton(
            text="Ingresar",
            on_click=agregar_tarea
        ),  lista_tareas
    )
    

f.app(main)