import flet as f

def main(page: f.Page):
    
    def on_text_change(e):
        print(f"Texto ingresado: {e.control.value}")

    text_field1 = f.TextField(
        label="Ingrese su nombre",
        hint_text="Escriba aquí...",
        border="outline",
        prefix_icon=f.icons.PERSON,
        suffix_icon=f.icons.CLEAR,
        max_length=20,
        on_submit=on_text_change,
        bgcolor="#005051"
    )

    text_field2 = f.TextField(
        label="Ingrese su contraseña",
        hint_text="Escriba aquí...",
        border="outline",
        prefix_icon=f.icons.LOCK,
        suffix_icon=f.icons.LOCK_OPEN,
        password=True,
        on_submit=on_text_change,
        bgcolor="#00782f"
    )

    text_field3 = f.TextField(
        label="👀",
        value="say Drake",
        border="outline",
        read_only=True,
        prefix_icon=f.icons.WALLET,
        suffix_icon=f.icons.BUSINESS_CENTER,
        on_submit=on_text_change,
        bgcolor="#2b0087",
        text_align="center"
    )
    def validar_texto(e):
        if not text_field4.value.strip():  # Verifica si está vacío
            text_field4.error_text = "Este campo no puede estar vacío"
        else:
            text_field4.error_text = None  # Elimina el error si el texto es válido
        page.update()  # Actualiza la interfaz

    text_field4 = f.TextField(
        label="Nombre",
        hint_text="Ingrese su nombre",
        prefix_icon=f.icons.PERSON,
        error_text=None,  # No muestra error inicialmente
        on_change=validar_texto,  # Valida cuando el usuario escribe
    )
    
    page.add(text_field1)
    page.add(text_field2)
    page.add(text_field3)
    page.add(text_field4)


f.app(main)