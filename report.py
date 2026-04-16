import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV
data = pd.read_csv("input.csv")

# Analysis
total_students = len(data)
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Subject-wise average
subject_avg = data.groupby("Subject")["Marks"].mean().reset_index()

# Create PDF
doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("STUDENT PERFORMANCE REPORT", styles['Title']))
elements.append(Spacer(1, 12))

# Summary Section
elements.append(Paragraph("Summary:", styles['Heading2']))
elements.append(Paragraph(f"Total Students: {total_students}", styles['Normal']))
elements.append(Paragraph(f"Average Marks: {average_marks:.2f}", styles['Normal']))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles['Normal']))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles['Normal']))
elements.append(Spacer(1, 12))

# Student Table
elements.append(Paragraph("Student Data:", styles['Heading2']))
table_data = [data.columns.tolist()] + data.values.tolist()

table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)
elements.append(Spacer(1, 15))

# Subject-wise Table
elements.append(Paragraph("Subject-wise Average:", styles['Heading2']))

sub_table_data = [subject_avg.columns.tolist()] + subject_avg.values.tolist()
sub_table = Table(sub_table_data)

sub_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.green),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(sub_table)

# Build PDF
doc.build(elements)

print("Professional Report Generated Successfully!")