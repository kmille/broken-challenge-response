FROM frolvlad/alpine-python3
ADD app.py /root/app.py
RUN apk update && apk add socat
COPY flag.txt /flag.txt
CMD socat tcp-l:2023,reuseaddr,fork exec:'python /root/app.py'
