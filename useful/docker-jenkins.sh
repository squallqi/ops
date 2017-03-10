SCRIPT_DIR=$(dirname $(readlink -e $0))
docker run -d -it\
 --name jenkins_jenkinsweb\
 -w /jenkins\
 -p 0.0.0.0:18086:8080\
 -v /root/jenkins-data:/var/lib/jenkins:rw\
 -v $SCRIPT_DIR/run.sh:/jenkins/run.sh:rw\
 --entrypoint=/bin/bash $IMAGE\
 -C ./run.sh /ci/web