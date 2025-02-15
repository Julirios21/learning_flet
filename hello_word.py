import flet as ft
import time as time

def main(page: ft.Page):
   page.add(ft.Text("Hola Flet", color="green"))

   t = ft.Text(value="0", color="blue")
   page.add(t)
   for i in range(10):
      t.value = f"step {i}"
      page.update()
      time.sleep(1)
ft.app(main)