from dotenv import load_dotenv
import os
import pyodbc
from fastapi import HTTPException

load_dotenv()

conn = pyodbc.connect(
    f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_NAME')};"
    f"UID={os.getenv('DB_USER')};"
    f"PWD={os.getenv('DB_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

def getList():
    cursor = conn.cursor()
    cursor.execute("SELECT WordId, Word, Translation FROM dbo.WordTranslations w")

    result = []
    for row in cursor.fetchall():
        result.append({"id": row[0], "text": row[1], "translation": row[2]})

    return result

def getById(id): 
    cursor = conn.cursor()
    cursor.execute("SELECT WordId, Word, Translation FROM dbo.WordTranslations w WHERE w.WordId = ?", 
        (id,)
        )
    row = cursor.fetchone()

    if row:
        return {"id": row[0], "text": row[1], "translation": row[2]}
    else:
        raise HTTPException(status_code=404, detail=f"Word with id {id} does not exist")
    
def addWord(data):
    cursor = conn.cursor()
