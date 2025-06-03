#base image with python installed
FROM python:3.11-slim 

#set working directory in the container
WORKDIR /app            # Set working directory in the container

#copy dependency file into container
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt
  
#Copy your python script into the container
COPY monitor.py .

#Start the application
CMD ["python", "monitor.py"]
