from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_final_pdf(results, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("TEST YAKUNIY NATIJALARI", styles["Title"]))
    elements.append(Spacer(1, 12))

    # 🔥 Jadval sarlavha
    data = [["#", "Ism", "To‘g‘ri", "Xato", "Test ball", "Esse", "Yakuniy", "Daraja"]]

    # 🔥 Saralash (eng yuqoridan pastga)
    results_sorted = sorted(results, key=lambda x: x["final"], reverse=True)

    for i, r in enumerate(results_sorted, 1):
        data.append([
            i,
            r["name"],
            r["correct"],
            r["wrong"],
            r["test_ball"],
            r["esse"],
            r["final"],
            r["grade"]
        ])

    table = Table(data, repeatRows=1)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # 🔥 STATISTIKA
    stats = {}
    for r in results:
        g = r["grade"]
        stats[g] = stats.get(g, 0) + 1

    elements.append(Paragraph("STATISTIKA:", styles["Heading2"]))

    for g in ["A+", "A", "B+", "B", "C+", "C", "Fail"]:
        if g in stats:
            elements.append(Paragraph(f"{g}: {stats[g]} ta", styles["Normal"]))

    doc.build(elements)
