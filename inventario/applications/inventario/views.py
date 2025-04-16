from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, CreateView, ListView, DetailView
from .forms import InventarioForm
from .models import Inventario
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

# Create your views here.

class InventarioCreateView(CreateView):
    form_class = InventarioForm
    template_name = "inventario/add-inventario.html"
    success_url = "."


class InventarioListView(ListView):
    template_name = "inventario/lista-inventario.html"
    context_object_name = "lista"
    paginate_by = 4
    context_object_name = "inventarios"
    model = Inventario
    

class InventarioDetailView(DetailView):
    model = Inventario
    template_name = "inventario/detail-inventario.html"
    context_object_name = "equipo"

def generar_pdf_equipo(request, equipo_id):
    # Obtener el equipo de la base de datos
    equipo = Inventario.objects.get(id=equipo_id)

    # Crear la respuesta HTTP con el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="equipo_{equipo.id}.pdf"'

    # Crear el PDF
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Título del documento
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Reporte de Equipo de Cómputo")

    # Línea separadora
    p.setStrokeColor(colors.blue)
    p.setLineWidth(2)
    p.line(50, height - 60, width - 50, height - 60)

    # Detalles en una tabla
    data = [
        ["Descripción:", equipo.descripcion],
        ["Marca:", equipo.marca.nombre],
        ["Modelo:", equipo.modelo],
        ["Color:", equipo.color],
        ["Número de Serie:", equipo.no_serie],
        ["Nombre del Resguardante:", equipo.nombre_resguardante],
        ["No. Factura:", equipo.num_factura],
        ["Observaciones:", equipo.observaciones],
        ["Fecha de creación:", equipo.created],
    ]

    # Definir la tabla
    table = Table(data, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Posicionar la tabla
    table.wrapOn(p, width, height)
    table.drawOn(p, 80, height - 250)

    # Pie de página
    p.setFont("Helvetica", 10)
    p.setFillColor(colors.grey)
    p.drawString(50, 50, "Reporte generado automáticamente - Sistema de Inventario")

    # Guardar el PDF
    p.showPage()
    p.save()

    return response
    