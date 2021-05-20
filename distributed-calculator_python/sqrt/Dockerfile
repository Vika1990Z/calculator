FROM python:3.7-alpine
LABEL maintainer="vika1990z <v.zubyenko@gmail.com>"
COPY . /app
WORKDIR /app
RUN pip install flask flask_cors
ENTRYPOINT ["python"]
EXPOSE 9000
CMD ["app.py"]