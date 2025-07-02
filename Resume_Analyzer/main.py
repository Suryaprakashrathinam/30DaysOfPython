from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from extract import extract_text
from analyzer import clean_text, split_into_sections, analyze_against_jd
from generate_report import create_pdf_report
import os  #  Needed for opening the PDF

class ResumeApp(BoxLayout):
    def process_resume(self):
        filechooser = self.ids.filechooser
        jd_input = self.ids.jd_input
        selected_label = self.ids.selected_file_label
        name_input = self.ids.name_input
        role_input = self.ids.role_input

        selected_file = filechooser.selection
        job_description = jd_input.text.strip()
        candidate_name = name_input.text.strip()
        job_role = role_input.text.strip()

        if not selected_file:
            selected_label.text = "No file selected!"
            return
        if not job_description:
            selected_label.text = "Please enter job description!"
            return
        if not candidate_name or not job_role:
            selected_label.text = "Please enter candidate name and job role!"
            return

        try:
            resume_text = extract_text(selected_file[0])
            cleaned_text = clean_text(resume_text)
            sections = split_into_sections(cleaned_text)
            report = analyze_against_jd(cleaned_text, job_description)

            print("\n Summary:\n", sections.get("summary", "Not found"))
            print("\n Skills:\n", sections.get("skills", "Not found"))
            print("\n Report:\n", report)

            # ✅ Save PDF and remember the path
            self.generated_report_path = create_pdf_report(
                candidate_name=candidate_name,
                job_role=job_role,
                report_data=report
            )

            selected_label.text = "Resume processed & PDF generated!"

        except Exception as e:
            selected_label.text = f"Error: {e}"

    # ✅ Add this method to support the "Download" button
    def download_report(self):
        try:
            if hasattr(self, 'generated_report_path') and os.path.exists(self.generated_report_path):
                os.startfile(self.generated_report_path)  # ✅ Windows-specific
            else:
                print("PDF not found. Please generate it first.")
        except Exception as e:
            print(f"Error opening report: {e}")

class ResumeAnalyzerApp(App):
    def build(self):
        return ResumeApp()

if __name__ == "__main__":
    ResumeAnalyzerApp().run()
