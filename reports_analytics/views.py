# reports_analytics/views.py
import tkinter as tk
from reports_analytics.controllers import generate_monthly_report

class AnalyticsDashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Analytics Dashboard")

        self.button_generate_report = tk.Button(self, text="Generate Monthly Report", command=self.generate_report)

        self.button_generate_report.pack()

    def generate_report(self):
        generate_monthly_report()
