# i.MX6 GPU/VPU

<a id="description"></a>

### Description

Vivante’s fourth generation (Gen 4) Vega ScalarMorphic architecture provides a foundation for our newest series of low-power, high-performance, silicon-efficient GPGPU cores. Gen 4 products support the most advanced GPGPU APIs and profiles for leading applications that take full advantage of GPU Compute for vision processing, gesture processing, Advanced Driver Assistance Systems, Augmented Reality, and much more. These cores are available as GPGPU only cores targeting high performance Compute applications that do not require any 3D functionality (CC or Compute Cores) or as part of our standard 3D products that give full flexibility to application developers and product offerings.  
(source: [vivantecorp.com](http://vivantecorp.com))

<a id="comparison-table"></a>

### Comparison Table

|     |     |     |
| --- | --- | --- |
| Graphics Processing Unit | Vivante GC880 | Vivante GC2000 |
| 3D Graphics Support | OpenGL ES 1.1/2.0 | OpenGL ES 1.1/2.0, OpenCL 1.1E |
| HW Video Dec/Enc | Multi- Format | Multi- Format |

<a id="supported-codecs"></a>

### Supported Codecs

All imx6 Soms have the same Video Processing Unit, which supports decoding the following codecs in hardware per Table 9-8 of the i.MX 6 Solo/DualLite Applications Processor Reference Manual and Table 9-8 of the i.MX 6 Dual/Quad Application Processor Reference Manual:

| Dec/Enc | Standard | Profile | Resolution | Bitrate | Comments |
| --- | --- | --- | --- | --- | --- |
| Decoder | MPEG-2 | Main-High | 1080 i/p, 30fps | 50 Mbps | 1080p+SD at 30fps, 720p60 |
| Decoder | MPEG4/XviD | SP/ASP | 1080 i/p, 30fps | 40 Mbps | —   |
| Decoder | H.263 | P0/P3 | 16CIF, 30fps | 20 Mbps | —   |
| Decoder | H.264 | BP/CBP/MP/HP | 1080 i/p, 30fps | 50 Mbps | 1080p+SD at 30fps, 720p60 |
| Decoder | H.264-MVC | BP/MP/HP | 720p, 30fps | —   | —   |
| Decoder | VC1 | SP/MP/AP | 1080 i/p, 30fps | 45 Mbps | 1080p+SD at 30fps, 720p60 |
| Decoder | DivX | 3/4/5/6 | 1090 i/p, 30fps | 20 Mbps | —   |
| Decoder | On2 VP8 | —   | 720p, 30fps | 20 Mbps | —   |
| Decoder | MJPEG | Baseline | 8192 x 8192 | 120 Mpixel/sec | Perf shown at 4:4:4 format |
| Decoder | RV  | 8/9/10 | 1080p, 30fps | 40 Mbps | —   |
| Decoder | On2 VP6 | —   | 720p, 30fps | 20 Mbps | —   |
| Decoder | Theora | —   | 720p, 30fps | 20 Mbps | —   |
| Decoder | AVS | Jizhun | 1080 i/p, 30fps | 40 Mbps | —   |
| /   |     |     |     |     |     |
| Encoder | MPEG4 | Simple | 720p, 30fps | —   | VPU can generate higher bitrate than the maximum specified by the corresponding standard |
| Encoder | H.263 | P0/P3 | 4CIF, 30fps | 8 Mbps | VPU can generate higher bitrate than the maximum specified by the corresponding standard |
| Encoder | H.264 | BP/CBP | 1080p, 30fps | 14 Mbps | VPU can generate higher bitrate than the maximum specified by the corresponding standard |
| Encoder | MJPEG | Baseline | 8192 x 8192 | 160 Mpixel/sec | Perf shown at 4:2:2 format |

A note from the Reference manual states: “RealNetworks video codec is disabled by default on [i.MX](http://i.MX) 6 series processors. Please contact your FSL sales representative for more details.”

<a id="external-links-and-references"></a>

### External Links and References

- IMX6 Software Development/Drivers
- IMX6 Som Documents
- SolidRun Som Website
- Freescale i.MX6 Series Documentation Website
- [vivantecorp.com](http://vivantecorp.com)