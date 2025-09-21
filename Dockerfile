# Use a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the model and application files
COPY movie_list.pkl .
COPY similarity.pkl .
COPY main.py .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the app when the container starts
CMD ["streamlit", "run", "main.py"]