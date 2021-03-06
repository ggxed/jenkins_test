REGISTRY 		:= ggxed
NAME 			:= git_test
#VERSION 		:= 0.0.2

BASE_IMAGE 		:= ${REGISTRY}/${NAME}
VERSION_IMAGE   := ${BASE_IMAGE}:${VERSION}
#BRANCH_IMAGE    := ${VERSION_IMAGE}-$(BRANCH)

#BRANCH := main

image:
	docker build -f Dockerfile -t ${BASE_IMAGE} .
	

push:
	docker login -u ggxed -p '7ffd023c-3aa8-45b2-9af8-090f157f6668'
	docker tag ${BASE_IMAGE} ${VERSION_IMAGE}
	docker push ${BASE_IMAGE}
	docker push ${VERSION_IMAGE}
	#docker tag ${BASE_IMAGE} ${BRANCH_IMAGE}
	#docker push ${REGISTRY}/${NAME}:${VERSION}-$(BRANCH)
pull:
	docker login -u ggxed -p '7ffd023c-3aa8-45b2-9af8-090f157f6668'
	docker pull ${REGISTRY}/${NAME}:${VERSION}
