#!/bin/bash
#
# Copyright (c) 2018 AT&T Intellectual Property. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DOCKER_REPO='nexus3.akraino.org:10003'

set -e -u -x -o pipefail

echo '---> Starting build-docker'

# Set container name and version
CON_NAME='akraino_container_probe'
source $WORKSPACE/version.properties

## Put any special build instructions here

# Build and push the Docker container
docker build -f Dockerfile -t ${CON_NAME}:${VERSION} .
docker tag ${CON_NAME}:${VERSION} ${DOCKER_REPO}/${CON_NAME}:${VERSION}
docker push ${DOCKER_REPO}/${CON_NAME}:${VERSION}

set +u +x
