# Use the official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Install Docker CLI (not the engine)
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Add Jenkins user to Docker group
RUN usermod -aG docker jenkins

# Switch back to Jenkins user
USER jenkins
