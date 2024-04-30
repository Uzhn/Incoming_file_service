import os
import shutil
from fastapi import UploadFile, HTTPException, status

from src.core.constants import IN_FOLDER


def upload_csv(file: UploadFile):
    try:
        if not file.filename.endswith(".csv"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only CSV files are allowed",
            )
        file_location = os.path.join(IN_FOLDER, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": "File uploaded successfully", "file_name": file.filename}
    except Exception as e:
        return {"error": f"Failed to upload file: {str(e)}"}
