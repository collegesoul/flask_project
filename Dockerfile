FROM python:3.11.6-alpine3.18

# Install Python pip, add the requirements to the docker image
# and install all required packages in the requirements.txt
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create a directory 'flaskProject' and add the app, db and error files
# to the created directory
RUN mkdir flaskProject
WORKDIR flaskProject
ADD *.py ./

EXPOSE 8080

