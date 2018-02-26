# Controlato

## Contributing

Controlato is developed in Java. To work on it, you need to install:

1. Java Development Kit (JDK)

### Installing the JDK

Go to http://www.oracle.com/technetwork/java/javase/downloads/index.html and download the latest JDK that corresponds to your operating system.

#### Installing on Ubuntu

Create a folder for your Java development environment:

    $ mkdir ~/java

Download or copy the JDK into this folder and perform a checksum to verify its consistency:

    $ sha256sum jdk-9.0.4_linux-x64_bin.tar.gz
      90c4ea877e816e3440862cfa36341bc87d05373d53389ec0f2d54d4e8c95daa2

Compare the hash (the returned alphanumeric string) that your machine calculated with the corresponding hash published in the download page. If they are the same then unzip the file:

    $ tar zxvf jdk-9.0.4_linux-x64_bin.tar.gz
    
The folder `jdk-9.0.4` is created at `~/java`, containing the development kit and the runtime. Let's create a symbolic link pointing to that folder that is independent on the version, thus we don't have to change our configurations everytime we upgrade the jdk:

    $ ln -sf /home/htmfilho/java/jdk-9.0.4 /home/htmfilho/java/jdk
 
