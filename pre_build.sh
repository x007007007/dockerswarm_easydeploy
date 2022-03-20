#!/bin/bash

cat <<EOF
================pre-build START $(date)====================
python interpreter: %(which python)
workspace         : $(realpath .)
EOF

python -m grpc_tools.protoc -I./src/ \
        --python_out=./src \
        --grpc_python_out=./src \
        ./src/dockerswarm_easydeploy_proto/client.proto

cat <<EOF
================pre-build DONE  $(date)====================
EOF