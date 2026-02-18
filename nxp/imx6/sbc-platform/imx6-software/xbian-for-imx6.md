# XBian for i.MX6

<a id="description"></a>

## Description

XBian is a small, fast and lightweight media center distro, originally for the Raspberry Pi, based on a minimal Raspbian image. It is also available for CuBox-i.

<a id="installation"></a>

## Installation

1. See xbian [downloads page](http://www.xbian.org/getxbian/) for download and installation instructions, including how to flash the image from Windows, Mac or Linux
2. Also [check the forums](http://forum.solid-run.com/kodi-xbmc-player-on-cubox-i-and-hummingboard-f7/xbian-beta-imx6--t1127.html) for other help and advice (note, the image linked near the top of the forum is outdated; the xbian downloads page has a turnkey installer and a more updated distribution).

<a id="configuration"></a>

## Configuration

**Notice:** [**XBMC**](https://developer.solid-run.com/knowledge-base/xbmc/) **has recently been renamed to Kodi. Some file names still refer to the old name**

<a id="ir-remote"></a>

#### IR Remote

<a id="setup"></a>

#### **Setup**

First, log in to the system using either telnet or ssh. Next, you need to determine what protocol your remote uses. The kernel of Xbian is built with many decoders, which are located here: /lib/modules/3.0.35-gb2e8f7c-dirty/kernel/drivers/media/rc

```
imon.ko
ir-jvc-decoder.ko
ir-lirc-codec.ko
ir-nec-decoder.ko
ir-rc5-decoder.ko
ir-rc5-sz-decoder.ko
ir-rc6-decoder.ko
ir-sony-decoder.ko
mceusb.ko
rc-loopback.ko
redrat3.ko
streamzap.ko
```

Sometimes you can search on the web to figure out which decoder will interpret your remote (NEC, Sony, etc), but another method is to list the keymaps that come with Xbian and see if your remote is listed:

```
ls /lib/udev/rc_keymaps/
```

For example, if your remote is a hauppauge, you can open the file and note that the first line states:

```
table hauppauge, type: RC5
```

which would indicate that the hauppauge remote needs the RC5 decoder.

Next, edit */etc/modules* (use nano or something else) and add the decoder module so it starts on bootup; omit the “.ko” when adding to the file. If you want to cover your bases, you can add all the modules to the file so they are loaded at startup.

Now, reboot your Cubox-i so the module gets loaded. Verify that the module got loaded by running “dmesg” and look around the 3second mark for something similar to the following:

```
[    3.389424] IR NEC protocol handler initialized
```

Run the commands

```
sudo service xbmc stop
ir-keytable -t
```

Now press a key on the remote. A new line should be displayed that looks like

```
event MSC: scancode = 72cd5c
```

The scancode is the unique code for this button. With this code, you can create a remote file. This file must be created at */etc/rc\_keymaps*/. You can name it anything you want. In the rest of this guide, */etc/rc\_keymaps/mycustomremote* is used as a file name. The file has the following structure:

```
# table mycustomremote, type: NEC
0x72cd5c      KEY_ENTER
0x72cd1c      KEY_LEFT
0x72cd48      KEY_RIGHT
0x72cd44      KEY_UP
0x72cd1d      KEY_DOWN
```

On the first line, give the name of the remote, and the type of remote. Valid types are (you might have to experiment a bit with the correct type):

```
    NEC
    RC-5
    RC-6
    JVC
    SONY
    LIRC
    other
```

Next, each button is on a single line. Each line begins with 0x, followed by the scancode you learnt from ir-keytable -t. Next is the name of the button. This should be a valid key name. See for a list of valid key codes.

If the special remote file is constructed, it can be tested.

```
ir-keytable -c -w /etc/rc_keymaps/mycustomremote
ir-keytable -t
```

Now press a key on the remote again. The output should now look like

```
event MSC: scancode = 72cd5c
event key down: KEY_ENTER (0x001c)
```

Besides the scancode, it will also display the name of the key pressed. If no name is displayed, change the type in the remote file, and try again using the two commands above.

Now restart the xbmc service and and test your remote in Kodi

```
sudo service xbmc start
```

After all is good in Kodi, edit the */etc/rc\_maps.cfg* file to add your mycustomremote keymap file so it is loaded at boot:

```
#driver table                    file
gpio-rc-recv    rc-empty        /etc/rc_keymaps/mycustomremote
```

You only need the path to the file if it is not */etc/rc\_keymaps*/. Use the driver and table reported by ir-keytable:

```
xbian@xbian-cubox ~ $ ir-keytable 
Found /sys/class/rc/rc0/ (/dev/input/event0) with:
         Driver gpio-rc-recv, table rc-empty
         Supported protocols: NEC 
         Enabled protocols: NEC 
         Name: gpio_ir_recv
         bus: 25, vendor/product: 0001:0001, version: 0x0100
         Repeat delay = 500 ms, repeat period = 125 ms
```

Reboot the Cubox, then verify that your codes have been loaded:

```
xbian@xbian-cubox ~ $ ir-keytable -r
scancode 0x85301f = KEY_CHANNELDOWN (0x193)
scancode 0x85302f = KEY_8 (0x09)
...
Enabled protocols: NEC
```

<a id="wifi"></a>

#### Wifi

<a id="setup"></a>

#### **Setup**

The current xbian build does not always successfully set up wifi from the Kodi GUI. As a result, you need to set it up from command line:

1. Connect an ethernet cable to your Cubox-i and boot it
2. From another computer, ssh into your Cubox-i (default username: xbian, default password: raspberry)
3. Upon login, you will get an xbian configuration screen
4. Navigate to the network settings, choose wifi, and enter your Wifi credentials
5. Disconnect ethernet and reboot

<a id="external-links"></a>

## External links

- [http://xbian.org](http://xbian.org)
- Download latest Xbian
- Xbian Forum
- Solid-Run Forum