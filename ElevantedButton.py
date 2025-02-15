import flet as f

def main(page: f.Page):
    page.add(f.ElevatedButton(
        text="que que?",
        icon=f.icons.CHECK)
    )
    page.add(f.TextButton(
        text="que texto?",
        icon=f.icons.CHECK)
    )
    page.add(f.OutlinedButton(
        text="outlinebutton?",
        icon=f.icons.CHECK)
    )
    page.add(f.IconButton(
        icon=f.icons.SMART_BUTTON)
    )
    
    

f.app(main)