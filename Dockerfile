# File: sap-gemini-backend/Dockerfile
#
# Uses a lightweight Python base image. Change this if your backend uses a different language.
FROM python:3.9-slim

# Set the working directory inside the container to '/app'.
WORKDIR /app

# Copy the requirements file and install the dependencies.
# This is a common practice to leverage Docker's layer caching.
# If requirements.txt doesn't change, this layer doesn't need to be rebuilt.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your backend code into the container.
# Make sure your Python file (e.g., app.py) is in the root of your repo.
COPY . .

# Expose the port that your application listens on.
# This must match the 'containerPort' in your deployment.yaml.
EXPOSE 8080

# This is the command that runs when the container starts.
# Replace 'app.py' with the actual name of your main backend file.
CMD ["python", "app.py"]