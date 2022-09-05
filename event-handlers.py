import secrets
def handle_click(e):
    pyscript.write("output2", f"you clicked the button {secrets.token_hex(5)}")