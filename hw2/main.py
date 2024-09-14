"""
Converts temps from F to C and C to F.
"""

from typing import Callable

import tkinter as tk

from functions.conversions import c_to_f, f_to_c

window = tk.Tk()
window.title("CIS 410 HW2: Convert Temp")
window.geometry("400x400")

temp_to_convert = tk.IntVar()
temp_to_convert_entry = tk.Entry(window, textvariable=temp_to_convert).pack()

lbl_text = tk.StringVar()
lbl_text.set("No data yet")
output_lbl = tk.Label(window, textvariable=lbl_text).pack()


def btn_call_wrapper(func: Callable) -> None:
    """
    Runs the passed function and updates the label based on the conversion

    Args:
        func (Callable): function to convert the number in the entry box
        reads from temp_to_convert

    Returns:
        None
    """
    converted = func(temp_to_convert.get())

    if func == c_to_f:
        output = f"{temp_to_convert.get()} C convetred to F: {round(converted)}"

    if func == f_to_c:
        output = f"{temp_to_convert.get()} F converted to C: {round(converted)}"

    lbl_text.set(output)


def main() -> None:

    convert_to_f_btn = tk.Button(
        window, text="to F", command=lambda: btn_call_wrapper(c_to_f), width=50, height=10, background="#FF6103"
    )
    convert_to_f_btn.pack()

    convert_to_c_btn = tk.Button(
        window, text="to C", command=lambda: btn_call_wrapper(f_to_c), width=50, height=10, background="#00FFFF"
    )
    convert_to_c_btn.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
