FROM docker.elastic.co/beats/filebeat:8.5.0

ENV RELEASE 1.2.0
ENV MIN_RELEASE 1

LABEL maintainer "Marouan MOHAMED <medmarouen@gmail.com>"

USER 0

RUN apt-get update && apt-get install -y openssl libapr1 libdbi1 libexpat1 ca-certificates

RUN dpkgArch="$(dpkg --print-architecture)" && \
    case "${dpkgArch}" in \
        amd64) ARCH='amd64' ;; \
        arm64) ARCH='armv7' && dpkg --add-architecture armv7  ;; \
        *) echo >&2 "error: unsupported architecture: ${dpkgArch}" && exit 1 ;; \
    esac &&  \
    apt-get install -y --no-install-recommends curl && \
    curl -Lo sidecar.deb https://github.com/Graylog2/collector-sidecar/releases/download/${RELEASE}/graylog-sidecar_${RELEASE}-${MIN_RELEASE}_$ARCH.deb && \
    dpkg -i sidecar.deb && rm sidecar.deb && apt-get purge -y --auto-remove curl


# Define default environment values
ENV GS_UPDATE_INTERVAL=60 \
    GS_SEND_STATUS="true" \
    GS_TLS_SKIP_VERIFY="false" \
    GS_LIST_LOG_FILES="[]" \
    GS_LOG_ROTATION_SIZE="10MiB" \
    GS_LOG_OLD_KEEP=10

ADD ./sidecar-config.yaml /graylog/sidecar-config.yaml

CMD /usr/bin/graylog-sidecar -c /graylog/sidecar-config.yaml

# USER filebeat

# docker buildx build --push --platform linux/arm64,linux/amd64 --tag medinvention/graylog-sidecar-filebeat:1.2.0 . -f Dockerfile.filebeat