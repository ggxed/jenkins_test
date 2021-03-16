REGISTRY 		:= ggxed
NAME 			:= git_test
VERSION 		:= 0.0.1

BASE_IMAGE 		:= ${REGISTRY}/${NAME}
VERSION_IMAGE   := ${BASE_IMAGE}:${VERSION}
#BRANCH_IMAGE    := ${VERSION_IMAGE}-$(BRANCH)

#BRANCH := main

image:
	docker build -f Dockerfile -t ${BASE_IMAGE} .


push:
	docker login -u ggxed -p '140870ec-2f5b-404d-85a2-64e20cf05237'
	docker tag ${BASE_IMAGE} ${VERSION_IMAGE}
	docker push ${BASE_IMAGE}
	docker push ${VERSION_IMAGE}
