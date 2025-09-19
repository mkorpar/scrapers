FROM python:3.14-rc-alpine
COPY scrapers.py . 
RUN python3 scrapers.py
