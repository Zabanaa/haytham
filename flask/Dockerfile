FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev

# Copy project files
COPY . /app/
