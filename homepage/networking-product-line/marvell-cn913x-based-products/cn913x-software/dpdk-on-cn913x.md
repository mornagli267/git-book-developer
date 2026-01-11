# DPDK on CN913X

<a id="running-dpdk"></a>

### Running DPDK

DPDK is supported in our CN913X platforms since commit #77cd41e in our [cn913x\_build](https://github.com/SolidRun/cn913x_build) repository.

Notes -

1. DPDK has been tested only on ClearFog-Base CN9130 based product.
2. Please notice that the support is for ethernet ports that are directly connected to the SoC (i.e. no L2 DSA switch support).

The images include test-pmd, but any DPDK application can be copied and used.

Before running a DPDK application, the following steps should be followed:

- Mount and allocate hugepages, for example:

```
mkdir -p /mnt/huge
mount -t hugetlbfs nodev /mnt/huge
echo 512 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
```

- insert MUSDK kernel modules, which are used by the MVPP2 PMD:

```
insmod /root/musdk_modules/mv_pp_uio.ko
insmod /root/musdk_modules/musdk_cma.ko
```

Now, the DPDK application can be used.

In order to set testpmd to transmit 64B packets from all 3 interfaces, the following command can be used:

```
/root/dpdk/dpdk-testpmd --vdev=eth_mvpp2,iface=eth0,iface=eth1,iface=eth2 \
-- --txd=1024 --txpkts=1500 --tx-first --auto-start --forward-mode=txonly \
--nb-cores=1 --stats-period=1
```

At the moment, switching back from DPDK to the Linux kernel is not supported (but possible), so once a DPDK application runs, the Linux kernel won’t be able to use the network interfaces.

Although not recommended, In order to switch back to the Linux kernel, the MTU size can be changed for the interface (and then, changed back to the original size).

```
ifconfig ethX mtu 1499
ifconfig ethX mtu 1500
```

changing the MTU size will re-associate the RXQ pools.

This hack is not stable, and will lead to error messages from the kernel.

More details can be found in the cn913x\_build repository.