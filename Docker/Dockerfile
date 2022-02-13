# Requires LoCred to build
FROM rockylinux:8

RUN yum -y install python3 python3-devel tree gcc gcc-c++

# Build Hapyka
RUN mkdir -p /opt/hapyka/hapyka
ADD hapyka /opt/hapyka/hapyka
COPY setup.py /opt/hapyka/
WORKDIR /opt/hapyka
RUN tree
RUN python3 ./setup.py build_py
RUN python3 ./setup.py install

RUN yum -y remove python3-devel tree gcc gcc-c++

ENTRYPOINT python3 /opt/hapyka/hapyka/hapyka_main.py