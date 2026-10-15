# Step 1: Use a lightweight, official Python runtime as the base layer
FROM python:3.10-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy our app.py file from your computer into the container
COPY app.py .

# Step 4: Tell the container to expose port 8000 to the outside network
EXPOSE 8000

# Step 5: The exact command to run the application when the container starts
CMD ["python", "app.py"]
