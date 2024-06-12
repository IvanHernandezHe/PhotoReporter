import tkinter as tk
from tkinter import filedialog
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
import pypandoc

def seleccionar_imagen():
    #ruta_imagen = 'files/logo.png'
    ruta_imagen = 'files/logo3.png'
    return ruta_imagen

def configurar_margenes(doc):
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.25)
        section.bottom_margin = Inches(0.25)
        section.left_margin = Inches(0.25)
        section.right_margin = Inches(0.25)
        section.header_distance = Inches(0.018)

def agregar_encabezado(doc, logo_path):

    header = doc.sections[0].header

    header_table = header.add_table(rows=1, cols=2, width=Inches(12))
    header_table.style = 'Light Shading Accent 1'

    cell_logo = header_table.cell(0, 0)
    paragraph_logo = cell_logo.paragraphs[0]
    paragraph_logo.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    #paragraph_logo.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY_MED
    run_logo = paragraph_logo.add_run()
    run_logo.add_picture(logo_path, width=Inches(3))
    cell_logo.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    cell_info = header_table.cell(0, 1)
    paragraph_info = cell_info.paragraphs[0]
    paragraph_info.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = paragraph_info.add_run('REPORTE FOTOGRÁFICO\n COMERCIALIZADORA DE PRODUCTOS Y SERVICIOS\n DE REFRIGERACIÓN RECAR SA DE CV')
    run.bold = True
    run.font.name = 'Segoe UI'
    run.font.size = Pt(10.2)
    cell_info.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

def agregar_tabla_informacion(doc):
    info_table = doc.add_table(rows=1, cols=2)
    info_table.style = 'Medium List 1 Accent 1'

    hdr_cells = info_table.rows[0].cells
    hdr_cells[0].text = 'Asignación:'
    hdr_cells[0].width = Inches(10)
    hdr_cells[1].text = 'Fecha:'

def guardar_documento(doc, filename):
    doc.save(filename)
    print(f"Documento guardado como '{filename}'")

def convertir_a_pdf(input_file, output_file):
    # pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)
    print(f"Documento guardado como '{output_file}'")

def main():
    logo_path = seleccionar_imagen()

    doc = Document()
    configurar_margenes(doc)
    agregar_encabezado(doc, logo_path)
    # doc.add_paragraph('')
    agregar_tabla_informacion(doc)

    docx_filename = 'ReporteConEncabezadoYMargenes.docx'
    pdf_filename = 'ReporteConEncabezadoYMargenes.pdf'

    guardar_documento(doc, docx_filename)
    convertir_a_pdf(docx_filename, pdf_filename)

if __name__ == "__main__":
    main()
