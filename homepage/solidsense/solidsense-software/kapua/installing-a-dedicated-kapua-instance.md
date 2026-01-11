# Installing a dedicated Kapua instance

> \[!WARNING] The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.

The SolidSense Kapua instance is not meant for production purpose, so we recommend the deployment of  a dedicated instance when Kapua is to be used in production, in particular if data have to be stored in the Kapua database.

### Installation procedure

Prerequisite for Kapua installation are the following

* 64 bit Linux system with minimum 6GB of RAM, we recommend 8GB, dual core system
* Java VM Version 8
* Docker 1.2+

The system needs to be connected to the internet during installation.

Here are the instructions:

```
$ git clone git@github.com:eclipse/kapua.git kapua
$ cd kapua/deployment/docker
$ ./docker-deploy
```

After you can connect to the console by

http://:8080

Default credentials

User: kapua-sys

Password: kapua-password

> \[!WARNING] **Please Note** We strongly recommend to change the the password as soon as possible.

### Changing Kapua sysadmin password

1. Log on Kapua as kapua-sys, go on the users screen and change the password using the credential tab. Remember that the password needs to be at least 12 characters long
2. Goto to the kapua/deployment/docker directory from installation
3. Edit (vi or nano as you like) the compose/docker-compose.yml
4. In each “environment” section of the file add the following line: -‘transport.credential.password=’
5. Note that the quote are mandatory
6. Then redeploy Kapua: bash docker-deploy.sh
