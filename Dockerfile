# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the port the app runs on (adjust if needed)
EXPOSE 8000

# Command to run the app
CMD ["python", "main.py"]

# docker build -t laber-law .
# docker run -p 8000:8000 labor-law

# docker stop gifted_villani
# docker run -p 8000:8000 laber-law:latest
# curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"user_input": "What is the process for resolving labor disputes, and how does the WIDI platform facilitate this?"}'