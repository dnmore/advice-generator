from tkinter import *
import requests

def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    response.raise_for_status()
    data = response.json()
    advice = data["slip"]["advice"]
    canvas.itemconfig(advice_text, text=advice)


window = Tk()
window.title("Need a piece of advice?")
window.config(padx=50, pady=50)

canvas = Canvas(width=640, height=320)
background_image = PhotoImage(file="background.png")
canvas.create_image(320, 160, image=background_image)
advice_text = canvas.create_text(280, 160, text="Click the emoji!", width=400, font=("Arial", 16, "bold"))

canvas.grid(column=0, row=0)

emoji_image = PhotoImage(file="emoji.png")
emoji_button = Button(image=emoji_image, borderwidth=5, command=get_advice, cursor="hand2")
emoji_button.grid(column=0, row=1)
window.mainloop()
