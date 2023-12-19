# Use an official Ubuntu runtime as a parent image
FROM ubuntu:22.04

# Set environment variables for Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# Install Java 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk curl wget unzip subversion perl git python3-pip

# Install icecream using pip
RUN pip3 install icecream

# Install SVN, Perl, and Git
RUN apt-get install -y subversion perl git

# Set the working directory to /app
WORKDIR /app

# Clone the Git repository
RUN git clone https://github.com/manhlamabc123/StaticBugCheckers

RUN cd StaticBugCheckers && \
    git clone -q https://github.com/rjust/defects4j.git && \
    cd defects4j && ./init.sh