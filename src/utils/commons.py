def read_file_content(file):
    file_data = io.BytesIO()
    file.seek(0)
    file_data.write(file.read())
    return file_data
