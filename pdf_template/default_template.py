from fpdf import FPDF
import pathlib
from pathlib import Path

# REQUIRED information
# Basic info:
# Name, Address, email, phone number
# Advanced info:
# Education: list[]
#   - School list(Period time)
#       - Deploma(gpa=None) / Position
# PRACTICAL EXPERIENCE: list[]
#   - Company/Team name(Period time)
#       - Position
#           - Work list
# PROJECT EXPERIENCE: list[]
#   - Project name(Period time)
#       - Project content list
# ACTIVITIES: list[]
#   - Company/Cooperation name(Period time)
#       - Position
#           - Work list
# SKILLS: string
#   - Skill list


# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100, 150))

pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# font ('times', 'courier', 'times', 'symbol', 'zpfding')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('times', 'B', 18)


# Add text
# w = width
# h = height
# ln (0/False; 1/True - move cursor to the next line)
pdf.cell(w=0, h=5, txt="Lyuyongkang Yuan", align='C')
pdf.ln()
pdf.set_font('times', '', 11)
pdf.cell(w=0, h=10, txt="2311 Erie Drive, Ann Arbor, MI 48105 | yuan.lyuyongkang@gmail.com | (734) 881-5555", align='C')
pdf.ln()
# ===================================== EDUCATION SECTION =============================
pdf.set_font('times', 'B', 12)
pdf.cell(w=0, h=5, txt="EDUCATION")
pdf.ln()
pdf.cell(w=0, h=0, border=1)
pdf.ln(3)
pdf.cell(w=0, h=0, txt="University of Michigan, Ann Arbor", align="L")
pdf.cell(w=0, h=0, txt="Sep 2021 - May 2023", align="R")
pdf.ln()

pdf.set_font('times', 'I', 11)
pdf.cell(w=0, h=0, txt="\x95")
pdf.set_x(18)
pdf.cell(w=0, h=0, txt="Bachelor of Science | Computer Science", align="L")
pdf.cell(w=0, h=0, txt="GPA: 3.4/4.0", align="R")
pdf.ln()
pdf.cell(w=0, h=0, txt="\x95")
pdf.set_x(18)
pdf.cell(w=0, h=0, txt="U-M Library Student Grant", align="L")

# ====================================== EDUCATION END =================================
pdf.ln()
# ====================================== PRACTICAL EXPERIENCE ==========================
pdf.set_font('times', 'B', 12)
pdf.cell(w=0, h=5, txt="PRACTICAL EXPERIENCE")
pdf.ln()
pdf.cell(w=0, h=0, border=1)
pdf.ln(3)
pdf.cell(w=0, h=0, txt="UM Ann Arbor, EECS 183 Elementary Programming Concepts", align="L")
pdf.ln()
pdf.set_font('times', 'BI', 11)
pdf.cell(w=0, h=0, txt="Course Grader", align="L")
pdf.cell(w=0, h=0, txt="Oct 2022 - Dec 2022", align="R")

pdf.ln(2.5)
pdf.set_font('times', "", 10)
pdf.cell(w=0, h=4, txt="\x95")
pdf.set_x(18)
pdf.multi_cell(w=0, h=4, txt="Familiarized project coding style review rubric made by Graduate Student Instructor and read through project spec to develop a grading plan for each project.")
pdf.ln(0.15)
pdf.cell(w=0, h=4, txt="\x95")
pdf.set_x(18)
pdf.multi_cell(w=0, h=4, txt="Reviewed 80+ students' program per job, finding segments that can be improved through code review and provide suggestions for revising to help them familiar with clean code.")
# ====================================== PRACTICAL END =================================
pdf.ln()
# ====================================== PROJECT =======================================
pdf.set_font('times', 'B', 12)
pdf.cell(w=0, h=5, txt="PROJECT")
pdf.ln()
pdf.cell(w=0, h=0, border=1)
# ...
pdf.ln(3)
pdf.set_font('times', 'BI', 11)
pdf.cell(w=0, h=0, txt="AR application design for optimizing the experience in the library", align="L")
pdf.cell(w=0, h=0, txt="Oct 2022 - Present", align="R")

pdf.ln(2.5)
pdf.set_font('times', "", 10)
pdf.cell(w=0, h=4, txt="\x95")
pdf.set_x(18)
pdf.multi_cell(w=0, h=4, txt="Applied Tesseract OCR to help recognized text in image file")
pdf.ln(0.15)
pdf.cell(w=0, h=4, txt="\x95")
pdf.set_x(18)
pdf.multi_cell(w=0, h=4, txt="Programing to split and assemble words to meaningful sentence and paragraph;")
pdf.ln(0.15)
pdf.cell(w=0, h=4, txt="\x95")
pdf.set_x(18)
pdf.multi_cell(w=0, h=4, txt="Mapping text to animation files through database system.")



# ====================================== PROJECT END ===================================
pdf.ln()
# ====================================== ACTIVITIES ====================================
pdf.set_font('times', 'B', 12)
pdf.cell(w=0, h=5, txt="ACTIVITIES")
pdf.ln()
pdf.cell(w=0, h=0, border=1)
# ...
# ====================================== ACTIVITIES END ================================
pdf.ln()
# ====================================== SKILLS ========================================
pdf.set_font('times', 'B', 12)
pdf.cell(w=0, h=5, txt="SKILLS")
pdf.ln()
pdf.cell(w=0, h=0, border=1)
# ...
# ====================================== SKILLS END ====================================



outputpath = Path('./pdf_template/templates/pdf_1.pdf')
pdf.output(outputpath)