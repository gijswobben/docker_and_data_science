# Start with a basic Python container
FROM python:3

# Create a directory to work in
WORKDIR /usr/src/app

# Copy a requirements file and install all requirements with pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code (and models) into the container
COPY . .

# Start the nameko service when the container starts
CMD ["nameko", "run", "wrapper"]
