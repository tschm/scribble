FROM tschm/docker:release-0.4

COPY --chown=jovyan:100 . /tmp/scribble

# copy the work folder into the image, hence the notebooks will be available with docker pull from dockerhub
COPY --chown=jovyan:100 ./work $WORK

# install the package
RUN pip install --no-cache-dir /tmp/scribble && \
    rm -r /tmp/scribble
