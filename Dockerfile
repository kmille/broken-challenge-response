FROM frolvlad/alpine-python3
ADD app.py /root/app.py
RUN apk update && apk add socat
CMD socat tcp-l:2023,reuseaddr,fork exec:'python /root/app.py'
