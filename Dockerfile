#page

Page up

#GNU

  GNU nano 3.2                                         Dockerfile                                                   
# Python image to use.
#
#,

#python_3.8

FROM python:3.8
# Set the working directory to /app

#work_dir

WORKDIR /app

#requirements file used
#,
#files

COPY requirements.txt .

# packages from requirements.txt
#install_packages


RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Copy the working_dir in the container (app)

COPY . .


# Run app.py
#container_launches

CMD [ "python3", "main.py", "--host=0.0.0.0"]

#,,
#'
