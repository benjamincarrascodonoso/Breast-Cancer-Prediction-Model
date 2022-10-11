from typing import Union

from fastapi import FastAPI , File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''

@app.post("/files/")
#async def create_file(file: Union[bytes, None] = File(default=None)):
async def upload_file(file: UploadFile = File(...)):

    if not file.filename:
        return {"message": "No file sent"}
    else:
        return {"file_name": file.filename}

@app.get("/uploadView")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
