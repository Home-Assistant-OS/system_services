ARG BUILD_FROM
FROM $BUILD_FROM

# Install required packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    gcc \
    musl-dev \
    python3-dev

# Set working directory
WORKDIR /usr/src/app

# Copy our service script
COPY run.py /usr/src/app/
RUN chmod a+x /usr/src/app/run.py

# Create service user
RUN adduser -S svcuser -G root

# Switch to service user
USER svcuser

# Run the service
CMD [ "python3", "/usr/src/app/run.py" ]

# Labels
LABEL \
    io.hass.name="System Process Manager" \
    io.hass.description="Essential system process and resource management service" \
    io.hass.type="service" \
    io.hass.version="1.0.0" \
    io.hass.arch="armhf|aarch64|i386|amd64" \
    maintainer="Home Assistant Core Team <core@home-assistant.io>"
