import tkinter as tk
from weather_automation import get_current_weather, get_current_date
import urllib.request
import io
from PIL import Image, ImageTk
global_image = None


def display_information(city):
    root = tk.Tk()
    root.title("WeatherGUI")
    root.minsize(200, 200)
    root.geometry("300x300+50+50")

    current_date = get_current_date()
    tk.Label(root, text="Today's Date: " + current_date).pack()
    tk.Label(root, text="Location: " + city).pack()


    weather_information = get_current_weather(city)
    weather_condition = weather_information["weather_condition"]
    tk.Label(root, text="Weather Condition: " + weather_condition).pack()

    temperature = weather_information["temperature"]
    degree_symbol = '\u00b0'
    tk.Label(root, text=f"Temperature: " + str(temperature) + degree_symbol + "F").pack()

    image_url = weather_information["picture"]
    image_byt = urllib.request.urlopen("https:" + image_url).read()
    image_buf = io.BytesIO(image_byt)
    pil_image = Image.open(image_buf)
    tk_image = ImageTk.PhotoImage(pil_image)
    global_image = tk_image
    img_label = tk.Label(root, image=tk_image)
    img_label.image = tk_image
    img_label.pack()

    btn = tk.Button(root, text='Enter New City', command=lambda: enter_new_city_button(root))
    btn.pack(pady=10)
    

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
    root.minsize(200, 200)
    root.geometry("300x300+50+50")

    tk.Label(root, text="Welcome to WeatherGUI").pack()

    frame = tk.Frame(root)
    frame.pack()

    city_var = tk.StringVar()

    city_label = tk.Label(frame, text='City', font=('calibre', 10, 'bold'))
    city_entry = tk.Entry(frame, textvariable=city_var, font=('calibre', 10, 'normal'))

    city_label.pack(side='left')
    city_entry.pack(side='left')

    sub_btn = tk.Button(root, text='Submit', command=lambda: submit(city_var, root))
    sub_btn.pack(pady=10)

    root.mainloop()

def main():
    gui()

if __name__ == "__main__":
    main()
