from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
import os, shutil
from main import process_document

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
  file = request.files['doc_file']
  job_book_number = request.form['job_book_number']

  # Validate job_book_number
  job_book_number = job_book_number.replace("-","").replace("_","")
  if len(job_book_number) not in [10,12]:
    return jsonify({"error": "job_book_number must have 10 or 12 digits"}), 400
  else:
    job_book_number = f"{job_book_number[:2]}-{job_book_number[2:8]}-{job_book_number[8:10]}"

  # Save file temporarily
  base_dir = os.path.dirname(os.path.abspath(__file__))
  temp_folder = os.path.join(base_dir, 'temp')
  file_path = os.path.join(temp_folder, file.filename)
  os.makedirs(temp_folder, exist_ok=True)
  # print(file_path)
  file.save(file_path)

  try:
    # Create Output Folder
    output_folder = os.path.join(temp_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)

    # Process the file
    if os.path.exists(output_folder):
      process_document(file_path, job_book_number, output_folder)

    # Create ZIP archive
    # print("Base Directory:", base_dir)
    # print("Temp Folder:", temp_folder)
    # print("File Path:", file_path)
    # print("Output Folder:", output_folder)
    # print(os.listdir(temp_folder))
    # print(os.listdir(output_folder))

    zip_file_base = os.path.join(temp_folder,'output')
    zip_file_path = zip_file_base + '.zip'
    # print(zip_file_base)
    # print(zip_file_path)
    shutil.make_archive(zip_file_base ,'zip', output_folder)

    # print(os.listdir(temp_folder))
    # print(os.listdir(output_folder))

    if not os.path.exists(zip_file_path):
      return jsonify({"error": f"ZIP file not found: {zip_file_path}"}), 500

    def generate():
      with open(zip_file_path, 'rb') as f:
          yield from f
      # Perform cleanup after streaming
      cleanup(temp_folder)

    return Response(
        generate(),
        headers={
            'Content-Disposition': f'attachment; filename={os.path.basename(zip_file_path)}',
            'Content-Type': 'application/zip',
        },
    )

  except Exception as e:
    cleanup(temp_folder)  # Cleanup in case of errors
    return jsonify({"error": str(e)}), 500


def cleanup(temp_folder):
  """
  Attempts to clean up the temporary folder and logs errors if any.
  """
  if os.path.exists(temp_folder):
    try:
      print(f"Attempting to clean up: {temp_folder}")
      shutil.rmtree(temp_folder)
      print("Cleanup successful.")
    except Exception as cleanup_error:
      print(f"Error during cleanup: {cleanup_error}")
  else:
    print(f"No temporary folder found: {temp_folder}")

if __name__ == '__main__':
  app.run(debug=True)