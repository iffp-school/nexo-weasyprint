FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    weasyprint \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    && pip install flask \
    && apt-get clean
COPY server.py .
EXPOSE 8080
CMD ["python", "server.py"]
