FROM python:3.11-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PYTHONWARNINGS=ignore \
    PIP_NO_CACHE_DIR=1

RUN python -m pip install --upgrade pip && \
    pip install \
      requests \
      PyJWT \
      beautifulsoup4 \
      Faker \
      pymongo \
      cryptography \
      pytest \
      pytest-playwright

COPY actors/ ./actors/
COPY api/ ./api/
COPY data_factory/ ./data_factory/
COPY email_service/ ./email_service/
COPY environment/ ./environment/
COPY files/ ./files/
COPY logger/ ./logger/
COPY models/ ./models/
COPY mongo/ ./mongo/
COPY scripts/ ./scripts/
COPY settings/ ./settings/
COPY ui/ ./ui/
COPY utils/ ./utils/

ENTRYPOINT ["python", "-u", "scripts/data_management/data_mng.py"]