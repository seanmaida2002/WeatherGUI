import tkinter as tk
from tkinter import ttk
from weather_automation import get_current_weather, get_current_date
import urllib.request
import io
from PIL import Image, ImageTk
global_image = None


def display_information(city):
    root = tk.Tk()
    root.title("WeatherGUI")
    root.minsize(200, 200)
    root.geometry("500x500")
    root.configure(bg="#87CEEB") 

    current_date = get_current_date()
    tk.Label(
        root, 
        text="Today's Date: " + current_date,
        background="#87CEEB",
        foreground="black",
        font=("Helvetica", 20, "bold"),
        pady=10
        ).pack()
    tk.Label(
        root, 
        text="Location: " + city,
        background="#87CEEB",
        foreground="black",
        font=("Helvetica", 20, "bold"),
        pady=10
        ).pack()


    weather_information = get_current_weather(city)
    weather_condition = weather_information["weather_condition"]
    tk.Label(
        root, 
        text="Weather Condition: " + weather_condition,
        background="#87CEEB",
        foreground="black",
        font=("Helvetica", 20, "bold"),
        pady=10
        ).pack()

    temperature = weather_information["temperature"]
    degree_symbol = '\u00b0'
    tk.Label(
        root, 
        text=f"Temperature: " + str(temperature) + degree_symbol + "F",
        background="#87CEEB",
        foreground="black",
        font=("Helvetica", 20, "bold"),
        pady=10
        ).pack()

    image_url = weather_information["picture"]
    image_byt = urllib.request.urlopen("https:" + image_url).read()
    image_buf = io.BytesIO(image_byt)
    pil_image = Image.open(image_buf)
    tk_image = ImageTk.PhotoImage(pil_image)
    global_image = tk_image
    img_label = tk.Label(root, image=tk_image, bg="#87CEEB")
    img_label.image = tk_image
    img_label.pack()

    btn= tk.Button(
        root,
        text='Enter New City',
        font=('Helvetica', 11, 'bold'),
        bg="#4DD0E1",
        fg="black",
        activebackground="#00ACC1",
        activeforeground="white",
        padx=10,
        pady=5,
        command=lambda: enter_new_city_button(root)
    )
    btn.pack(pady=20)

    root.mainloop()

def enter_new_city_button(root):
    root.destroy()
    gui()
    

def submit(city_var, root):
    city=city_var.get()
    root.destroy()
    display_information(city)

def gui():
    root = tk.Tk()
    root.title("WeatherGUI")
    root.minsize(300, 300)
    root.geometry("350x250+100+100")
    root.configure(bg="#87CEEB") 

    # Title label
    tk.Label(
        root,
        text="🌤️ Welcome to WeatherGUI",
        background="#87CEEB",
        foreground="black",
        font=("Helvetica", 20, "bold"),
        pady=10
    ).pack()

    # Frame for input
    frame = tk.Frame(root, bg="#87CEEB")
    frame.pack(pady=20)

    city_var = tk.StringVar()

    city_label = tk.Label(
        frame,
        text='Enter City:',
        font=('Helvetica', 16),
        bg="#87CEEB",
        fg="black"
    )
    city_label.pack(side='left', padx=(0, 10))

    city_entry = tk.Entry(
        frame,
        textvariable=city_var,
        font=('Helvetica', 16),
        width=20,
        bg="#FFFFFF",
        fg="black"
    )
    city_entry.pack(side='left')

    # Submit button
    sub_btn = tk.Button(
        root,
        text='Check Weather',
        font=('Helvetica', 11, 'bold'),
        bg="#4DD0E1",
        fg="black",
        activebackground="#00ACC1",
        activeforeground="white",
        padx=10,
        pady=5,
        command=lambda: submit(city_var, root)
    )
    sub_btn.pack(pady=20)

    root.mainloop()

def main():
    gui()

if __name__ == "__main__":
    main()
