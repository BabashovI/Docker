FROM alpine

ARG AUTHOR=Ibrahim Babashov
ENV ENV=/etc/profile

RUN mkdir /vpn
COPY scripts/. /vpn/scripts/
COPY files/. /vpn/files/
COPY vpn_conf_files/. /vpn/conf_files/
WORKDIR /vpn
RUN apk update && apk add screen openssh openvpn vim python3

ENTRYPOINT /bin/sh /vpn/scripts/./entry.sh && \
    ls -l /dev/net/tun && \
    /bin/sh
