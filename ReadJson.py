import tkinter as tk
from tkinter import ttk, messagebox
import json

def load_json_data(filename="system_info.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        messagebox.showerror("Hata", f"JSON dosyası okunamadı: {e}")
        return None

def display_json_data():
  
    data = load_json_data()

    if data is None:
        return

 
    root = tk.Tk()
    root.title("Sistem Bilgileri Görüntüleyici")

   
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

   
    categories = list(data.keys()) 
    selected_category = tk.StringVar(value=categories[0])

    category_label = tk.Label(frame, text="Veri Kategorisini Seçin:")
    category_label.grid(row=0, column=0, padx=5, pady=5)

    category_menu = ttk.Combobox(frame, textvariable=selected_category, values=categories, width=40)
    category_menu.grid(row=0, column=1, padx=5, pady=5)

    text_box = tk.Text(frame, width=80, height=20)
    text_box.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    text_box.config(state=tk.DISABLED) 

    def show_selected_category():
        category = selected_category.get()
        text_box.config(state=tk.NORMAL) 
        text_box.delete(1.0, tk.END)  
        formatted_data = json.dumps(data[category], indent=4)
        text_box.insert(tk.END, formatted_data) 
        text_box.config(state=tk.DISABLED)  

    show_button = tk.Button(frame, text="Veriyi Göster", command=show_selected_category)
    show_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    display_json_data()
