#first stage - builder
FROM golang:1.15-buster as builder
LABEL maintainer="vika1990z <v.zubyenko@gmail.com>"
WORKDIR /distributed-calculator
COPY app.go .
RUN go get -d -v
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .
#second stage
FROM debian:buster-slim
WORKDIR /root/
COPY --from=builder /distributed-calculator/app .
CMD ["./app"]
