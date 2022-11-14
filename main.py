import requests
import tkinter

BACKGROUND = "white"
FONT_NAME = "Courier"
word_count = 0


#--------------------------------------------------------------------GETTING KANYE QUOTE
def next_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote, text=data["quote"])


#-------------------------------------------------------------------------------UI SETUP
window = tkinter.Tk()
window.title("Kanye Quotes")
window.config(padx=20, pady=20, height=1000, width=300, bg=BACKGROUND)

#---------------------------------------------------------------PHOTOS
kanye_photo = tkinter.PhotoImage(file="Photos/kanye.png")
kanye = kanye_photo.subsample(6, 6)
quote_box_photo = tkinter.PhotoImage(file="Photos/quotation_box.png")
quote_box = quote_box_photo.subsample(4, 4)

#---------------------------------------------------------------CANVAS
canvas = tkinter.Canvas(width=350,
                        height=580,
                        bg=BACKGROUND,
                        highlightthickness=0)
canvas.create_image(175, 300, image=quote_box)
quote = canvas.create_text(175,
                           200,
                           text="",
                           font=(FONT_NAME, 18, "bold"),
                           width=300)
canvas.grid(row=1, column=1)

#--------------------------------------------------------------BUTTONS
quote_button = tkinter.Button(image=kanye,
                              command=next_quote,
                              bg=BACKGROUND,
                              highlightthickness=0)
quote_button.grid(row=2, column=1)

#------------------------------------------------------------------------------MAINLOOP
next_quote()
window.mainloop()
