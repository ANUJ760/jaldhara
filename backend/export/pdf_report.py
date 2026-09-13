from fpdf import FPDF
from datetime import datetime

class ReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Jaldhara Simulation Report', 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def generate_pdf_report(job_id: int, report_data: dict, output_path: str):
    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    
    # Title Page
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", 0, 1)
    pdf.cell(0, 10, f"Project Name: {report_data.get('project_name', 'Dam Break Study')}", 0, 1)
    pdf.cell(0, 10, f"AOI Name: {report_data.get('aoi_name', 'Kosi Area')}", 0, 1)
    pdf.ln(10)
    
    # Dam Metadata
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, 'Dam Metadata Summary', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, f"Dam Height: {report_data.get('dam_height')} m", 0, 1)
    pdf.cell(0, 10, f"Reservoir Volume: {report_data.get('reservoir_volume')} MCM", 0, 1)
    pdf.ln(5)
    
    # Breach Parameters
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, 'Breach Parameters', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, f"Width: {report_data.get('breach_width')} m", 0, 1)
    pdf.cell(0, 10, f"Formation Time: {report_data.get('formation_time')} hrs", 0, 1)
    pdf.ln(5)
    
    # Methodology
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, 'Methodology', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10, "Simulations were performed using SPH and Delft3D engines. Outputs compared using spatial divergence metrics.")
    
    pdf.output(output_path, 'F')
    return output_path
