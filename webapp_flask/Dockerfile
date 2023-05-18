# Use a base Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install the required dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the necessary files to the working directory
COPY webapp.py /app/webapp.py
COPY templates /app/templates/
COPY finalized_model.sav /app/finalized_model.sav

# Expose the desired port

ENV FLASK_APP="webapp.py"

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
