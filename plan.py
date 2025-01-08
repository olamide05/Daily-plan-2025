import os
from fpdf import FPDF

class DailyPlanPDF(FPDF):
    def header(self):
        self.set_font("Arial", style="B", size=16)
        self.cell(0, 10, "Daily Plan", ln=True, align="C")
        self.ln(5)

    def add_table_headers(self, headers):
        self.set_font("Arial", style="B", size=12)
        for header, width in headers:
            self.set_fill_color(200, 220, 255)  
            self.cell(width, 10, header, border=1, align="C", fill=True)
        self.ln()

    def add_table_row(self, row, col_widths):
        self.set_font("Arial", size=12)
        row_heights = [
            self.get_string_width(col) // width * 10 + 10
            for col, width in zip(row, col_widths)
        ]
        row_height = max(row_heights)

        for col, width in zip(row, col_widths):
            x_start = self.get_x()
            y_start = self.get_y()
            self.multi_cell(width, 10, col, border=1, align="L")
            self.set_xy(x_start + width, y_start)

        self.ln(row_height)


# Original daily plan
daily_plan_fixed = [
    ("7:00-8:00", "workout and get ready", "stretch and push ups and prepare for the day"),
    ("8:00-10:00", "Neet Code and HackerRank", "Solve 2-3 algorithm problems, review weak areas."),
    ("10:00-12:30", "College Work", "Focus on coursework, complete assignments."),
    ("12:30-1:30", "Break/Exercise", "Relax, go for a walk, or light exercise."),
    ("2:00-4:00", "study udemy course", "Follow up with the course and its projects."),
    ("4:00-5:00", "work on personal projects", "Work on personal projects and take notes, also do some research."),
    ("6:00-7:00", "Review, Testing, and Planning", "Test project features, analyze progress, and set goals for the next day."),
    ("7:00-7:30", "Learn or Explore New Concepts", "Learn an advanced topic like Kubernetes, CI/CD, or cloud computing.")
]


headers = [("Time", 40), ("Activity", 80), ("Goal/Key Task", 70)]
col_widths = [40, 80, 70]

# PDF Generation
pdf = DailyPlanPDF()
pdf.add_page()
pdf.add_table_headers(headers)

for entry in daily_plan_fixed:
    pdf.add_table_row(entry, col_widths)

# Determine desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_path = os.path.join(desktop_path, "Daily_Plan.pdf")

# Output
pdf.output(output_path)
print(f"PDF successfully created at: {output_path}")
