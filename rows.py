import flet as f

def main(page: f.Page):
    page.add(
        f.Row(controls=[
            f.Text("value 1"),
            f.Text("value 2"),
            f.Text("value 3")
            ]
        )
    )

    page.add(
        f.Column(controls=[
            f.Text("value 1"),
            f.Text("value 2"),
            f.Text("value 3")
            ]
        )
    )

f.app(main)