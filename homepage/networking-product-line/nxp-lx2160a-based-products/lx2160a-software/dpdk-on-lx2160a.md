# DPDK on LX2160A

NXP LX216X SoC and SolidRun products based on it support DPDK for all native network interfaces, as well as certain PCI cards.

There are several options for versions, including NXP forks and upstream. SolidRun supports the NXP fork matching the respective NXP BSP release:

- LS-5.15.71-2.2.0: DPDK 21.11.2 (NXP fork): [GitHub - nxp-qoriq/dpdk](https://github.com/nxp-qoriq/dpdk/tree/lf-5.15.71-2.2.0) tag `lf-5.15.71-2.2.0`
- LSDK-21.08 (legacy): DPDK 20.11.2 (NXP fork): [GitHub - nxp-qoriq/dpdk](https://github.com/nxp-qoriq/dpdk/tree/LSDK-21.08) tag `LSDK-21.08`

<a id="revision-and-notes"></a>

# Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 02 Jul 2025 |     | 0   | Draft |
| 22 Oct 2025 |     | 1   | add dpdk-dumpcap example |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Prebuilt Binaries](#prebuilt-binaries)<br>- [Building from Source](#building-from-source)<br>  - [Native Build on LX2160 (Ubuntu)](#native-build-on-lx2160-ubuntu)<br>    - [Install Dependencies](#install-dependencies)<br>    - [Download Sources](#download-sources)<br>    - [Compile](#compile)<br>    - [Install](#install)<br>  - [Cross Build on PC](#cross-build-on-pc)<br>- [Run Examples](#run-examples)<br>  - [Port Mapping](#port-mapping)<br>    - [LX2160A Honeycomb & Clearfog-CX](#lx2160a-honeycomb-clearfog-cx)<br>    - [LX2162A Clearfog](#lx2162a-clearfog)<br>  - [Native Interface Preparation](#native-interface-preparation)<br>    - [Unbind Linux Drivers](#unbind-linux-drivers)<br>      - [Map dpni objects to dpmac objects](#map-dpni-objects-to-dpmac-objects)<br>      - [Unbind Linux Driver from, and destroy a dpni object](#unbind-linux-driver-from-and-destroy-a-dpni-object)<br>    - [Bind to DPDK](#bind-to-dpdk)<br>  - [PCI Network Interfaces](#pci-network-interfaces)<br>  - [testpmd](#testpmd)<br>  - [dumpcap](#dumpcap)<br>- [Known Issues](#known-issues)<br>  - [Secondary dpdk process fails opening ethernet ports](#secondary-dpdk-process-fails-opening-ethernet-ports) |     |     |

<a id="prebuilt-binaries"></a>

# Prebuilt Binaries

The SolidRun LX2160A Reference BSP version *ls-5.15.7102.2.0* dated *03/07/2025* or later compiles a binary distribution of DPDK that can be execute `testpmd`. This is for validation purposes only, in deployment customers are expected to build their own. Binaries are available [here](https://images.solid-run.com/LX2k/lx2160a_build/).

<a id="building-from-source"></a>

# Building from Source

<a id="native-build-on-lx2160-ubuntu"></a>

## Native Build on LX2160 (Ubuntu)

<a id="install-dependencies"></a>

### Install Dependencies

```
apt-get install build-essential git meson pciutils
```

<a id="download-sources"></a>

### Download Sources

```
git clone https://github.com/nxp-qoriq/dpdk
cd dpdk
# pick desired tag here from list above
git reset --hard lf-5.15.71-2.2.0
cd ..
```

<a id="compile"></a>

### Compile

To configure and compile dpdk using an out-of-tree build directory `dpdk-build`:

```
meson setup --reconfigure -Dexamples=all --buildtype release --strip dpdk-build dpdk
meson compile -C dpdk-build
```

<a id="install"></a>

### Install

DPDK may be executed from inside the build-directory, or installed system-wide:

```
meson install -C dpdk-build
```

<a id="cross-build-on-pc"></a>

## Cross Build on PC

The SolidRun LX2160A Reference BSP performs cross-compilation of DPDK as part of a full build - for details please refer to it’s build-script: [GitHub - SolidRun/lx2160a\_build - runme.sh](https://github.com/SolidRun/lx2160a_build)

Alternatively DPDK may be built as part of Yocto: [GitHub - SolidRun/meta-solidrun-arm-lx2xxx - Yocto BSP](https://github.com/SolidRun/meta-solidrun-arm-lx2xxx/tree/kirkstone)

<a id="run-examples"></a>

# Run Examples

<a id="port-mapping"></a>

## Port Mapping

LX216X SoC native ports use nxp internal names dpmac.X where X is in \[1-20\].  
These names are relevant when preparing interfaces for use with DPDK:

<a id="lx2160a-honeycomb-clearfog-cx"></a>

### LX2160A Honeycomb & Clearfog-CX

| **Port Names** |     |     |     |
| --- | --- | --- | --- |
| dpmac.9 (SFP+) | dpmac.7 (SFP+) | dpmac.17 (RJ45) | TBD. |
| dpmac.10 (SFP+) | dpmac.8 (SFP+) |

<a id="lx2162a-clearfog"></a>

### LX2162A Clearfog

| **Port Names** |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| dpmac.5 (SFP28) | dpmac.3 (SFP+) |     | dpmac.16 (RJ45) | dpmac.15 (RJ45) | dpmac.13 (RJ45) | dpmac.14 (RJ45) |
| dpmac.6 (SFP28) | dpmac.4 (SFP+) | dpmac.12 (RJ45) | dpmac.11 (RJ45) | dpmac.17 (RJ45) | dpmac.18 (RJ45) |

<a id="native-interface-preparation"></a>

## Native Interface Preparation

The LX216XA SoCs are using specially managed network interfaces that must be prepared for use with DPDK.

<a id="unbind-linux-drivers"></a>

### Unbind Linux Drivers

Network interface drivers must first be unbound from the Linux kernel before they are usable with DPDK. Consider from the tables above which interfaces should be used with DPDK, then unbind only selected interfaces according to the instructions below:

<a id="map-dpni-objects-to-dpmac-objects"></a>

#### Map dpni objects to dpmac objects

For unbinding linux drivers the dpni object assigned to a specific dpmac port is required. The actual mapping is configuration specific and subject to invocations of `ls-addni` command, the DPL (part of bootloader image), and the dpdp `dynamic_dpl.sh` script. With same configuration the mapping can be considered stable across reboots.

  
The command below retrieves the dpmac objects attached to up to 20 dpni objects that may be present at runtime:

```
for i in $(seq 0 1 19); do
  restool dpni info dpni.$i | grep endpoint: | xargs echo dpni.$i:
done
```

Example output on LX2162A Clearfog:

```
dpni.0: endpoint: dpmac.18, link is down
dpni.1: endpoint: dpmac.17, link is down
dpni.2: endpoint: dpmac.16, link is up
dpni.3: endpoint: dpmac.15, link is down
dpni.4: endpoint: dpmac.14, link is down
dpni.5: endpoint: dpmac.13, link is down
dpni.6: endpoint: dpmac.12, link is down
dpni.7: endpoint: dpmac.11, link is down
dpni.8: endpoint: dpmac.6, link is down
dpni.9: endpoint: dpmac.5, link is down
dpni.10: endpoint: dpmac.4, link is down
dpni.11: endpoint: dpmac.3, link is down
dpni.12:
dpni.13:
dpni.14:
dpni.15:
dpni.16:
dpni.17:
dpni.18:
dpni.19:
```

<a id="unbind-linux-driver-from-and-destroy-a-dpni-object"></a>

#### Unbind Linux Driver from, and destroy a dpni object

For each dpni object representing a dpmac instance that shall be used with DPDK, execute the commands below (substitung Y for the particular dpni object number):

```
echo dpni.Y > /sys/bus/fsl-mc/drivers/fsl_dpaa2_eth/unbind
restool dpni destroy dpni.Y

# example unbinding LX2162 upper row ports (2x SFP, 4x RJ45)
for y in 11 9 5 4 3 2; do
  echo dpni.$y > /sys/bus/fsl-mc/drivers/fsl_dpaa2_eth/unbind
  restool dpni destroy dpni.$y
done
```

<a id="bind-to-dpdk"></a>

### Bind to DPDK

After choosing the list of interfaces that DPDK should use - after unbinding Linux drivers - and after destroying any attached dpni objects, they can be prepared for DPDK using the `nxp/dpaa2/dynamic_dpl.sh` script:

```
# bind LX2162 upper row ports (2x SFP, 4x RJ45) on named dprc object
export DPRC=dprc.2
export DPDMAI_COUNT=38 # more interfaces means fewer dpdma available
dynamic_dpl.sh dpmac.5 dpmac.3 dpmac.16 dpmac.15 dpmac.13 dpmac.14
```

Note: `dynamic_dpl.sh` is in the path on lx2160a\_build, yocto requires calling `bash /usr/share/dpdk/dpaa2/dynamic_dpl.sh`.

Example output:

```
parent - dprc.1
Creating Non nested DPRC
NEW DPRCs
dprc.1
  dprc.2
Using board type as 2160
Using High Performance Buffers

##################### Container  dprc.2  is created ####################

Container dprc.2 have following resources :=>

 * 3 DPMCP
 * 16 DPBP
 * 8 DPCON
 * 16 DPSECI
 * 6 DPNI
 * 34 DPIO
 * 8 DPCI
 * 38 DPDMAI
 * 0 DPRTC


######################### Configured Interfaces #########################

Interface Name        Endpoint              Mac Address              
==============        ========              ==================       
dpni.2                dpmac.5               -Dynamic-                
dpni.3                dpmac.3               -Dynamic-                
dpni.4                dpmac.16              -Dynamic-                
dpni.5                dpmac.15              -Dynamic-                
dpni.9                dpmac.13              -Dynamic-                
dpni.11               dpmac.14              -Dynamic-
```

<a id="pci-network-interfaces"></a>

## PCI Network Interfaces

This was tested specifically with an Intel X710 card - steps may need adaptation for other cards.

```
echo Y > /sys/module/vfio_pci/parameters/disable_idle_d3
dpdk-devbind.py --bind vfio-pci 01:00.*
```

For `testpmd` need to specifically pass each pci device - e.g.:

```
dpdk-testpmd -a 01:00.0 -a 01:00.1 -a 01:00.2 -a 01:00.3 -- -i
```

<a id="testpmd"></a>

## testpmd

```
# enable 2G pages
dpdk-hugepages.py --setup 2G

# interactive testpmd session
export DPRC=dprc.2
dpdk-testpmd -- -i
```

Example Output:

```
EAL: Detected CPU lcores: 16
EAL: Detected NUMA nodes: 1
EAL: Detected static linkage of DPDK
EAL: Multi-process socket /var/run/dpdk/rte/mp_socket
fslmc: Skipping invalid device (power)
EAL: Selected IOVA mode 'VA'
EAL: No available 2048 kB hugepages reported
EAL: No available 32768 kB hugepages reported
EAL: No available 64 kB hugepages reported
EAL: VFIO support initialized
PMD: dpni.2: netdev created, connected to dpmac.13
PMD: dpni.3: netdev created, connected to dpmac.14
PMD: dpni.4: netdev created, connected to dpmac.15
PMD: dpni.5: netdev created, connected to dpmac.16
TELEMETRY: No legacy callbacks, legacy socket not created
Interactive-mode selected
testpmd: create a new mbuf pool <mb_pool_0>: n=267456, size=2176, socket=0
testpmd: preferred mempool ops selected: dpaa2
Configuring Port 0 (socket 0)
Port 0: 42:26:DB:BB:38:16
Configuring Port 1 (socket 0)
Port 1: 22:1B:F6:3E:B8:C9
Configuring Port 2 (socket 0)
Port 2: 9E:6D:6D:BB:1A:01
Configuring Port 3 (socket 0)
Port 3: 1E:B2:B5:BF:96:CD
Checking link statuses...
Done
```

<a id="dumpcap"></a>

## dumpcap

dumpcap utility runs as a secondary process to a dpdk application.

First execute testpmd (see complete instructions above), and instruct it to start tx/rx queues:

```
dpdk-hugepages.py --setup 2G
export DPRC=dprc.2
dpdk-testpmd -- -i
...
testpmd> start
...
```

Packet capture can now be started from a second terminal on one of the available ports:

```
export DPRC=dprc.2
dpdk-dumpcap --list-interfaces
...
dpdk-dumpcap -p 0 -w port0.pcapng
...
Capturing on 'dpni.2'
Packets captured: 163
```

<a id="known-issues"></a>

# Known Issues

<a id="secondary-dpdk-process-fails-opening-ethernet-ports"></a>

## Secondary dpdk process fails opening ethernet ports

A secondary dpdk process can fail to initialise while a primary application (e.g. testpmd) is already active, e.g.:

```
root@lx2162a-rev2-clearfog:~# dpdk-dumpcap --help
fslmc: Skipping invalid device (power)
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
dpaa2_net: SG pool creation failed

fslmc: Unable to probe
EAL: Error - exiting with code: 1
  Cause: No Ethernet ports found
```

This is caused by a bug in dpaa2 driver that was resolved in 2024: [https://mails.dpdk.org/archives/dev/2024-September/301170.html](https://mails.dpdk.org/archives/dev/2024-September/301170.html)

SolidRun BSP has this patch backported on dpdk v21.11 since 22/10.2025. NXP DPDK v22.11 also has resolved this issue.