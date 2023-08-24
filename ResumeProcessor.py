from parsers.ParseResumeToJson import ParseResume
from ReadPdf import read_single_pdf
import os.path
import pathlib
import json

# file_path = "D:\\resume parser\\Resumes-20230612T113554Z-001\\Resumes\\Abhinav.pdf"
SAVE_DIRECTORY = r'D:\DS\resumes\acads\asd'
file_path ='D:\\DS\\resumes\\acads\\link.pdf'
# D:\\resume parser\\Resumes-20230612T113554Z-001\\Resumes

class ResumeProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        print(input_file)
        self.input_file_name = input_file

    def process(self) -> bool:
        try:
            resume_dict = self._read_resumes()
            self._write_json_file(resume_dict)
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def _read_resumes(self) -> dict:
        data = read_single_pdf(self.input_file_name)
        output = ParseResume(data).get_JSON()
        return output



    def _write_json_file(self, resume_dictionary: dict):
        file_name = str("Resume-" + self.input_file +
                        resume_dictionary["unique_id"] + ".json")
        save_directory_name = pathlib.Path(SAVE_DIRECTORY) / file_name
        json_object = json.dumps(resume_dictionary, sort_keys=True, indent=14)
        with open(save_directory_name, "w+") as outfile:
            outfile.write(json_object)
