# Set the base image to jupyter
FROM tschm/jupyter:1.2.0 as jupyter

# copy the work folder into the image, hence the notebooks will be available with docker pull from dockerhub
# hardcoded parameters!? see https://github.com/moby/moby/issues/35018
COPY --chown=jovyan:users ./work $WORK

RUN conda install numpy numexpr matplotlib && conda clean -y --all