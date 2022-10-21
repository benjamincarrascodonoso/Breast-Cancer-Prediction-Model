# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install python-multipart
RUN pip install tensorflow==2.9.0
RUN pip install Pillow
RUN pip install pydicom
RUN pip install numpy
# 
COPY ./app /code/app
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

