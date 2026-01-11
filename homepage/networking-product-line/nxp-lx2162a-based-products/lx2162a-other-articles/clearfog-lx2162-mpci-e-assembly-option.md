# ClearFog LX2162 mPCI-E Assembly Option

## Revisions and Notes

|            |           |              |           |
| ---------- | --------- | ------------ | --------- |
| **Date**   | **Owner** | **Revision** | **Notes** |
| 17/09/2025 | Josua     | 1            | release   |

> \[!INFO] No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

## Introduction

LX2162A Clearfog board has 2x mini-pcie connectors by default supporting just USB-2.0 interface.

There is an assembly option for rerouting lanes from 2x RJ45 ports to the mpcie connectors, enabling PCI-E Gen. 3 x1 on each connector while disabling 2x RJ45 ports.

This page describes the required rework.

## Electrical Rework

| **Component**   | **Description**                         | **Part Number**       |
| --------------- | --------------------------------------- | --------------------- |
| capacitor 100nF | CAP CER 0.1uF ±10% 25V X7R 0402 Low ESR | e.g. 0402X104K250SNT  |
| resistor 0-Ohm  | RES SMD 0 OHM JUMPER 1/16W 0402         | e.g. CR0402-J/-000GLF |

| **Part Label** | **Part**        | **Action**                  |
| -------------- | --------------- | --------------------------- |
| C130           | capacitor 100nF | remove                      |
| C131           | capacitor 100nF | remove                      |
| C137           | capacitor 100nF | remove                      |
| C138           | capacitor 100nF | remove                      |
| C153           | capacitor 100nF | remove                      |
| C154           | capacitor 100nF | remove                      |
| C157           | capacitor 100nF | remove                      |
| C158           | capacitor 100nF | remove                      |
| C3122          | capacitor 100nF | place (reuse removed parts) |
| C3123          | capacitor 100nF | place (reuse removed parts) |
| C3124          | capacitor 100nF | place (reuse removed parts) |
| C3125          | capacitor 100nF | place (reuse removed parts) |
| R59            | resistor 0-Ohm  | place                       |
| R60            | resistor 0-Ohm  | place                       |
| R65            | resistor 0-Ohm  | place                       |
| R67            | resistor 0-Ohm  | place                       |

Components are located next to the 8-port ethernet phy near SoM and RJ45 connectors, covered by the black heatsink.

![lx2162a-clearfog-mpcie-rework.jpg](../../../../.gitbook/assets/lx2162a-clearfog-mpcie-rework.jpg)

## Software Changes

The default software images are configured for 8xRJ45 ports, and zero PCI-E. After rework images with SerDes #2 protocols 7 or 11 should be selected instead - indicated by including these numbers within their filenames, e.g. “lx2162a\_rev2\_som\_clearfog\_multi\_2000\_650\_2900\_18\_**11**\_0-daa413c.img.xz“.
