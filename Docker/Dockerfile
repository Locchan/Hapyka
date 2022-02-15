# Requires LocPy to build
FROM locchan:locpy

# Build Hapyka
RUN mkdir -p /opt/hapyka
ADD hapyka /opt/hapyka
ADD setup.py /opt/
ADD Docker/_build.sh /opt
RUN /bin/bash /opt/_build.sh

ENTRYPOINT hapyka_main.py