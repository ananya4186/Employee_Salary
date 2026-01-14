FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pytest
CMD ["python", "employee_salary.py"]
