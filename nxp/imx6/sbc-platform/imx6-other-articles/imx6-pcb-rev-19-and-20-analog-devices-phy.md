# i.MX6 PCB rev 1.9 and 2.0 - Analog Devices PHY

i.MX6 SOM rev 1.9 and 2.0 migrates from Atheros PHY AR8035 to Analog Devices ADIN 1300 PHY.

This article comes to detail the software modifications required to accomodate this hardware change.

{% hint style="info" %}
Please note that using those modifications you will be able to support both the AR8035 and the ADIN1300 phys in the same kernel / u-boot images.
{% endhint %}


## U-boot

In order to add support for this PHY in U-boot, you can perform **one** of the follow options:

* Clone and build SolidRun's U-boot repository, branch  **v2018.01-solidrun-imx6**, which includes the PHY support. [https://github.com/SolidRun/u-boot/](https://github.com/SolidRun/u-boot/)

```
git clone https://github.com/SolidRun/u-boot.git -b v2018.01-solidrun-imx6
```

Or

* Apply the following patch to your U-boot repository (If you're using SolidRun's u-boot)

```
From 1b9da6319d32cb66cc05df695bc07fd8cf65a311 Mon Sep 17 00:00:00 2001
From: Alvaro-Karsz <alvaro.karsz@solid-run.com>
Date: Sun, 9 Jan 2022 14:58:51 +0200
Subject: [PATCH] Add support for Analog Devices PHY.
New configurations for ADIN1300 PHY, including:
  * New ETH mask with ADIN1300 address, which is 1.
  * 125MHz Clock out.
  * Delay before attepting to read the PHY registers.
  * SW reset.
Signed-off-by: Alvaro-Karsz <alvaro.karsz@solid-run.com>
---
 board/solidrun/mx6cuboxi/mx6cuboxi.c | 74 +++++++++++++++++++++++++++-
 1 file changed, 72 insertions(+), 2 deletions(-)
diff --git a/board/solidrun/mx6cuboxi/mx6cuboxi.c b/board/solidrun/mx6cuboxi/mx6cuboxi.c
index adc2c6a00e..a4b85d758f 100644
--- a/board/solidrun/mx6cuboxi/mx6cuboxi.c
+++ b/board/solidrun/mx6cuboxi/mx6cuboxi.c
@@ -308,8 +308,60 @@ int board_phy_config(struct phy_device *phydev)
 	return 0;
 }
 
-/* On Cuboxi Ethernet PHY can be located at addresses 0x0 or 0x4 */
-#define ETH_PHY_MASK	((1 << 0x0) | (1 << 0x4))
+
+
+
+#define ADIN1300_MII_EXT_REG_PTR	0x10
+#define ADIN1300_MII_EXT_REG_DATA	0x11
+#define ADIN1300_CLK_CFG_REG		0xff1f
+#define ADIN1300_MII_CONTROL_REG	0x0
+#define ADIN_PHY_ADDR			0x1
+#define ADIN_PHY_ID			0x283bc30
+
+
+/*ADIN1300 PHY - write to MMD registers*/
+int adin_phy_mmd_write(struct phy_device *phydev, int regnum, u16 val)
+{
+	int ret;
+
+	/*write to external pointer register*/
+	ret = phy_write(phydev, MDIO_MMD_VEND1,
+			ADIN1300_MII_EXT_REG_PTR, regnum);
+
+	if (ret)
+		return ret;
+
+	/*write to external data register*/
+	return phy_write(phydev, MDIO_MMD_VEND1,
+			ADIN1300_MII_EXT_REG_DATA, val);
+}
+
+
+/*additional init for ADIN1300 PHY*/
+int eth_init_adin_phy(struct phy_device *phydev)
+{
+	int ret;
+
+
+	/* Configure clock by writing to the clock register
+	 * 0x10 -> GE_CLK_FREE_125_EN
+	 */
+	ret = adin_phy_mmd_write(phydev, ADIN1300_CLK_CFG_REG, 0x10);
+	if (ret)
+		return ret;
+
+	/* Do SW reset by writing to MII control register
+	 * 0x8000 -> SFT_RST
+	 */
+	return phy_write(phydev, MDIO_MMD_VEND1,
+			ADIN1300_MII_CONTROL_REG, 0x8000);
+}
+
+
+/* On Cuboxi Ethernet PHY can be located at addresses 0x0 or 0x4
+ * Update: ADIN PHY is located at address 0x1.
+ */
+#define ETH_PHY_MASK	((1 << 0x0) | (1 << 0x4) | (1 << ADIN_PHY_ADDR))
 
 int board_eth_init(bd_t *bis)
 {
@@ -330,6 +382,13 @@ int board_eth_init(bd_t *bis)
 	if (!bus)
 		return -EINVAL;
 
+	/* Add a 20ms delay before searching for phy devices.
+	 * ADIN PHY needs a delay before attempting to read the PHY registers.
+	 * Without this delay, PHY register read will result in 0,
+	 * thus, the phy id will be read as 0.
+	 */
+	mdelay(20);
+
 	phydev = phy_find_by_mask(bus, ETH_PHY_MASK, PHY_INTERFACE_MODE_RGMII);
 	if (!phydev) {
 		ret = -EINVAL;
@@ -341,6 +400,17 @@ int board_eth_init(bd_t *bis)
 	if (ret)
 		goto free_phydev;
 
+
+	/* If this board has a ADIN1300 PHY,
+	 * additional configurations are required
+	 */
+	if (phydev->phy_id == ADIN_PHY_ID) {
+		ret = eth_init_adin_phy(phydev);
+		if (ret)
+			goto free_phydev;
+	}
+
+
 	return 0;
 
 free_phydev:
-- 
2.25.1
```

## Linux Kernel

In order to add support in Linux kernel, you can perform **one** of the follow options:

* Clone and build SolidRun's Linux repository(4.9),  which includes the PHY support. [https://github.com/SolidRun/linux-fslc](https://github.com/SolidRun/linux-fslc)

```
git clone https://github.com/SolidRun/linux-fslc.git
```

Or

* Apply the following patch to your Linux repository (If you're using SolidRun's Linux)

```
From d625f2afc9f329226c9b08a9bebb72cd4d8412e3 Mon Sep 17 00:00:00 2001
From: Alvaro-Karsz <alvaro.karsz@solid-run.com>
Date: Tue, 11 Jan 2022 11:42:45 +0200
Subject: [PATCH] Add support for Analog Devices PHY

* Backport ADIN driver from kernel 5.15 to this one.
* Add to the drvier a new feature - clock out configuration as 125MHz.
* Add post reset delay option to FEC drvier.
* Update relevant drevicetrees.
* Update relevant defconfig file.

Signed-off-by: Alvaro-Karsz <alvaro.karsz@solid-run.com>
---
 arch/arm/boot/dts/imx6qdl-sr-som.dtsi     |  32 +-
 arch/arm/configs/imx_v7_cbi_hb_defconfig  |   4 +
 drivers/net/ethernet/freescale/fec_main.c |  16 +-
 drivers/net/phy/Kconfig                   |  10 +
 drivers/net/phy/Makefile                  |   2 +-
 drivers/net/phy/adin.c                    | 980 ++++++++++++++++++++++
 include/linux/phy.h                       |   3 +-
 7 files changed, 1042 insertions(+), 5 deletions(-)
 create mode 100644 drivers/net/phy/adin.c

diff --git a/arch/arm/boot/dts/imx6qdl-sr-som.dtsi b/arch/arm/boot/dts/imx6qdl-sr-som.dtsi
index d8e44571..5d820ccf 100644
--- a/arch/arm/boot/dts/imx6qdl-sr-som.dtsi
+++ b/arch/arm/boot/dts/imx6qdl-sr-som.dtsi
@@ -77,10 +77,38 @@
 &fec {
 	pinctrl-names = "default";
 	pinctrl-0 = <&pinctrl_microsom_enet_ar8035>;
-	phy-mode = "rgmii";
-	phy-reset-duration = <2>;
+	phy-mode = "rgmii-id";
+	phy-reset-duration = <10>;
+	phy-reset-post-delay = <21>;
 	phy-reset-gpios = <&gpio4 15 GPIO_ACTIVE_LOW>;
 	status = "okay";
+
+
+	mdio {
+		#address-cells = <1>;
+		#size-cells = <0>;
+
+		/*
+		 * The PHY can appear at either address 0 or 4 due to the
+		 * configuration (LED) pin not being pulled sufficiently.
+		 */
+		ethernet-phy@0 {
+			reg = <0>;
+			qca,clk-out-frequency = <125000000>;
+			qca,smarteee-tw-us-1g = <24>;
+		};
+
+		ethernet-phy@4 {
+			reg = <4>;
+			qca,clk-out-frequency = <125000000>;
+			qca,smarteee-tw-us-1g = <24>;
+		};
+
+		/* Analog devices PHY */
+		ethernet-phy@1 {
+			reg = <1>;
+		};
+	};
 };
 
 &iomuxc {
diff --git a/arch/arm/configs/imx_v7_cbi_hb_defconfig b/arch/arm/configs/imx_v7_cbi_hb_defconfig
index 67132e04..c12b7103 100644
--- a/arch/arm/configs/imx_v7_cbi_hb_defconfig
+++ b/arch/arm/configs/imx_v7_cbi_hb_defconfig
@@ -5153,3 +5153,7 @@ CONFIG_FMC_CHARDEV=m
 # CONFIG_PGP_PRELOAD is not set
 # CONFIG_LOCALVERSION_AUTO is not set
 CONFIG_PROC_DEVICETREE=y
+
+
+# ADIN PHY
+CONFIG_ADIN_PHY=y
diff --git a/drivers/net/ethernet/freescale/fec_main.c b/drivers/net/ethernet/freescale/fec_main.c
index d0dc1441..1989f785 100644
--- a/drivers/net/ethernet/freescale/fec_main.c
+++ b/drivers/net/ethernet/freescale/fec_main.c
@@ -3341,7 +3341,7 @@ static int fec_reset_phy(struct platform_device *pdev)
 {
 	int err, phy_reset;
 	bool active_high = false;
-	int msec = 1;
+	int msec = 1, phy_post_delay = 0;
 	struct device_node *np = pdev->dev.of_node;
 
 	if (!np)
@@ -3358,6 +3358,11 @@ static int fec_reset_phy(struct platform_device *pdev)
 	else if (!gpio_is_valid(phy_reset))
 		return 0;
 
+	err = of_property_read_u32(np, "phy-reset-post-delay", &phy_post_delay);
+	/* valid reset duration should be less than 1s */
+	if (!err && phy_post_delay > 1000)
+		return -EINVAL;
+
 	active_high = of_property_read_bool(np, "phy-reset-active-high");
 
 	err = devm_gpio_request_one(&pdev->dev, phy_reset,
@@ -3375,6 +3380,15 @@ static int fec_reset_phy(struct platform_device *pdev)
 
 	gpio_set_value_cansleep(phy_reset, !active_high);
 
+	if (!phy_post_delay)
+		return 0;
+
+	if (phy_post_delay > 20)
+		msleep(phy_post_delay);
+	else
+		usleep_range(phy_post_delay * 1000,
+			phy_post_delay * 1000 + 1000);
+
 	return 0;
 }
 #else /* CONFIG_OF */
diff --git a/drivers/net/phy/Kconfig b/drivers/net/phy/Kconfig
index 2651c8d8..64af78fc 100644
--- a/drivers/net/phy/Kconfig
+++ b/drivers/net/phy/Kconfig
@@ -154,6 +154,16 @@ config AMD_PHY
 	---help---
 	  Currently supports the am79c874
 
+config ADIN_PHY
+        tristate "Analog Devices Industrial Ethernet PHYs"
+        help
+          Adds support for the Analog Devices Industrial Ethernet PHYs.
+          Currently supports the:
+          - ADIN1200 - Robust,Industrial, Low Power 10/100 Ethernet PHY
+          - ADIN1300 - Robust,Industrial, Low Latency 10/100/1000 Gigabit
+            Ethernet PHY
+
+
 config AQUANTIA_PHY
         tristate "Aquantia PHYs"
         ---help---
diff --git a/drivers/net/phy/Makefile b/drivers/net/phy/Makefile
index e58667d1..d3a33563 100644
--- a/drivers/net/phy/Makefile
+++ b/drivers/net/phy/Makefile
@@ -20,7 +20,7 @@ obj-$(CONFIG_MDIO_OCTEON)	+= mdio-octeon.o
 obj-$(CONFIG_MDIO_SUN4I)	+= mdio-sun4i.o
 obj-$(CONFIG_MDIO_THUNDER)	+= mdio-thunder.o
 obj-$(CONFIG_MDIO_XGENE)	+= mdio-xgene.o
-
+obj-$(CONFIG_ADIN_PHY)          += adin.o
 obj-$(CONFIG_AMD_PHY)		+= amd.o
 obj-$(CONFIG_AQUANTIA_PHY)	+= aquantia.o
 obj-$(CONFIG_AT803X_PHY)	+= at803x.o
diff --git a/drivers/net/phy/adin.c b/drivers/net/phy/adin.c
new file mode 100644
index 00000000..cd942c58
--- /dev/null
+++ b/drivers/net/phy/adin.c
@@ -0,0 +1,980 @@
+// SPDX-License-Identifier: GPL-2.0+
+/**
+ *  Driver for Analog Devices Industrial Ethernet PHYs
+ *
+ * Copyright 2019 Analog Devices Inc.
+ */
+#include <linux/kernel.h>
+#include <linux/bitfield.h>
+#include <linux/delay.h>
+#include <linux/errno.h>
+#include <linux/init.h>
+#include <linux/module.h>
+#include <linux/mii.h>
+#include <linux/phy.h>
+#include <linux/property.h>
+
+/* ADIN1300 PHY Backport to kernel 4.9 */
+
+/* Changes outside this file:
+ *
+ * 1) New member mmds_present to struct phy_c45_device_ids (include/linux/phy.h)
+ * 2) New member mdix_ctrl to struct phy_device (include/linux/phy.h)
+ * 3) New phy-reset-post-delay option in device tree (drivers/net/ethernet/freescale/fec_main.c).
+ */
+
+/* All phy_{read/write}_mmd calls are replaced with adin_{read/write}_mmd calls.
+ * In this kernel, read/write mmd is supported for clause 45 only, which is not our case.
+ */
+
+int adin_read_mmd(struct phy_device *phydev, int devad, u32 regnum);
+int adin_write_mmd(struct phy_device *phydev, int devad, u16 regnum, u16 val);
+
+/* Intentionally not adding header guards.
+ * This is code that should be removed as we upgrade the kernel.
+ * Some things should be removed after each upgrade.
+ * Most of the following bits of code have been taken from the latest PHY code.
+ */
+
+/* The following part was taken from ANALOG DEVICES website,
+ * "compatibility layer 4.19" and includes fixes I added to fit it to 4.9 kernel */
+
+#define PHY_ID_MATCH_MODEL(id) .phy_id = (id), .phy_id_mask = GENMASK(31, 4)
+
+#define phydev_warn(_phydev, format, args...)	\
+	dev_warn(&_phydev->mdio.dev, format, ##args)
+
+#define phydev_info(_phydev, format, args...)	\
+	dev_info(&_phydev->mdio.dev, format, ##args)
+
+#include <linux/version.h>
+
+#if LINUX_VERSION_CODE > KERNEL_VERSION(4, 19, 999)
+#error "Please check this compat layer and see what needs to be removed. After that, please adjust the KERNEL_VERSION(x,y,z) until all things are un-needed. Somewhere around version 5.3, all these should go way."
+#endif
+
+/* FIXME: These go away starting at kernel 5.0.
+ *        Unfortunately, these need to be macros/renames, because there are
+ *        already __mdiobus_{read,write} in 4.19, but no phy_modify_mmd_*()
+ *        functions yet. And MMD hooks need to be locked, because the MDIO
+ *        lock re-work isn't present in this kernel version.
+ */
+#define __mdiobus_read			mdiobus_read
+#define __mdiobus_write			mdiobus_write
+
+static inline int phy_modify_mmd_changed(struct phy_device *phydev, int devad,
+					 u32 regnum, u16 mask, u16 set)
+{
+	int new, ret;
+
+	ret = adin_read_mmd(phydev, devad, regnum);
+	if (ret < 0)
+		return ret;
+
+	new = (ret & ~mask) | set;
+	if (new == ret)
+		return 0;
+
+	ret = adin_write_mmd(phydev, devad, regnum, new);
+
+	return ret < 0 ? ret : 1;
+}
+
+static inline int phy_modify_mmd(struct phy_device *phydev, int devad,
+				 u32 regnum, u16 mask, u16 set)
+{
+	int ret;
+
+	ret = phy_modify_mmd_changed(phydev, devad, regnum, mask, set);
+
+	return ret < 0 ? ret : 0;
+}
+
+static inline int phy_clear_bits_mmd(struct phy_device *phydev, int devad,
+				     u32 regnum, u16 val)
+{
+	return phy_modify_mmd(phydev, devad, regnum, val, 0);
+}
+
+static inline int phy_set_bits_mmd(struct phy_device *phydev, int devad,
+				   u32 regnum, u16 val)
+{
+	return phy_modify_mmd(phydev, devad, regnum, 0, val);
+}
+
+/* END of "compatibility layer 4.19" */
+
+/* The following part includes required fixes
+ * I added to port this driver to 4.9 kernel
+ */
+
+#define PHY_CABLETEST				6
+#define PHY_POLL_CABLE_TEST			0x00000004
+#define DOWNSHIFT_DEV_DISABLE			0
+#define ETHTOOL_PHY_EDPD_DFLT_TX_MSECS		0xffff
+#define ETHTOOL_PHY_EDPD_NO_TX			0xfffe
+#define ETHTOOL_PHY_EDPD_DISABLE		0
+
+static inline bool phy_polling_mode(struct phy_device *phydev)
+{
+	if (phydev->state == PHY_CABLETEST)
+		if (phydev->drv->flags & PHY_POLL_CABLE_TEST)
+			return true;
+
+	return phydev->irq == PHY_POLL;
+}
+
+int genphy_c45_restart_aneg(struct phy_device *phydev)
+{
+	return phy_set_bits_mmd(phydev, MDIO_MMD_AN, MDIO_CTRL1,
+				MDIO_AN_CTRL1_ENABLE | MDIO_AN_CTRL1_RESTART);
+}
+
+static inline int genphy_c45_check_and_restart_aneg(struct phy_device *phydev,
+						    bool restart)
+{
+	int ret;
+
+	if (!restart) {
+		/* Configure and restart aneg if it wasn't set before */
+		ret = adin_read_mmd(phydev, MDIO_MMD_AN, MDIO_CTRL1);
+		if (ret < 0)
+			return ret;
+
+		if (!(ret & MDIO_AN_CTRL1_ENABLE))
+			restart = true;
+	}
+
+	if (restart)
+		return genphy_c45_restart_aneg(phydev);
+
+	return 0;
+}
+
+int genphy_c45_read_link(struct phy_device *phydev)
+{
+	u32 mmd_mask = MDIO_DEVS_PMAPMD;
+	int val, devad;
+	bool link = true;
+
+	if (phydev->c45_ids.mmds_present & MDIO_DEVS_AN) {
+		val = adin_read_mmd(phydev, MDIO_MMD_AN, MDIO_CTRL1);
+		if (val < 0)
+			return val;
+
+		/* Autoneg is being started, therefore disregard current
+		 * link status and report link as down.
+		 */
+		if (val & MDIO_AN_CTRL1_RESTART) {
+			phydev->link = 0;
+			return 0;
+		}
+	}
+
+	while (mmd_mask && link) {
+		devad = __ffs(mmd_mask);
+		mmd_mask &= ~BIT(devad);
+
+		/* The link state is latched low so that momentary link
+		 * drops can be detected. Do not double-read the status
+		 *in polling mode to detect such short link drops except
+		 *the link was already down.
+		 */
+		if (!phy_polling_mode(phydev) || !phydev->link) {
+			val = adin_read_mmd(phydev, devad, MDIO_STAT1);
+			if (val < 0)
+				return val;
+		else if (val & MDIO_STAT1_LSTATUS)
+			continue;
+		}
+
+		val = adin_read_mmd(phydev, devad, MDIO_STAT1);
+		if (val < 0)
+			return val;
+
+		if (!(val & MDIO_STAT1_LSTATUS))
+			link = false;
+	}
+
+	phydev->link = link;
+
+	return 0;
+}
+
+int __mdiobus_modify_changed(struct mii_bus *bus, int addr, u32 regnum,
+			     u16 mask, u16 set)
+{
+	int new, ret;
+
+	ret = __mdiobus_read(bus, addr, regnum);
+	if (ret < 0)
+		return ret;
+
+	new = (ret & ~mask) | set;
+	if (new == ret)
+		return 0;
+
+	ret = __mdiobus_write(bus, addr, regnum, new);
+
+	return ret < 0 ? ret : 1;
+}
+
+static inline int __phy_modify_changed(struct phy_device *phydev, u32 regnum,
+				       u16 mask, u16 set)
+{
+	return __mdiobus_modify_changed(phydev->mdio.bus, phydev->mdio.addr,
+					regnum, mask, set);
+}
+
+int __phy_modify(struct phy_device *phydev, u32 regnum, u16 mask, u16 set)
+{
+	int ret;
+
+	ret = __phy_modify_changed(phydev, regnum, mask, set);
+
+	return ret < 0 ? ret : 0;
+}
+
+int phy_modify(struct phy_device *phydev, u32 regnum, u16 mask, u16 set)
+{
+	/* This function is ported from kernel 5.15, and, in the original function,
+	 * the mdio bus mutex is locked.
+	 * Locking the mutex in this kernel will cause a deadlock,
+	 * since __phy_modify will call eventually to __mdiobus_modify_changed
+	 * which will try to lock this mutex as well.
+	 * So, no need to lock the mutex here.
+	 */
+	return __phy_modify(phydev, regnum, mask, set);
+}
+
+static inline int phy_clear_bits(struct phy_device *phydev, u32 regnum, u16 val)
+{
+	return phy_modify(phydev, regnum, val, 0);
+}
+
+static inline int phy_set_bits(struct phy_device *phydev, u32 regnum, u16 val)
+{
+	return phy_modify(phydev, regnum, 0, val);
+}
+
+enum phy_tunable_id {
+	ETHTOOL_PHY_ID_UNSPEC,
+	ETHTOOL_PHY_DOWNSHIFT,
+	ETHTOOL_PHY_FAST_LINK_DOWN,
+	ETHTOOL_PHY_EDPD,
+	__ETHTOOL_PHY_TUNABLE_COUNT,
+};
+
+#if __has_attribute(__fallthrough__)
+# define fallthrough                    __attribute__((__fallthrough__))
+#else
+# define fallthrough                    do {} while (0)  /* fallthrough */
+#endif
+
+/* END - ADIN1300 PHY Backport to kernel 4.9 */
+
+/* ORIGINAL DRIVER STARTS HERE, WITH SMALL FIXES */
+
+#define PHY_ID_ADIN1200				0x0283bc20
+#define PHY_ID_ADIN1300				0x0283bc30
+
+#define ADIN1300_MII_EXT_REG_PTR		0x0010
+#define ADIN1300_MII_EXT_REG_DATA		0x0011
+
+#define ADIN1300_PHY_CTRL1			0x0012
+#define   ADIN1300_AUTO_MDI_EN			BIT(10)
+#define   ADIN1300_MAN_MDIX_EN			BIT(9)
+
+#define ADIN1300_RX_ERR_CNT			0x0014
+
+#define ADIN1300_PHY_CTRL_STATUS2		0x0015
+#define   ADIN1300_NRG_PD_EN			BIT(3)
+#define   ADIN1300_NRG_PD_TX_EN			BIT(2)
+#define   ADIN1300_NRG_PD_STATUS		BIT(1)
+
+#define ADIN1300_PHY_CTRL2			0x0016
+#define   ADIN1300_DOWNSPEED_AN_100_EN		BIT(11)
+#define   ADIN1300_DOWNSPEED_AN_10_EN		BIT(10)
+#define   ADIN1300_GROUP_MDIO_EN		BIT(6)
+#define   ADIN1300_DOWNSPEEDS_EN	\
+	(ADIN1300_DOWNSPEED_AN_100_EN | ADIN1300_DOWNSPEED_AN_10_EN)
+
+#define ADIN1300_PHY_CTRL3			0x0017
+#define   ADIN1300_LINKING_EN			BIT(13)
+#define   ADIN1300_DOWNSPEED_RETRIES_MSK	GENMASK(12, 10)
+
+#define ADIN1300_INT_MASK_REG			0x0018
+#define   ADIN1300_INT_MDIO_SYNC_EN		BIT(9)
+#define   ADIN1300_INT_ANEG_STAT_CHNG_EN	BIT(8)
+#define   ADIN1300_INT_ANEG_PAGE_RX_EN		BIT(6)
+#define   ADIN1300_INT_IDLE_ERR_CNT_EN		BIT(5)
+#define   ADIN1300_INT_MAC_FIFO_OU_EN		BIT(4)
+#define   ADIN1300_INT_RX_STAT_CHNG_EN		BIT(3)
+#define   ADIN1300_INT_LINK_STAT_CHNG_EN	BIT(2)
+#define   ADIN1300_INT_SPEED_CHNG_EN		BIT(1)
+#define   ADIN1300_INT_HW_IRQ_EN		BIT(0)
+#define ADIN1300_INT_MASK_EN	\
+	(ADIN1300_INT_LINK_STAT_CHNG_EN | ADIN1300_INT_HW_IRQ_EN)
+#define ADIN1300_INT_STATUS_REG			0x0019
+
+#define ADIN1300_PHY_STATUS1			0x001a
+#define   ADIN1300_PAIR_01_SWAP			BIT(11)
+
+/* EEE register addresses, accessible via Clause 22 access using
+ * ADIN1300_MII_EXT_REG_PTR & ADIN1300_MII_EXT_REG_DATA.
+ * The bit-fields are the same as specified by IEEE for EEE.
+ */
+#define ADIN1300_EEE_CAP_REG			0x8000
+#define ADIN1300_EEE_ADV_REG			0x8001
+#define ADIN1300_EEE_LPABLE_REG			0x8002
+#define ADIN1300_CLOCK_STOP_REG			0x9400
+#define ADIN1300_LPI_WAKE_ERR_CNT_REG		0xa000
+
+#define ADIN1300_GE_SOFT_RESET_REG		0xff0c
+#define   ADIN1300_GE_SOFT_RESET		BIT(0)
+
+#define ADIN1300_GE_RGMII_CFG_REG		0xff23
+#define   ADIN1300_GE_RGMII_RX_MSK		GENMASK(8, 6)
+#define   ADIN1300_GE_RGMII_RX_SEL(x)		\
+		FIELD_PREP(ADIN1300_GE_RGMII_RX_MSK, x)
+#define   ADIN1300_GE_RGMII_GTX_MSK		GENMASK(5, 3)
+#define   ADIN1300_GE_RGMII_GTX_SEL(x)		\
+		FIELD_PREP(ADIN1300_GE_RGMII_GTX_MSK, x)
+#define   ADIN1300_GE_RGMII_RXID_EN		BIT(2)
+#define   ADIN1300_GE_RGMII_TXID_EN		BIT(1)
+#define   ADIN1300_GE_RGMII_EN			BIT(0)
+
+/* RGMII internal delay settings for rx and tx for ADIN1300 */
+#define ADIN1300_RGMII_1_60_NS			0x0001
+#define ADIN1300_RGMII_1_80_NS			0x0002
+#define	ADIN1300_RGMII_2_00_NS			0x0000
+#define	ADIN1300_RGMII_2_20_NS			0x0006
+#define	ADIN1300_RGMII_2_40_NS			0x0007
+
+#define ADIN1300_GE_RMII_CFG_REG		0xff24
+#define   ADIN1300_GE_RMII_FIFO_DEPTH_MSK	GENMASK(6, 4)
+#define   ADIN1300_GE_RMII_FIFO_DEPTH_SEL(x)	\
+		FIELD_PREP(ADIN1300_GE_RMII_FIFO_DEPTH_MSK, x)
+#define   ADIN1300_GE_RMII_EN			BIT(0)
+
+/* RMII fifo depth values */
+#define ADIN1300_RMII_4_BITS			0x0000
+#define ADIN1300_RMII_8_BITS			0x0001
+#define ADIN1300_RMII_12_BITS			0x0002
+#define ADIN1300_RMII_16_BITS			0x0003
+#define ADIN1300_RMII_20_BITS			0x0004
+#define ADIN1300_RMII_24_BITS			0x0005
+
+/**
+ * struct adin_cfg_reg_map - map a config value to aregister value
+ * @cfg:	value in device configuration
+ * @reg:	value in the register
+ */
+struct adin_cfg_reg_map {
+	int cfg;
+	int reg;
+};
+
+static const struct adin_cfg_reg_map adin_rgmii_delays[] = {
+	{ 1600, ADIN1300_RGMII_1_60_NS },
+	{ 1800, ADIN1300_RGMII_1_80_NS },
+	{ 2000, ADIN1300_RGMII_2_00_NS },
+	{ 2200, ADIN1300_RGMII_2_20_NS },
+	{ 2400, ADIN1300_RGMII_2_40_NS },
+	{ },
+};
+
+static const struct adin_cfg_reg_map adin_rmii_fifo_depths[] = {
+	{ 4,  ADIN1300_RMII_4_BITS },
+	{ 8,  ADIN1300_RMII_8_BITS },
+	{ 12, ADIN1300_RMII_12_BITS },
+	{ 16, ADIN1300_RMII_16_BITS },
+	{ 20, ADIN1300_RMII_20_BITS },
+	{ 24, ADIN1300_RMII_24_BITS },
+	{ },
+};
+
+/**
+ * struct adin_clause45_mmd_map - map to convert Clause 45 regs to Clause 22
+ * @devad:		device address used in Clause 45 access
+ * @cl45_regnum:	register address defined by Clause 45
+ * @adin_regnum:	equivalent register address accessible via Clause 22
+ */
+struct adin_clause45_mmd_map {
+	int devad;
+	u16 cl45_regnum;
+	u16 adin_regnum;
+};
+
+static const struct adin_clause45_mmd_map adin_clause45_mmd_map[] = {
+	{ MDIO_MMD_PCS,	MDIO_PCS_EEE_ABLE,	ADIN1300_EEE_CAP_REG },
+	{ MDIO_MMD_AN,	MDIO_AN_EEE_LPABLE,	ADIN1300_EEE_LPABLE_REG },
+	{ MDIO_MMD_AN,	MDIO_AN_EEE_ADV,	ADIN1300_EEE_ADV_REG },
+	{ MDIO_MMD_PCS,	MDIO_CTRL1,		ADIN1300_CLOCK_STOP_REG },
+	{ MDIO_MMD_PCS, MDIO_PCS_EEE_WK_ERR,	ADIN1300_LPI_WAKE_ERR_CNT_REG },
+};
+
+struct adin_hw_stat {
+	const char *string;
+	u16 reg1;
+	u16 reg2;
+};
+
+static const struct adin_hw_stat adin_hw_stats[] = {
+	{ "total_frames_checked_count",		0x940A, 0x940B }, /* hi + lo */
+	{ "length_error_frames_count",		0x940C },
+	{ "alignment_error_frames_count",	0x940D },
+	{ "symbol_error_count",			0x940E },
+	{ "oversized_frames_count",		0x940F },
+	{ "undersized_frames_count",		0x9410 },
+	{ "odd_nibble_frames_count",		0x9411 },
+	{ "odd_preamble_packet_count",		0x9412 },
+	{ "dribble_bits_frames_count",		0x9413 },
+	{ "false_carrier_events_count",		0x9414 },
+};
+
+/**
+ * struct adin_priv - ADIN PHY driver private data
+ * @stats:		statistic counters for the PHY
+ */
+struct adin_priv {
+	u64			stats[ARRAY_SIZE(adin_hw_stats)];
+};
+
+static int adin_lookup_reg_value(const struct adin_cfg_reg_map *tbl, int cfg)
+{
+	size_t i;
+
+	for (i = 0; tbl[i].cfg; i++) {
+		if (tbl[i].cfg == cfg)
+			return tbl[i].reg;
+	}
+
+	return -EINVAL;
+}
+
+static u32 adin_get_reg_value(struct phy_device *phydev,
+			      const char *prop_name,
+			      const struct adin_cfg_reg_map *tbl,
+			      u32 dflt)
+{
+	struct device *dev = &phydev->mdio.dev;
+	u32 val;
+	int rc;
+
+	if (device_property_read_u32(dev, prop_name, &val))
+		return dflt;
+
+	rc = adin_lookup_reg_value(tbl, val);
+	if (rc < 0) {
+		phydev_warn(phydev,
+			    "Unsupported value %u for %s using default (%u)\n",
+			    val, prop_name, dflt);
+		return dflt;
+	}
+
+	return rc;
+}
+
+static int adin_config_rgmii_mode(struct phy_device *phydev)
+{
+	u32 val;
+	int reg;
+
+	if (!phy_interface_is_rgmii(phydev))
+		return phy_clear_bits_mmd(phydev, MDIO_MMD_VEND1,
+					  ADIN1300_GE_RGMII_CFG_REG,
+					  ADIN1300_GE_RGMII_EN);
+
+	reg = adin_read_mmd(phydev, MDIO_MMD_VEND1, ADIN1300_GE_RGMII_CFG_REG);
+	if (reg < 0)
+		return reg;
+
+	reg |= ADIN1300_GE_RGMII_EN;
+
+	if (phydev->interface == PHY_INTERFACE_MODE_RGMII_ID ||
+	    phydev->interface == PHY_INTERFACE_MODE_RGMII_RXID) {
+		reg |= ADIN1300_GE_RGMII_RXID_EN;
+
+		val = adin_get_reg_value(phydev, "adi,rx-internal-delay-ps",
+					 adin_rgmii_delays,
+					 ADIN1300_RGMII_2_00_NS);
+		reg &= ~ADIN1300_GE_RGMII_RX_MSK;
+		reg |= ADIN1300_GE_RGMII_RX_SEL(val);
+	} else {
+		reg &= ~ADIN1300_GE_RGMII_RXID_EN;
+	}
+
+	if (phydev->interface == PHY_INTERFACE_MODE_RGMII_ID ||
+	    phydev->interface == PHY_INTERFACE_MODE_RGMII_TXID) {
+		reg |= ADIN1300_GE_RGMII_TXID_EN;
+
+		val = adin_get_reg_value(phydev, "adi,tx-internal-delay-ps",
+					 adin_rgmii_delays,
+					 ADIN1300_RGMII_2_00_NS);
+		reg &= ~ADIN1300_GE_RGMII_GTX_MSK;
+		reg |= ADIN1300_GE_RGMII_GTX_SEL(val);
+	} else {
+		reg &= ~ADIN1300_GE_RGMII_TXID_EN;
+	}
+
+	return adin_write_mmd(phydev, MDIO_MMD_VEND1,
+			     ADIN1300_GE_RGMII_CFG_REG, reg);
+}
+
+static int adin_config_rmii_mode(struct phy_device *phydev)
+{
+	u32 val;
+	int reg;
+
+	if (phydev->interface != PHY_INTERFACE_MODE_RMII)
+		return phy_clear_bits_mmd(phydev, MDIO_MMD_VEND1,
+					  ADIN1300_GE_RMII_CFG_REG,
+					  ADIN1300_GE_RMII_EN);
+
+	reg = adin_read_mmd(phydev, MDIO_MMD_VEND1, ADIN1300_GE_RMII_CFG_REG);
+	if (reg < 0)
+		return reg;
+
+	reg |= ADIN1300_GE_RMII_EN;
+
+	val = adin_get_reg_value(phydev, "adi,fifo-depth-bits",
+				 adin_rmii_fifo_depths,
+				 ADIN1300_RMII_8_BITS);
+
+	reg &= ~ADIN1300_GE_RMII_FIFO_DEPTH_MSK;
+	reg |= ADIN1300_GE_RMII_FIFO_DEPTH_SEL(val);
+
+	return adin_write_mmd(phydev, MDIO_MMD_VEND1,
+			     ADIN1300_GE_RMII_CFG_REG, reg);
+}
+
+static int adin_set_downshift(struct phy_device *phydev, u8 cnt)
+{
+	u16 val;
+	int rc;
+
+	if (cnt == DOWNSHIFT_DEV_DISABLE)
+		return phy_clear_bits(phydev, ADIN1300_PHY_CTRL2,
+				      ADIN1300_DOWNSPEEDS_EN);
+
+	if (cnt > 7)
+		return -E2BIG;
+
+	val = FIELD_PREP(ADIN1300_DOWNSPEED_RETRIES_MSK, cnt);
+	val |= ADIN1300_LINKING_EN;
+
+	rc = phy_modify(phydev, ADIN1300_PHY_CTRL3,
+			ADIN1300_LINKING_EN | ADIN1300_DOWNSPEED_RETRIES_MSK,
+			val);
+	if (rc < 0)
+		return rc;
+
+	return phy_set_bits(phydev, ADIN1300_PHY_CTRL2,
+			    ADIN1300_DOWNSPEEDS_EN);
+}
+
+static int adin_set_edpd(struct phy_device *phydev, u16 tx_interval)
+{
+	u16 val;
+
+	if (tx_interval == ETHTOOL_PHY_EDPD_DISABLE)
+		return phy_clear_bits(phydev, ADIN1300_PHY_CTRL_STATUS2,
+				(ADIN1300_NRG_PD_EN | ADIN1300_NRG_PD_TX_EN));
+
+	val = ADIN1300_NRG_PD_EN;
+
+	switch (tx_interval) {
+	case 1000: /* 1 second */
+		fallthrough;
+	case ETHTOOL_PHY_EDPD_DFLT_TX_MSECS:
+		val |= ADIN1300_NRG_PD_TX_EN;
+		fallthrough;
+	case ETHTOOL_PHY_EDPD_NO_TX:
+		break;
+	default:
+		return -EINVAL;
+	}
+
+	return phy_modify(phydev, ADIN1300_PHY_CTRL_STATUS2,
+			  (ADIN1300_NRG_PD_EN | ADIN1300_NRG_PD_TX_EN),
+			  val);
+}
+
+static int adin_config_init(struct phy_device *phydev)
+{
+	int rc;
+
+	phydev->mdix_ctrl = ETH_TP_MDI_AUTO;
+
+	rc = adin_config_rgmii_mode(phydev);
+	if (rc < 0)
+		return rc;
+
+	rc = adin_config_rmii_mode(phydev);
+	if (rc < 0)
+		return rc;
+
+	rc = adin_set_downshift(phydev, 4);
+
+	if (rc < 0)
+		return rc;
+
+	rc = adin_set_edpd(phydev, ETHTOOL_PHY_EDPD_DFLT_TX_MSECS);
+	if (rc < 0)
+		return rc;
+
+	phydev_dbg(phydev, "PHY is using mode '%s'\n",
+		   phy_modes(phydev->interface));
+
+	/* Driver Fix I added: Configure clock by writing to clock register, 125MHz  + SW reset */
+
+	/* Configure clock */
+	adin_write_mmd(phydev, MDIO_MMD_VEND1, 0xff1f, BIT(4));
+	/* SW reset */
+	adin_write_mmd(phydev, MDIO_MMD_VEND1, 0x0, BIT(15));
+
+	return 0;
+}
+
+static int adin_phy_ack_intr(struct phy_device *phydev)
+{
+	/* Clear pending interrupts */
+	int rc = phy_read(phydev, ADIN1300_INT_STATUS_REG);
+
+	return rc < 0 ? rc : 0;
+}
+
+static int adin_phy_config_intr(struct phy_device *phydev)
+{
+	if (phydev->interrupts == PHY_INTERRUPT_ENABLED)
+		return phy_set_bits(phydev, ADIN1300_INT_MASK_REG,
+				    ADIN1300_INT_MASK_EN);
+
+	return phy_clear_bits(phydev, ADIN1300_INT_MASK_REG,
+			      ADIN1300_INT_MASK_EN);
+}
+
+static int adin_cl45_to_adin_reg(struct phy_device *phydev, int devad,
+				 u16 cl45_regnum)
+{
+	const struct adin_clause45_mmd_map *m;
+	int i;
+
+	if (devad == MDIO_MMD_VEND1)
+		return cl45_regnum;
+
+	for (i = 0; i < ARRAY_SIZE(adin_clause45_mmd_map); i++) {
+		m = &adin_clause45_mmd_map[i];
+		if (m->devad == devad && m->cl45_regnum == cl45_regnum)
+			return m->adin_regnum;
+	}
+
+	phydev_err(phydev,
+		   "No translation available for devad: %d reg: %04x\n",
+		   devad, cl45_regnum);
+
+	return -EINVAL;
+}
+
+int adin_read_mmd(struct phy_device *phydev, int devad, u32 regnum)
+{
+	struct mii_bus *bus = phydev->mdio.bus;
+	int phy_addr = phydev->mdio.addr;
+	int adin_regnum;
+	int err;
+
+	regnum = (u16)regnum;
+
+	adin_regnum = adin_cl45_to_adin_reg(phydev, devad, regnum);
+	if (adin_regnum < 0)
+		return adin_regnum;
+
+	err = __mdiobus_write(bus, phy_addr, ADIN1300_MII_EXT_REG_PTR,
+			      adin_regnum);
+	if (err)
+		return err;
+
+	return __mdiobus_read(bus, phy_addr, ADIN1300_MII_EXT_REG_DATA);
+}
+
+int adin_write_mmd(struct phy_device *phydev, int devad, u16 regnum,
+		   u16 val)
+{
+	struct mii_bus *bus = phydev->mdio.bus;
+	int phy_addr = phydev->mdio.addr;
+	int adin_regnum;
+	int err;
+
+	adin_regnum = adin_cl45_to_adin_reg(phydev, devad, regnum);
+	if (adin_regnum < 0)
+		return adin_regnum;
+
+	err = __mdiobus_write(bus, phy_addr, ADIN1300_MII_EXT_REG_PTR,
+			      adin_regnum);
+	if (err)
+		return err;
+
+	return __mdiobus_write(bus, phy_addr, ADIN1300_MII_EXT_REG_DATA, val);
+}
+
+static int adin_config_mdix(struct phy_device *phydev)
+{
+	bool auto_en, mdix_en;
+	int reg;
+
+	mdix_en = false;
+	auto_en = false;
+	switch (phydev->mdix_ctrl) {
+	case ETH_TP_MDI:
+		break;
+	case ETH_TP_MDI_X:
+		mdix_en = true;
+		break;
+	case ETH_TP_MDI_AUTO:
+		auto_en = true;
+		break;
+	default:
+		return -EINVAL;
+	}
+
+	reg = phy_read(phydev, ADIN1300_PHY_CTRL1);
+	if (reg < 0)
+		return reg;
+
+	if (mdix_en)
+		reg |= ADIN1300_MAN_MDIX_EN;
+	else
+		reg &= ~ADIN1300_MAN_MDIX_EN;
+
+	if (auto_en)
+		reg |= ADIN1300_AUTO_MDI_EN;
+	else
+		reg &= ~ADIN1300_AUTO_MDI_EN;
+
+	return phy_write(phydev, ADIN1300_PHY_CTRL1, reg);
+}
+
+static int adin_config_aneg(struct phy_device *phydev)
+{
+	int ret;
+
+	ret = adin_config_mdix(phydev);
+	if (ret)
+		return ret;
+
+	return genphy_config_aneg(phydev);
+}
+
+static int adin_mdix_update(struct phy_device *phydev)
+{
+	bool auto_en, mdix_en;
+	bool swapped;
+	int reg;
+
+	reg = phy_read(phydev, ADIN1300_PHY_CTRL1);
+	if (reg < 0)
+		return reg;
+
+	auto_en = !!(reg & ADIN1300_AUTO_MDI_EN);
+	mdix_en = !!(reg & ADIN1300_MAN_MDIX_EN);
+
+	/* If MDI/MDIX is forced, just read it from the control reg */
+	if (!auto_en) {
+		if (mdix_en)
+			phydev->mdix = ETH_TP_MDI_X;
+		else
+			phydev->mdix = ETH_TP_MDI;
+		return 0;
+	}
+
+	/**
+	 * Otherwise, we need to deduce it from the PHY status2 reg.
+	 * When Auto-MDI is enabled, the ADIN1300_MAN_MDIX_EN bit implies
+	 * a preference for MDIX when it is set.
+	 */
+	reg = phy_read(phydev, ADIN1300_PHY_STATUS1);
+	if (reg < 0)
+		return reg;
+
+	swapped = !!(reg & ADIN1300_PAIR_01_SWAP);
+
+	if (mdix_en != swapped)
+		phydev->mdix = ETH_TP_MDI_X;
+	else
+		phydev->mdix = ETH_TP_MDI;
+
+	return 0;
+}
+
+static int adin_read_status(struct phy_device *phydev)
+{
+	int ret;
+
+	ret = adin_mdix_update(phydev);
+	if (ret < 0)
+		return ret;
+
+	return genphy_read_status(phydev);
+}
+
+static int adin_soft_reset(struct phy_device *phydev)
+{
+	int rc;
+	/* The reset bit is self-clearing, set it and wait */
+	rc = phy_set_bits_mmd(phydev, MDIO_MMD_VEND1,
+			      ADIN1300_GE_SOFT_RESET_REG,
+			      ADIN1300_GE_SOFT_RESET);
+	if (rc < 0)
+		return rc;
+
+	msleep(20);
+
+	/* If we get a read error something may be wrong */
+	rc = adin_read_mmd(phydev, MDIO_MMD_VEND1,
+			   ADIN1300_GE_SOFT_RESET_REG);
+
+	return rc < 0 ? rc : 0;
+}
+
+static int adin_get_sset_count(struct phy_device *phydev)
+{
+	return ARRAY_SIZE(adin_hw_stats);
+}
+
+static void adin_get_strings(struct phy_device *phydev, u8 *data)
+{
+	int i;
+
+	for (i = 0; i < ARRAY_SIZE(adin_hw_stats); i++) {
+		strlcpy(&data[i * ETH_GSTRING_LEN],
+			adin_hw_stats[i].string, ETH_GSTRING_LEN);
+	}
+}
+
+static int adin_read_mmd_stat_regs(struct phy_device *phydev,
+				   const struct adin_hw_stat *stat,
+				   u32 *val)
+{
+	int ret;
+
+	ret = adin_read_mmd(phydev, MDIO_MMD_VEND1, stat->reg1);
+	if (ret < 0)
+		return ret;
+
+	*val = (ret & 0xffff);
+
+	if (stat->reg2 == 0)
+		return 0;
+
+	ret = adin_read_mmd(phydev, MDIO_MMD_VEND1, stat->reg2);
+	if (ret < 0)
+		return ret;
+
+	*val <<= 16;
+	*val |= (ret & 0xffff);
+
+	return 0;
+}
+
+static u64 adin_get_stat(struct phy_device *phydev, int i)
+{
+	const struct adin_hw_stat *stat = &adin_hw_stats[i];
+	struct adin_priv *priv = phydev->priv;
+	u32 val;
+	int ret;
+
+	if (stat->reg1 > 0x1f) {
+		ret = adin_read_mmd_stat_regs(phydev, stat, &val);
+		if (ret < 0)
+			return (u64)(~0);
+	} else {
+		ret = phy_read(phydev, stat->reg1);
+		if (ret < 0)
+			return (u64)(~0);
+		val = (ret & 0xffff);
+	}
+
+	priv->stats[i] += val;
+
+	return priv->stats[i];
+}
+
+static void adin_get_stats(struct phy_device *phydev,
+			   struct ethtool_stats *stats, u64 *data)
+{
+	int i, rc;
+
+	/* latch copies of all the frame-checker counters */
+	rc = phy_read(phydev, ADIN1300_RX_ERR_CNT);
+	if (rc < 0)
+		return;
+
+	for (i = 0; i < ARRAY_SIZE(adin_hw_stats); i++)
+		data[i] = adin_get_stat(phydev, i);
+}
+
+static int adin_probe(struct phy_device *phydev)
+{
+	struct device *dev = &phydev->mdio.dev;
+	struct adin_priv *priv;
+
+	priv = devm_kzalloc(dev, sizeof(*priv), GFP_KERNEL);
+	if (!priv)
+		return -ENOMEM;
+
+	phydev->priv = priv;
+
+	return 0;
+}
+
+static struct phy_driver adin_driver[] = {
+	{
+		PHY_ID_MATCH_MODEL(PHY_ID_ADIN1200),
+		.name		= "ADIN1200",
+		 /* FIXME: remove this when the `get_features` hook becomes available */
+		.features	= PHY_BASIC_FEATURES,
+		.probe		= adin_probe,
+		.config_init	= adin_config_init,
+		.soft_reset	= adin_soft_reset,
+		.config_aneg	= adin_config_aneg,
+		.read_status	= adin_read_status,
+		.ack_interrupt	= adin_phy_ack_intr,
+		.config_intr	= adin_phy_config_intr,
+		.get_sset_count	= adin_get_sset_count,
+		.get_strings	= adin_get_strings,
+		.get_stats	= adin_get_stats,
+		.resume		= genphy_resume,
+		.suspend	= genphy_suspend,
+	},
+	{
+		PHY_ID_MATCH_MODEL(PHY_ID_ADIN1300),
+		.name		= "ADIN1300",
+		 /* FIXME: remove this when the `get_features` hook becomes available */
+		.features	= PHY_GBIT_FEATURES,
+		.probe		= adin_probe,
+		.config_init	= adin_config_init,
+		.soft_reset	= adin_soft_reset,
+		.config_aneg	= adin_config_aneg,
+		.read_status	= adin_read_status,
+		.ack_interrupt	= adin_phy_ack_intr,
+		.config_intr	= adin_phy_config_intr,
+		.get_sset_count	= adin_get_sset_count,
+		.get_strings	= adin_get_strings,
+		.get_stats	= adin_get_stats,
+		.resume		= genphy_resume,
+		.suspend	= genphy_suspend,
+	},
+};
+
+module_phy_driver(adin_driver);
+
+static struct mdio_device_id __maybe_unused adin_tbl[] = {
+	{ PHY_ID_MATCH_MODEL(PHY_ID_ADIN1200) },
+	{ PHY_ID_MATCH_MODEL(PHY_ID_ADIN1300) },
+	{ }
+};
+
+MODULE_DEVICE_TABLE(mdio, adin_tbl);
+MODULE_DESCRIPTION("Analog Devices Industrial Ethernet PHY driver");
+MODULE_LICENSE("GPL");
diff --git a/include/linux/phy.h b/include/linux/phy.h
index cc374eb4..69cc7481 100644
--- a/include/linux/phy.h
+++ b/include/linux/phy.h
@@ -320,6 +320,7 @@ enum phy_state {
  */
 struct phy_c45_device_ids {
 	u32 devices_in_package;
+	u32 mmds_present;
 	u32 device_ids[8];
 };
 
@@ -424,7 +425,7 @@ struct phy_device {
 	struct net_device *attached_dev;
 
 	u8 mdix;
-
+	u8 mdix_ctrl;
 	void (*adjust_link)(struct net_device *dev);
 };
 #define to_phy_device(d) container_of(to_mdio_device(d), \
-- 
2.25.1

```

If you are using a different U-boot/Linux kenrel, and you're not able to apply this patch, please contact us for assistance.
