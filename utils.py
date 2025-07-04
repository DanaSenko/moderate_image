from fastapi import UploadFile

def validate_image(file: UploadFile):
    if not (file.filename.lower().endswith('.jpg') or file.filename.lower().endswith('.jpeg') or file.filename.lower().endswith('.png')):
        return False
    return True