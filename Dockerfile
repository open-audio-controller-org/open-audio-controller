FROM registry.access.redhat.com/ubi8/ubi
RUN yum update -y
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN yum install -y 	http://mirror.centos.org/centos/7/os/x86_64/Packages/alsa-lib-1.1.8-1.el7.x86_64.rpm http://mirror.centos.org/centos/7/os/x86_64/Packages/alsa-lib-devel-1.1.8-1.el7.x86_64.rpm
RUN yum install -y gcc python3-devel portaudio-devel
RUN pip3 install --upgrade pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
# WORKDIR /open-audio-controller/tests
# RUN coverage run test_suite.py
# ENTRYPOINT ["coverage", "report"]
EXPOSE 5000
ENTRYPOINT ["flask", "run"]