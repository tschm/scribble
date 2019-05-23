# Set the base image to beakerx
FROM lobnek/jupyter:v2.8 as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# install the pyaddepar package
COPY --chown=beakerx:beakerx . /home/beakerx/tmp

# install the package
RUN pip install --no-cache-dir /home/beakerx/tmp && \
    pip install --no-cache-dir -r /home/beakerx/tmp/requirements.txt && \
    rm -r /home/beakerx/tmp

WORKDIR ${WORK}
