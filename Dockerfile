# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

##just made new changes to check
# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
