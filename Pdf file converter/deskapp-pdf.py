import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import docx2txt
import os


def pdf_to_word(input_pdf, output_docx):
    os.system(f"pandoc {input_pdf} -o {output_docx}")


def pdf_to_image(input_pdf, output_image):
    images = convert_from_path(input_pdf)
    for i, image in enumerate(images):
        image.save(f"{output_image}_{i + 1}.jpeg", "JPEG")


def get_pdf_file():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_file:
        input_pdf_entry.delete(0, tk.END)
        input_pdf_entry.insert(0, pdf_file)


def convert_pdf():
    input_pdf = input_pdf_entry.get()
    if not input_pdf:
        status_label.config(text="Please select a PDF file.")
        return

    output_format = output_format_var.get()
    if output_format == "Word":
        output_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
        if output_file:
            pdf_to_word(input_pdf, output_file)
            status_label.config(text="Conversion to Word complete.")
    elif output_format == "Image":
        output_folder = filedialog.askdirectory()
        if output_folder:
            pdf_to_image(input_pdf, output_folder)
            status_label.config(text="Conversion to Images complete.")


app = tk.Tk()
app.title("PDF Converter")

input_pdf_label = tk.Label(app, text="Select PDF file:")
input_pdf_label.pack()

input_pdf_entry = tk.Entry(app, width=50)
input_pdf_entry.pack()

browse_button = tk.Button(app, text="Browse", command=get_pdf_file)
browse_button.pack()

output_format_label = tk.Label(app, text="Select Output Format:")
output_format_label.pack()

output_format_var = tk.StringVar()
output_format_var.set("Word")

word_radio = tk.Radiobutton(app, text="Word", variable=output_format_var, value="Word")
image_radio = tk.Radiobutton(app, text="Image", variable=output_format_var, value="Image")

word_radio.pack()
image_radio.pack()

convert_button = tk.Button(app, text="Convert", command=convert_pdf)
convert_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
