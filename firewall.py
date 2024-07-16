import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageGrab
import pytesseract
import random
import string
import os

class AuthApp:
    def __init__(self, root):
        self.root = root
        self.name_var = tk.StringVar()
        self.passw_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Login Page")
        self.root.geometry("500x600")
        self.root.configure(background="skyblue")


        # Title
        tk.Label(self.root, text='Login Page', font=('calibre', 20, 'bold'), bg='#f0f0f0').pack(pady=20)

        # Setup the login form
        form_frame = tk.Frame(self.root, bg='#f0f0f0')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text='Username', font=('calibre', 10, 'bold'), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text='Password', font=('calibre', 10, 'bold'), bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.passw_var, font=('calibre', 10, 'normal'), show='*').grid(row=1, column=1, padx=5, pady=5)
        
        # Setup the CAPTCHA section
        self.image_canvas = tk.Canvas(self.root, bg='white', width=400, height=100)
        self.image_canvas.pack(pady=10)

        self.draw_canvas_frame = tk.Frame(self.root, bg='black', bd=2)
        self.draw_canvas_frame.pack(pady=10)
        self.draw_canvas = tk.Canvas(self.draw_canvas_frame, bg='white', width=400, height=100)
        self.draw_canvas.pack()

        self.text_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.text_frame.pack(pady=10)

        tk.Button(self.text_frame, text="Clear", command=self.clear_canvas, bg='#d9534f', fg='white').grid(row=0, column=0, padx=5)
        tk.Button(self.text_frame, text="Verify and Submit", command=self.verify_and_submit, bg='#5cb85c', fg='white').grid(row=0, column=1, padx=5)

        self.generate_text()
        self.display_text_image()

        self.draw_canvas.bind("<B1-Motion>", self.paint)
        self.draw_canvas.bind("<ButtonRelease-1>", self.reset)

        self.last_x, self.last_y = None, None

    def submit(self):
        name = self.name_var.get()
        password = self.passw_var.get()
        
        print("The name is:", name)
        print("The password is:", password)
        
        self.name_var.set("")
        self.passw_var.set("")

    def generate_text(self):
        self.generated_text = ''.join(random.choices(string.ascii_uppercase, k=4))
        print(f"Generated Text: {self.generated_text}")  # For debugging

    def display_text_image(self):
        width, height = 400, 100
        self.text_image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(self.text_image)
        font = ImageFont.truetype("arial.ttf", size=48)

        text_bbox = draw.textbbox((0, 0), self.generated_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), self.generated_text, font=font, fill='black')
        self.text_image.save("text_image.png")

        self.text_image_tk = tk.PhotoImage(file="text_image.png")
        self.image_canvas.create_image(200, 50, image=self.text_image_tk)

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.draw_canvas.create_line(self.last_x, self.last_y, x, y, fill='black', width=3)
        self.last_x, self.last_y = x, y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.draw_canvas.delete("all")

    def verify_and_submit(self):
        self.draw_canvas.update()
        file_path = "drawing.png"
        x = self.root.winfo_rootx() + self.draw_canvas.winfo_x() + 100
        y = self.root.winfo_rooty() + self.draw_canvas.winfo_y() + 410
        x1 = x + self.draw_canvas.winfo_width()
        y1 = y + self.draw_canvas.winfo_height()

        crop_box = (x + 2, y + 2, x1 - 2, y1 - 2)
        ImageGrab.grab(bbox=crop_box).save(file_path)

        image = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ').strip().replace(" ", "")
        print(f"Extracted Text: {extracted_text}")  # For debugging

        if extracted_text == self.generated_text:
            messagebox.showinfo("Success", "Authentication Passed")
            self.submit()
        else:
            messagebox.showerror("Failed", "Authentication Failed. Please try again.")
            self.clear_canvas()
            self.generate_text()
            self.display_text_image()

        os.startfile(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()
