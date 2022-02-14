# Requires LoCred to build
FROM rockylinux:8
ENV PYTHON_VER="3.10.2"
RUN yum groupinstall "Development Tools" -y
RUN yum install openssl-devel libffi-devel bzip2-devel tar tree wget -y

# Build Python 3.10

WORKDIR /tmp
RUN wget "https://www.python.org/ftp/python/$PYTHON_VER/Python-$PYTHON_VER.tgz"
RUN tar xvf "Python-$PYTHON_VER.tgz"
WORKDIR "/tmp/Python-$PYTHON_VER"
RUN ./configure --enable-optimizations
RUN make altinstall

# Build Hapyka
RUN mkdir -p /opt/hapyka/hapyka
ADD hapyka /opt/hapyka/hapyka
COPY setup.py /opt/hapyka/
WORKDIR /opt/hapyka
RUN tree
RUN python3 ./setup.py build_py
RUN python3 ./setup.py install

RUN yum --setopt=groupremove_leaf_only=1 groupremove 'Development Tools' -y
RUN yum --setopt=groupremove_leaf_only=1 remove openssl-devel libffi-devel tar bzip2-devel -y

ENTRYPOINT python3 /opt/hapyka/hapyka/hapyka_main.py