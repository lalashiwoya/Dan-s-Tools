from backend.tools import PDFMerger
import pytest


@pytest.fixture(params=[
    ("/Users/danliu/job_application", "/Users/danliu/job_application")
])
def pdf_merger(request):
    save_dir, input_dir = request.param
    return PDFMerger(save_dir=save_dir, input_dir=input_dir)


@pytest.mark.parametrize("output_file_path", ["test_merged_output"])
def test_merge_from_folder(pdf_merger, output_file_path):
   pdf_merger.merge_from_folder(output_file_path)

@pytest.mark.parametrize("output_file_path", ["test_merged_output_1"])
@pytest.mark.parametrize("input_file_names", [["Resume", "masters"]])
def test_merge_specific_files_from_folder(pdf_merger, input_file_names, output_file_path):
    pdf_merger.merge_specific_files_from_folder(input_file_names, output_file_path)