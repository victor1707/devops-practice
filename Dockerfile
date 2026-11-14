FROM python:3.12-slim
WORKDIR /app
COPY app.py .
EXPOSE 8080
# TODO (lesson 3): add ENV APP_VERSION and see it in the response
CMD ["python", "app.py"]
