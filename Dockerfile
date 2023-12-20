# Use an official Ubuntu runtime as a parent image
FROM ubuntu:22.04

# Set environment variables for Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# Set the timezone (replace "America/New_York" with your desired timezone)
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Java 8, curl, wget, unzip, SVN, Perl, Git, Python, pip, and cpan
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk curl wget unzip python3 python3-pip cpanminus subversion perl git

# Install icecream using pip
RUN pip3 install icecream

# Set the working directory to /app
WORKDIR /app

# Clone the Git repository
RUN git clone https://github.com/manhlamabc123/StaticBugCheckers

RUN cd StaticBugCheckers && \
    git clone -q https://github.com/rjust/defects4j.git && \
    cd defects4j && cpanm --installdeps . && ./init.sh
