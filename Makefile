NAME    := smartspace/storage
VERSION := 0.0.1
BRANCH    := main

GIT_COMMIT_ID := latest

REGISTRY := smartspace



image:
    docker build -f Dockerfile -t ${NAME}:${VERSION} .


push:
      docker push ${NAME}:${VERSION}
