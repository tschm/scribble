FROM jupyter/base-notebook:1386e2046833 as jupyter

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

# copy the work folder into the image, hence the notebooks will be available with docker pull from dockerhub
# hardcoded parameters!? see https://github.com/moby/moby/issues/35018
COPY --chown=jovyan:users ./work /home/jovyan/work

# copy the config.ini file
COPY /binder/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py

RUN conda install numpy numexpr matplotlib beakerx && conda clean -y --all