FROM ubuntu:18.04

# Updating the repository
RUN apt-get update && \
    apt-get install -qy git && \
# Installing SSH server
    apt-get install -qy openssh-server && \
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd && \
    mkdir -p /var/run/sshd && \
# Installing JDK 11
    apt-get install -qy default-jdk && \
# Installing maven
    apt-get install -qy maven && \
# Cleanup the old packages
    apt-get -qy autoremove && \
# Adding user jenkins to the image
    adduser --quiet jenkins && \
# Setting password for the jenkins user
    echo "jenkins:password" | chpasswd && \
    mkdir /home/jenkins/.m2

# Copy authorized keys
COPY .ssh/authorized_keys /home/jenkins/.ssh/authorized_keys

RUN chown -R jenkins:jenkins /home/jenkins/.m2/ && \
    chown -R jenkins:jenkins /home/jenkins/.ssh/

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
