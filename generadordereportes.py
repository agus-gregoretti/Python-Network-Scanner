from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data, target_network):
    file_name = "Reporte_Auditoria_Pro.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = styles['Title']
    title_style.textColor = colors.HexColor("#2c3e50")
    title_style.fontSize = 24

    elements = []
    elements.append(Paragraph("Reporte de Auditoría de Red", title_style))
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(f"<b>Red Analizada:</b> {target_network}", styles['Normal']))
    elements.append(Spacer(1, 15))

    # Configuración de Tabla
    col_widths = [110, 150, 210]
    tabla = Table(data, colWidths=col_widths)
    
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ])
    
    tabla.setStyle(style)
    elements.append(tabla)
    doc.build(elements)