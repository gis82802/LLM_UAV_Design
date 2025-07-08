

# **GNSS antennas**

## **RF design considerations for u-blox GNSS receivers**

**Application note**

#### **Abstract**

This document provides an overview of important antenna and interference issues to be considered when integrating u-blox GNSS receivers.



**[www.u-blox.com](http://www.u-blox.com/)** UBX-15030289 - R03



## <span id="page-1-0"></span>**Document information**

| Title                  | GNSS antennas                                      |             |  |
|------------------------|----------------------------------------------------|-------------|--|
| Subtitle               | RF design considerations for u-blox GNSS receivers |             |  |
| Document type          | Application note                                   |             |  |
| Document number        | UBX-15030289                                       |             |  |
| Revision and date      | R03                                                | 16-Oct-2019 |  |
| Disclosure restriction |                                                    |             |  |

This document applies to the following products:

**Product name**

All u-blox GNSS products

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

|   | Document information2 |                                                   |    |  |  |
|---|-----------------------|---------------------------------------------------|----|--|--|
|   |                       | Contents<br>3                                     |    |  |  |
| 1 |                       | Introduction5                                     |    |  |  |
| 2 |                       | Antenna basics5                                   |    |  |  |
|   | 2.1                   | General considerations 5                          |    |  |  |
|   | 2.2                   | Antenna requirements5                             |    |  |  |
|   | 2.3                   | Antenna placement 6                               |    |  |  |
|   | 2.4                   | Active and passive antennas6                      |    |  |  |
| 3 |                       | Passive antenna types8                            |    |  |  |
|   | 3.1                   | Patch antenna 8                                   |    |  |  |
|   | 3.2                   | Helix antenna 9                                   |    |  |  |
|   | 3.3                   | Monopole antennas 9                               |    |  |  |
|   |                       | 3.3.1<br>Chip antenna9                            |    |  |  |
|   |                       | 3.3.2<br>Fractal Element Antenna (FEA)12          |    |  |  |
|   | 3.4                   | Dipole antenna12                                  |    |  |  |
|   | 3.5                   | Loop antenna 13                                   |    |  |  |
|   | 3.6                   | Planar Inverted F Antenna (PIFA) 14               |    |  |  |
|   | 3.7                   | High-end GNSS antennas 14                         |    |  |  |
| 4 |                       | Which antenna is best for my application?<br>     | 15 |  |  |
|   | 4.1                   | Helix or patch?15                                 |    |  |  |
|   | 4.2                   | Other antenna types 15                            |    |  |  |
| 5 |                       | Design considerations                             | 16 |  |  |
|   | 5.1                   | Patch antennas 16                                 |    |  |  |
|   |                       | 5.1.1<br>Ground plane16                           |    |  |  |
|   |                       | 5.1.2<br>Placement 17                             |    |  |  |
|   |                       | 5.1.3<br>ESD issues18                             |    |  |  |
|   | 5.2                   | Helix antennas 18                                 |    |  |  |
|   |                       | 5.2.1<br>Ground plane19                           |    |  |  |
|   |                       | 5.2.2<br>Placement 19                             |    |  |  |
|   | 5.3                   | Antenna matching19                                |    |  |  |
|   | 5.4                   | GSM applications 20                               |    |  |  |
|   |                       | 5.4.1<br>Isolation between GNSS and GSM antenna20 |    |  |  |
|   | 5.5                   | Dual antenna systems 20                           |    |  |  |
| 6 |                       | Interference issues                               | 23 |  |  |
|   | 6.1                   | Sources of noise 23                               |    |  |  |
|   | 6.2                   | Eliminating digital noise sources24               |    |  |  |
|   |                       | 6.2.1<br>Power and ground planes24                |    |  |  |
|   |                       | 6.2.2<br>High-speed signal lines25                |    |  |  |
|   |                       | 6.2.3<br>Decoupling capacitors 25                 |    |  |  |
|   | 6.3                   | Shielding 26                                      |    |  |  |



| 6.3.1<br>Feed through capacitors 27                                     |    |  |  |  |
|-------------------------------------------------------------------------|----|--|--|--|
| 6.3.2<br>Shielding sets of sub-system assembly 28                       |    |  |  |  |
| 6.4<br>Increasing jamming immunity29                                    |    |  |  |  |
| 6.4.1<br>In-band jamming29                                              |    |  |  |  |
| 6.4.2<br>Out-band jamming 30                                            |    |  |  |  |
| 7<br>Performance tests                                                  | 31 |  |  |  |
| 7.1<br>Sky View31                                                       |    |  |  |  |
| 7.2<br>Statistic View31                                                 |    |  |  |  |
| 7.3<br>Supply voltage check32                                           |    |  |  |  |
| 7.4<br>Sensitivity test 32                                              |    |  |  |  |
| 7.5<br>Startup test32                                                   |    |  |  |  |
| Appendix<br>                                                            | 33 |  |  |  |
| A<br>Example of receiver signal to noise (C/No) performance calculation | 33 |  |  |  |
| Related documents<br>                                                   | 35 |  |  |  |
| Revision history<br>35                                                  |    |  |  |  |
| Contact                                                                 | 36 |  |  |  |



# <span id="page-4-0"></span>**1 Introduction**

Antennas are a critical part of any GNSS receiver design and their importance cannot be stated highly enough. Even the best receiver cannot bring back what has been lost due to a poor antenna, in-band jamming, or a bad RF board design. GNSS signals are extremely weak and present unique demands on the antenna. The choice and implementation of the antenna can ultimately play a significant role in GNSS performance.

This document considers some of the RF and interference issues when implementing a GNSS antenna.

## <span id="page-4-1"></span>**2 Antenna basics**

### <span id="page-4-2"></span>**2.1 General considerations**

A GNSS receiver needs to receive signals from as many satellites as possible. Optimal performance will not be available in narrow streets and underground parking lots or if objects cover the antenna. Poor visibility may result in position drift or a prolonged Time-To-First-Fix (TTFF). **Good sky visibility is therefore an important advantage.** A GNSS receiver will only achieve the specified performance if the average carrier to noise power density ratio (C/N0) of the strongest satellites reaches at least 44 dBHz. In a well-designed system, the average of the C/N<sup>0</sup> ratio of high elevation satellites should be in the range between 44 dBHz and about 50 dBHz. With a standard off-the-shelf active antenna, 47 dBHz should easily be achieved.

### <span id="page-4-3"></span>**2.2 Antenna requirements**

For optimal performance, use antennas with high gain (e.g. >4 dBic) and active antennas with an LNA with a low noise figure (<2 dB). Ideally, the antenna has:

- A low level of directivity<sup>1</sup> (se[e Figure 1\)](#page-4-4)
- Good antenna visibility to the sky
- Good matching between antenna and cable impedance
- High gain
- Filter



<span id="page-4-4"></span>**Figure 1: Antenna radiation pattern showing low directivity (left) vs. high directivity (right)**

**☞** Appendix [A](#page-32-1) provides an example of how to estimate the influence of the noise figure (NF) and gain on antenna performance.

<sup>1</sup> Antenna gain increases with the level of directivity.



### <span id="page-5-0"></span>**2.3 Antenna placement**

The position of the antenna mounting is crucial for an optimal performance of the GNSS receiver. When using patch antennas, the antenna plane should be parallel to the geographic horizon. The antenna must have full view of the sky ensuring a direct line-of-sight with as many visible satellites as possible.

#### **1 st choice placement 2**

Recommended antenna positions Performance may be degraded!



#### **nd choice placement**

If recommended placements are not available, these may also be viable.



Note: Window and roof reduce GNSS signal and obstruct sky view<sup>2</sup>



Note: There may be multipath signals and an obstructed sky view



Note: Fiberglass airfoil attenuates the GNSS signal

**Figure 2: Recommended antenna position**

**☞** Place the antenna as far away as possible from radiating or jamming signals.

### <span id="page-5-1"></span>**2.4 Active and passive antennas**

Passive antennas contain only the radiating element, e.g. the ceramic patch or the helix structure. Sometimes they also contain a passive matching network to match the electrical connection to 50 Ohms impedance. Active antennas have an integrated Low-Noise Amplifier (LNA). This is beneficial

<sup>2</sup> Some cars have a metallic coating on the windscreens. GPS/GALILEO reception may not be possible in such a car without the use of SuperSense® Technology. There is usually a small section, typically behind the rear view mirror, reserved for mobile phone and GPS/GALILEO antennas.



in two respects. First, the losses of the cable after the LNA no longer affect the overall noise figure of the GNSS receiver system. Secondly, the LNA in the antenna helps to reduce the overall noise figure of the system resulting in a better sensitivity. Some receivers are designed so that they will only work with active antennas.

Active antennas need a power supply that will contribute to GNSS system power consumption, typically in the order of 3 to 20 mA. Usually, the supply voltage is fed to the antenna through the coaxial RF cable. Inside the antenna, the DC component on the inner conductor will be separated from the RF signal and routed to the supply pin of the LNA.

The use of an active antenna is always advisable if the RF cable length between the receiver and antenna exceeds about 10 cm. Care should be taken that the gain of the LNA inside the antenna does not lead to an overload condition at the receiver. For receivers that also work with passive antennas an antenna LNA gain of 15 dB is usually sufficient, even for cable lengths up to 5 m. There is no need for the antenna LNA gain to exceed 26 dB for use with u-blox receivers (at the RF input). With shorter cables and a gain above 35 dB, an overload condition might occur on some receivers.

When comparing the gain figures of active and passive antennas, keep in mind that the gain of an active antenna is composed of two components, the antenna gain of the passive radiator, given in dBic, and the LNA power gain, given in dB. A low antenna gain cannot be compensated by high LNA gain. It is not possible to judge the quality of the antenna if a manufacturer provides one total gain figure. Information is needed on the antenna gain (in dBic), the amplifier gain, and the amplifier noise figure.

| Active antenna                                                                                                                                                                                                                                                                                                                  | Passive antenna                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Needs more power (10 – 60 mW) than a passive antenna.<br>Is more tolerant to minor impedance miss-match or cable<br>length than a passive antenna (see section 5.3).<br>Helps to keep the receiver noise figure low.<br>Is less affected by jamming into the antenna cable than a<br>passive antenna (if equipped with filter). | Does not add anything to the power budget.<br>Antenna must be connected with a carefully designed micro<br>strip or strip line of maximum 10 cm to the GNSS receiver to<br>ensure good GNSS performance.<br>Jamming signals coupled into the micro-strip or strip line<br>negatively affect the performance.<br>RF design experience is required to properly design a passive<br>antenna. |

**Table 1: Active vs. passive antenna**



## <span id="page-7-0"></span>**3 Passive antenna types**

The GNSS signal is right-hand circular polarized (RHCP). This results in a style of antenna that is different from the well-known whip antennas used for linear polarized signals.

### <span id="page-7-1"></span>**3.1 Patch antenna**

The most common antenna type for GNSS applications is the patch antenna. Patch antennas are flat, generally have a ceramic and metal body and are mounted on a metal base plate. They are often cast in a housing.

Patch antennas are ideal for situations where the antenna is mounted on a flat surface, e.g. the roof or the dashboard of a car. Patch antennas can show a very high gain, especially if they are mounted on top of a large ground plane (70 x 70 mm). Ceramic patch antennas are very popular because of the low costs and the huge variation of available sizes (40 x 40 mm down to 10 x 10 mm; typical 25 x 25 mm).

#### **Antenna type**



25 x 25 mm patch **Application example**



u-blox reference design with 25 x 25 mm patch (C04-5H)

#### **Figure 3: Examples of patch antennas**

A smaller antenna will present a smaller aperture to collect the signal energy from the sky, resulting in a lower overall gain of the antenna. This is the result of pure physics and there is no "magic" to get around this problem. Amplifying the signal after the antenna will not improve the signal to noise ratio.

- **☞** Patch antennas of 25 mm by 25 mm show optimal performance and are cost-efficient. Patches smaller than 17 mm by 17 mm tend to demonstrate moderate navigation performance<sup>3</sup> . Performance is dependent on the ground plane size.
- **☞** For more information about u-blox reference designs see our website a[t www.u-blox.com.](http://www.u-blox.com/)

<sup>3</sup> Unless enhanced by u-blox SuperSense® technology.



### <span id="page-8-0"></span>**3.2 Helix antenna**



**Figure 4: Helix antenna**

Another style is the quadrifilar helix antenna. The actual geometric size depends on the dielectric that fills the space between the active parts of the antenna. If the antenna is only loaded with air it will be comparatively large (60 mm length and 45 mm diameter), high dielectric constant ceramics result in a much smaller form factor. The smaller the dimensions of the antenna, the more performance-critical tight manufacturing tolerances become.

As with patch antennas, filling the antenna with a high dielectric constant material can reduce the size of helix antennas. Sizes in the order of 18 mm length and 10 mm diameter are being offered to the market.

Again, antenna gain will decrease with decreasing size of the antenna.

**☞** Helical antennas are typically used in applications where multiple antenna orientations are possible. They are robust and demonstrate good navigation performance.





Helix: GeoHelix-P2 (Sarantel)

#### **Application example**



u-blox reference design with helix antenna (C05-5H)

**Figure 5: Examples of helix antenna**

**☞** For more information about u-blox reference designs see our website a[t www.u-blox.com.](http://www.u-blox.com/)

### <span id="page-8-1"></span>**3.3 Monopole antennas**

### <span id="page-8-2"></span>**3.3.1 Chip antenna**

Chip antennas are becoming increasingly important for GNSS designs. Their low cost and extremely small size (down to 3.2 x 1.6 x 1.1 mm), as well as high gain and omni-directional radiation patterns make them particularly attractive in consumer electronic applications such as mobile telephones and PNDs. Due to their miniature size, a variety of factors influence the performance of chip antennas. These factors include the footprint, ground plane size, isolation distance (typical 5 mm) and mounting of the chip antenna and GNSS device. The isolation distance or "keep-out area" can have an important impact on antenna efficiency, and thus on GNSS performance, and needs to be carefully considered



in designs. Isolation distances must be included to avoid deviations in antenna performance. Even with these measures acceptable performance cannot always be guaranteed due to potential detuning effects created by nearby objects.

Even if some antenna manufacturers claim that a ground plane is not required, the available ground plane has a significant impact on the GNSS performance of a chip antenna. Therefore, not only the size of the chip but also the ground plane must be considered in the design. For designs with a sufficiently large ground plane a chip antenna can provide satisfactory GNSS performance. However, in designs with an inadequate ground plane and device layout their performance is insufficient for GNSS.

Chip antennas have a 3 dB loss compared to helical or patch antennas due to linear polarization and their performance is highly dependent on the size of the ground plane.

#### **Antenna type**



Chip antenna

**Figure 6: Example of chip antenna**







Chip antenna PCB 80 x 40 mm Chip antenna PCB 80 x 40mm, C/No vs. elevation The average C/N0 is 43.4 dBHz.



Chip antenna PCB 24 x 15mm Chip antenna PCB 24x15mm, C/No vs. elevation The average C/N0 is 34.7 dBHz.

#### **Figure 7: Performance of chip antenna with 80 x 40 cm PCB**

#### <span id="page-9-0"></span>**Figure 8: Comparison of patch and chip antennas**

**15mm**

**24mm**



[Figure 8](#page-9-0) shows a performance comparison between a 25 x 25 mm patch antenna as reference and two chip antennas.



**Figure 9: Comparison of 25 x 25 mm patch antenna with chip antennas**

**☞** Chip antennas are not recommended for use in devices where navigation is an essential feature.

**☞** For more information about u-blox reference designs see our website a[t www.u-blox.com.](http://www.u-blox.com/)

A linear polarized whip or a PCB strip antenna is a simple and economical antenna solution if the user is willing to accept significantly weaker signals. Compared to a patch or helix these antennas have additional losses due to:

- Polarization mismatch of about -3 dB due to linear polarization
- Lower signals due to massively in-homogenous sensitivity pattern (directivity)
- Lower overall gain

The PCB strip is perhaps the cheapest way to implement a GNSS antenna, but it has some definite drawbacks which must be considered. Depending on the geometry chosen, the antenna has a high directivity. PCB antennas are typically bigger than chip antennas and usually have a larger bandwidth than chip or patch antennas. In addition, implementing PCB strip antennas requires RF expertise.

#### **Antenna type Performance**



Ground plane [mm] Typ. gain [dBic] 100 x 30 1.0

PCB antenna

**Figure 10: Example and performance of PCB antenna**

**☞** PCB antennas are not recommended for use in devices where navigation is an essential feature.



### <span id="page-11-0"></span>**3.3.2 Fractal Element Antenna (FEA)**

A fractal antenna is an antenna that uses a self-similar design to maximize the length, or increase the perimeter on the inside sections or the outer structure, made of material that can receive or transmit electromagnetic signals within a given total surface area.

Fractal antennas have a 3 dB loss compared to helical or patch antennas due to linear polarization and their performance is highly dependent on the size of the ground plane.



#### **Figure 11: Example and performance of FEA antenna**





**☞** FEA antennas are not recommended for use in devices where navigation is an essential feature.

### <span id="page-11-1"></span>**3.4 Dipole antenna**

Dipole antennas can be a very cost-effective solution, especially when printed on a PCB. They show acceptable performance in indoor environments. The field does not depend on a ground plane.

Dipole antennas are linear, not circular polarized. This results in a 3 dB loss in open space for GNSS but has some advantage for the backlobe, which is useful for indoor reception. Dipole antennas demonstrate similar drawbacks as PCB antennas and require RF expertise.



**Antenna type**





Dipole antenna Printed PCB dipole antenna

**Figure 13: Examples and performance of dipole antennas**



**Figure 14: High directivity (virtually no reception perpendicular to antenna orientation)**

**☞** Dipole antennas are not recommended for use in devices where navigation is an essential feature.

### <span id="page-12-0"></span>**3.5 Loop antenna**

The loop antenna shown in [Figure 15](#page-12-1) is printed on a sticker, which is attached to a windshield. Since its field is independent of a ground plane, its impedance and center frequency are not very sensitive to objects in the near field.

#### **Antenna type Performance**



Ground plane [mm] Typ. gain [dBic] None +4.5

Loop antenna

<span id="page-12-1"></span>**Figure 15: Example and performance of loop antenna**





### <span id="page-13-0"></span>**3.6 Planar Inverted F Antenna (PIFA)**

The PIFA antenna literally looks like the letter 'F' lying on its side with the two shorter sections providing feed and ground points and the 'tail' (or top patch) providing the radiating surface. PIFAs make good embedded antennas in that they exhibit a somewhat omni-directional pattern and can be made to radiate in more than one frequency band. They are linear polarized and their efficiency is only moderate.



PIFA antenna

**Figure 16: Example of PIFA antenna**

**☞** PIFAs are mainly used in cellular phones (E-911). Their use in devices where navigation is an essential feature is not recommended.

### <span id="page-13-1"></span>**3.7 High-end GNSS antennas**

For precision applications such as surveying or timing, some very high-end systems exist. Common to these designs is large size, high power consumption and high price. These designs are highly optimized to suppress multi-path signals reflected from the ground (choke ring antennas, multi-path limiting antennas, MLA). Another area of optimization is accurate determination of the phase center of the antenna. For precision GNSS applications with position resolution in the millimeter range, it is important that signals from satellites at all elevations virtually meet at exactly the same point inside the antenna. For this type of application receivers with multiple antenna inputs are often required.



## <span id="page-14-0"></span>**4 Which antenna is best for my application?**

Helix and patch antennas are the most widely used types in GNSS applications. This chapter examines some of the considerations to be made when selecting the antenna type.

**☞** Always test the actual performance of different antenna types in a real-life environment before beginning the mechanical design of the GNSS-enabled product.

### <span id="page-14-1"></span>**4.1 Helix or patch?**

For practical applications the possibilities of integrating a certain style of antenna into the actual device is of primary concern. Some designs naturally prefer the patch type of antenna, e.g. for rooftop applications. Others prefer the pole-like style of the helix antenna, which is quite similar to the style of mobile phone antennas. Furthermore, it is important that the antenna's main lobe points to the sky in order to receive as many satellites as possible with the maximum antenna gain. If the application is a hand-held device, the antenna should be designed in a way that natural user operation results in optimum antenna orientation. The helix antenna seems to be more appropriate in this respect.

However, keep in mind that comparable antenna gain requires comparable size of the antenna aperture, which will lead to a larger volume filled by a helix antenna in comparison to a patch antenna. Helix antennas with a "reasonable" size will therefore typically show a lower sensitivity compared to a "reasonably"-sized patch antenna.

A helix antenna might result in a "more satellites on the screen" situation in difficult signal environments when directly compared with a patch antenna. This is due to the fact that the helix will more easily pick up reflected signals through its omni-directional radiation pattern. However, the practical use of these signals is very limited because of the uncertain path of the reflected signals. Therefore, the receivers can see more satellites but the navigation solution will be degraded because of distorted range measurements in a multi-path environment.

| Helix antennas     | Patch antennas                                                         |
|--------------------|------------------------------------------------------------------------|
| omnidirectional    | high gain                                                              |
| robust             | low cost                                                               |
| cost               | large variety of sizes available on market                             |
| space requirements | less isolation between feed and antenna when compared to helix antenna |

**Table 2: Helix vs. Patch Antennas**

### <span id="page-14-2"></span>**4.2 Other antenna types**

In devices where navigation is not a core feature, chip, fractal, PCB, PIFA or dipole antennas can be an alternative to patch or helical antennas due to their small size and/or low cost. It is important to understand that these antennas do not provide the reception quality of patch or helical antennas. For this reason using patch or helical antennas is recommended in applications where navigation performance matters.



# <span id="page-15-0"></span>**5 Design considerations**

### <span id="page-15-1"></span>**5.1 Patch antennas**

Patch antennas are ideal for an application where the antenna sits on a flat surface, e.g. the roof of a car. Patch antennas can demonstrate a very high gain, especially if they are mounted on top of a large ground plane. Ceramic patch antennas are very popular because of their small size, typically measuring 25 x 25 mm<sup>2</sup> down to 10 x 10 mm<sup>2</sup> . Very cheap construction techniques can use ordinary circuit board material such as FR-4 or even air as a dielectric, but this will result in a much larger size, typically in the order of 10 x 10 cm<sup>2</sup> . [Figure 17](#page-15-3) shows a typical example of the radiation pattern of a 16 x 16 mm<sup>2</sup> ceramic patch antenna. This measurement only shows the upper sphere of the radiation pattern. Depending on the ground plane size there will also be a prominent back lobe present.



<span id="page-15-3"></span>**Figure 17: Typical radiation pattern of a patch antenna**

### <span id="page-15-2"></span>**5.1.1 Ground plane**



<span id="page-15-4"></span>**Figure 18: Typical gain and axial ratio of a patch antenna with respect to ground plane size**

For the specific example shown in [Figure 18](#page-15-4) it is easy to see that the so-called axial ratio, the relation of major to minor axis of the elliptical polarization has a minimum at the 50 x 50 mm<sup>2</sup> square ground plane. At this point, the polarization of the antenna is closest to an ideal circular polarization (axial ratio = 0 dB). At a 100 x 100 mm<sup>2</sup> square ground plane size this particular patch shows an axial ratio in the order of 10 dB, which is closer to linear polarization than to circular and will result in respective losses. This effect can also be seen in the left graph of the figure, where the gain no longer increases with the increasing ground plane size. In conclusion, the correct dimensions for the size of the ground plane can serve as a useful compromise between maximum gain and reasonable polarization loss.



A good allowance for ground plane size is typically in the area of 50 x 50 to 70 x 70 mm<sup>2</sup> . This number is largely independent of the size of the patch itself (when considering ceramic patches). Patch antennas with small ground planes will also have a certain back lobe in their radiation pattern, making them susceptible to radiation coming from the backside of the antenna, e.g. multi-path signals reflected off the ground. The larger the size of the ground plane, the less severe this effect becomes.

Smaller-sized patches will usually reach their maximum gain with a slightly smaller ground plane compared to a larger size patch. However, the maximum gain of a small-sized patch with optimum ground plane may still be much lower than the gain of a large-size patch on a less than optimal ground plane.

[Figure 19](#page-16-1) illustrates the impact of ground plane size, patch size and patch thickness on the antenna gain.



<span id="page-16-1"></span>**Figure 19: Antenna gain vs. ground plane**

**☞** It is not only the gain and axial ratio of the patch antenna that is affected by the size of the ground plane but also the matching of the antenna to the 50 Ohms impedance of the receiver.

### <span id="page-16-0"></span>**5.1.2 Placement**

The performance of a patch antenna heavily depends on the size, shape and symmetry of the ground plane. Improper placement of the patch will yield poor antenna performance and strong directivity (se[e Figure 20\)](#page-16-2).







<span id="page-16-2"></span>**Figure 20: Placement of patch antenna**

**Best Good Not recommended**



In addition the following placement issues need to be taken into account for patch antennas:

- No components should be placed close to the patch antenna
- Maintain a minimum distance between the antenna and the housing of the device
- No signal lines should pass under or near the antenna

#### <span id="page-17-0"></span>**5.1.3 ESD issues**

**⚠** GNSS receivers are sensitive to Electrostatic Discharge (ESD). Special precautions are required when handling.

Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, additional ESD measures as shown in [Figure 21](#page-17-2) can also avoid failures in the field.

> **Passive antennas (>2 dBic or performance sufficient)**









**Active antennas**

LNA with appropriate ESD rating

#### <span id="page-17-2"></span>**Figure 21: ESD precautions**

**☞** Protection measure A is preferred due to performance and protection-level considerations.



### <span id="page-17-1"></span>**5.2 Helix antennas**

Helix antennas can be designed for use with or without ground plane. If a helix antenna is designed without ground plane it can be tuned into such to show a more omni-directional radiation pattern as shown in [Figure 22.](#page-17-3)

Although we can determine an axial ratio close to 9 dB between zero degree and 90 degrees elevation, which compares to the patch antenna, the back lobe of the helix generally degrades much smoother and does not show any sensitivity at the –180 degree direction. In contrast, the back lobe of a patch antenna depends very much on the size and shape of the ground plane.

#### <span id="page-17-3"></span>**Figure 22: Radiation pattern of helix antenna without ground plane (Sarantel)**



### <span id="page-18-0"></span>**5.2.1 Ground plane**

Helix antennas typically do not require ground planes. However, a ground plane can significantly improve performance (e.g. 2-3 dB).

Due to antenna near field radiation patterns, currents can be induced in ground planes in close proximity to the antenna. This can negatively affect the radiation pattern of the antenna and overall performance, and additionally increases the antenna's susceptibility to hand loading and interference. For this reason ground planes should be kept a minimum distance from the radiating section of a helix antenna. See the recommendations of the manufacturer for more information (e.g. Sarantel).

### <span id="page-18-1"></span>**5.2.2 Placement**

Helix antennas can either be placed internally in the GNSS device or used as a free space antenna.

With free space antennas ground planes within 5 mm of the antenna radiating section can affect the performance of the antenna. In addition mechanical supports should be provided to hold the antenna in place. Certain system parts around the antenna, for example PCB or LCD screen, may lead to impairment of the antenna radiation pattern.

### <span id="page-18-2"></span>**5.3 Antenna matching**

All common GNSS antennas are designed for a 50 Ohms electrical load. Therefore, it is important to select a 50 Ohms-cable to connect the antenna to the receiver. However, there are several circumstances under which the matching impedance of the antenna might shift considerably. This means that the antenna no longer presents a 50-Ohms source impedance. Typically what happens is that the center frequency of the antenna is shifted away from GNSS frequency - usually towards lower frequencies – by some external influence. The reasons for this effect are primarily disturbances in the near field of the antenna. This can either be a ground plane that does not have the size for which the antenna was designed, or it can be an enclosure with a different dielectric constant than air.

In order to analyze effects like this you can employ electrical field simulations, which will result in exact representation of the electric fields in the near field of the antenna. Furthermore, these distortions of the near field will also show their effect in the far field, changing the radiation pattern of the antenna. Unfortunately, there is no simple formula to calculate the frequency shift of a given antenna in any specified environment. So you must do either extensive simulation or experimental work. Usually, antenna manufacturers offer a selection of pre-tuned antennas, so the user can test and select the version that best fits the given environment. However, testing equipment such as a scalar network analyzer is recommended to verify the matching.

Again, it must be pointed out that the smaller the size of the antenna, the more sensitive it will be to distortions in the near field. Also the antenna bandwidth will decrease with decreasing antenna size, making it harder to achieve optimum tuning.









**Figure 24: Dependency of center frequency on ground plane dimension for a 25 x 25 mm<sup>2</sup> patch**

An LNA placed very close to the antenna can help to relieve the matching requirements. If the interconnect length between the antenna and LNA is much shorter than the wavelength (9.5 cm on FR-4), the matching losses become less important. Under these conditions the matching of the input to the LNA becomes more important. Within a reasonable mismatch range, integrated LNAs can show a gain decrease in the order of a few dBs versus an increase of noise figure in the order of several tenths of a dB. If your application requires a very small antenna, an LNA can help to match the impedance of the antenna to a 50 Ohms cable. This effect is indeed beneficial if the antenna cable between the antenna and the receiver is only short. In this case, there is no need for the gain of the LNA to exceed 10 - 15 dB. In this environment the sole purpose of the LNA is to provide impedance matching and not signal amplification.

## <span id="page-19-0"></span>**5.4 GSM applications**

GSM uses power levels up to 2 W (+33 dBm). The absolute maximum power input at the GNSS receiver is typically -5 dBm.

### <span id="page-19-1"></span>**5.4.1 Isolation between GNSS and GSM antenna**

For GSM applications, plan a minimum isolation of 40dB. In a hand-held type design an isolation of approximately 20 dB can be reached with careful placement of the antennas, but this is not sufficient. In such applications an additional input filter is needed on the GNSS side to block the high energy from the GSM transmitter. Examples of these kinds of filters would be a SAW Filter from Epcos (B9444) or Murata.



**Figure 25: GNSS and GSM antenna isolation**

### <span id="page-19-2"></span>**5.5 Dual antenna systems**

Dual antenna systems are typically used to switch between internal antennas and external active antennas. [Figure 26](#page-20-0) an[d Figure 27](#page-21-0) give examples of dual antenna systems.



The following points need to be considered for the design:

- Most switches require DC-blockers at every input, and when selecting the switch or Schmitt trigger, particular attention needs to be given to the switching thresholds function of the antenna being used. Depending on the switch an additional buffer may be necessary.
- The LNA is placed before the SAW filter because LNAs can accept a maximum power of between 10 to 15 dBm.
- Placing the LNA after the SAW filter will reduce sensitivity by ~1 dBm but the maximum input power will be higher (typically 25 dBm).
- It is recommended to power the LNA through VCC\_RF.
- Selection of the ESD diode depends on the voltage supply (see the Integration manual for the specific u-blox receiver).
- The antenna detection circuitry is the same as that in the Integration manual for the specific ublox receiver.
- Open Circuit Detection must be activated on the module so that the antenna supply can be switched off when there is no antenna.



<span id="page-20-0"></span>**Figure 26: Example of dual antenna system using an electronic switch** 



As an alternative to the solution shown i[n Figure 26](#page-20-0) a mechanical switch can also be used (se[e Figure](#page-21-0)  [27\)](#page-21-0). For values of the components identified see the Integration Manual for the specific u-blox receiver.



<span id="page-21-0"></span>**Figure 27: Example of dual antenna system using a mechanical switch** 



## <span id="page-22-0"></span>**6 Interference issues**

A typical GNSS receiver has a very low dynamic range. This is because the antenna should only detect thermal noise in the GNSS frequency band, given that the peak power of the GNSS signal is 15 dB below the thermal noise floor. This thermal noise floor is usually very constant over time. Most receiver architectures use an automatic gain control (AGC) circuitry to automatically adjust to the input levels presented by different antenna and pre-amplifier combinations. The control range of these AGCs can be as large as 50 dB. However, the dynamic range for a jamming signal exceeding the thermal noise floor is typically only 6 to 12 dB, due to the one or two-bit quantization schemes commonly used in GNSS receivers. If there are jamming signals present at the antenna and the levels of these signals exceed the thermal noise power, the AGC will regulate the jamming signal, suppressing the GNSS signal buried in thermal noise even further. Depending on the filter characteristics of the antenna and the front end of the GNSS receiver, the sensitivity to such in-band jamming signals decreases more or less rapidly if the frequency of the jamming signal moves away from GNSS signal frequency. To conclude, a jamming signal exceeding thermal noise floor within a reasonable bandwidth (e.g. 100 MHz) around GNSS signal frequency will degrade the performance significantly.

Even out-of-band signals can affect the GNSS receiver performance. If these jamming signals are strong enough so that even antenna and front-end filter attenuation are not sufficient, the AGC will still regulate the jamming signal. Moreover, very high jamming signal levels can result in non-linear effects in the pre-amplifier stages of the receiver, resulting in desensitizing of the whole receiver. One such particularly difficult scenario is the transmitting antenna of a DCS<sup>4</sup> handset (max. 30 dBm at 1710 MHz) in close proximity to the GNSS antenna. When integrating GNSS with other RF transmitters, special care is necessary.

If the particular application requires integration of the antenna with other digital systems, make sure that the jamming signal levels are kept to an absolute minimum. Even harmonics of a CPU clock can reach as high as 1.5 GHz and still exceed thermal noise floor.

On the receiver side there is not much that can be done to improve the situation without significant effort. Of course, high price military receivers have integrated counter-measures against intentional jamming. But the methods employed are out of the scope of this document and might even conflict with export restrictions for dual-use goods.

The recommendations and concepts in this section are completely dependent on the specific applications. In situations where an active antenna is used in a remote position, e.g. >1 m away from other electronics, interference should not be an issue.

**☞** If antenna and electronics are to be tightly integrated, read the following sections very carefully.

### <span id="page-22-1"></span>**6.1 Sources of noise**

Basically two sources are responsible for most of the interference with GNSS receivers:

- 1. Strong RF transmitters close to GNSS frequency, e.g. DCS at 1710 MHz or radars at 1300 MHz.
- 2. Harmonics of the clock frequency emitted from digital circuitry.

The first problem can be very difficult to solve, but if GNSS and RF transmitter are to be integrated close to each other, there is a good chance that there is an engineer at hand who knows the specifications of the RF transmitter. In most cases, counter-measures such as filters will be required for the transmitter to limit disruptive emissions below the noise floor near the GNSS frequency.

Even if the transmitter is quiet in the GNSS band, a very strong emission close to it can cause saturation in the front-end of the receiver. Typically, the receiver's front-end stage will reach its

<sup>4</sup> Digital Communication System



compression point, which will in turn increase the overall noise figure of the receiver. In that case, only special filtering between the GNSS antenna and receiver input will help to reduce signal levels to the level of linear operation at the front-end.

The second problem is more common but also regularly proves to be hard to solve. Here, the emitting source is not well specified and the emission can be of broadband nature, making specific countermeasures very difficult. Moreover, the GNSS band is far beyond the 1-GHz limit that applies to almost all EMC regulations. So, even if a device is compliant with respect to EMC regulations it might severely disturb a GNSS receiver.

If the GNSS antenna is to be placed very close to some other electronics, e.g. the GNSS receiver itself or a PDA-like appliance, the EMC issue must be taken very seriously right from the concept phase of the design. It is one of the most demanding tasks in electrical engineering to design a system that is essentially free of measurable emissions in a given frequency band.

## <span id="page-23-0"></span>**6.2 Eliminating digital noise sources**

Digital noise is caused by the short rise-times of digital signals. Data and address buses with risetimes in the nanosecond range will emit harmonics up to several GHz. The following sections contain some general hints on how to decrease the level of noise emitted from a digital circuit board that is potentially in close proximity to the GNSS receiver or the antenna.

### <span id="page-23-1"></span>**6.2.1 Power and ground planes**

Use solid planes for power and ground interconnect. This will typically result in a PCB with at least four layers but will also result in a much lower radiation. Solid ground planes ensure that there is a defined return path for the signals routed on the signal layer. This will reduce the "antenna" area of the radiating loop. Planes should be solid in a sense that there are no slots or large holes inside the plane.

The outer extent of the power plane should be within the extent of the ground plane. This prevents the edges of the two planes from forming a slot antenna at the board edges. It is a good idea to have a ground frame on the circumference of every layer that is connected to the ground plane with as many vias as possible. If necessary, a shield can then be easily mounted on top of this frame (see [Figure 28\)](#page-23-2). Furthermore, free space on the outermost layers can be filled with ground shapes connected to the ground plane to shield radiation from internal layers.



<span id="page-23-2"></span>**Figure 28: Signal and power plane extends should lie within ground plane extends**



**Figure 29: Further improvement of reduction of power plane radiation**



### <span id="page-24-0"></span>**6.2.2 High-speed signal lines**

Keep high-speed lines as short as possible. This will reduce the area of the noise-emitting antenna, i.e. the conductor traces. Furthermore, the use of line drivers with controlled signal rise-time is suggested whenever driving large bus systems. Alternatively, high-speed signal lines can be terminated with resistors or even active terminations to reduce high-frequency radiation originating from overshoot and ringing on these lines.

If dielectric layers are thick compared to the line width, route ground traces between the signal lines to increase shielding. This is especially important if only two layer boards are used (see [Figure 30\)](#page-24-2).



<span id="page-24-2"></span>**Figure 30: Terminating radiation of signal lines**

### <span id="page-24-1"></span>**6.2.3 Decoupling capacitors**

Use a sufficient number of decoupling capacitors in parallel between power and ground nets. Small size, small-capacitance types reduce high-frequency emissions. Large size, high-capacitance types stabilize low frequency variations. It is preferred to have a large number of small value capacitors in parallel rather than having a small number of large value capacitors. Every capacitor has an internal inductance in series with the specified capacitance. In addition to resonance, the capacitor will also behave like an inductor. If many capacitors are connected in parallel, the total inductance will decrease while the total capacitance will increase. [Figure 31](#page-24-3) shows the impedance dependence of SMD capacitors.



#### <span id="page-24-3"></span>**Figure 31: Impedance of 0805 size SMD capacitors vs. frequency, MuRata**

If the power and ground plane are not connected by an efficient capacitor network, the power plane may act as a radiating patch antenna with respect to the ground. Furthermore, ceramic capacitors come with different dielectric materials. These materials show different temperature behavior. For industrial temperature range applications, at least a X5R quality should be selected. Y5V or Z5U types may lose almost all of their capacitance at extreme temperatures, resulting in potential system failure at low temperatures because of excessive noise emissions from the digital part. Tantalum capacitors show good thermal stability, however, their high ESR (equivalent series resistance) limits the usable frequency range to some 100 kHz.





**Figure 32: Temperature dependency of COG/NPO dielectric, AVX**



**Figure 33: Temperature dependency of X7R dielectric, AVX**



**Figure 34: Temperature dependency of Y5V dielectric, AVX**

### <span id="page-25-0"></span>**6.3 Shielding**

If employing counter-measures cannot solve the EMI problems, the solution may be shielding of the noise source. In the real world, shields are not perfect. The shielding effectiveness you can expect from a solid metal shield is somewhere in the order of 30 - 40 dB. If a thin PCB copper layer is used as a shield, these values can be even lower. Perforation of the shield will also lower its effectiveness.

Be aware of the negative effects that holes in the shield can have on shielding effectiveness. Lengthy slots might even turn a shield into a radiating slot antenna. Therefore, a proper shield has to be tightly closed and very well connected to the circuit board.



### <span id="page-26-0"></span>**6.3.1 Feed through capacitors**

The basic concept of shielding is that a metal box will terminate all electrical fields on its surface. In practice we have the problem that we need to route some signals from inside to outside of this box.



#### <span id="page-26-1"></span>**Figure 35: Ideal shielding**

The proposed setup for such a system is shown in [Figure 35.](#page-26-1) A feed through capacitor removes all high-frequency content from the outgoing signal line. It is important to note that any conductor projecting through the shielding box is subject to picking up noise inside and re-radiating it outside, regardless of the actual signal it is intended to carry. Therefore, also DC lines (e.g. the power supply) should be filtered with feed through capacitors. When selecting feed through capacitors, it is important to choose components with appropriate frequency behavior. As with the ordinary capacitors, small-value types will show better attenuation at high frequencies (se[e Figure 36\)](#page-26-2). For the GNSS frequency band the 470 pF capacitor is the optimum choice of the Murata NFM21C series.



#### <span id="page-26-2"></span>**Figure 36: MuRata's NFM21C feed through capacitors**



Any feed through capacitor will only achieve its specified performance if it has a proper ground connection.

If the use of a special feed through capacitor is not feasible for a particular design, a simple capacitor between the signal line and shielding ground placed very close to the feed through of the signal line will also help. A 12 pF SMD capacitor works quite well at the GNSS frequency range. Larger capacitance values will be less efficient.

Keep in mind that a feed through capacitor is basically a high frequency "short" between the signal line and ground. If the ground point that the capacitor is connected to is not ideal, meaning the ground connection or plane has a finite resistance, noise will be injected into the ground net. Therefore, try to place any feed trough capacitor far away from the most noise-sensitive parts of the circuit. To emphasize this once again, make sure there is a very good ground connection for the feed through capacitor.

If there is no good ground connection available at the point of the feed through, or injection of noise into the non-ideal ground net must be avoided totally, inserting a component with high resistance at high frequencies might be a good alternative. Ferrite beads are the components of choice if a high DC resistance cannot be accepted. Otherwise, for ordinary signal lines you can insert a 1 K series resistor, which forms a low-pass filter together with the parasitic capacitance of the conductor trace.

See also the MuRata web page for extensive discussion on EMC counter-measures.

### <span id="page-27-0"></span>**6.3.2 Shielding sets of sub-system assembly**

Yet another problem arises if multiple building blocks are combined in a single system. [Figure 37](#page-27-1) shows a possible scenario. In this case, the supply current traveling through the inductive ground connection between the two sub-systems will cause a voltage difference between the two shields of the sub-system. The shield of the other system will then act as a transmitting antenna, radiating with respect to the ground and shield of the GNSS receiver and the attached antenna.



<span id="page-27-1"></span>**Figure 37: Two shielded sub-systems, connected by a "poor" ground**

This situation can be avoided by ensuring a low-inductivity ground connection between the two shields. But then it might be difficult to control the path of the ground return currents to the power supply since the shield is probably connected to the supply ground at more than one location. The preferred solution is shown in [Figure 38.](#page-28-2) Again, it is important to have a good (i.e. low inductance) interconnection between the outer shield and the shielding ground of the GNSS receiver.





#### <span id="page-28-2"></span>**Figure 38: Proper shielding of a sub-system assembly**

It is clear that the situation illustrated i[n Figure 38](#page-28-2) can become complex if the component "some other electronics" contains another wireless transmitter system with a second antenna, which is referenced to the systems shielding ground. As already pointed out, in a setup like this it is important to keep the shield free from supply currents with high-frequency spectral content. If there are to be additional connections to the shielding ground, these should be of a highly inductive nature.

### <span id="page-28-0"></span>**6.4 Increasing jamming immunity**

Jamming signals come from in-band and out-band frequency sources.

### <span id="page-28-1"></span>**6.4.1 In-band jamming**

With in-band jamming the signal frequency is very close to the GPS frequency of 1575 MHz. Such jamming signals are typically caused by harmonics from displays, micro-controller, bus systems, etc.



**Figure 40: In-band jamming sources**



Measures against in-band jamming include:

- Maintaining a good grounding concept in the design
- Shielding
- Layout optimization
- Filtering
- Placement of the GNSS antenna
- Adding a CDMA, GSM, WCDMA bandbass filter before handset antenna

### <span id="page-29-0"></span>**6.4.2 Out-band jamming**

Out-band jamming is typically caused by signal frequencies that are different from the GNSS carrier. The sources are usually wireless communication systems such as GSM, CDMA, WCDMA, WiFi, BT, etc.



#### <span id="page-29-2"></span>**Figure 41: Out-band jamming signals**

Measures against out-band jamming include maintaining a good grounding concept in the design and adding a SAW or bandpass ceramic filter into the antenna input line to the GNSS receiver (see [Figure](#page-29-1)  [42\)](#page-29-1).



<span id="page-29-1"></span>**Figure 42: Measures against in-band jamming**



# <span id="page-30-0"></span>**7 Performance tests**

For a successful integration of a GNSS design, it is recommended to perform outdoor static measurements (with measurements performed in a defined location and with good sky visibility). u-center is the ideal tool for the design verification. The Sky View and the Statistic View functions are especially helpful. See the u-blox website to download u-center.

## <span id="page-30-1"></span>**7.1 Sky View**

The Sky View tool of the u-center software is an excellent means to analyze antenna performance as well as the environmental conditions for satellite observation. The polar plot graphically displays the average satellite signal strength, the position of satellites in the sky, identifies satellites by number and indicates which satellites are being used.

When recording over a long time period, Sky View is excellent for displaying the antenna visibility and to perform a comparison between two designs. Regarding the distribution of GNSS satellites, customers should conduct at least 12-hour measurements to have a 360-degree antenna visibility view with their design. Record a second 12-hour test with the design turned by 180 degree on the horizontal plane. Compare the recorded files for both designs for the north and the south hemisphere.

The following pictures show 24-hour outdoor measurements done with the design. The picture on the left side shows mediocre performance (recommendations were not followed), the one on the right side shows successful integration of the design.



**Figure 43: 24-hour Sky View test with poor antenna Figure 44: 24-hour Sky View test with a** 



**standalone reference**

**☞** These pictures show examples of possible measurements. Bear in mind that the plots might be influenced by the environment (e.g. buildings or hills close by) as well as GNSS conditions (e.g. no satellites above the North and South Pole).

### <span id="page-30-2"></span>**7.2 Statistic View**

The u-center Statistic View values displayed in the table below can be easily copied from the u-center software and pasted in an Excel sheet for comparison purposes.

| Title                           | Current          |      | Minimum Maximum Average |       | Deviation Unit |           |
|---------------------------------|------------------|------|-------------------------|-------|----------------|-----------|
| SVs Used                        | 6                | 5    | 11                      | 8     | 1              |           |
| Used SVs                        | 3,11,14,21,28,31 |      |                         |       |                |           |
| SVs Tracked                     | 7                | 7    | 12                      | 9     | 1              |           |
| Tracked SVs 3,11,14,20,21,28,31 |                  |      |                         |       |                |           |
| SV C/N0                         | 42.13            | 35.7 | 44.5                    | 41.56 |                | 1.06 dBHz |



Average, minimum and maximum signal strength ratios, so called C/No (carrier to noise ratio), provide good estimates of the signal reception quality.



### <span id="page-31-0"></span>**7.3 Supply voltage check**

Once a design prototype is ready the supply voltage ripple at the module should be checked. It must be below 50 mV p-p.

- Place the LDO for the GNSS close to the receiver.
- Use wide PCB traces or power planes.
- Ensure that there are no inductors, resistors, fuses or diodes between the LDO and the GNSS receiver.

### <span id="page-31-1"></span>**7.4 Sensitivity test**

Check the C/No values in the \$GPGSV or the UBX-NAV-SVINFO messages. Under open sky, a good design should reach up to 50 dBHz for the strongest signals. If it reaches 45 dBHz, it can still be acceptable but the source of the reduction should be investigated (e.g. a small antenna).

Designs with maximal signal strengths below 40 dBHz usually provide degraded performance (long TTFF times, lower coverage, accuracy, and dynamic).

### <span id="page-31-2"></span>**7.5 Startup test**

With good sky visibility the device should make a cold start within 30 - 40 seconds. (Take the average of 10-20 tests).



## <span id="page-32-0"></span>**Appendix**

# <span id="page-32-1"></span>**A Example of receiver signal to noise (C/No) performance calculation**

[Figure 45](#page-32-2) shows a typical GNSS receiver system setup. It is apparent that the noise figure of the first LNA (NF1) will dominate the receiver noise performance. If the first LNA is absent, the losses between the antenna and receiver input should be minimal. These losses are represented by gain (G1) and NF<sup>1</sup> (G<sup>1</sup> < 1!). If the cable losses are reasonably low, the first amplifier stage of the GNSS receiver (LNA2) dominates the noise performance of the system. Even the best receiver cannot compensate the cable losses, in best cases it will only add no further losses.



<span id="page-32-2"></span>**Figure 45: GNSS receiver setup with antenna**

[Table 4](#page-32-3) shows an example calculation for a typical GNSS receiver processing chain as depicted in [Figure 45.](#page-32-2) The final stage of the receiver is summarized on the row "Receiver". Gain and noise figure are arbitrarily chosen since this figure will not include the transition to the digital signal processing domain. To the user of a GNSS RF chip the internal analog noise figure of the receiver is usually not visible, because the user can only access the digitized output signals of this stage. If quantization architecture and gain control mechanisms are known, the user can however reverse-calculate the noise figure of the analog part. Finally, in digital signal processing there are noise contributions which do not fit into the concept of noise figure theory. To name just one, quantization errors will always contribute a fixed amount of noise, regardless of the signal pre-amplification.

| Stage    | Power Gain of<br>Stage | Cascaded<br>Power Gain | Noise Figure of<br>Stage | Cascaded<br>Noise Figure | Equiv.<br>Carrier Power | Noise Power<br>Density | C/No   |
|----------|------------------------|------------------------|--------------------------|--------------------------|-------------------------|------------------------|--------|
|          | [dB]                   | [dB]                   | [dB]                     | [dB]                     | [dBm]                   | [dBm/Hz]               | [dBHz] |
| Antenna  |                        |                        |                          | 0.00                     | -130                    | -173.98                | 43.98  |
| Cable    | -1                     | -1                     | 1                        | 1.00                     | -131                    | -173.98                | 42.98  |
| 1st LNA  | 10                     | 9                      | 2                        | 3.00                     | -121                    | -161.98                | 40.98  |
| Cable    | -3                     | 6                      | 3                        | 3.26                     | -124                    | -164.71                | 40.71  |
| 2nd LNA  | 10                     | 16                     | 2                        | 3.56                     | -114                    | -154.42                | 40.42  |
| Receiver | 60                     | 76                     | 10                       | 3.97                     | -54                     | -94.01                 | 40.01  |

<span id="page-32-3"></span>**Table 4: Example of receiver gain and noise calculation**

The highlighted fields in [Table 4](#page-32-3) are the input values, the other fields show the results calculated from these numbers. For a higher gain antenna, one could increase the carrier power in the first line by the antenna gain given in dBic. You could also make a different assumption for the antenna noise



temperature in the first line and change the initial noise power density accordingly. Of course, gain and noise figure of the analog signal processing stage differ for every receiver implementation. [Figure 46](#page-33-0) illustrates the direct relation between the receiver noise figure and the C/No measure that is available to the receiver. Again, it is easy to see the dominant influence of the first processing stages. If the first LNA would have a higher gain, e.g. 25 dB instead of only 10 dB, the contribution of the subsequent stages to the sensitivity degradation would be negligible.



<span id="page-33-0"></span>**Figure 46: C/No and noise figure in receiver processing chain**



## <span id="page-34-0"></span>**Related documents**

- [1] GNSS Compendium, doc. no. GPS-X-02007
- <span id="page-34-2"></span>[2] u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification (Public version), doc. no. [UBX-13003221](http://www.u-blox.com/docs/UBX-13003221)

**☞** For regular updates to u-blox documentation and to receive product change notifications, register on our homepage [\(www.u-blox.com\)](http://www.u-blox.com/).

## <span id="page-34-1"></span>**Revision history**

| Revision | Date        | Name       | Comments                                                                                                                                                                                                                                      |
|----------|-------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -        | 29-Jan-2009 | jfuh, tgri | Initial release                                                                                                                                                                                                                               |
| A1       | 02-Jul-2009 | jfuh, tgri | New CI, 2.2 Antenna, 2.3 Dipole antenna, 5.1.2 Placement, 5.1.3 ESD<br>protection measures, 5.5 Mechanical dual antenna system solution, 6.4<br>Increasing jamming immunity, Appendix.<br>Last revision with old document number GPS-X-08014. |
| R03      | 16-Oct-2019 | rmak       | Corrected ground plane size in Section 5.1.1. Updated Figure 41. Updated<br>Reference [2] and Contact section.                                                                                                                                |



## <span id="page-35-0"></span>**Contact**

For complete contact information, visit us at [www.u-blox.com.](http://www.u-blox.com/)

#### **u-blox Offices**

#### **North, Central and South America**

#### **u-blox America, Inc.**

Phone: +1 703 483 3180 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Regional Office West Coast:**

Phone: +1 408 573 3640 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Technical Support:**

Phone: +1 703 483 3185 E-mail: [support@u-blox.com](mailto:support@u-blox.com)

#### **Headquarters Europe, Middle East, Africa**

#### **u-blox AG**

Phone: +41 44 722 74 44 E-mail: [info@u-blox.com](mailto:info@u-blox.com) Support: [support@u-blox.com](mailto:support@u-blox.com)

#### **Asia, Australia, Pacific**

#### **u-blox Singapore Pte. Ltd.**

Phone: +65 6734 3811 E-mail: [info\\_ap@u-blox.com](mailto:info_ap@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office Australia:**

Phone: +61 2 8448 2016 E-mail: [info\\_anz@u-blox.com](mailto:info_anz@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office China (Beijing):**

Phone: +86 10 68 133 545 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Chongqing):**

Phone: +86 23 6815 1588 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shanghai):**

Phone: +86 21 6090 4832 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shenzhen):**

Phone: +86 755 8627 1083 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office India:**

Phone: +91 80 405 092 00 E-mail: [info\\_in@u-blox.com](mailto:info_in@u-blox.com) Support: [support\\_in@u-blox.com](mailto:support_in@u-blox.com)

#### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Korea:**

Phone: +82 2 542 0861 E-mail: [info\\_kr@u-blox.com](mailto:info_kr@u-blox.com) Support: [support\\_kr@u-blox.com](mailto:support_kr@u-blox.com)

#### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 E-mail: [info\\_tw@u-blox.com](mailto:info_tw@u-blox.com) Support: [support\\_tw@u-blox.com](mailto:support_tw@u-blox.com)