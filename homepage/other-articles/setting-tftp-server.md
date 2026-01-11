# Setting TFTP Server

<a id="for-ubuntu"></a>

### For Ubuntu

1. Install the TFTP Server

```
sudo apt update
sudo apt install tftpd-hpa
```

2. Configure the TFTP Server

`sudo nano /etc/default/tftpd-hpa`

```
TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/var/tftpboot"
TFTP_ADDRESS=":69"
TFTP_OPTIONS="--secure"
```

Save and close the file.

3. Create and Set Permissions for the TFTP Root Directory

```
sudo mkdir /var/tftpboot
sudo chown tftp:tftp /var/tftpboot
sudo chmod -R 775 /var/tftpboot
```

4. Restart the TFTP Service

```
sudo systemctl restart tftpd-hpa
```

5. Check the Status of the TFTP Service

```
sudo systemctl status tftpd-hpa
```

<a id="for-any-distro-using-the-docker"></a>

### For any distro using the docker

1. Create and Set Permissions for the TFTP Root Directory if needed

```
sudo mkdir /var/tftpboot
sudo chmod -R 775 /var/tftpboot
```

2. Run the tftp docker container:

```
docker run -p 0.0.0.0:69:69/udp -v /var/tftpboot:/var/tftpboot -i -t pghalliday/tftp
```

<a id="for-windows"></a>

### For Windows

1. [Download](https://bitbucket.org/phjounin/tftpd64/downloads/) and install tftpd64
2. Select the network and directory with the files you need to transfer

![image-20240513-101152.png](./attachments/image-20240513-101152.png)