import tkinter as tk
import os

def run_script():
    project_name = project_name_entry.get()
    num_days = num_days_var.get()

    if int(num_days) <= 1:
        print("Number of days should be greater than 1")
        return

    number_start = "0" if include_today_var.get() else "1"

    language = "fr_FR" if language_var.get() == "Français" else "en_EN"

    with open('script.sh', 'r') as file:
        script = file.read()

    script = script.replace('$project_name$', project_name)
    script = script.replace('$number_days$', num_days)
    script = script.replace('$number_start$', number_start)
    script = script.replace('$language$', language)

    os.system(script)

def validate(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

root = tk.Tk()
root.title("Things Toolkit")

tk.Label(root, text="Project Name:").grid(row=0, column=0, sticky='e')
project_name_entry = tk.Entry(root)
project_name_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Days:").grid(row=1, column=0, sticky='e')
num_days_var = tk.StringVar()
num_days_entry = tk.Entry(root, textvariable=num_days_var, validate="key", validatecommand=(root.register(validate), '%P'))
num_days_entry.grid(row=1, column=1)

include_today_var = tk.IntVar()
tk.Checkbutton(root, text="Include Today", variable=include_today_var).grid(row=2, column=0, columnspan=2)

tk.Label(root, text="Language:").grid(row=3, column=0, sticky='e')
language_var = tk.StringVar(root)
language_var.set("Français") # default value
tk.OptionMenu(root, language_var, "Français", "English").grid(row=3, column=1)

run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
