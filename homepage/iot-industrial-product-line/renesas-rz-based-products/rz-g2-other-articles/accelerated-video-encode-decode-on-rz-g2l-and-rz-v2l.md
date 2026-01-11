# Accelerated Video Encode & Decode on RZ/G2L and RZ/V2L

RZ/G2L and RZ/V2L SoCs include hardware h264 encoding and decoding hardware.  
This page gives example on usage.

<a id="requirements"></a>

### Requirements

This feature requires Renesas' proprietary “RZ MPU Video Codec Library for RZ/G2L & RZ/V2L” which is an optional feature of [SolidRun Yocto for RZ Family](https://github.com/SolidRun/meta-solidrun-arm-rzg2lc).

<a id="decode"></a>

### Decode

```
# Get Demo File
wget https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_h264.mov

# This requires an active wayland compositor, e.g. weston
gst-launch-1.0 filesrc location=big_buck_bunny_720p_h264.mov \
  ! qtdemux ! h264parse ! omxh264dec ! vspmfilter outbuf-alloc=true ! waylandsink
```

<a id="encode"></a>

### Encode

TBD.