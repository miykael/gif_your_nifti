FROM debian:stable-slim

ADD . /code
WORKDIR /code
ENV DEBIAN_FRONTEND noninteractive

# try to provide binary packages for requirements.txt, amend this list if necessary
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    python3-setuptools \
    python3-wheel \
    python3-pip \
    python3-numpy \
    python3-nibabel \
    python3-matplotlib \
    python3-imageio \
    python3-skimage

# should not build things from source, can be forced with '--only-binary all'
RUN pip3 install --upgrade-strategy only-if-needed .

# minor cleanup
RUN apt-get clean && \
    rm -rf /var/lib/apt && \
    rm -rf /code/gifs

ENTRYPOINT ["/usr/local/bin/gif_your_nifti"]
