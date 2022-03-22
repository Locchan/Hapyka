#!/bin/bash

set -e

yum groupinstall "Development Tools" -y

cd /opt
python3 /opt/setup.py build_py
python3 /opt/setup.py install

yum --setopt=groupremove_leaf_only=1 groupremove 'Development Tools' -y

cd /

rm -rf opt/*