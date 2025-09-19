FROM python:3.14-rc-alpine
COPY scrapers.py . 
ENTRYPOINT ["python3", "scrapers.py"]
