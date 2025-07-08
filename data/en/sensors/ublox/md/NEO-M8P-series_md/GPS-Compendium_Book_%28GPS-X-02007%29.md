# **GPS Essentials of Satellite Navigation**

**Compendium**

# locate, communicate, accelerate

#### **Abstract**

Theory and Principles of Satellite Navigation. Overview of GPS/GNSS Systems and Applications.







| Document Information |                                       |
|----------------------|---------------------------------------|
| Title                | GPS                                   |
| Subtitle             | Essentials of<br>Satellite Navigation |
| Document type        | Compendium                            |
| Document number      | GPS-X-02007-D                         |
| Document status      | Released                              |

This document and the use of any information contained therein, is subject to the acceptance of the u-blox terms and conditions. They can be downloaded from [www.u-blox.com.](http://www.u-blox.com/)

u-blox makes no warranties based on the accuracy or completeness of the contents of this document and reserves the right to make changes to specifications and product descriptions at any time without notice.

u-blox reserves all rights to this document and the information contained herein. Reproduction, use or disclosure to third parties without express permission is strictly prohibited. Copyright © 2009, u-blox AG.



## <span id="page-2-0"></span>**Foreword**

#### **Where on Earth am I?**

The answer to this seemingly simple question can sometimes be a matter of life and death. Consider an aviator trying to find a safe destination to land, or the crew of a ship in distress seeking assistance, or a hiker in the mountains disoriented by poor weather conditions. Your position on Earth is of vital importance and can have an immense variety of implications and applications.

These needn't be as dramatic as the circumstances above, but there can be situations that also have a significant impact on our daily lives. How do I find that address that I've been searching for, how can businesses keep track of their mobile assets, how do governments implement road-pricing systems, or when and where should the public transit vehicle trigger the next traffic light? The potential applications and uses of position information are seemingly limitless. Our position on this blue planet has always been vitally important to human beings and today our exact position is something that we can obtain with astonishing ease.



Among the most stunning technological developments in recent years have been the immense advances in the realm of satellite navigation or Global Navigation Satellite Systems (GNSS) technologies. In a matter of a few years, satellite navigation has evolved from the level of science fiction to science fact with a dynamic and rapidly growing industry providing customers around the world with technology devoted to the rapid, reliable and readily available determination of their position.

As global leaders in this fascinating and rapidly changing industry, u-blox AG is a team of dedicated satellite navigation enthusiasts with a tradition of innovation and quality. As part of our commitment to customer service, u-blox is pleased to be able to provide you with this compendium to help lead you into the remarkable world of satellite navigation.

The aim of this book is to provide a comprehensive overview of the way in which satellite navigation systems function and the applications in which they can be used. The current level of development as well as changes and new advances will be examined. It is written for users who are interested in the technology as well as specialists involved in satellite navigation applications. The document is structured in such a way that the reader can graduate from simple facts to more complex concepts. The basic theory of satellite navigation will be introduced and supplemented by other important facets. This compendium is intended to additionally serve as an aid in understanding the technology that goes specifically into current satellite navigation receivers, modules and ICs. Important new developments will be dealt with in separate sections. Acquiring an understanding of the various current coordinate systems involved in using GNSS equipment can be a difficult task. Therefore, a separate chapter is devoted to introducing cartography.

We hope that this document will be of assistance to you and that you will be as enthusiastic as we are about the technology involved in determining position. It is indeed an immensely fascinating world and industry that answers the question "where on Earth am I?"



## <span id="page-3-1"></span>**Author's preface**

In 1990, I was traveling by train from Chur to Brig in the Swiss canton of Valais. In order to pass the time during the journey, I had brought along a few trade journals with me. While thumbing through an American publication, I came across a technical article that described a new positioning and navigation system involving satellites. The new system, known as Global Positioning System or GPS, employed a number of US satellites to determine one's position anywhere in the world to within an accuracy of about 100m[1](#page-3-0) .

As an avid sportsman and mountain hiker, I had on many occasions ended up in precarious situations due to a lack of knowledge of the area I was in. Therefore, I was fascinated by the revolutionary prospect of being able to determine my position even in fog or at night by using a GPS receiver.

I began to intensively occupy myself with GPS, arousing a great deal of enthusiasm for this technology among students at my university, which resulted in several research semesters and graduate theses on the subject. With time I felt that I had become a true expert on the subject and wrote technical articles about GPS for various publications.

## **Why read this book?**

The development of the many new and fascinating potential applications of satellite navigation requires an appreciation of the way in which these systems function. If you are familiar with the technical background of the system, it becomes possible to develop and use new positioning and navigation equipment. As well as the possibilities, this book also looks at some of the limitations of the system in order to protect you from unrealistic expectations.

## **How did this book come about?**

In 2000 I decided to reduce the amount of time I spent lecturing at my university in order to gain an overview of the commercial satellite navigation industry. My desire was to work for a company directly involved with satellite navigation and just such a company was u-blox AG, who received me with open arms. u-blox asked me to produce a brochure that they could give to their customers, and this compendium is the result and is a summation of earlier articles and newly compiled chapters.

## **A heartfelt wish**

I wish you every success as you embark on your journey through the wide-ranging world of satellite navigation and trust that you will successfully navigate your way through this fascinating technical field. Enjoy your read!

For questions or if you find errors in this book please contact us at [GPScompendium@u-blox.com](mailto:GPScompendium@u-blox.com).

Jean-Marie Zogg October 2001 July 2006 February 2009

<span id="page-3-0"></span><sup>1</sup> That was in 1990, positional data is now accurate to within 5 to 10m!



<span id="page-4-0"></span>

| Foreword | 3                                                              |  |
|----------|----------------------------------------------------------------|--|
|          | Author's preface4                                              |  |
|          | Contents5                                                      |  |
|          | Introduction10                                                 |  |
| 1        | Satellite navigation made simple12                             |  |
| 1.1      | The principle of measuring signal transit time 12              |  |
| 1.1.1    | Basic principles of satellite navigation  13                   |  |
| 1.1.2    | Signal travel time 15                                          |  |
| 1.1.3    | Determining position 16                                        |  |
| 1.1.4    | The effect and correction of time error 17                     |  |
| 2        | Coordinate systems18                                           |  |
| 2.1      | Introduction 18                                                |  |
| 2.2      | Geoid  18                                                      |  |
| 2.3      | Ellipsoid and datum  19                                        |  |
| 2.3.1    | Ellipsoid 19                                                   |  |
| 2.3.2    | Customized local reference ellipsoids and datum 20             |  |
| 2.3.3    | National reference systems 21                                  |  |
| 2.3.4    | Worldwide reference ellipsoid WGS-84  21                       |  |
| 2.3.5    | Transformation from local to worldwide reference ellipsoid 22  |  |
| 2.3.6    | Converting coordinate systems 24                               |  |
| 2.4      | Planar regional coordinates, projection  24                    |  |
| 2.4.1    | Gauss-Krüger projection (Transversal Mercator Projection)  25  |  |
| 2.4.2    | UTM projection  25                                             |  |
| 2.4.3    | Swiss projection system (Conformal Double Projection)  27      |  |
| 2.4.4    | Worldwide conversion of coordinates 28                         |  |
| 2.5      | Georeferencing of raster maps  29                              |  |
| 2.5.1    | Introduction  29                                               |  |
| 2.5.2    | Basics of transformation 29                                    |  |
| 2.5.3    | Determining the transformation coordinate 29                   |  |
| 2.5.4    | Determining the transformation parameters a, b, c, d, e, f  30 |  |
| 2.5.5    | Example (raster map to WGS84) 32                               |  |



| 3 |       | Foundations of satellite technology<br>34                                  |  |
|---|-------|----------------------------------------------------------------------------|--|
|   | 3.1   | Kepler's laws  34                                                          |  |
|   | 3.1.1 | Kepler's first law 34                                                      |  |
|   | 3.1.2 | Kepler's second law 34                                                     |  |
|   | 3.1.3 | Kepler's third law  35                                                     |  |
|   | 3.2   | Satellite orbits 36                                                        |  |
|   | 3.3   | Orbital altitude  38                                                       |  |
|   | 3.4   | Radio frequencies  39                                                      |  |
|   | 3.5   | Time systems  40                                                           |  |
|   | 3.5.1 | International Atomic Time (TAI)  40                                        |  |
|   | 3.5.2 | Coordinated Universal Time (UTC) 40                                        |  |
|   | 3.5.3 | GPS Time 40                                                                |  |
|   | 3.5.4 | Satellite Time 40                                                          |  |
|   | 3.5.5 | Local Time 41                                                              |  |
| 4 |       | GNSS technology: the GPS example<br>42                                     |  |
|   | 4.1   | Introduction 42                                                            |  |
|   | 4.2   | Description of the entire system 42                                        |  |
|   | 4.3   | Space segment  43                                                          |  |
|   | 4.3.1 | Satellite distribution and movement  43                                    |  |
|   | 4.3.2 | The GPS satellites  46                                                     |  |
|   | 4.3.3 | Generating the satellite signal  48                                        |  |
|   | 4.4   | Control segment  51                                                        |  |
|   | 4.4.1 | Deactivation possibilities and artificial distortion of the signal (SA) 51 |  |
|   | 4.5   | User segment  52                                                           |  |
|   | 4.6   | The GPS message  56                                                        |  |
|   | 4.6.1 | Introduction  56                                                           |  |
|   | 4.6.2 | Structure of the navigation message  56                                    |  |
|   | 4.6.3 | Information contained in the subframes 57                                  |  |
|   | 4.6.4 | TLM and HOW  57                                                            |  |
|   | 4.6.5 | Subdivision of the 25 pages 58                                             |  |
|   | 4.6.6 | Comparison between ephemeris and almanac data 58                           |  |
|   | 4.7   | GPS modernization 60                                                       |  |
|   | 4.7.1 | New modulation procedure, BOC and MBOC 60                                  |  |
|   | 4.7.2 | GPS modernization 64                                                       |  |
| 5 |       | GLONASS, GALILEO and Beidou/Compass66                                      |  |
|   | 5.1   | Introduction 66                                                            |  |
|   |       |                                                                            |  |



| 5.2   | GLONASS: the Russian system  67                                              |  |
|-------|------------------------------------------------------------------------------|--|
| 5.2.1 | Completion of GLONASS 68                                                     |  |
| 5.3   | GALILEO 71                                                                   |  |
| 5.3.1 | Overview 71                                                                  |  |
| 5.3.2 | Projected GALILEO services 72                                                |  |
| 5.3.3 | Accuracy  74                                                                 |  |
| 5.3.4 | GALILEO technology 75                                                        |  |
| 5.3.5 | Most important properties of the three GNSS systems 79                       |  |
| 5.4   | The Chinese system Beidou 1 and Beidou 2/Compass 80                          |  |
| 5.4.1 | Current system: Beidou 1  80                                                 |  |
| 5.4.2 | Future system: Beidou 2/Compass  80                                          |  |
| 6     | Calculating position<br>81                                                   |  |
| 6.1   | Introduction 81                                                              |  |
| 6.2   | Calculating a position  81                                                   |  |
| 6.2.1 | The principle of measuring signal travel time (evaluation of pseudorange) 81 |  |
| 6.2.2 | Linearization of the equation 83                                             |  |
| 6.2.3 | Solving the equation  85                                                     |  |
| 6.2.4 | Summary 85                                                                   |  |
| 6.3   | Determination of travel time in detail 86                                    |  |
| 6.3.1 | Time systems 86                                                              |  |
| 6.3.2 | Determination of travel time in detail  86                                   |  |
| 6.3.3 | Determination of travel time error  89                                       |  |
| 6.3.4 | Additional influences affecting travel time 89                               |  |
| 6.4   | Error analysis and DOP 90                                                    |  |
| 6.4.1 | Introduction  90                                                             |  |
| 6.4.2 | The influence of satellite geometry on accuracy, the DOP value 91            |  |
| 7     | Improved GPS: DGPS, SBAS, A-GPS and HSGPS<br>100                             |  |
| 7.1   | Introduction 100                                                             |  |
| 7.2   | Sources of GPS error 100                                                     |  |
| 7.3   | Possibilities for reducing the measurement error 101                         |  |
| 7.3.1 | DGPS based on signal travel time delay measurement  103                      |  |
| 7.3.2 | DGPS based on carrier phase measurement 106                                  |  |
| 7.3.3 | DGPS post-processing (signal travel time and phase measurement)  106         |  |
| 7.3.4 | Transmitting the correction data 107                                         |  |
| 7.3.5 | DGPS classification according to the broadcast range 108                     |  |
| 7.3.6 | Standards for the transmission of correction signals  108                    |  |



| 7.3.7      | Overview of the different correction services  109           |  |
|------------|--------------------------------------------------------------|--|
| 7.4        | DGPS services for real-time correction 110                   |  |
| 7.4.1      | Introduction  110                                            |  |
| 7.4.2      | Terrestrial services based on RTCM SC-104  110               |  |
| 7.4.3      | Satellite services based on RTCM SC-104  111                 |  |
| 7.5        | Wide Area DGPS (WADGPS) 112                                  |  |
| 7.5.1      | Satellite based augmentation systems, SBAS (WAAS, EGNOS) 112 |  |
| 7.5.2      | Overview of existing and planned systems 113                 |  |
| 7.5.3      | Overview of planned RNSS  115                                |  |
| 7.5.4      | SBAS system description 116                                  |  |
| 7.5.5      | Satellite DGPS services using RTCM SC-104 117                |  |
| 7.6        | Achievable accuracy with DGPS and SBAS  118                  |  |
| 7.7        | Assisted-GPS (A-GPS, AGPS) 118                               |  |
| 7.7.1      | Introduction  118                                            |  |
| 7.7.2      | Principle of A-GPS  119                                      |  |
| 7.7.3      | Reference network  121                                       |  |
| 7.7.4      | A-GPS network  121                                           |  |
| 7.7.5      | A-GPS with online aiding data (real-time A-GPS)  122         |  |
| 7.7.6      | A-GPS with offline aiding data (predicted orbits)  123       |  |
| 7.7.7      | Architectures 124                                            |  |
| 7.7.8      | Control plane architecture 124                               |  |
| 7.7.9      | User plane architecture 125                                  |  |
| 7.7.10     | Architecture advantages 125                                  |  |
| 7.7.11     | OMA-Secure User Plane Location Architecture (OMA-SUPL)  126  |  |
| 7.8        | High Sensitivity GPS (HSGPS)  127                            |  |
| 7.8.1      | Improved oscillator stability  127                           |  |
| 7.8.2      | Antennas 127                                                 |  |
| 7.8.3      | Noise figure considerations 128                              |  |
|            |                                                              |  |
| 7.8.4      | Correlators and correlation time 128                         |  |
| 7.9        | GNSS-repeater or re-radiation antenna 129                    |  |
| 7.10       | Pseudolites for indoor applications 129                      |  |
| 8          | Data formats and hardware interfaces130                      |  |
|            |                                                              |  |
| 8.1<br>8.2 | Introduction 130<br>Data interfaces  131                     |  |
| 8.2.1      | The NMEA-0183 data interface  131                            |  |
| 8.2.2      | Conversion from NMEA to KML  142                             |  |



| 8.2.4    | Proprietary data interfaces 150               |  |
|----------|-----------------------------------------------|--|
| 8.3      | Hardware interfaces  153                      |  |
| 8.3.1    | Antennas 153                                  |  |
| 8.3.2    | Supply 154                                    |  |
| 8.3.3    | Time pulse: 1PPS and time systems 155         |  |
| 8.3.4    | Converting the TTL level to RS-232 155        |  |
| 9        | GNSS RECEIVERS158                             |  |
| 9.1      | Basics of GNSS handheld receivers 158         |  |
| 9.2      | GNSS receiver modules 159                     |  |
| 9.2.1    | Basic design of a GNSS module  159            |  |
| 10       | GNSS applications<br>161                      |  |
| 10.1     | Introduction 161                              |  |
| 10.2     | Description of the various applications  162  |  |
|          | 10.2.1<br>Location Based Services (LBS) 162   |  |
|          | 10.2.2<br>Commerce and industry  162          |  |
|          | 10.2.3<br>Communications technology 163       |  |
|          | 10.2.4<br>Agriculture and forestry 164        |  |
|          | 10.2.5<br>Science and research 164            |  |
|          | 10.2.6<br>Tourism and sport  166              |  |
|          | 10.2.7<br>Military 166                        |  |
|          | 10.2.8<br>Time measurement 166                |  |
| Appendix | 167                                           |  |
| A        | Resources in the World Wide Web167            |  |
| A.1      | Summary reports and links  167                |  |
| A.2      | Differential GPS  167                         |  |
| A.3      | GPS institutes  167                           |  |
| A.4      | GNSS newsgroup and GNSS technical journal 168 |  |
| B        | Index<br>169                                  |  |
| B.1      | List of figures 169                           |  |
| B.2      | List of tables  172                           |  |
| B.3      | Sources 173                                   |  |
| C        | Revision history174                           |  |



## <span id="page-9-0"></span>**Introduction**

Satellite Navigation is a method employing a Global Navigation Satellite System (GNSS) to accurately determine position and time anywhere on Earth. Satellite Navigation receivers are currently used by both private individuals and businesses for positioning, locating, navigating, surveying, and determining the exact time in an evergrowing list of personal, leisure and commercial applications.

Using a GNSS system, the following values can accurately be determined anywhere on the globe [\(Figure](#page-9-1) 1):

- 1. Exact position (longitude, latitude and altitude coordinates) accurate to within 20m to approx. 1mm.
- 2. Exact time (Universal Time Coordinated, UTC) accurate to within 60ns to approx. 5ns.

Speed and direction of travel (course) can be derived from these values, which are obtained from satellites orbiting the Earth. Speed of travel may also be determined directly by means of Doppler shift measurements.



#### <span id="page-9-1"></span>**Figure 1: The basic function of satellite navigation**

As of 2009, the **G**lobal **P**ositioning **S**ystem (GPS) developed and operated by the United States Department of Defense (DoD) was the only fully operational GNSS system. The rapidly developing Satellite Navigation industry has sprung up around the GPS system, and for this reason the terms GPS and Satellite Navigation are sometimes used interchangeably. This document will place an emphasis on GPS, although other emerging GNSS systems will be introduced and discussed.

GPS (the full name of the system is: **NAV**igation **S**ystem with **T**iming **A**nd **R**anging **G**lobal **P**ositioning **S**ystem, NAVSTAR-GPS) is intended for both civilian and military use. The civilian signal SPS (Standard Positioning Service) can be used freely by the general public, while the military signal PPS (Precise Positioning Service) is available only to authorized government agencies. The first satellite was placed in orbit on February 22, 1978, and it is planned to have up to 32 operational satellites orbiting the Earth at an altitude of 20,180 km on 6 different orbital planes. The orbits are inclined at 55° to the equator, ensuring that at least 4 satellites are in radio communication with any point on the planet. Each satellite orbits the Earth in approximately 12 hours and has four atomic clocks onboard.

During the development of the GPS system, particular emphasis was placed on the following three aspects:

- 1. It had to provide users with the capability of determining position, speed and time, whether in motion or at rest.
- 2. It had to have a continuous, global, all-weather 3-dimensional positioning capability with a high degree of accuracy.
- 3. It had to offer potential for civilian use.

Within the next five or six years there will likely be 3 fully independent GNSS systems available. The United States will continue to provide GPS and Russia and the European Union should respectively bring their GLONASS and GALILEO systems into full operation. All of these systems will undergo modernization and improvements, which should improve their reliability and make new potential services and applications available[2](#page-10-0) .

This compendium will examine the essential principles of Satellite Navigation and move beyond these into specific applications and technologies. GPS will receive particular focus because of its importance as forerunner and industry standard, and important developments such as Differential-GPS (DGPS), Assisted-GPS (AGPS) and Device Interfaces will be treated in separate sections. This is all with the goal of providing the reader with a solid foundation and understanding of this fascinating and increasingly important field.

<span id="page-10-0"></span><sup>2</sup> Among these will be important advances for aviation, wherein approaches and landings using satellite navigation should become possible.



## <span id="page-11-0"></span>**1 Satellite navigation made simple**

#### *Do you want to . . .*

- o understand, how the distance of lightning can be simply determined?
- o understand, how Satellite Navigation essentially functions?
- o know, how many atomic clocks are onboard a GPS satellite?
- o know, how to determine a position on a plane?
- o understand, why Satellite Navigation requires four satellites to determine a position?

*Then you should read this chapter!* 

## <span id="page-11-1"></span>**1.1 The principle of measuring signal transit time**

At some time or other during a thunderstorm you have almost certainly attempted to work out how far away you are from a bolt of lightning. The distance can be established quite easily ([Figure](#page-11-2) 2): distance = the time the lightning flash is perceived (start time) until the thunder is heard (stop time) multiplied by the speed of sound (approx. 330 m/s). The difference between the start and stop time is referred to as the signal travel time. In this case the signal is sound waves traveling through the air.



#### <span id="page-11-2"></span>**Figure 2: Determining the distance of a lightning flash**

#### distance sound of speed timetravel

Satellite Navigation functions by the same principle. One calculates position by establishing the distance relative to reference satellites with a known position. In this case the distance is calculated from the travel time of radio waves transmitted from the satellites.



#### <span id="page-12-0"></span>**1.1.1 Basic principles of satellite navigation**

Satellite Navigation Systems all use the same basic principles to determine coordinates:

- Satellites with a known position transmit a regular time signal.
- Based on the measured travel time of the radio waves (electromagnetic signals travel through space at the speed of light c = 300'000km/s) the position of the receiver is calculated.

We can see the principle more clearly using a simple model. Imagine that we are in a car and need to determine our position on a long and straight street. At the end of the street is a radio transmitter sending a time signal pulse every second. Onboard the car we are carrying a clock, which is synchronized to the clock at the transmitter. By measuring the elapsed travel time from the transmitter to the car we can calculate our position on the street ([Figure](#page-12-1) 3).



#### <span id="page-12-1"></span>**Figure 3: In the simplest case distance is determined by measuring the travel time**

The distance D is calculated by multiplying the travel time by the velocity of light c.

#### D = • c

Because the time of the clock onboard our car may not be exactly synchronized with the clock at the transmitter, there can be a discrepancy between the calculated and actual distance traveled. In navigation this observed distance referenced to the local clock is referred to as pseudorange. In our example a travel time of one microsecond (1μs) generates a pseudorange of 300m.

We could solve the problem of local clock synchronization by outfitting our car with an exact atomic clock, but this would probably exceed our budget. Another solution involves using a second synchronized time signal transmitter, for which the separation (A) to the first transmitter is known. By measuring both travel times it is possible to exactly establish the distance (D) despite having an imprecise onboard clock.





#### <span id="page-13-1"></span>**Figure 4: With two transmitters it is possible to calculate the exact position despite time errors.**

$$
D = \frac{(\Delta \tau_1 - \Delta \tau_2) \bullet c + A}{2}
$$

As we have seen, in order to exactly calculate the position and time along a line (by definition a line expands in one dimension) we require two time signal transmitters. From this we can draw the following conclusion: When an unsynchronized onboard clock is employed in calculating position, it is necessary that the number of time signal transmitters exceed the number of unknown dimensions by a value of one.

For example:

- On a plane (expansion in two dimensions) we need three time-signal transmitters.
- In three-dimensional space we need four time-signal transmitters.

Satellite Navigation Systems use satellites as time-signal transmitters. Contact to at least four satellites [\(Figure](#page-13-0) 5) is necessary in order to determine the three desired coordinates (Longitude, Latitude, Altitude) as well as the exact time. We explain this in more detail in the following sections.



<span id="page-13-0"></span>



#### <span id="page-14-0"></span>**1.1.2 Signal travel time**

Satellite Navigation Systems employ satellites orbiting high above the Earth and distributed in such a way that from any point on the ground there is line-of-sight contact to at least 4 satellites.

Each one of these satellites is equipped with onboard atomic clocks. Atomic clocks are the most precise time measurement instruments known, losing a maximum of one second every 30,000 to 1,000,000 years. In order to make them even more accurate, they are regularly adjusted or synchronized from various control points on Earth. GNSS satellites transmit their exact position and onboard clock time to Earth. These signals are transmitted at the speed of light (300,000km/s) and therefore require approx. 67.3ms to reach a position on the Earth's surface directly below the satellite. The signals require a further 3.33s for each additional kilometer of travel. To establish position, all that is required is a receiver and an accurate clock. By comparing the arrival time of the satellite signal with the onboard clock time the moment the signal was transmitted, it is possible to determine the signal travel time [\(Figure](#page-14-1) 6).



#### <span id="page-14-1"></span>**Figure 6: Determining the signal travel time**

As with the example of the car, the distance D to the satellite can be determined from the known signal travel time :

c•D distance travel time • speed of :light 



#### <span id="page-15-0"></span>**1.1.3 Determining position**

Imagine that you are wandering across a vast plateau and would like to know where you are. Two satellites are orbiting far above you transmitting their onboard clock times and positions. By using the signal travel time to both satellites you can draw two circles with the radii D1 and D2 around the satellites. Each radius corresponds to the calculated distance to the satellite. All possible positions relative to the satellites are located on these circles. If the position above the satellites is excluded, the location of the receiver is at the exact point where the two circles intersect beneath the satellites [\(Figure](#page-15-1) 7), therefore, two satellites are sufficient to determine a position on the X/Y plane.



<span id="page-15-1"></span>**Figure 7: The position of the receiver at the intersection of the two circles** 

In the real world, a position has to be determined in three-dimensional space rather than on a plane. As the difference between a plane and three-dimensional space consists of an extra dimension (height Z), an additional third satellite must be available to determine the true position. If the distance to the three satellites is known, all possible positions are located on the surface of three spheres whose radii correspond to the distance calculated. The position is the point where all three of the spheres intersect [\(Figure](#page-15-2) 8).



<span id="page-15-2"></span>**Figure 8: The position is determined at the point where all three spheres intersect** 



#### <span id="page-16-0"></span>**1.1.4 The effect and correction of time error**

The conclusions in the previous section are only valid if the clock at the receiver and the atomic clocks onboard the satellites are synchronized, i.e., the signal travel time can be precisely determined. If the measured travel time between the satellites and an earthbound navigational receiver is incorrect by just 1μs, a position error of 300m is produced. As the clocks onboard all the GNSS satellites are synchronized, the signal travel time in the case of all three measurements is inaccurate by the same amount. Mathematics can help us in this situation.

When performing mathematical calculations, we remember that if N variables are unknown, we need N independent equations to identify them. If the time measurement is accompanied by a constant unknown error (t), in 3-dimensional space we will have four unknown variables:

- longitude (X)
- latitude (Y)
- height (Z)
- time error (t)

These four variables require four equations, which can be derived from four separate satellites.

Satellite Navigation systems are deliberately constructed in such a way that from any point on Earth, at least 4 satellites are "visible" [\(Figure](#page-16-1) 9). Thus, despite an inaccuracy on the part of the receiver clock and resulting time errors, a position can be calculated to within an accuracy of approx. 5 – 10m.



<span id="page-16-1"></span>**Figure 9: Four satellites are required to determine a position in 3-D space.** 



## <span id="page-17-0"></span>**2 Coordinate systems**

*If you would like to . . .* 

- o know what a geoid is
- o understand why the Earth is depicted primarily as an ellipsoid
- o understand why over 200 different map reference systems are used worldwide
- o know what WGS-84 means
- o understand how it is possible to convert one datum into another
- o know what Cartesian and ellipsoidal coordinates are
- o understand how maps of countries are made
- o know how country coordinates are calculated from the WGS-84 coordinates

*then this chapter is for you!* 

## <span id="page-17-1"></span>**2.1 Introduction**

A significant problem to overcome when using a GNSS system is the fact that there are a great number of differing coordinate systems worldwide. As a result, the position measured and calculated does not always correspond with one's supposed position.

In order to understand how GNSS systems function, it is necessary to examine some of the basics of geodesy: the science that deals with the surveying and mapping of the Earth's surface. Without this basic knowledge, it is difficult to understand the apparently bewildering necessity of combining the appropriate map reference systems (datums) and grids. Of these there are more than 100 different datums and approx. 10 different grids to select from. If an incorrect combination is made, a position can be out by several hundred meters.

## <span id="page-17-2"></span>**2.2 Geoid**

We have known that the Earth is round since Columbus. But how round is it really? Describing the shape of our blue planet has always been a challenging scientific task. Over the centuries several different models have been presented to represent an approximation of the true shape of the earth as faithfully as possible.

The geoid represents the true shape of the earth; defined as the surface, where the mean sea level is zero. This shape is defined by the gravity of the earth, thus its geometrical description is rather complex. Using the Greek word for Earth, this geometrical shape of this surface is called geoid [\(Figure](#page-18-2) 10).

Because the distribution of the mass of the Earth is uneven and, as a result, the level surface of the oceans and seas do not lie on the surface of a geometrically definable shape, approximations like ellipsoids have to be used. Differing from the actual shape of the Earth, a geoid is a theoretical body, whose surface intersects the gravitational field lines everywhere at right angles.

A geoid is often used as a reference level for measuring height. For example, the reference point in Switzerland for measuring height is the "Repère Pierre du Niton (RPN, 373.600 m) in the Geneva harbor basin. This height originates from point to point measurements with the port of Marseilles (mean height above sea level 0.00m).





## <span id="page-18-2"></span><span id="page-18-0"></span>**2.3 Ellipsoid and datum**

#### <span id="page-18-1"></span>**2.3.1 Ellipsoid**

A geoid is a difficult shape to manipulate when conducting calculations. A simpler, more definable shape is therefore needed when carrying out daily surveying operations. Such a substitute surface is known as an ellipsoid. If the surface of an ellipse is rotated about its symmetrical north-south pole axis, a spheroid is obtained as a result ([Figure](#page-18-3) 11).

An ellipsoid is defined by two parameters:

- Semi major axis a (on the equatorial plane)
- Semi minor axis b (on the north-south pole axis)

The amount by which the shape deviates from the ideal sphere is referred to as flattening (f).



<span id="page-18-3"></span>**Figure 11: Producing a spheroid** 



#### <span id="page-19-0"></span>**2.3.2 Customized local reference ellipsoids and datum**

#### **2.3.2.1 Local reference ellipsoids**

When dealing with an ellipsoid, care must be taken to ensure that the natural perpendicular does not intersect vertically at a point with the ellipsoid, but rather with the geoid. Normal ellipsoidal and natural perpendiculars do not therefore coincide, they are distinguished by "vertical deflection" [\(Figure](#page-19-1) 13), i.e., points on the Earth's surface are incorrectly projected. In order to keep this deviation to a minimum, each country has developed its own customized non-geocentric ellipsoid as a reference surface for carrying out surveying operations ([Figure](#page-19-2) 12). The semi axes a and b as well as the mid-point are selected in such a way that the geoid and ellipsoid match national territories as accurately as possible.

#### **2.3.2.2 Datum, map reference systems**

National or international map reference systems based on certain types of ellipsoids are called datums. Depending on the map used when navigating with GNSS receivers, care should be taken to ensure that the relevant map reference system has been entered into the receiver.

There are over 120 map reference systems available, such as: CH-1903 for Switzerland, NAD83 for North America, and WGS-84 as the global standard.



<span id="page-19-2"></span>

An ellipsoid is well suited for describing the positional coordinates of a point in degrees of longitude and latitude. Information on height is either based on the geoid or the reference ellipsoid. The difference between the measured orthometric height H, i.e. based on the geoid, and the ellipsoidal height h, based on the reference ellipsoid, is known as geoid undulation N [\(Figure](#page-19-1) 13).



<span id="page-19-1"></span>**Figure 13: Difference between geoid and ellipsoid** 



#### <span id="page-20-0"></span>**2.3.3 National reference systems**

Different reference systems are used throughout Europe, and each reference system employed for technical applications during surveying has its own name. The non-geocentric ellipsoids that form the basis of these are summarized in the following table ([Table](#page-20-2) 1). If the same ellipsoids are used, they are distinguished from country to country in respect of their local references

| Country       | Name    | Reference    | Local reference      | Semi major axis | Flattening  |
|---------------|---------|--------------|----------------------|-----------------|-------------|
|               |         | ellipsoid    |                      | a (m)           | (1: )       |
| Germany       | Potsdam | Bessel 1841  | Rauenberg            | 6377397.155     | 299.1528128 |
| France        | NTF     | Clarke 1880  | Pantheon, Paris      | 6378249.145     | 293.465     |
| Italy         | SI 1940 | Hayford 1928 | Monte Mario, Rome    | 6378388.0       | 297.0       |
| Netherlands   | RD/NAP  | Bessel 1841  | Amersfoort           | 6377397.155     | 299.1528128 |
| Austria       | MGI     | Bessel 1841  | Hermannskogel        | 6377397.155     | 299.1528128 |
| Switzerland   | CH1903  | Bessel 1841  | Old Observatory Bern | 6377397.155     | 299.1528128 |
| International | Hayford | Hayford      | Country independent  | 6378388.000     | 297.000     |

<span id="page-20-2"></span>**Table 1: National reference systems** 

#### <span id="page-20-1"></span>**2.3.4 Worldwide reference ellipsoid WGS-84**

The details displayed and calculations made by a GNSS receiver primarily involve the WGS-84 (World Geodetic System 1984) reference system. The WGS-84 coordinate system is geocentrically positioned with respect to the center of the Earth. Such a system is called ECEF (Earth Centered, Earth Fixed). The WGS-84 coordinate system is a three-dimensional, right-handed, Cartesian coordinate system with its original coordinate point at the center of mass (= geocentric) of an ellipsoid, which approximates the total mass of the Earth.

The positive X-axis of the ellipsoid [\(Figure](#page-20-3) 14) lies on the equatorial plane (that imaginary surface which is encompassed by the equator) and extends from the center of mass through the point at which the equator and the Greenwich meridian intersect (the 0 meridian). The Y-axis also lies on the equatorial plane and is offset 90° to the east of the X-axis. The Z-axis lies perpendicular to the X and Y-axis and extends through the geographical North Pole.



#### <span id="page-20-3"></span>**Figure 14: Illustration of the Cartesian coordinates**

The parameters of the WGS-84 ellipsoid are summarized in [Table](#page-21-1) 2.





| Parameter of WGS-84 Reference Ellipsoids |                       |                  |  |  |  |  |  |
|------------------------------------------|-----------------------|------------------|--|--|--|--|--|
| Semi major axis a (m)                    | Semi minor axis b (m) | Flattening (1: ) |  |  |  |  |  |
| 6,378,137.00                             | 6,356,752.31          | 298,257223563    |  |  |  |  |  |

#### <span id="page-21-1"></span>**Table 2: The WGS-84 ellipsoid**

Ellipsoidal coordinates (, h), rather than Cartesian coordinates (X, Y, Z) are generally used for further processing [\(Figure](#page-21-2) 15). corresponds to latitude, to longitude and h to the ellipsoidal height, i.e. the length of the vertical P line to the ellipsoid.



<span id="page-21-2"></span>**Figure 15: Illustration of the ellipsoidal coordinates** 

#### <span id="page-21-0"></span>**2.3.5 Transformation from local to worldwide reference ellipsoid**

#### **2.3.5.1 Geodetic datum**

As a rule, reference systems are generally local rather than geocentric ellipsoids. The relationship between a local (e.g. CH-1903) and a global, geocentric system (e.g. WGS-84) is referred to as the geodetic datum. In the event that the axes of the local and global ellipsoid are parallel, or can be regarded as being parallel for applications within a local area, all that is required for datum transition are three shift parameters, known as the datum shift constants X, Y, Z.

A further three angles of rotation x, y, z and a scaling factor m [\(Figure](#page-22-0) 16) may have to be added so that the complete transformation formula contains 7 parameters. The geodetic datum specifies the location of a local three-dimensional Cartesian coordinate system with regard to the global system.





#### <span id="page-22-0"></span>**Figure 16: Geodetic datum**

The following table [\(Table](#page-22-2) 3) shows examples of the various datum parameters. Additional values can be found under[3](#page-22-1) .

| Country     | Name    | X (m)   | Y (m)   | Z (m)   | x (´´) | x (´´) | x (´´) | m (ppm) |
|-------------|---------|----------|----------|----------|---------|---------|---------|---------|
| Germany     | Potsdam | 586      | 87       | 409      | -0.52   | -0.15   | 2.82    | 9       |
| France      | NTF     | -168     | -60      | 320      | 0       | 0       | 0       | 1       |
| Italy       | SI 1940 | -225     | -65      | 9        | -       | -       | -       | -       |
| Netherlands | RD/NAP  | 565.04   | 49.91    | 465.84   | 0.4094  | -0.3597 | 1.8685  | 4.0772  |
| Austria     | MGI     | -577.326 | -577.326 | -463.919 | 5.1366  | 1.4742  | 5.2970  | -2.4232 |
| Switzerland | CH1903  | 660.077  | 13.551   | 369.344  | 0.8065  | 0.5789  | 0.9542  | 5.66    |

<span id="page-22-2"></span>

#### **2.3.5.2 Datum conversion**

Converting a datum means by definition converting one three-dimensional Cartesian coordinate system (e.g. WGS-84) into another (e.g. CH-1903) by means of three-dimensional shift, rotation and extension. The geodetic datum must be known, in order to effect the conversion. Comprehensive conversion formulae can be found in specialist literature[4](#page-22-3) , or conversion can be carried out directly via the Internet[5](#page-22-4) . Once conversion has taken place, Cartesian coordinates can be transformed into ellipsoidal coordinates.

<span id="page-22-1"></span><sup>3</sup> <http://www.geocities.com/mapref/mapref.html>

<span id="page-22-3"></span><sup>4</sup> B. Hofmann-Wellenhof: GPS in der Praxis, Springer-Verlag, Wien 1994, ISBN 3-211-82609-2

<span id="page-22-4"></span><sup>5</sup> Bundesamt für Landestopographie: [http://www.swisstopo.ch](http://www.swisstopo.ch/)



#### <span id="page-23-0"></span>**2.3.6 Converting coordinate systems**

#### **2.3.6.1 Converting Cartesian to ellipsoidal coordinates**

Cartesian and ellipsoidal coordinates can be converted from the one representation to the other. As and h show up on the right side of the following equations, these equations have to be evaluated iteratively for an accurate solution.

$$
e2 = \frac{a2 - b2}{a2}
$$
$$
RN = \frac{a}{\sqrt{1 - e2 \sin2 \varphi a2}}
$$

$$
\varphi = \arctan\left[\frac{z}{\sqrt{x^2 + y^2}} \cdot \frac{1}{1 - \frac{R_v}{R_v + h}} e^2\right]
$$
\n(17a)

$$
\lambda = \tan^{-1}\left(\frac{y}{x}\right) \tag{18a}
$$

$$
h = \frac{\sqrt{x^2 + y^2}}{\cos{(\varphi)}} - R_N
$$
\n(19a)

#### **2.3.6.2 Converting ellipsoidal to Cartesian coordinates**

Ellipsoidal coordinates can be converted into Cartesian coordinates.

$$
x = [R_N + h] \cos (\varphi) \cos (\lambda)
$$
 (20a)

$$
y = [R_N + h] \cdot \cos (\varphi) \cdot \sin (\lambda)
$$
 (21a)

$$
z = [R_N \cdot [1 - e^2] + h] \cdot \sin (\varphi)
$$
 (22a)

## <span id="page-23-1"></span>**2.4 Planar regional coordinates, projection**

Usually the ordnance survey depicts the position of a point P on the surface of the earth through the ellipsoid coordinates' latitude and longitude (in relation to the reference ellipsoid) and height (in relation to the ellipsoid or geoid).

Given that geoid calculations (e.g. the distance between two buildings) on an ellipsoid are numerically awkward, general survey technical practices project the ellipsoid onto a plane. This leads to planar, right-angled X and Y regional coordinates. Most maps feature a grid, which enables finding a point in the open easily. In the case of planar regional coordinates there are mappings (projections) of ellipsoid coordinates of the survey reference ellipsoid in a calculation plane. The projection of the ellipsoid in a plane is not possible without distortions. It is



possible, however, to choose the projection in such as way that the distortions are kept to a minimum. Usual projection processes are cylindrical or Mercator projection or the Gauss-Krüger and UTM projection. Should position information be used in conjunction with map material, it must be remembered which reference system and which projection configuration is going to be used for making the maps.

#### <span id="page-24-0"></span>**2.4.1 Gauss-Krüger projection (Transversal Mercator Projection)**

The Gauss-Krüger projection is a tangential conformal transverse Mercator projection and is only applicable to a limited area or region. An elliptical cylinder is laid around the earth's rotation ellipsoid (e.g. Bessel ellipsoid), whereby the cylinder surface touches the ellipsoid in the central meridian (an important meridian for the region to be illustrated, e.g. 9°) along its whole longitude and in the poles. The cylinder position with regard to the ellipsoid is transversal, e.g. rotated by 90° ([Figure](#page-24-2) 17)). In order to keep the longitudinal and surface distortions to a minimum, 3° wide zones of the rotation ellipsoid are used. The zone width is fixed around the central meridian. Different central meridians are used depending on the region (e. g. 6°, 9°, 12°, 15°, ....).



#### <span id="page-24-2"></span>**Figure 17: Gauss-Krüger projection**

The values in the north-south direction are counted as the distance from the equator. In order to avoid negative values in the west-east direction the value of +500000m (Offset) is accepted for the central meridian. The central meridian's number of degrees is divided by 3 and placed in front of this value.

Example of a position:

| Ellipsoid coordinates :              | N:46.86154°  | E 9.51280°   |
|--------------------------------------|--------------|--------------|
| Gauss-Krüger (Central meridian: 9°): | N-S: 5191454 | W-E: 3539097 |

The position is at a distance of 5191454m from the equator and 39097m from the central meridian (9°).

#### <span id="page-24-1"></span>**2.4.2 UTM projection**

In contrast to the Gauss-Krüger projection the UTM (Universal Transversal Mercator) system projects almost the entire surface of the earth on 6020 = 1200 planes. The actual projection of the rotation ellipsoid on the transversal cylinder is carried out in accordance with the same process as in the Gauss-Krüger projection.

The UTM system is often based on the WGS84 ellipsoid. However, it only defines the projection and the coordinate system and not the reference ellipsoid and the geodesic datum.

The UTM system divides the whole world into 6° wide longitudinal zones ([Figure](#page-25-0) 18). These are numbered from 1 to 60 beginning with 180° W, and ending with 180° E. If, for example zone 1 stretches from 180° W to 174°



W, the central meridian of this zone 1 is situated at 177° W, zone 2 stretches from 174° W to 168°, the central meridian of this zone 2 is situated at 171° W, etc.

The central meridians for each projection zone are 3°, 9°, 15°, 21°, 27°, 33°, 39°, 45°, 51°, 57°, 63°, 69°, 75°, 81°, 87°, 93°, 99°, 105°, 111°, 117°, 123°, 129°, 135°, 141°, 147°, 153°, 159°, 165°, 171°, 177° east (E) and west (W) (longitude) [\(Figure](#page-25-1) 19).

In the north-south direction (to the poles) the zones are subdivided, with an exception in the 8° belt of latitude, and are identified with letters beginning with C. Only the area between 80° south to 84° north is admitted. The line from 80° south to 72° south is designated as Section C, the line from 72° south to 64° south Section D, etc. An exception to this is belt known as latitude X between 72° north and 84° north. It is 12° wide.



<span id="page-25-0"></span>**Figure 18: Principle of projecting one zone (of sixty)** 



<span id="page-25-1"></span>**Figure 19: Designation of the zones using UTM, with examples** 



As is the case with Gauss-Krüger Projection, the north-south value is measured in kilometers as the distance of the point from the equator. In order to avoid negative values in the southern hemisphere, the equator is arbitrarily assigned the value of 10,000,000m.

The west-east values are the distance of the point from the central meridian, which (also as with the Gauss-Krüger Projection) is given the value of 500,000m.

An example of UTM coordinates in comparison to WGS 84 would be:

| WGS 84:   | N 46,86074°   | E 9,51173°    |
|-----------|---------------|---------------|
| UTM: 32 T | 5189816 (N-S) | 0539006 (W-E) |

#### <span id="page-26-0"></span>**2.4.3 Swiss projection system (Conformal Double Projection)**

The Bessel ellipsoid is conformally projected onto a plane in two steps, i.e. angle preserving. Initially there is conformal projection of the ellipsoid on a sphere, then the sphere is conformally projected onto a plane using an oblique cylindrical projection. This process is called double projection ([Figure](#page-26-1) 20). A main point is fixed in the plane on the ellipsoid (old observatory from Bern) in the projection of the origin (with Offset: YOst = 600,000 m and XNord= 200,000 m) of the coordinate system.

On Switzerland's map (e.g. scale 1:25000) there are two different pieces of coordinate information:

- The regional coordinates projected in the plane (X and Y in kilometers) with the accompanying grid and
- The geographical coordinates (Longitude and latitude in degrees and seconds) related to the Bessel ellipsoid



#### <span id="page-26-1"></span>**Figure 20: The principle of double projection**

The signal transit time from 4 satellites must be known by the time the positional coordinates are issued. Only then, after considerable calculation and conversion, is the position issued in Swiss land survey coordinates ([Figure](#page-26-2) [21\)](#page-26-2).



<span id="page-26-2"></span>**Figure 21: From satellite to position** 



#### <span id="page-27-0"></span>**2.4.4 Worldwide conversion of coordinates**

The internet offers various possibilities for converting coordinates from one system into another.

#### **2.4.4.1 Example: conversion of WGS-84 coordinates to CH-1903 coordinates**

(From reference systems in practice, Urs Marti, Dieter Egger, Swiss Federal Office of Topography)

Accuracy is within 1 meter!

#### **1. Conversion of latitude and longitude:**

The latitude and longitude of the WGS-84 data have to be converted into sexagesimal seconds [´´].

Example:

- 1. The latitude (WGS-84) of 46° 2´ 38,87´´ once converted is 165758.87´´. This integer is described as B: B = 165758.87´´.
- 2. The longitude (WGS-84) of 8° 43´ 49,79´´ once converted is 31429.79´´. This integer is described as L: L = 31429.79´´.

#### **2. Calculation of auxiliary integers:**

$$
\Phi = \frac{B - 169028.66''}{10000} \qquad \qquad \Lambda = \frac{L - 26782.5''}{10000}
$$

Example:

#### **3. Calculation of the abscissa (W---E): y**

)54.44()36.0()51.10938()93.211455(37.600072][ <sup>2</sup> <sup>3</sup> *my*

Example: y = 700000.0m

#### **4. Calculation of the ordinate (S---N): x**

)79.119()56.194()63.76()25.3745()95.308807(07.200147][ <sup>2</sup> <sup>2</sup> <sup>2</sup> <sup>3</sup> *mx*

Example: x = 100000.0m

#### **5. Calculation of the height H:**

(][ *HeightmH WGS*<sup>84</sup> )94.6()73.2()55.49

Example:

HeightWGS-84 = 650.60m results from the conversion: H = 600m



## <span id="page-28-0"></span>**2.5 Georeferencing of raster maps**

#### <span id="page-28-1"></span>**2.5.1 Introduction**

Georeferencing refers to the transformation of a raster map (source) into a vector map (image). With raster maps the location of every point is given by the pixel coordinates (X;Y) and can be stored in various data formats such as .JPG, .BMP, .GIF, or .PNG. These maps can be obtained from satellite photographs or by scanning maps into a computer file. With vector maps each point is determined by the geographic coordinates (X', Y'). The raster map is transformed into the vector map with its geographical coordinate system by using an appropriate mathematical transformation (see [Figure](#page-28-4) 22). In this section the transformational process is explained.



<span id="page-28-4"></span>**Figure 22: Raster map with pixel coordinates X,Y (left) and vector map with geographic coordinates X', Y' (right)** 

#### <span id="page-28-2"></span>**2.5.2 Basics of transformation**

The transformation of a raster map into a vector map with coordinate system takes place through the geometric rules of affine transformation. This is also referred to as a linear transformation. The procedure is only suitable for smaller sections of maps, covering an area of up to a few kilometers. In the coordinate transformation, the coordinates of the source coordinate system (X, Y) are transformed into another system (X', Y').

#### <span id="page-28-3"></span>**2.5.3 Determining the transformation coordinate**

Algebraic representation (for definition, see [Figure](#page-29-1) 23): *fYeXdY*

$$
X' = a \bullet X + b \bullet Y + c
$$
$$
Y' = d \bullet X + e \bullet Y + f
$$



Matrix representation:





<span id="page-29-1"></span>**Figure 23: Definition of the source points** 

#### <span id="page-29-0"></span>**2.5.4 Determining the transformation parameters a, b, c, d, e, f**

The 6 transformation parameters (a, b, c, d, e, f) must be defined as 3 coordinate pairs (calibration points). In order to calculate the 6 parameters, 6 equations with 6 unknown variables must be solved. The derivation of the formula to determine the transformation parameters (a, b, c, d, e, f) occurs in 3 steps.

#### **1. Calibration of the image:**

Three calibration points are selected that are well distributed on the map (see [Figure](#page-29-2) 24). The source coordinates (X, Y) and the translated coordinates (X', Y') are defined for each of these calibration points.



<span id="page-29-2"></span>



Calibration Coordinates:

X1, Y1, X1', Y1' X2, Y2, X2', Y2' [I] X3' Y3' X3', Y3'

## **2. Construction of the transformation equation:**

Formula [I] can be rearranged for all 6 of the transformed coordinates

X1' = a•X1 + b•Y1 + c Y1' = d•X1 + e•Y1 + f X2' = a•X2 + b•Y2 + c [II] Y2' = d•X2 + e•Y2 + f X3' = a•X3 + b•Y3 + c Y3' = d•X3 + e•Y3 + f

Equation [II] is then represented in the matrix form

<span id="page-30-0"></span>

| X<br>'1<br><br>           |   | YX<br>1<br>      |     | 011 |    | 00  |       | a<br><br>                |       |
|-----------------------------|---|-------------------|-----|-----|----|-----|--------|----------------------------|-------|
| <br><br>Y<br>'1<br><br> |   | <br>0<br>       | 00  |     | YX | 111 | <br> | <br><br>b<br><br>      |       |
| <br><br>X<br>'2           |   | <br>YX           | 122 |     | 0  | 00  |       | <br><br>c                |       |
| <br><br>Y<br>'2<br><br> |  | <br>0<br>       | 00  |     | YX | 122 | <br> | <br><br><br>d<br><br> | [III] |
| <br><br>X<br>'3<br><br> |   | <br>YX<br>3<br> |     | 013 |    | 00  | <br> | <br><br>e<br><br>      |       |
| Y<br>'3<br><br><br><br> |   | 0<br><br>       | 00  |     | YX | 133 | <br> | f<br><br><br><br>      |       |

#### <span id="page-30-1"></span>**3. Determining the transformation parameters a, b, c, d, e, f:**

The solution vectors (a, b, c, d, e, f) are sought and can be obtained by rearranging Equation [[III](#page-30-0)].

| a<br><br>                     |   | YX<br>1<br>     |    | 011 |    | 00  |            | <br>1 | X<br>'1<br><br>                     |      |
|---------------------------------|---|------------------|----|-----|----|-----|-------------|--------|---------------------------------------|------|
| <br><br>b<br><br>           |   | <br>0<br>      | 00 |     | YX | 111 | <br>      |        | <br><br>Y<br>'1<br><br>           |      |
| <br><br>c                     |   | <br>YX<br>2     |    | 012 |    | 00  |            |        | <br><br>X<br>'2                     |      |
| <br><br>d<br><br>           |  | <br>0<br>      | 00 |     | YX | 122 | <br>      |       | <br><br>Y<br>'2<br><br>           | [IV] |
| <br><br>e                     |   | <br>YX<br>3     |    | 013 |    | 00  |            |        | <br><br>X<br>'3                     |      |
| <br><br>f<br><br><br><br> |   | <br>0<br><br> | 00 |     | YX | 133 | <br><br> |        | <br><br>Y<br>'3<br><br><br><br> |      |



#### <span id="page-31-0"></span>**2.5.5 Example (raster map to WGS84)**

The following map [\(Figure](#page-31-1) 25) is to be georeferenced. For calibration three reference points are used.



<span id="page-31-1"></span>**Figure 25: Raster map with three calibration points[6](#page-31-2)**

|                     | X (Pixel) | Y (Pixel) | X' (°)    | Y' (°)    |
|---------------------|-----------|-----------|-----------|-----------|
| Calibration Point 1 | 111       | 76        | -1.974449 | 42.733900 |
| Calibration Point 2 | 1220      | 87        | -1.784248 | 42.732135 |
| Calibration Point 3 | 623       | 738       | -1.886730 | 42.650122 |

Determining the transformation parameter according to equation [[IV](#page-30-1)]

| a<br><br>                     |   | 0.0001887<br><br>                      |
|---------------------------------|---|------------------------------------------|
| <br><br>b<br><br>           |   | <br><br>- 0.0000134<br><br>          |
| <br><br>c                     |   | <br><br>-1.9943709                     |
| <br><br>d<br><br>           |  | <br><br>- 0.0000004<br><br>          |
| <br><br>e                     |   | <br><br>- 0.0001263                    |
| <br><br>f<br><br><br><br> |   | <br><br>42.7435373<br><br><br><br> |

<span id="page-31-2"></span><sup>6</sup> http://maps.google.com/



#### Determining the coordinates of a position



<span id="page-32-1"></span>**Figure 26: Determining position with the pixel coordinates X = 643 and Y = 370** 

With the formula:

*fYeXdY cYbXaX* ''

X' and Y' result in the following geographic coordinates: Longitude X' = - 1.883248° and Latitude Y' = 42.69659°



**Figure 27: Verifying the calculated geographic coordinates with Google Earth[7](#page-32-0)**

<span id="page-32-2"></span><span id="page-32-0"></span><sup>7</sup> http://maps.google.com/



# <span id="page-33-0"></span>**3 Foundations of satellite technology**

## <span id="page-33-1"></span>**3.1 Kepler's laws**

The motion of satellites in space is determined by the Laws of Planetary Motion described by Johannes Kepler (1571-1630). Kepler observed that the motion of bodies in space followed three relatively simple mathematical laws.

#### <span id="page-33-2"></span>**3.1.1 Kepler's first law**

According to Kepler, the planets orbit on a plane. The orbit forms an ellipse with the sun at one of the foci.

This law also applies to satellites (as orbiting bodies in space). Satellites also orbit along a plane ([Figure](#page-33-4) 28). Their orbit around the Earth forms an ellipse with the Earth at one of the foci.



#### <span id="page-33-4"></span>**Figure 28: Satellites move along a plane**

- The **Apogee** expresses the furthest point of an elliptical orbit from the center of the Earth. If one subtracts the value of the Earth's radius (approx. 6378 km) from this value, one determines the satellite's maximum altitude above the Earth's surface.
- The **Perigee** is the closest point of the orbital ellipse to the Earth. Subtracting the Earth's radius determines the satellite's minimal altitude above the surface of the Earth.

#### <span id="page-33-3"></span>**3.1.2 Kepler's second law**

The second law states that: "A line joining a planet and the sun sweeps out equal areas during equal intervals of time.[8](#page-33-5) " This is also known as the law of equal areas.

For satellites this means that a line joining a satellite and the Earth sweeps out equal areas during equal intervals of time. Thus, if Times Tv\_1 and Tv\_2 are the same, then the areas A\_1 and A\_2 will also be the same (see [Figure](#page-34-1) 29).

<span id="page-33-5"></span><sup>8</sup> "[Kepler's](http://demonstrations.wolfram.com/KeplersSecondLaw/) Second Law" by Jeff Bryant with Oleksandr Pavlyk, The Wolfram Demonstrations Project





<span id="page-34-1"></span>**Figure 29: Depiction of Kepler's second law** 

#### <span id="page-34-0"></span>**3.1.3 Kepler's third law**

This law states that the squares of the orbital periods of planets are directly proportional to the cubes of the [semi-major](http://en.wikipedia.org/wiki/Semi-major_axis) axis of the orbits. This means not only that larger objects have longer orbits, but also that the speed of a planet in a longer orbit is lower than in a smaller orbit:

3 2 *a P* is constant for all planets.

P = orbital Period, a = semi-major axis of the orbital ellipse

From this law the satellite orbital altitude (h) (see [Figure](#page-35-1) 30) above the Earth's surface can be derived:

$$
h = \sqrt[3]{3,9860042 \cdot 10^{14} \frac{m^3}{s^2} \cdot \left(\frac{P}{2\pi}\right)^2} - R_e
$$
 [m]

Re: Radius of the Earth (6378.137km)

P: orbital period of the satellite around the Earth





**Figure 30: Determining the orbital altitude (h) of a satellite** 

## <span id="page-35-1"></span><span id="page-35-0"></span>**3.2 Satellite orbits**

The orbit describes the position of a satellite in space. Satellites used for navigation move around the Earth in endless circular or elliptical orbits. The spatial orientation (e.g. orbital inclination, excentricity, length, altitude above the ground) and the parameters of motion (e.g. orbital period) have a significant impact on the usability and performance of these satellites ([Figure](#page-35-2) 31).



#### <span id="page-35-2"></span>**Figure 31: Satellite orbits**

- The **inclination**, also referred to as the angle of inclination or the axial tilt, expresses the tilt of the circular or elliptical orbit of the satellite around the Earth relative to the equatorial plane. For example, with an inclination of 90° an orbit would pass directly over the polar caps. All satellite orbits that do not lie along the equatorial plane are referred to as "inclined orbits".
- The **Ephemeris** of a satellite is a mathematical description of its orbit. The high precision satellite orbital data is necessary for a receiver to calculate the satellite's exact position in space at any given time. Orbital data with reduced exactness is referred to as an **Almanac** (see [Figure](#page-36-0) 32). With the help of the Almanac the receiver can calculate which satellites are visible over the horizon from an approximate



position and time. Each satellite transmits its own Ephemeris as well as the Almanacs of all existing satellites. The current Almanac Data can also be viewed over the internet9 .

#### <span id="page-36-0"></span>**Figure 32: Almanac**

- The **Elevation** describes the angle of a satellite relative to the horizontal plane. If a satellite is directly above the point of observation on the ground, then the elevation is 90°. If the satellite is at the horizon, then the elevation is 0°.
- The **Azimuth** is the angle between a reference plane and a point. In the case of satellites the reference plane is the plane of the horizon based on true North. The Azimuth is the angle between the satellite and true North (North = 0°, East = 90°, South = 180°, West = 270°).



#### <span id="page-36-1"></span>**Figure 33: Azimuth**

**Excentricity** defines the so-called Numerical Excentricity "e", which is the deviation of an elliptical satellite orbit (excentric orbit) from a geometrically exact circular orbit. Numerical Excentricity is defined by the equation:

| e | 2a<br>2b<br><br> |
|---|--------------------|
|   | 2a                 |

<sup>9</sup> http://www.navcen.uscg.gov/gps/almanacs.htm



where a is the semi-major axis and b is the semi-minor axis of the elliptical orbit (see [Figure](#page-33-4) 28). For completely circular orbits the value of e = 0, and approaches 1 the more the length (i.e. the semimajor axis) of the ellipse is stretched relative to the semi-minor axis.

## <span id="page-37-0"></span>**3.3 Orbital altitude**

The orbital altitude gives the elevation above the Earth's surface of a point on a circular or elliptical satellite orbit. Originally, commercial communications satellites were preferentially brought into circular equatorial (Inclination 0°) orbits with an altitude of about 36,000 km above the ground. Satellites on this orbit rotate around the earth in 24 hours (orbital period: 24 hours), so that there is no relative movement with respect to the Earth. For this reason such satellites are also referred to as Geosynchronous (**GEO**) satellites, with an orbit referred to as Geostationary. GEO satellites are used by communications satellite systems such as Inmarsat and Thuraya as well as SBAS systems such as WAAS and EGNOS (see Section [7.5.1\)](#page-111-1).

In addition to the relatively high altitude GEO satellites, which can provide coverage to large areas of the Earth's surface, other satellite systems (e.g. Iridium, Globalstar, GPS und GALILEO) employ satellites with much lower orbital altitudes. These lower altitude satellites must orbit the Earth with increased speed in order to provide the necessary centrifugal force to compensate for the increased gravitational pull experienced at lower altitudes. In contrast to the GEO satellites, these satellites move relative to the Earth and rotate in so-called Non-Geostationary Satellite Orbits (NGSO).

Generally, six different categories of orbits are classified:

- Geosynchronous Earth Orbit (**GEO**): geostationary orbit with an altitude of approximately 36,000km
- Medium Earth Orbit (**MEO**): inclined orbit with medium altitude of about 10,000 km
- Low Earth Orbit (**LEO**): low altitude orbit up to approximately 1'000 km
- Highly (Inclined) Elliptical Earth Orbit (**HEO**)
- Inclined Geosynchronous Orbit (**IGSO**)
- Polar Earth Orbit (**PEO**): LEO orbit over the polar caps

#### **Example 1: Determining the altitude of a GEO satellite:**

Satellites with a geostationary orbit have a very exact altitude which can be calculated.

The mean siderial[10](#page-37-1) Earth day has a duration of 23 hours, 56 minutes, 4.099 seconds = 86164.099 s and represents a geometrically complete rotation of the Earth of 360° in a system with fixed stars.

From Section [3.1.3](#page-34-0) we know the formula:

$$
h = \sqrt[3]{3.9860042 \cdot 10^{14} \frac{\text{m}^3}{\text{s}^2} \cdot \left(\frac{T}{2\pi}\right)^2} - R_e = \sqrt[3]{3.9860042 \cdot 10^{14} \frac{\text{m}^3}{\text{s}^2} \cdot \left(\frac{86164.099 \text{s}}{2\pi}\right)^2} - 6378137 \text{m} =
$$

m 35786035 km 35,786.035 

<span id="page-37-1"></span> <sup>10</sup> relative to the fixed position of the stars



#### **Example 2: Determining the orbital period of a GPS satellite.**

GPS satellites have a medium level altitude of 20,184.5 km above the Earth. The mean orbital period T of a GPS satellite is determinded by:

$$
T = 2 \cdot \pi \cdot \sqrt[2]{\frac{(h+R_e)^3}{3,9860042 \cdot 10^{14} \frac{m^3}{s^2}}} = 2 \cdot \pi \cdot \sqrt[2]{\frac{(20184500 m + 6378137 m)^3}{3,9860042 \cdot 10^{14} \frac{m^3}{s^2}}} =
$$

43084s 58min11h 

This represents a half siderial day. Since the Earth also rotates in this time, after two orbits the GPS satellite will find itself over the same point on the Earth's surface.

## <span id="page-38-0"></span>**3.4 Radio frequencies**

The transmission of information for satellite-based navigation and telecommunication systems takes place through radio broadcasts between the different system components:

- User Link: between satellite and user (e.g. user terminal)
- Feeder Link: between satellite and central station on the Earth (e.g. ground station, control station)
- Intersatellite Link: between satellites in space (directly, without using a ground station)

Transmission is differentiated based on its direction:

- Upwards (Uplink, or Reverse Link): Transmission from satellite transmission station (ground station and/or user terminal) "up" to satellites; e.g.: User Uplink, the transmission direction of a mobile user terminal
- Downwards (Downlink, Forward Link): Transmission from satellites "down" to satellite transmission station

Satellite transmission frequencies are assigned and regulated by the World Radio Conference (WRC) of the International Telecommunication Union (ITU). [Table](#page-38-1) 4 shows typical microwave electromagnetic transmission frequencies used by satellite communication and navigation as specified in ITU-R V.431-7.

| Band    | Frequency            |
|---------|----------------------|
| L-Band  | 1.0 GHz to 2.0 GHz   |
| S-Band  | 2.0 GHz to 4.0 GHz   |
| C-Band  | 4.0 GHz to 8.0 GHz   |
| X-Band  | 8.0 GHz to 12.0 GHz  |
| Ku-Band | 12.0 GHz to 18.0 GHz |
| K-Band  | 18.0 GHz to 27.0 GHz |
| Ka-Band | 27.0 GHz to 40.0 GHz |
| V-Band  | 40.0 GHz to 75 GHz   |
| W-Band  | 75 GHz to 110 GHz    |

<span id="page-38-1"></span>**Table 4: Satellite communication and navigation frequencies** 



## <span id="page-39-0"></span>**3.5 Time systems**

Time plays an essential role in satellite-based positioning. GPS distinguishes between five different important Time Systems.

#### <span id="page-39-1"></span>**3.5.1 International Atomic Time (TAI)**

The International Atomic Time Scale (Temps Atomique International = TAI) was introduced in order to produce a universal "absolute" time scale, which could simultaneously meet the different physical requirements of diverse applications. Such an application is GPS positioning, for which this time scale is very important.

Since 1967 the second has been defined by an atomic physical constant. The nonradioactive element Caesium ( 133Cs) was chosen as a reference. The resonance frequency between selected energy levels of this atom was set at 9 192 631 770 Hz. The so defined time has become part of the SI-System (Système International) of measures. The starting point of Atomic Time was set to January 1, 1958 at 00:00h.

#### <span id="page-39-2"></span>**3.5.2 Coordinated Universal Time (UTC)**

Coordinated Universal Time (UTC) was introduced in order to provide a time scale that is based on Atomic time and adapted to the actual world time on Earth. UTC was earlier referred to as Greenwich Mean Time (GMT) or Zulu-Tim[e11](#page-39-5).

UTC differs from TAI in the second count, i.e. UTC = TAI - n, where n equals whole seconds, which can be added at the end of December 31 and June 30 of each year (leap seconds). These leap seconds are necessary to reflect the general slowing trend of the Earth and to correct clocks that keep uniform, precise time.

#### <span id="page-39-3"></span>**3.5.3 GPS Time**

The general GPS system time is expressed as a week number and the number of elapsed seconds in that week. The start date is Sunday, January 6, 1980 at 0:00h (UTC). Every GPS week begins in the night between Saturday and Sunday, where the continuous time scale is given through the main clock of the Master Control Station. Time differences that occur between GPS and UTC time are continually calculated and included in the navigation information. GPS time and UTC differ from each other in whole seconds (in 2009 the difference between GPS time and UTC was 15 seconds) and a fraction of a second. The GPS control stations keep the difference between the second marks for GPS time and UTC less than 1μs. The difference between GPS time and UTC is transmitted with the GPS navigation message (see Section [4.6\)](#page-55-0) in sub-frame 4.

#### <span id="page-39-4"></span>**3.5.4 Satellite Time**

Because of the constant and irregular frequency errors of the onboard atomic clocks of the GPS satellites, the individual satellite times deviate from the GPS system time. The control station monitors the satellite clocks, and any observed time differences are communicated. The time deviation needs to be considered when performing local GPS measurements.

<span id="page-39-5"></span><sup>11</sup> http://www.bipm.org/en/scientific/tai/time\_server.html



#### <span id="page-40-0"></span>**3.5.5 Local Time**

Local Time refers to the time used in a specific region or area. The relationship between Local Time and UTC is determined by the time zones and by the regulations for standard and daylight saving time.

| local | 2009-07-09 15:08:21 | Thursday  | day 190     | timezone UTC+2          |
|-------|---------------------|-----------|-------------|-------------------------|
| UTC   | 2009-07-09 13:08:21 | Thursday  | day 190     | MJD 55021.54746         |
| GPS   | 2009-07-09 13:08:36 | week 1539 | 392916 s    | cycle 1 week 0515 day 4 |
| Loran | 2009-07-09 13:08:45 | GRI 9940  | 472 s until | next TOC 13:16:13 UTC   |
| TAI   | 2009-07-09 13:08:55 | Thursday  | day 190     | 34 leap seconds         |

[Table](#page-40-1) 5 is an example of a local time recorded on July 9, 2009 in Switzerland.

<span id="page-40-1"></span>

| Table 5: Time systems, January 200912 |  |  |  |  |  |
|---------------------------------------|--|--|--|--|--|
|---------------------------------------|--|--|--|--|--|

For the year 2009 the following time values are valid:

- TAI UTC = +34sec
- GPS UTC = +15sec
- TAI GPS = +19sec

<span id="page-40-2"></span><sup>12</sup> http://www.leapsecond.com/java/gpsclock.htm



## <span id="page-41-0"></span>**4 GNSS technology: the GPS example**

*If you would like to . . .* 

- o understand why three different GPS segments are needed
- o know what function each individual segment has
- o know how a GPS satellite is basically constructed
- o know what sort of information is transmitted to Earth
- o understand how a satellite signal is generated
- o understand how Satellite Navigation signal travel time is determined
- o understand what correlation means
- o understand why a minimum period of time is required for the GPS system to come online
- o know what frames and subframes are

*then this chapter is for you!* 

## <span id="page-41-1"></span>**4.1 Introduction**

All GNSS systems function on the same basic principles. In the following sections we will explore the different segments of GNSS technology by specifically looking at the GPS system. GPS is the pioneer and forerunner of GNSS technology and is the only fully functional GNSS system in operation. GPS and GNSS are often used interchangeably, although GPS specifically refers to NAVSTAR GPS, developed by the United States Department of Defense and managed by the United States Air Force 50th Space Wing. The GPS system has been fully operational since 1993. [13](#page-41-3)



## <span id="page-41-2"></span>**4.2 Description of the entire system**

The GPS system is comprised of three functional segments ([Figure](#page-42-2) 34):

- The space segment (all operating satellites)
- The control segment (all ground stations involved in the monitoring of the system: master control stations, monitor stations, and ground control stations)
- The user segment (all civilian and military users)

<span id="page-41-3"></span><sup>13</sup> http://en.wikipedia.org/wiki/Global\_Positioning\_System





#### <span id="page-42-2"></span>**Figure 34: The three GPS segments**

As can be seen in [Figure](#page-42-2) 34 there is unidirectional communication between the space segment and the user segment. The ground control stations have bidirectional communication with the satellites.

### <span id="page-42-0"></span>**4.3 Space segment**

#### <span id="page-42-1"></span>**4.3.1 Satellite distribution and movement**

The space segment of the GPS system consists of up to 32 operational satellites [\(Figure](#page-43-0) 35) orbiting the Earth on 6 different orbital planes (four to five satellites per plane). They orbit at a height of 20,180km above the Earth's surface and are inclined at 55° to the equator. Any one satellite completes its orbit in around 12 hours. Due to the rotation of the Earth, a satellite will be at its initial starting position above the earth's surface [\(Figure](#page-43-1) 36) after approx. 24 hours (23 hours 56 minutes to be precise).





**Figure 35: GPS satellites orbit the Earth on 6 orbital planes** 

<span id="page-43-0"></span>Satellite signals can be received anywhere within a satellite's effective range. [Figure](#page-43-1) 36 shows the effective range (shaded area) of a satellite located directly above the equator/zero meridian intersection.



<span id="page-43-1"></span>**Figure 36: 24 hour tracking of a GPS satellite with its effective range** 



The distribution of the satellites at a specific time can be seen in [Figure](#page-44-0) 37. It is due to this ingenious pattern of distribution and to the high orbital altitudes that communication with at least 4 satellites is ensured at all times anywhere in the world.



<span id="page-44-0"></span>**Figure 37: Position of the GPS satellites at 12:00 hrs UTC on 14th April 2001** 



#### <span id="page-45-0"></span>**4.3.2 The GPS satellites**

#### **4.3.2.1 Satellite construction**

All of the satellites use onboard atomic clocks to maintain synchronized signals, which are transmitted over the same frequency (1575.42 MHz). The minimum signal strength received on Earth is approx. -158dBW to -160dBW[14](#page-45-1). According to the specifications, the maximum strength is approx. -153dBW.



<span id="page-45-3"></span>

#### **4.3.2.2 The communication link budget analysis**

The link budget analysis [\(Table](#page-45-2) 6) between a satellite and a user is suitable for establishing the required level of satellite transmission power. According to the specifications, the minimum amount of power received must not fall below –160dBW (-130dBm). In order to ensure this level is maintained, the satellite L1 carrier transmission power, modulated with the C/A code, must be 21.9W. Polarization mismatch and antenna reception gain are a function of receiver design. The sum of these two parameters may vary largely. Depending on the design values between +5 dB to -10dB are typical.

|                                                                         | Gain (+) /loss (-) | Absolute value                 |
|-------------------------------------------------------------------------|--------------------|--------------------------------|
| Power at the satellite transmitter                                      |                    | 13.4dBW (43.4dBm=21.9W)        |
| Satellite antenna gain (due to concentration<br>of the signal at 14.3°) | +13.4dB            |                                |
| Radiate power EIRP                                                      |                    | 26.8dBW (56.8dBm)              |
| (Effective Integrated Radiate Power)                                    |                    |                                |
| Loss due to polarization mismatch                                       | -3.4dB             |                                |
| Signal attenuation in space                                             | -184.4dB           |                                |
| Signal attenuation in the atmosphere                                    | -2.0dB             |                                |
| Gain from the reception antenna                                         | +3.0dB             |                                |
| Power at receiver input                                                 |                    | -160dBW (-130dBm=100.0*10-18W) |

#### <span id="page-45-2"></span>**Table 6: L1 carrier link budget analysis modulated with the C/A code**

<span id="page-45-1"></span><sup>14</sup> Global Positioning System, Standard Positioning System Service,Signal Specification, 2nd Edition, 1995, page 18, <http://www.navcen.uscg.gov/pubs/gps/sigspec/gpssps1.pdf>



According to the specifications, the power of the received GPS signal in open sky is at least -160dBW (-130dBm). The maximum of the spectral power density of the received signal is given as -190dBm/Hz [\(Figure](#page-46-0) 39). The spectral power density of the thermal background noise is about –174dBm/Hz (at a temperature of 290K). Thus the maximum received signal power is approximately 16dB below the thermal background noise level.



<span id="page-46-0"></span>**Figure 39: Spectral Power Density of received signal and thermal noise** 





#### **4.3.2.3 Satellite signals**

The following information (the navigation message) is transmitted by the satellite at a rate of 50 bits per second [ [15](#page-47-1)]:

- Satellite time and synchronization signals
- Precise orbital data (ephemeris)
- Time correction information to determine the exact satellite time
- Approximate orbital data for all satellites (almanac)
- Correction signals to calculate signal transit time
- Data on the ionosphere
- Information on the operating status (health) of the satellite

The time required to transmit all this information is 12.5 minutes. By using the navigation message, the receiver is able to determine the transmission time of each satellite signal and the exact position of the satellite at the time of transmission.

Each GPS satellite transmits a unique signature assigned to it. This signature consists of a Pseudo Random Noise (PRN) Code of 1023 zeros and ones, broadcast with a duration of 1ms and continually repeated [\(Figure](#page-47-2) 40).



#### <span id="page-47-2"></span>**Figure 40: Pseudo Random Noise (PRN)**

The signature code serves the following two purposes for the receiver:

- Identification: the unique signature pattern identifies the satellite from which the signal originated.
- Signal travel time measurement

#### <span id="page-47-0"></span>**4.3.3 Generating the satellite signal**

#### **4.3.3.1 Simplified block diagram**

Onboard each of the satellites are four highly accurate atomic clocks. The resonance frequency of one of these clocks generates the following time pulses and frequencies required for operations (Figs. 13 and 14):

- The 50Hz data pulse
- The C/A (Coarse/Acquisition) code (a PRN-Code broadcast at 1.023MHz), which modulates the data using an exclusive-or operation (EXOR)[16](#page-47-3) spreading the data over a 2MHz bandwidth.
- The frequency of the civil L1 carrier (1575.42MHz)

The data modulated by the C/A code modulates the L1 carrier in turn by using Binary-Phase-Shift-Keying (BPSK)[17](#page-47-3) . With every change in the modulated data there is a 180° change in the L1 carrier phase.

<span id="page-47-1"></span><sup>15</sup> NAVCEN: GPS SPS Signal Specifications, 2nd Edition, 1995, <http://www.navcen.uscg.gov/pubs/gps/sigspec/gpssps1.pdf>

<span id="page-47-3"></span><sup>16</sup> A logical operation on two operands that results in a logical value of *true* if and only if exactly one of the operands has a value of *true*.







<span id="page-48-0"></span>**Figure 41: Simplified satellite block diagram** 



<span id="page-48-1"></span>**Figure 42: Data structure of a GPS signal** 

<sup>17</sup> A method of modulating a carrier wave so that data is translated into 0/180° phase shifts of the carrier.



#### **4.3.3.2 Detailed block diagram**

Satellite navigation signals are generated using a process known as DSSS (Direct Sequence Spread Spectrum) modulation[18](#page-49-0) . This is a procedure in which a nominal or baseband (not to be confused with the baseband chip in the receiver) frequency is deliberately spread out over a wider bandwidth through superimposing a higher frequency signal. The principle of spread-spectrum modulation was first devised in the 1940s in the United States, by screen actress Hedy Lamarr and pianist George Anthell[19](#page-49-1) . This process allows for secure radio links even in difficult environments.

GPS satellites are each equipped with four extremely stable atomic clocks (possessing a stability of greater than 20**·**10-12 ) [20](#page-49-2). The nominal or baseband frequency of 10.23MHz is produced from the resonant frequency of one of these onboard clocks. In turn, the carrier frequency, data pulse frequency and C/A (coarse/acquisition) code are all derived from this frequency ([Figure](#page-49-4) 43). Since all the GPS satellites transmit on 1575.42 MHz, a process known as a CDMA (Code Division Multiple Access) Multiplex [21](#page-49-3) is used.

The C/A code plays an important role in the multiplexing and modulation. It is a constantly repeated sequence of 1023 bits known as a pseudo random noise (PRN) code. This code is unique to each satellite and serves as its identifying signature. The C/A code is generated using a feedback shift register[22](#page-49-5). The generator has a frequency of 1.023 MHz and a period of 1023 chips[23](#page-49-6) , which corresponds to 1ms. The C/A code is a Gold Code[24](#page-49-7) , which has advantageous correlation properties. This has important implications later on in the navigation process in the calculation of position.



<span id="page-49-4"></span>**Figure 43: Detailed block diagram of a GPS satellite** 

<span id="page-49-0"></span><sup>18</sup> Lemme H.: Schnelles Spread-Spectrum-Modem auf einem Chip, Elektronik 1996, H. 15 p. 38 to p. 45

<span id="page-49-1"></span><sup>19</sup> [http://www.maxim-ic.com/appnotes.cfm/appnote\\_number/1890](http://www.maxim-ic.com/appnotes.cfm/appnote_number/1890)

<sup>20</sup> Parkinson B., Spilker J.: Global Positioning System, Volume 1, AIAA-Inc.

<span id="page-49-3"></span><span id="page-49-2"></span><sup>21</sup> A form of multiplexing that divides up a radio channel by using different pseudo-random code sequences for each user. CDMA is a form of "spread-spectrum" signalling, since the modulated code signal has a much higher bandwidth than the data being communicated.

<span id="page-49-5"></span><sup>22</sup> A shift register whose input bit is a linear function of its previous state.

<span id="page-49-6"></span><sup>23</sup> The transition time for individual bits in the pseudo-random sequence.

<span id="page-49-7"></span><sup>24</sup> A Gold code isrepresents a binary sequence which is generated from two m-sequences of same length n. A set of Gold codes can be

generated by variation of the phase shift of these two m-sequences. It is characteristic for Gold codes that the cross correlation function of these codes assumes just three distinct values.



## <span id="page-50-0"></span>**4.4 Control segment**

The GPS control segment (Operational Control System OCS) consists of a Master Control Station located in the state of Colorado, five monitor stations (each equipped with atomic clocks and distributed around the globe in the vicinity of the equator), and three ground control stations transmitting information to the satellites.

The most important tasks of the control segment are:

- Observing the movement of the satellites and computing orbital data (ephemeris)
- Monitoring the satellite clocks and predicting their behavior
- Synchronizing onboard satellite time
- Relaying precise orbital data received from satellites
- Relaying the approximate orbital data of all satellites (almanac)
- Relaying further information, including satellite health, clock errors etc.

#### <span id="page-50-1"></span>**4.4.1 Deactivation possibilities and artificial distortion of the signal (SA)**

The control segment also oversees the artificial distortion of signals (SA, Selective Availability), in order to degrade the system's positional accuracy for civil use. Until May 2000 the U.S. DoD (the GPS operators) intentionally degraded system accuracy for political and strategic reasons. This consisted of either modulating the time signals of the local satellites with a random error signal, or falsifying the ephemeris. At the beginning of May 2000, the SA system was deactivated[25](#page-50-2) . With this action the precision of position suddenly improved from approximately 100 m to 13 m (95% value) [26](#page-50-3). (See [Figure](#page-50-4) 44 and [Figure](#page-51-1) 45)



<span id="page-50-4"></span>**Figure 44: Improvement of position accuracy after the deactivation of SA on May 2, 2000** 

<span id="page-50-2"></span><sup>25</sup> http://www.ngs.noaa.gov/FGCS/info/sans\_SA/docs/statement.html

<span id="page-50-3"></span><sup>26</sup> http://pnt.gov/public/sa/diagram.shtml





<span id="page-51-1"></span>**Figure 45: Improvement of position accuracy as function of time** 

After May 2, 2000 the artificial distortion (SA) could be regionally or globally reactivated as necessary[27](#page-51-2) . The theory of this was to maintain the possibility of degrading or limiting the availability of GPS in specific crisis regions, while providing the unlimited system accuracy outside of these areas. In practice there were no known instances of reactivating the SA system.

On September 18, 2007, the US DoD reported that with the next generation of GPS satellites (GPS III), satellite navigation signals can no longer be artificially distorted[28](#page-51-3), [29](#page-51-4) . The technical possibility for signal distortion will no longer be included in this generation of satellites. This decision on the part of the US Government to not add signal distortion capability to GPS III satellites and to refrain from implementing the existing SA measures should guarantee the reliability of the GPS system for civilian users.

## <span id="page-51-0"></span>**4.5 User segment**

The radio signals transmitted by the GPS satellites take approx. 67 milliseconds to reach a receiver on Earth. As the signals travel at a constant speed (the speed of light c), their travel time determines the exact distance between the satellites and the user. Speed of light is however a function of the medium which will be discussed in detail later.

Four different signals are generated in the receiver, each having the same structure as the signals received from the 4 satellites. By synchronizing the signals generated in the receiver with those from the satellites, the signal time shifts t of the four satellites are measured as a time mark [\(Figure](#page-52-0) 46). The measured time shifts t of all 4 satellite signals are then used to determine the exact signal travel time. These time shifts multiplied by the speed of light are called pseudoranges.

<sup>27</sup> http://pnt.gov/public/sa/sa.shtml

<span id="page-51-4"></span><span id="page-51-3"></span><span id="page-51-2"></span><sup>28</sup> http://www.defenselink.mil/releases/release.aspx?releaseid=11335

<sup>29</sup> http://insidegnss.com/node/200



|                                      |    |                 | 1 ms |  |
|--------------------------------------|----|-----------------|------|--|
| Satellite<br>signal                  |    |                 |      |  |
| Receiver<br>signal<br>(synchronised) |    | Synchronisation |      |  |
| Receiver                             |    |                 |      |  |
| time mark                            | t |                 |      |  |

#### <span id="page-52-0"></span>**Figure 46: Measuring signal travel time**

In order to determine the position of a user, radio communication with four different satellites is required. The distance to the satellites is determined by the travel time of the signals. The receiver then calculates the user's latitude , longitude , altitude h and time t from the pseudoranges and known position of the four satellites. Expressed in mathematical terms, this means that the four unknown variables h and t are determined from the distance and known position of these four satellites, although a fairly complex level of iteration is required, which will be dealt with in greater detail at a later stage.

As mentioned earlier, all the GPS satellites transmit on the same frequency, but with a different C/A code. Identification of the satellites and signal recovery take place by means of a correlation. As the receiver is able to recognize all C/A codes currently in use, by systematically shifting and comparing every known code with all incoming satellite signals, a complete match will eventually occur (that is to say the correlation factor CF is one), and a correlation point will be attained [\(Figure](#page-52-1) 47). The correlation point is used to measure the actual signal travel time and to identify the satellite.



#### <span id="page-52-1"></span>**Figure 47: Demonstration of the correction process across 30 bits**

The quality of the correlation is expressed here as a CF (correlation factor). The value range of the CF lies between minus one and plus one and is only plus one when the signals completely match (bit sequence and phase).



$$
CF = \frac{1}{N} \bullet \sum_{i=1}^{N} [(mB) - (uB)]
$$

- mB: number of all matched bits
- uB: number of all unmatched bits
- N: number of observed bits.

As a result of the Doppler Effect (satellites and receivers are in relative motion to one another) the transmitted signals can be shifted by up to 5000 Hz at the point of reception. The determination of the signal travel time and data recovery therefore requires not only correlation with all possible codes at all possible phase shifts, but also identification of the correct phase carrier frequency. Furthermore, the local reference frequency may have also an offset which adds to the frequency span that needs to be searched. 1 ppm of frequency error in the local oscillator corresponds to 1.575 kHz Doppler shift. [Figure](#page-53-0) 48 assumes some arbitrary local oscillator offset on top of the 5000 kHz Doppler shift for illustration. Through systematic shifting and comparison of all the codes [\(Figure](#page-52-1) 47) and the carrier frequency with the incoming satellite signals there comes a point that produces a complete agreement (i.e. the correlation factor is one) ([Figure](#page-53-0) 48). A search position in the carrier frequency level is known as a bin.



#### <span id="page-53-0"></span>**Figure 48: Search for the maximum correlation in the code and carrier frequency domains**

The spectral power density of the received GPS signal lays at approximately 16 dB below the spectral power density of the thermal or background noise (see [Figure](#page-46-0) 39). The demodulation and despreading of the received GPS signal causes a system gain GG of:

$$
G_G = \frac{Modulation \ rate \ of \ C/A - Code}{Data \ rate \ of \ information \ signal} = \frac{1023 bps}{50 bps} = 20,500 = 43 dB
$$

After despreading, the power density of the usable signal is greater than that of the thermal or background signal noise ([Figure](#page-54-0) 49).





<span id="page-54-0"></span>**Figure 49: Spectral power density of the correlated signal and thermal signal noise** 

The sensitivity of a GPS Receiver can be improved through increasing the correlation time (Dwell Time). The longer a correlator remains at a specific point in the code-frequency domain, the lower will be the required GPS signal strength at the antenna. When the correlation time is increased by a factor of k, there will be an improvement GR in the difference between the Signal and the Thermal Background Noise of:

#### GR = log10 (k)

Doubling the Dwell Time increases the difference between the Signal and the Thermal Background Noise (the sensitivity of the receiver) by 3dB. In practice it is not a problem to increase the correlation time up to 20 ms. If the value of the transmitted data is known, then this time can be increased even more.



## <span id="page-55-0"></span>**4.6 The GPS message**

#### <span id="page-55-1"></span>**4.6.1 Introduction**

The GPS message[30](#page-55-3) is a continuous stream of data transmitted at 50 bits per second. Each satellite relays the following information to Earth:

- System time and clock correction values
- Its own highly accurate orbital data (ephemeris)
- Approximate orbital data for all other satellites (almanac)
- System health, etc.

The navigation message is needed to calculate the current position of the satellites and to determine signal travel times.

The data stream is modulated to the HF carrier wave of each individual satellite. Data is transmitted in logically grouped units known as frames or pages. Each frame is 1500 bits long and takes 30 seconds to transmit. The frames are divided into 5 subframes. Each subframe is 300 bits long and takes 6 seconds to transmit. In order to transmit a complete almanac, 25 different frames are required. Transmission time for the entire almanac is therefore 12.5 minutes. Unless equipped with GPS enhancement (see Chapter [7\)](#page-99-0) a GPS receiver must have collected the complete almanac at least once in order to calculate its initial position.

#### <span id="page-55-2"></span>**4.6.2 Structure of the navigation message**

A frame is 1500 bits long and takes 30 seconds to transmit. The 1500 bits are divided into five subframes each of 300 bits (duration of transmission 6 seconds). Each subframe is in turn divided into 10 words each containing 30 bits. Each subframe begins with a telemetry word and a handover word (HOW). A complete navigation message consists of 25 frames (pages). The structure of the navigation message is illustrated in a diagram in [Figure](#page-56-2) 50.

<span id="page-55-3"></span><sup>30</sup> GPS Standard Positioning Service Signal Specification, 2nd Edition, June 2, 1995





<span id="page-56-2"></span>**Figure 50: Structure of the entire navigation message** 

#### <span id="page-56-0"></span>**4.6.3 Information contained in the subframes**

A frame is divided into five subframes, each subframe transmitting different information.

- Subframe 1 contains the time values of the transmitting satellite, including the parameters for correcting signal transit delay and onboard clock time, as well as information on satellite health and an estimate of the positional accuracy of the satellite. Subframe 1 also transmits the so-called 10-bit week number (a range of values from 0 to 1023 can be represented by 10 bits). GPS time began on Sunday, 6th January 1980 at 00:00:00 hours. Every 1024 weeks the week number restarts at 0. This event is called a "week rollover".
- Subframes 2 and 3 contain the ephemeris data of the transmitting satellite. This data provides extremely accurate information on the satellite's orbit.
- Subframe 4 contains the almanac data on satellite numbers 25 to 32 (N.B. each subframe can transmit data from one satellite only), the difference between GPS and UTC time (leap seconds or UTC offset) and information regarding any measurement errors caused by the ionosphere.
- Subframe 5 contains the almanac data on satellite numbers 1 to 24 (N.B. each subframe can transmit data from one satellite only). All 25 pages are transmitted together with information on the health of satellite numbers 1 to 24.

#### <span id="page-56-1"></span>**4.6.4 TLM and HOW**

The first word of every single frame, the Telemetry word (TLM), contains a preamble sequence 8 bits in length (10001011) used for synchronization purposes, followed by 16 bits reserved for authorized users. As with all words, the final 6 bits of the telemetry word are parity bits.

The Handover word (HOW) immediately follows the telemetry word in each subframe. The Handover word is 17 bits in length (a range of values from 0 to 131071 can be represented using 17 bits) and contains within its structure the start time for the next subframe, which is transmitted as time of the week (TOW). The TOW count



begins with the value 0 at the beginning of the GPS week (transition period from Saturday 23:59:59 hours to Sunday 00:00:00 hours) and is increased by a value of 1 every 6 seconds. As there are 604,800 seconds in a week, the count runs from 0 to 100,799, before returning to 0. A marker is introduced into the data stream every 6 seconds and the HOW transmitted, in order to allow synchronization with the P code. Bit Nos. 20 to 22 are used in the handover word to identify the subframe just transmitted.

#### <span id="page-57-0"></span>**4.6.5 Subdivision of the 25 pages**

A complete navigation message requires 25 pages and lasts 12.5 minutes. A page or a frame is divided into five subframes. In the case of subframes 1 to 3, the information content is the same for all 25 pages. This means that a receiver has the complete clock values and ephemeris data from the transmitting satellite every 30 seconds.

The only difference in the case of subframes 4 and 5 is how the information transmitted is organized.

- In the case of subframe 4, pages 2, 3, 4, 5, 7, 8, 9 and 10 relay the almanac data on satellite numbers 25 to 32. In each case, the almanac data for one satellite only is transferred per page. Page 18 transmits the values for correction measurements as a result of ionospheric scintillation, as well as the difference between UTC and GPS time. Page 25 contains information on the configuration of all 32 satellites (i.e. block affiliation) and the health of satellite numbers 25 to 32.
- In the case of subframe 5, pages 1 to 24 relay the almanac data on satellite numbers 1 to 24. In each case, the almanac data for one satellite only is transferred per page. Page 25 transfers information on the health of satellite numbers 1 to 24 and the original almanac time.

#### <span id="page-57-1"></span>**4.6.6 Comparison between ephemeris and almanac data**

Using both ephemeris and almanac data, the satellite orbits and therefore the relevant coordinates of a specific satellite can be determined at a defined point in time. The difference between the values transmitted lies mainly in the accuracy of the figures. In the following table [\(Table](#page-57-2) 7), a comparison is made between the two sets of figures.

| Information                                                | Ephemeris   | Almanac     |
|------------------------------------------------------------|-------------|-------------|
|                                                            | No. of bits | No. of bits |
| Square root of the semi major axis of<br>orbital ellipse a | 32          | 16          |
| Eccentricity of orbital ellipse e                          | 32          | 16          |

<span id="page-57-2"></span>**Table 7: Comparison between ephemeris and almanac data** 

The orbit of a satellite follows an ellipse. For an explanation of the terms used in [Table](#page-57-2) 7, see [Figure](#page-58-0) 51.





#### <span id="page-58-0"></span>**Figure 51: Ephemeris terms**

Semi-major axis of orbital ellipse: *a*  Semi-minor axis of orbital ellipse: *b* 

Eccentricity of the orbital ellipse: <sup>2</sup> 22 a ba <sup>e</sup>



## <span id="page-59-0"></span>**4.7 GPS modernization**

#### <span id="page-59-1"></span>**4.7.1 New modulation procedure, BOC and MBOC**

#### **4.7.1.1 BPSK(1)-modulation**

In order for all satellites to transmit on the same frequency, the GPS signals are spread out (modulated) with a special code. For civilian Standard Positioning System (SPS) signals this code consists of a Pseudo Random Noise Code (PRN) of 1023 zeroes or ones and is known as the C/A-Code. The code, with a period of 1 millisecond, has a chiprate of 1.023Mbit/s. It is continuously repeated and due to its unique structure enables the receiver to identify from which satellite the signal originates.

The spreading (or modulation) of the data signal is achieved with an exclusive-or (EXOR) operation [\(Figure](#page-59-2) 52). The result is referred to as Binary Phase Shift Keying (BPSK(1)). The nominal or baseband frequency signal is generated by one of the atomic clocks and all satellite signals are derived from this. The nominal or baseband frequency is then spread or modulated by the C/A Code at 1 • 1.023Mbit/s.



#### <span id="page-59-2"></span>**Figure 52: With BPSK the navigation data signal is first spread by a code**



The Power Spectral Density (PSD) of BPSK(1) signals is shown in [Figure](#page-59-3) 53.

<span id="page-59-3"></span>**Figure 53: Power spectral density of BPSK(1) signals (signal strength normalized at 1 W per signal)** 



#### **4.7.1.2 Introduction of BOC-modulation**

In the futurethe base modulation for GPS and the European GALILEO systems will be a new modulation process called Binary Offset Code Modulation (BOC). With BOC the BPSK signal undergoes a further modulation[31](#page-60-0) . The modulation frequency is always a multiple of the Baseband Frequency of 1.023MHz. The properties of this modulation are communicated in a specific way. For example BOC(10,5) means that the modulation frequency is a factor of 10 times the Nominal or Baseband Frequency (10 • 1.023MHz) and the chiprate of the C/A Code is 5 times the base (5 • 1,023Mbit/s) ([Figure](#page-60-1) 54).



<span id="page-60-1"></span>**Figure 54: Block schematic of a BOC(10,5) modulator** 

With BOC the signal is better distributed over the bandwidth and the influence of opposing signal reflection (multipath) on the reception of the navigation signal is reduced in comparison to BPSK. BPSK(1) and BOC(1,1) have a minimal impact on each other when used simultaneously because their power spectrum density maxima are separated [\(Figure](#page-61-0) 55).

<span id="page-60-0"></span><sup>31</sup> Journal of the Institute of Navigation, 2002, Vol.48, No. 4, pp 227-246, Author: John W. Betz





<span id="page-61-0"></span>**Figure 55: With BPSK(1) and BOC(1,1) the signal maxima are separated (signal strength normalized at 1 W per signal)** 

#### **4.7.1.3 MBOC modulation (multiplexed BOC, MBOC(6,1,1/11)**

On July 26, 2007 the USA and EU agreed that GPS and GALILEO would use the same modulation type. The new modulation, known as MBOC(6,1,1/11), will be used with the new GPS signal L1C (L1 Civil) and for the GALILEO signal L1 OS (L1 Open Service, sometimes referred to as E1). MBOC modulation is an expansion of BOC modulation, and combines two BOC modulators and adds their signals together with different weighting ([Figure](#page-61-1) [56\)](#page-61-1).

$$
MBOC(6,1,1/11) = \frac{10}{11} \cdot BOC(1,1) + \frac{1}{11} \cdot BOC(6,1)
$$



<span id="page-61-1"></span>**Figure 56: MBOC(6,1,1/11) modulators for L1C and L1 OS** 



By combining two BOC signals, more performance is available at higher frequencies [\(Figure](#page-62-0) 57). As a result tracking performance is improved and the receiver is less susceptible to noise, interference and multipath. In order to take advantage of all of the properties, the receiver bandwidth must be approximately 20 MHz (BPSK(1) approx. 2 MHz).



<span id="page-62-0"></span>**Figure 57: Power spectral density of MBOC(6,1,1/11) compared with BPSK(1) (P = 1W per signal)** 



#### <span id="page-63-0"></span>**4.7.2 GPS modernization**

Since the activation of the GPS system in 1978 all the satellites transmit the following three signals to the Earth:

- On the L1-Frequency (1575.42MHz): one civilian signal (SPS-Service with the C/A-Signal, BPSK(1)) and one military signal (PPS-service with the P(Y)-Signal, BPSK(10))
- On the L2-Frequency (1227.60MHz): a second P(Y)-Signal for military applications.

The U.S. DoD has planned incremental improvements to the GPS signal structure ([Figure](#page-64-0) 59). For civilian applications the introduction of a second and third frequency is very important; when more frequencies can be used for establishing position, then the influence of the ionosphere on the signal travel time can be compensated or even eliminated. This compensation is possible because the transmission velocity *c [32](#page-63-1)* in the ionosphere is dependent on the frequency. In addition to the two new signals, the modernization of GPS will provide an increase in the signal strength for civilian users as well as additional capabilities for military applications.

The GPS operators have the following time plan for GPS modernization[33](#page-63-2):

By the end of 2009, eight new satellites of the type IIR-M (Block 2, Replenishment and Military) brought into orbit. IIR-M satellites transmit additional signals such as:

- A new civilian signal at a frequency of 1227.60 MHz, the so-called L2C signal.
- Further military signals at 1575.42 MHz and 1227.60 MHz: the M signals. These M signals employ BOC(10,5) modulation.

After the end of 2009, 24 satellites of the type GPS IIF (Block 2, Follow-ON) will be brought into orbit ([Figure](#page-63-4) 58, left[34](#page-63-3)). The most important characteristic of these satellites is:

 IIF satellites transmit a new civilian signal at a frequency of 1176.45 MHz (L5 Frequency). This signal is more robust than previous civilian signals and can be used in aviation during critical approaches.





<span id="page-63-4"></span>**Figure 58: GPS IIF satellite (left) und GPS III satellite (right)** 

After 2013 a new satellite generation is planned. This new series will have the designation GPS III (Block 3) [\(Figure](#page-63-4) 58, right[35](#page-63-5)). The most important characteristic of these satellites are:

 Increase of the signal strength of the M signals (= M+) through the deployment of concentrated-beam antennas.

<span id="page-63-1"></span><sup>32</sup> Approximately 300,000,000 m/s

<span id="page-63-2"></span><sup>33</sup> Ray Clore, GPS Constellation Update, TimeNav'07 Navigation Systems Status, Geneva 2007

<span id="page-63-3"></span><sup>34</sup> http://www.boeing.com/defense-space/space/gps/index.html

<span id="page-63-5"></span><sup>35</sup> http://www.aero.org/publications/crosslink/summer2002/07.html



- Improvement of the C/A signal structure of the civilian L1-Frequency. The new signal will be designated L1C.
- Transmission of an Integrity Signal
- Search and Rescue capabilities
- No built-in technical capability to produce artificial degradation (Selective Availability, SA)



#### <span id="page-64-0"></span>**Figure 59: With modernization the number of available GPS frequencies will be increased**

The GPS ground stations will also be renewed. The entire system overhaul should be complete and operational by 2021. The new signals will then be fully available to users.



## <span id="page-65-0"></span>**5 GLONASS, GALILEO and Beidou/Compass**

 *Do you want to . . .* 

- o know, how the Russian Navigation System GLONASS functions
- o understand, why GLONASS will be built up
- o know, which system Europe will be activating
- o understand, why GALILEO will provide different services
- o know, what SAR can mean for sailors
- o know, how the new modulation process BOC functions
- o know, about the system planned by the People's Republic of China

*then this chapter is for you!* 

## <span id="page-65-1"></span>**5.1 Introduction**

On December 28, 2005 the first GALILEO satellite was brought into orbit. By 2014 there will probably be three independent GNSS systems available: GPS, GLONASS and GALILEO. GPS will also be modernized in the near future and will therefore become more reliable (see Section [4.7](#page-59-0)). This chapter gives an overview of the existing GLONASS system, the future European GALILEO system, and the GNSS system planned by the People's Republic of China: Beidou/Compass.



## <span id="page-66-0"></span>**5.2 GLONASS: the Russian system**

GLONASS is an abbreviation for a GNSS system currently operated by the Russian Defense Ministry. The designation GLONASS stands for **Glo**bal **Na**vigation **S**atellite **S**ystem. The program was first started by the former Soviet Union, and is today under the jurisdiction of the Commonwealth of Independent States (CIS). The first three test-satellites were launched into orbit on October 12, 1982.

The most important facts of the GLONASS system are:



 24 planned satellites (21 standard + 3 reserve satellites). This number has never been achieved. At the beginning of 2008 there were 14 satellites in operation [\(Figure](#page-66-2) 60[36](#page-66-1)). The relatively short lifespan of the individual satellites of 3 to 4 years hampered the completion of the system.

|          |                |         |     |          | Operation |                | Life-time |            | Satellite health status | Comments               |
|----------|----------------|---------|-----|----------|-----------|----------------|-----------|------------|-------------------------|------------------------|
| Orb. pl. | Orb. slot      | RF chnl | #GC | Launched | begins    | Operation ends | (months)  | In almanac | In ephemeris (UTC)      |                        |
|          | $\overline{2}$ | 01      | 728 | 25.12.08 | 20.01.09  |                | 6.6       | $\pm$      | $+10:5913.07.09$        | In operation           |
|          | $\overline{3}$ | 05      | 727 | 25.12.08 | 17.01.09  |                | 6.6       | $\ddot{}$  | +10:59 13.07.09         | In operation           |
| 1        | 4              | 06      | 795 | 10.12.03 | 29.01.04  | 01.05.09       | 67.1      |            | $-23.2122.05.09$        | <b>Maintenance</b>     |
|          | ô.             | 01      | 701 | 10:12:03 | 08:12:04  | 18.06.09       | 67.1      | ÷          | $-09:3306.0709$         | Maintenance            |
|          | $\tau$         | 05      | 712 | 26.12.04 | 07.10.05  |                | 54.6      | $+$        | +11:31 13.07.09         | In operation           |
|          | 8              | 06      | 729 | 25.12.08 | 12.02.09  |                | 6.6       | $+$        | +12:01 13.07.09         | In operation           |
|          | 9              | $-2$    | 722 | 25.12.07 | 25.01.08  |                | 18.6      | $\pm$      | +12:0013.07.09          | In operation (L1 only) |
|          | 10             | $-7$    | 717 | 25.12.06 | 03.04.07  |                | 30.6      | $+$        | $+12:0013.07.09$        | In operation           |
|          | 11             | 00      | 723 | 25.12.07 | 22.01.08  |                | 18.6      | $+$        | +12:0013.07.09          | In operation           |
| H        | 13             | $-2$    | 721 | 25.12.07 | 08.02.08  |                | 18.6      | $+$        | +10:59 13.07.09         | In operation           |
|          | 14             | $-7$    | 715 | 25.12.06 | 03.04.07  |                | 30.6      | $\star$    | +10:59 13.07.09         | In operation           |
|          | 15             | 00      | 716 | 25.12.06 | 12.10.07  |                | 30.6      | $^{+}$     | +10:59 13.07.09         | In operation           |
|          | 17             | 04      | 718 | 26.10.07 | 04:12:07  |                | 20.6      | $+$        | $+11:00113.07.09$       | In operation           |
|          | 18             | $-3$    | 724 | 25.09.08 | 26.10.08  |                | 9.6       | $\ddot{}$  | +12:00 13.07.09         | In operation           |
|          | 19             | 03      | 720 | 26.10.07 | 25.11.07  |                | 20.6      | $\pm$      | +12:01 13.07.09         | In operation           |
|          | 20             | 02      | 719 | 26.10.07 | 27.11.07  |                | 20.6      | $\pm$      | +12:01 13.07.09         | In operation           |
| Ш        | 21             | 04      | 725 | 25.09.08 | 05.11.08  |                | 9.6       | $+$        | $+10:5913.07.09$        | In operation           |
|          | 22             | $-3$    | 726 | 25.09.08 | 13,11.08  |                | 9.6       | $+$        | $+10:5913.07.09$        | In operation           |
|          | 23             | 03      | 714 | 25.12.05 | 31.08.06  |                | 42.6      | $+$        | +10:59 13.07.09         | In operation           |
|          | 24             | 02      | 713 | 25.12.05 | 31.08.06  |                | 42.6      | $\ddot{}$  | +10:59 13.07.09         | In operation           |

<span id="page-66-2"></span>**Figure 60: Status of GLONASS as of July 2009** 

<span id="page-66-1"></span><sup>36</sup> <http://www.glonass-ianc.rsa.ru/pls/htmldb/f?p=202:20:2776707736388438778::NO>



 3 orbital levels [\(Figure](#page-67-2) 61[37](#page-67-1)) with an angle of 64.8° from the equator (this is the highest angle of all the GNSS systems and allows better reception in polar regions)



<span id="page-67-2"></span>**Figure 61: The three orbitals of GLONASS** 

- Orbital altitude of 19,100 km and orbital period of 11h15.8min
- Every GLONASS satellite transmits two codes (C/A and P-Code) on two frequencies. Every satellite transmits the same code, but at different frequencies in the vicinity of 1602MHz (L1 Band) and 1246 MHz (L2 Band). The frequencies can be determined through the following formula (k is the frequency channel of the satellite under consideration):
  - o Frequency in L1 Band: f1 = 1602 MHz + k (9/16) MHz
  - o Frequency in L2 Band: f2 = 1246 MHz + k (7/16) MHz

#### <span id="page-67-0"></span>**5.2.1 Completion of GLONASS**

The GLONASS system requires 24 functional satellites for full deployment. The CIS intends to have its system fully operational. At regular intervals a Proton-K DM-2 launches three GLONASS-M satellites (Uragan satellites) into orbit ([Figure](#page-68-0) 62[38](#page-67-3)). The M series have a lifespan of 7-8 years and transmit 2 civilian signals.

<sup>37</sup> Sergey Revnivykh, 46-th CGSIC Meeting, Fort Worth, TX, USA, September 26, 2006

<span id="page-67-3"></span><span id="page-67-1"></span><sup>38</sup> http://www.nasa.gov/multimedia/imagegallery/index.html







<span id="page-68-0"></span>**Figure 62: GLONASS-M satellite and the launch of a Proton-K-DM2 rocket** 

After 2009 the GLONASS-K series of satellites are to be launched. These are expected to have a lifespan of 10- 12 years and transmit three civilian signals. By 2009/2010 the required 24 satellites should be in orbit ([Figure](#page-68-2) [63](#page-68-2)[39](#page-68-1)).



#### <span id="page-68-2"></span>**Figure 63: GLONASS development plan**

The measured position accuracy of GLONASS should gradually approach that of GPS [\(Figure](#page-69-0) 64, [ [40](#page-68-3)]).

<span id="page-68-1"></span><sup>39</sup> Sergey Revnivykh, Munich Satellite Navigation Summit, 21-23 February, 2006

<span id="page-68-3"></span><sup>40</sup> Sergey V. Averin, European Navigation Conference GNSS-2006





<span id="page-69-0"></span>**Figure 64: By completion of development the measured positioning accuracy should equal that of GPS** 

With the modernization and deployment of GLONASS the following changes to the system can be expected:

- Renewal of the control segment.
- Modernization of the time-referencing principle.
- More Precise measurement and transmission of Ephemeris and satellite times.
- Improved stability of satellite clocks.
- The reference ellipsoid in use (Geodetic Reference Frame PZ-90) will be approximated to ITRF.
- A third civilian signal (L3) will be introduced with the GLONASS-K satellites.
- A Search and Rescue Function will be introduced with GLONASS-K.
- It is considered to also send CDMA signals on L1 later



## <span id="page-70-0"></span>**5.3 GALILEO**

#### <span id="page-70-1"></span>**5.3.1 Overview**

GALILEO is the European GNSS system being developed by the European Union (EU), in close cooperation with the European Space Agency (ESA). GALILEO will consist of a constellation of 30 satellites on 3 circular orbits at an altitude of 23,222 km above the Earth[41](#page-70-2). These satellites are to be supported by a worldwide network of ground stations.

The key arguments from the perspective of the EU for introducing GALILEO are:

To attain independence from the USA.



- To have a precise navigation system. The open service (OS) is expected to provide a precision of approximately 4 to 15m. Critical security services should have a precision of 4 to 6m. Sensitivity to multipath reception will also be reduced. This improvement will be achieved through the application of BOC and MBOC modulation. GPS will also introduce BOC and MBOC when it is modernized.
- To have a purely civilian navigation system. GALILEO is being conceived and implemented according to civilian criteria. For some services GALILEO will offer a guarantee of function.
- Providing more services. GALILEO will offer five different functions.
- Offer a Search and Rescue Function. Search and Rescue (SAR) functions are already being offered by other organizations. New with GALILEO is that an alarm can be acknowledged.
- Increased Security through Integrity Messages. GALILEO will be more reliable in that it includes an integrity message. This will immediately inform users of errors that develop. On top of this is a guarantee of availability. For the Open Service there will be neither the availability guarantee nor the integrity messages. These services are only available through EGNOS[42](#page-70-3) .
- Creation of Employment.
- Attain GNSS know-how. With GALILEO, Europe wants to acquire expertise and provide the domestic industry with a sustainable growth in competence. For example, the atomic clocks used by GALILEO are to be manufactured in Europe ([Figure](#page-70-5) 65[43](#page-70-4)).



**Figure 65: Rubidium and Hydrogen-Maser atomic clocks** 



<span id="page-70-5"></span><span id="page-70-2"></span><sup>41</sup> http://www.esa.int/esaNA/SEMJQSXEM4E\_galileo\_0.html

<span id="page-70-3"></span><sup>42</sup> **E**uropean **G**eostationary **N**avigation **O**verlay **S**ervice

<span id="page-70-4"></span><sup>43</sup> http://www.esa.int/esaNA/SEM5IURMD6E\_galileo\_0.html



 To improve the worldwide coverage of satellite signals. GALILEO will offer better reception than GPS to cities located in higher latitudes. This is possible because the GALILEO satellites have orbits at an angle of 56° from the equator as well as an altitude of 23,616km. In addition, modern GNSS receivers are able to evaluate GPS and GALILEO signals. This multiplies the number of visible satellites from which signals can be received, increasing the level of coverage and the accuracy.

#### <span id="page-71-0"></span>**5.3.2 Projected GALILEO services**

For certain critical applications GALILEO will provide information about the system integrity in order to assure the accuracy of positioning. Integrity is understood to be the reliability of information and data provided. Users will quickly (within 6 seconds) receive a warning when the system accuracy falls below the given minima. The GALILEO operators are of the opinion that these warnings are provided soon enough even for critical applications (e.g. aircraft landings). Each service provides different demands on function, accuracy, availability, integrity and other parameters.

#### **5.3.2.1 Open Service, OS**

Open Service (OS) is foreseen for mass-market applications. It provides free signals for the determination of position and time. Applications with lower demands for accuracy will use cheaper single-frequency receivers. Because the transmitted frequencies from GALILEO and GPS (L1) are the same for this application, navigation receivers will be able to combine the signals. Due to the increase in the number of satellite signals received there will be an improvement in the reception properties even in suboptimal conditions (e.g. in urban environments). OS will not be provided with System Integrity Information and the GALILEO operators make no guarantees of availability and accept no liability.

#### **5.3.2.2 Commercial Service, CS**

The Commercial Service (CS) is envisaged for market applications with higher performance demands than the OS. CS is designed to provide a variety of beneficial services to its customers on a fee for usage basis. Typical examples of these applications would be services providing high-speed data transmission, guarantees of availability, exact-time related services, as well as local correction signals for maximal positioning accuracy.

#### **5.3.2.3 Safety of Life Service, SoL**

The Safety of Life Service (SoL) is envisaged primarily for transportation applications for which an impairment of the navigation system without adequate warning could result in a life-threatening situation. The primary difference to OS is the worldwide high level of information integrity provided to such crucial applications as maritime navigation, aviation and rail traffic. This service is only accessible by using a certified double-frequency receiver. To achieve the necessary signal protection, SoL will be deployed using the aviation communication channels (L1 and E5).

#### **5.3.2.4 Public Regulated Service, PRS**

GALILEO is a civilian system that will also provide stable and access-protected services for governmental (including military) purposes. The Public Regulated Service (PRS) will be available to such clients as police and fire departments and border patrols. Access to this service is restricted and controlled by a civilian agency. The PRS must be available continually and under all conditions, especially during crisis situations where other services can be disrupted. The PRS will be independent of the other services and will be characterized by a high level of signal stability. PRS will also be protected against electronic interference and deception.

#### **5.3.2.5 Search and Rescue, SAR**

The SAR service will be used by humanitarian search and rescue services. Emergency transmitters and satellites enable the location of individual persons, crafts and vehicles in aviation, land and maritime emergencies. At the end of the 1970s, the USA, Canada, the USSR and France developed a satellite system for the location of activated distress beacons. The system is referred to as SARSAT (**S**earch **A**nd **R**escue **S**atellite-**A**ided **T**racking). The Russian name for the system is "COSPAS". The COSPAS-SARSAT system employs six LEO (Low Earth Orbit)



and five GEO (geostationary) satellites. The GALILEO-SAR service is planned to expand and improve the existing COSPAS-SARSAT system[44](#page-72-0) in the following ways:

- Almost instantaneous reception of emergency calls from any location on Earth (currently there are delays of an average of one hour).
- Exact determination of position of the distress beacons (to within meters instead of the current accuracy of 5 km).
- Improved effectiveness of the Space Segment through the availability of more satellites to overcome localized hindrances during suboptimal conditions (30 GALILEO satellites in medium orbits will supplement the existing LEO and GEO satellites of the COSPAS-SARSAT system).

GALILEO will introduce a new SAR function; the distress signal reply (from the SAR operator to the emergency transmitter radio) will begin. This should simplify rescue measures and reduce the number of false alarms. The GALILEO SAR service will be defined in cooperation with COSPAS-SARSAT, with the characteristics and functions of the service being governed by the IMO (International Maritime Organization) and ICAO (International Civil Aviation Organization).



<span id="page-72-1"></span>**Figure 66: Unlike SARSAT-COSPAS, GALILEO's Search and Rescue service also provides a reply to the distress signal** 

<span id="page-72-0"></span><sup>44</sup> http://www.cospas-sarsat.org/Status/spaceSegmentStatus.htm



#### <span id="page-73-0"></span>**5.3.3 Accuracy**

Depending on the service GALILEO will provide differing levels of accurac[y45](#page-73-1) . When dual-frequency receivers are used, the accuracy can be improved by compensating for signal travel-time errors caused by ionospheric conditions. By utilizing local measures (e.g. DGPS) the precision can be increased to within centimeters. [Table](#page-73-2) 8 shows the anticipated accuracy of 95% of all measurements.

| Service | Receiver Type    | Horizontal Positioning Accuracy | Vertical Positioning Accuracy |
|---------|------------------|---------------------------------|-------------------------------|
| OS      | Single Frequency | 15m                             | 35m                           |
|         | Double Frequency | 4m                              | 8m                            |
| CS      | Double Frequency | <1m                             | <1m                           |
| PRS     | Single Frequency | 6.5m                            | 12m                           |
| SoL     | Double Frequency | 4-6m                            | 4-6m                          |

<span id="page-73-2"></span>**Table 8: Planned positioning accuracies for GALILEO** 

<span id="page-73-1"></span><sup>45</sup> <http://www.gsa.europa.eu/go/communications-center/publications>



#### <span id="page-74-0"></span>**5.3.4 GALILEO technology**

The space segment of GALILEO will consist of 30 satellites (3 of which will be active reserve satellites). They will be placed in circular orbits at an altitude of 23,616 km providing for worldwide coverage. The satellites (each with a weight of 680 kg and dimensions of 2.7 m x 1.2 m x 1.1 m) will be evenly distributed over 3 orbits, having an angle of 56° to the equator [\(Figure](#page-74-1) 67) and an orbital period of 14 hours and 5 minutes.



**Figure 67: Constellation of the GALILEO satellites (picture: ESA-J.Huart)** 

<span id="page-74-1"></span>The GALILEO satellites are expected to have a mass of 700 kg and dimensions of 2.7 x 1.2 x 1.1 m. They are designed to have an operational lifespan of 15 years. The required power of 1500 W will be generated by large area solar panels. In order to maintain current navigation data, the satellites will be in radio contact to the ground segment of the system at regular intervals of 100 minutes.



**Figure 68: GALILEO satellite (Picture: ESA-J.Huart)** 

<span id="page-74-2"></span>The ground segment of the system will consist of a series of control centers, together with a global network of stations for various tasks. This includes the monitoring of signal integrity and the coordination of the foreseen extensive Search and Rescue services.



There are worldwide control centers planned for navigation and satellite control. The core of the ground segment will consist of two GALILEO control centers in Germany and Italy[46](#page-75-0) . The main control center will be the German Aerospace (DLR) Center at Oberpfaffenhofen. From there the control of normal operation of the 30 satellites is planned for at least 20 years. A second comprehensive control center with its own specific responsibilities for normal operation will be located at Fucino in Italy. This is also to be a backup to the main control center in the event of any problems that should arise there. Control of the positioning of the 30 satellites will be evenly divided between the European Satellite Control Center (ESA/ESOC) in Darmstadt, Germany, and the French National Space Studies Center (CNES) in Toulouse, France. A chain of about 30 Integrity Monitoring Stations (IMS) distributed worldwide will control the integrity of the satellite signals. Two control centers will evaluate the IMS information and sound an alarm in the event of an excessive deviation in position data.

It is planned that three Arianne 5 rockets, each carrying eight satellites [\(Figure](#page-75-1) 69), and three Soyuz rockets, each carrying two GALILEO satellites will transport the satellites into Middle Earth Orbit (MEO).



**Figure 69: Ariane 5 rocket delivering 8 GALILEO satellites into space (GALILEO-industries.net)** 

#### <span id="page-75-1"></span>**5.3.4.1 Signal frequencies**

Depending on the services, there will be different frequencies, modulation formats, and data transmission rates used (See [Table](#page-75-4) 9 and [Figure](#page-76-0) 70[47](#page-75-2), [48](#page-75-3)). The principal modulation formats will be BPSK and BOC. As an exception, E5a and E5b employ a slightly modified version of BOC modulation known as AltBOC.

| Band: Frequency<br>(MHz) | Signal Name | Frequency of Maxima (MHz) | Services     | Modulation     | Data Rate<br>(Bit/s) |
|--------------------------|-------------|---------------------------|--------------|----------------|----------------------|
| E5: 1191.795             | E5a (l5)    | 1176.45                   | OS, CS       | AltBOC(15, 10) | 50                   |
|                          | E5b         | 1207.14                   | OS, CS, SoL  | AltBOC(15, 10) | 250                  |
| E6: 1278.75              | E6b         | 1278.75                   | CS           | BPSK(5)        | 1000                 |
|                          | E6a         | 1268.52 & 1288.98         | PRS          | BOC(10, 5)     | -                    |
| L1: 1575.42              | L1 (L1 OS)  | 1574.661 & 1576.178       | OS, CS, SoL  | MBOC(6,1,1/11) | 250                  |
| E1, E2: 1575.42          | E2 & E1     | 1560.075 & 1590.765       | PRS          | BOC (15, 2.5)  | -                    |
| L6: 1544.5               | L6          | 1544.5                    | SAR-Downlink | -              | -                    |

#### <span id="page-75-4"></span>**Table 9: Frequency plan of GALILEO and distribution of services**

<span id="page-75-0"></span><sup>46</sup> http://www.esa.int/esaCP/SEMT498A9HE\_Austria\_0.html

<span id="page-75-2"></span><sup>47</sup> http://www.esa.int/esaNA/SEM86CSMD6E\_galileo\_0.html

<span id="page-75-3"></span><sup>48</sup> The MBOC Modulation, G. W. Hein et al., InsideGNSS Sept./Oct. 2007, Page 43





#### <span id="page-76-0"></span>**Figure 70: Frequencies with reserved bandwidths for GALILEO services**

Additionally E5a, E5b, E6 and L1 transmit a pilot channel. The pilot channel is free of navigation data and the phase is shifted at 90° to the other signals. This reduces the acquisition time of the receiver. Between L1 and E6 is the SAR-Downlink frequency.



<span id="page-76-1"></span>**Figure 71: Planned GALILEO frequencies** 



#### **5.3.4.2 Time plan**

On June 26, 2004, after many years of difficult negotiations, the USA and the EU were able to sign an agreement in Dublin. The goal of the agreement was to secure the smooth cooperation (interoperability) and compatibility of GALILEO and its American counterpart GPS.

On December 10, 2004, upon the recommendation of the European Commission, the European Council confirmed the technical characteristics of the system emphasizing the services to be offered. On July 26, 2007, the agreement concerning common civilian signals in the L1 Band was made public: The GPS L1C and the GALILEO L1F signals are to be modulated with MBOC(6,1,1/11) According to the European Commission, GALILEO should begin operation in 2013/2014.

The construction of the system will take place in four phases:

- Project definition: The goal of the definition phase was to establish the fundamental parameters and specifications of the system. This part of the overall project was completed in 2003.
- Development and tests in orbit: On December 28, 2005, the first experimental satellite GIOVE-A was launched into orbit from the Russian Cosmodrome at Baikonur in Kasachstan [\(Figure](#page-77-1) 72). GIOVE is an acronym for **G**ALILEO **I**n-**O**rbit **V**alidation **E**lement as well as being the Italian name for the planet Jupiter. The second experimental satellite (GIOVE-B) was successfully launched into orbit on April 27, 2008[49](#page-77-0) and a third (GIOVE-A2) in 2008. With the experimental satellites, the EU will secure the frequency bands for GALILEO operation and determine the orbits for the test phase satellites. These pioneer satellites will also serve in the testing of important technology, such as atomic clocks, in the hard conditions of space. GIOVE-A has two Rubidium atomic clocks (with a stability of approximately 10 nanoseconds per day) and GIOVE-B will have two passive Hydrogen-Maser atomic clocks (with a stability of less than 1 nanosecond per day) onboard.



**Figure 72: GIOVE-A and its launch on December 28, 2005 (picture ESA)** 

<span id="page-77-1"></span><span id="page-77-0"></span><sup>49</sup> http://www.giove.esa.int/



- Should the experimental phase with GIOVE-A and GIOVE-B (and possibly GIOVE-A2) be successful, four satellites will be launched into orbit in 2009 and tested[50](#page-78-1) . With this "minimum constellation", scientists can test if the satellites can deliver exact position and time data to test locations on the ground.
- Implementation and start-up of complete system: If the results of the first two phases are positive, the system will then be built up for full operation. The remaining satellites (four should already be operational) will be finished and launched into orbit by 2013/2014.
- Operation: As soon as all the satellites are in orbit the system can begin operation. At the end of the buildup phase there should be 27 operations and 3 reserve satellites in orbit. The ground stations as well as local and regional service stations will be constructed.

#### <span id="page-78-0"></span>**5.3.5 Most important properties of the three GNSS systems**

*GPS GLONASS GALILEO*  Start of development 1973 1972 2001 1st Satellite Launch Feb. 22, 1978 October 12, 1982 December 28, 2005 Number Satellites Minimum: 24 / Maximum: 32 Currently: 14 Planned: 24 + 3 passive reserves Currently: Test Satellite Planned: 27 + 3 active reserves Orbitals 6 3 3 Inclination 55° 64.8° 56° Altitude 20,180 km 19,100 km 23,222 km Orbital Period 11 hours 58 min 11 hours 15.8 min 14 hours 5 min Geodetic Data World Geodetic System 1984 (WGS 84) Parametry Zemli 1990 (PZ-90) Galileo Terrestrial Reference Frame (GTRF) Time System[51](#page-78-3) GPS-Time Glonass-Time GST (GALILEO System Time) Signal Characteristic CDMA[52](#page-78-4) FDMA[53](#page-78-5) CDMA[52](#page-78-6) Frequencies 2 frequencies, with a 3rd frequency planned 24 3 Encryption Military Signal Military Signal CS and PRS services Services 2 (civilian + military) / 4 2 (civilian + military) 5 Responsibility US Department of Defense Russian Defense Ministry Civilian Governments of the EU Integrity Signal Currently none but planned none Planned

[Table](#page-78-2) 10 lists the most important properties of the three existing (resp. planned) GNSS systems.

<span id="page-78-6"></span><span id="page-78-2"></span>**Table 10: Comparison of the most important properties of GPS, GLONASS and GALILEO (as of February 2008)** 

<span id="page-78-1"></span><sup>50</sup> http://www.esa.int/esaNA/SEMPOSXEM4E\_galileo\_0.html

<span id="page-78-3"></span><sup>51</sup> Deviation from UTC is indicated

<span id="page-78-4"></span><sup>52</sup> Code Identification: Code is different for every satellite

<span id="page-78-5"></span><sup>53</sup> Frequeny Identification: Frequeny is different for every satellite



## <span id="page-79-0"></span>**5.4 The Chinese system Beidou 1 and Beidou 2/Compass**

#### <span id="page-79-1"></span>**5.4.1 Current system: Beidou 1**

Between 2000 and 2007, China placed 4 geostationary satellites into service for the local Beidou system. The satellites (Beidou-1A to Beidou-1D) transmit over China. Position is interactively determined between stallites and navigation revceivers. The signals are transmitted and received in an iterative method:

- A signal is transmitted from the navigation receiver to the four GEO satellites.
- All four satellites receive the signal.
- All four satellites transmit the exact time of signal reception to a ground station.
- The ground station calculates the longitude and latitude of the navigation receiver and determines its elevation.
- The ground station transmits the position to the GEO satellites.
- The GEO satellites transmit the position to the navigation receiver.

#### <span id="page-79-2"></span>**5.4.2 Future system: Beidou 2/Compass**

The People's Republic of China plans a GNSS system currently known as Beidou 2 or Compass, CNSS (Compass Navigation Satellite System). The planned system will consist of five GEO and thirty MEO satellites[54](#page-79-3) . The GEO satellites will expand the entire system similar to SBAS. Beidou/Compass should offer two navigation services:

- Open Service: with position accuracy of 10m, velocity accuracy of 0.2 m/s and time precision of 50ns.
- Service for authorized users: This service should be more reliable than the Open Service.

The MEO satellites will be distributed over six orbits. The first of these satellites was launched into orbit in April of 2007 [\(Figure](#page-79-4) 73). The exact time of completion of the total system remains unclear, 2013 is targeted.



<span id="page-79-4"></span>**Figure 73: Launch of 1st Compass MEO satellite in April 2007 with ChangZheng 3A rocket** 

<span id="page-79-3"></span><sup>54</sup> http://www.china.org.cn/english/MATERIAL/188713.htm



## <span id="page-80-0"></span>**6 Calculating position**

*If you would like to . . .* 

- o understand how coordinates and time are determined
- o know what pseudorange is
- o understand why a GNSS receiver must produce a position estimate at the start of a calculation
- o understand how a non-linear equation is solved using four unknown variables
- o know what degree of accuracy is asserted by the GPS system operator

*then this chapter is for you!* 

## <span id="page-80-1"></span>**6.1 Introduction**

GNSS systems combine sophisticated satellite and radio technology to provide navigation receivers with radio signals indicating among other things the time of transmission and the identity of the transmitting satellite. Calculating the position from these signals requires mathematical operations that will be examined in this chapter.

## <span id="page-80-2"></span>**6.2 Calculating a position**

#### <span id="page-80-3"></span>**6.2.1 The principle of measuring signal travel time (evaluation of pseudorange)**

In order for a GNSS receiver to determine its position, it must receive time signals from four separate satellites (Sat 1 ... Sat 4), in order to calculate the signal travel times t1 ... t4 [\(Figure](#page-80-4) 74).



<span id="page-80-4"></span>**Figure 74: Four satellite signals must be received** 



Calculations are effected in a Cartesian, three-dimensional coordinate system with a geocentric origin [\(Figure](#page-81-0) [75\)](#page-81-0). The range of the user from each of the four satellites R1, R2, R3 and R4 can be determined with the help of signal travel times t1, t2, t3 and t4 between the four satellites and the user. As the locations XSat,YSat and ZSat of the four satellites are known, the user coordinates can be calculated.



#### <span id="page-81-0"></span>**Figure 75: Three-dimensional coordinate system**

Due to the atomic clocks onboard the satellites, the time at which the satellite signal is transmitted is known very precisely. All satellite clocks are adjusted or synchronized with each other and UTC (universal time coordinated). In contrast, the receiver clock is not synchronized to UTC and is therefore slow or fast by t0. The sign t0 is positive when the user clock is fast. The resultant time error t0 causes inaccuracies in the measurement of signal travel time and the distance R. As a result, an incorrect distance is measured that is known as pseudo distance or pseudorange PSR[55](#page-81-1) .

| <br><br>t<br>tt<br>measured<br>0 | (1a) |
|---------------------------------------|------|
|                                       |      |

$$
PSR = \Delta t_{measured} \cdot c = (\Delta t + \Delta t_0) \cdot c \tag{2a}
$$

<sup>0</sup> ctRPSR (3a)

- R: true range of the satellite from the user
- c: speed of light
- t: signal travel time from the satellite to the user
- t0: difference between the satellite clock and the user clock
- PSR: pseudorange

<span id="page-81-1"></span><sup>55</sup> Manfred Bauer: Vermessung und Ortung mit Satelliten, Wichman-Verlag, Heidelberg, 1997, ISBN 3-87907-309-0



The distance R from the satellite to the user can be calculated in a Cartesian system as follows:

$$
R = \sqrt{\left(X_{Sat} - X_{User}\right)^2 + \left(Y_{Sat} - Y_{User}\right)^2 + \left(Z_{Sat} - Z_{User}\right)^2}
$$
\n(4a)

thus (4) into (3)

$$
PSR = \sqrt{(X_{\text{Sat}} - X_{\text{User}})^2 + (Y_{\text{Sat}} - Y_{\text{User}})^2 + (Z_{\text{Sat}} - Z_{\text{User}})^2} + c \cdot \Delta t_0
$$
 (5a)

In order to determine the four unknown variables (t0 , XUser, YUser and ZUser), four independent equations are necessary.

The following is valid for the four satellites (i = 1 ... 4):

$$
PSR_i = \sqrt{\left(X_{Sat\_i} - X_{User}\right)^2 + \left(Y_{Sat\_i} - Y_{User}\right)^2 + \left(Z_{Sat\_i} - Z_{User}\right)^2} + c \cdot \Delta t_0
$$
\n(6a)

#### <span id="page-82-0"></span>**6.2.2 Linearization of the equation**

The four equations in 6a produce a non-linear set of equations. In order to solve the set, the root function is first linearized according to the Taylor model, the first part only being used ([Figure](#page-82-1) 76).



<span id="page-82-1"></span>**Figure 76: Conversion of the Taylor series** 

Generally (with 
$$
\Delta x = x - x_0
$$
):  $f(x) = f(x_0) + \frac{f'}{\pi}(x_0) \cdot \Delta x + \frac{f''}{2!}(x_0)^2 \cdot \Delta x + \frac{f'''}{3!}(x_0)^3 \cdot \Delta x + ...$   
\nSimplified (1st part only):  $f(x) = f(x_0) + f'(x_0) \cdot \Delta x$  (7a)

In order to linearize the four equations (6a), an arbitrarily estimated value x0 must therefore be incorporated in the vicinity of x. This means that instead of calculating XUser , YUser and ZUser directly, an estimated position XTotal, YTotal and ZTotal is initially used ([Figure](#page-83-0) 77).





#### <span id="page-83-0"></span>**Figure 77: Estimating a position**

The estimated position includes an error produced by the unknown variables x, y and z.

$$
X_{\text{User}} = X_{\text{Total}} + \Delta x
$$
  
\n
$$
Y_{\text{User}} = Y_{\text{Total}} + \Delta y
$$
  
\n
$$
Z_{\text{User}} = Z_{\text{Total}} + \Delta z
$$
 (8a)

The distance RTotal from the four satellites to the estimated position can be calculated in a similar way to equation (4a):

$$
R_{Total\_i} = \sqrt{\left(X_{Sat\_i} - X_{Total}\right)^2 + \left(Y_{Sat\_i} - Y_{Total}\right)^2 + \left(Z_{Sat\_i} - Z_{Total}\right)^2}
$$
(9a)

Equation (9a) combined with equations (6a) and (7a) produces:

$$
PSR_i = R_{Total_i} + \frac{\partial (R_{Total_i})}{\partial x} \cdot \Delta x + \frac{\partial (R_{Total_i})}{\partial y} \cdot \Delta y + \frac{\partial (R_{Total_i})}{\partial z} \cdot \Delta z + c \cdot \Delta t_0
$$
\n(10a)

After carrying out partial differentiation, this gives the following:

$$
PSR_i = R_{Total_i} + \frac{X_{Total} - X_{Sat_i}}{R_{Total_i}} \cdot \Delta x + \frac{Y_{Total} - Y_{Sat_i}}{R_{Total_i}} \cdot \Delta y + \frac{Z_{Total} - Z_{Sat_i}}{R_{Total_i}} \cdot \Delta z + c \cdot \Delta t_0
$$
\n(11a)



#### <span id="page-84-0"></span>**6.2.3 Solving the equation**

After transposing the four equations (11a) (for i = 1 ... 4) the four variables (x, y, z and t0) can now be solved according to the rules of linear algebra:

$$
\begin{bmatrix}\nPSR_1 - R_{Total-1} \\
PSR_2 - R_{Total-2} \\
PSR_3 - R_{Total-3} \\
PSR_4 - R_{Total-4} \\
\end{bmatrix} = \begin{bmatrix}\n\frac{X_{Total} - X_{Sat-1}}{R_{Total} - X_{Sat-2}} & \frac{Y_{Total} - Y_{Sat-1}}{R_{Total} - Y_{Sat-2}} & \frac{Z_{Total} - Z_{Sat-1}}{R_{Total} - Z_{Sat-2}} & c \\
\frac{X_{Total} - X_{Sat-2}}{R_{Total} - X_{Sat-3}} & \frac{Y_{Total} - Y_{Sat-2}}{R_{Total} - Y_{Sat-3}} & \frac{Z_{Total} - Z_{Sat-2}}{R_{Total} - Z_{Sat-3}} & c \\
\frac{X_{Total} - X_{Sat-3}}{R_{Total} - X_{Sat-4}} & \frac{Y_{Total} - Y_{Sat-4}}{R_{Total} - Y_{Sat-4}} & \frac{Z_{Total} - Z_{Sat-4}}{R_{Total} - Z_{sat-4}} & c \\
\frac{X_{Total} - X_{Sat-1}}{R_{Total} - X_{sat-4}} & \frac{Y_{Total} - Y_{Sat-1}}{R_{Total} - Y_{sat-4}} & \frac{Z_{Total} - Z_{Sat-1}}{R_{Total} - Z_{sat-4}} & c \\
\frac{X_{Total} - X_{Sat-2}}{R_{Total} - X_{Sat-2}} & \frac{Y_{Total} - Y_{Sat-2}}{R_{Total} - Y_{Sat-2}} & \frac{Z_{Total} - Z_{Sat-2}}{R_{Total} - Z_{Sat-2}} & c \\
\frac{X_{Total} - X_{Sat-3}}{R_{Total} - X_{Sat-3}} & \frac{Y_{Total} - Y_{Sat-3}}{R_{Total} - Y_{Sat-3}} & \frac{Z_{Total} - Z_{Sat-3}}{R_{Total} - Z_{Sat-4}} & c \\
\frac{X_{Total} - X_{Sat-4}}{R_{Total} - X_{Sat-4}} & \frac{Y_{Total} - Y_{Sat-4}}{R_{Total} - X_{sat-4}} & \frac{Z_{Total} - Z_{Sat-4}}{R_{Total} - Z_{sat-4}} & c\n\end{bmatrix}
$$
\n(13a)

The solution of x, y and z is used to recalculate the estimated position XTotal , YTotal and ZTotal in accordance with equation (8a).

$$
X_{\text{Total\_New}} = X_{\text{Total\_Old}} + \Delta X
$$
\n
$$
Y_{\text{Total\_New}} = Y_{\text{Total\_Old}} + \Delta y
$$
\n
$$
Z_{\text{Total\_New}} = Z_{\text{Total\_Old}} + \Delta Z
$$
\n(14a)

The estimated values XTotal\_New , YTotal\_New and ZTotal\_New can now be entered into the set of equations (13a) using the normal iterative process, until error components x, y and z are smaller than the desired error (e.g. 0.1 m). Depending on the initial estimation, three to five iterative calculations are generally required to produce an error component of less than 1 cm.

#### <span id="page-84-1"></span>**6.2.4 Summary**

In order to determine a position, the user (or the user's receiver software) will either use the last measurement value, or estimate a new position and calculate error components (x, y and z) down to zero by repeated iteration. This then gives:

$$
X_{\text{User}} = X_{\text{Total\_New}}
$$
  
\n
$$
Y_{\text{User}} = Y_{\text{Total\_New}}
$$
  
\n
$$
Z_{\text{User}} = Z_{\text{Total\_New}}
$$
  
\n(15a)

The calculated value of t0 corresponds to receiver time error and can be used to adjust the receiver clock.



## <span id="page-85-0"></span>**6.3 Determination of travel time in detail**

#### <span id="page-85-1"></span>**6.3.1 Time systems**

For determining signal travel times from satellites to receivers, different time systems are important (see Section [3.5\)](#page-39-0).

- **UTC**, Coordinated Universal Time (see Section [3.5.2](#page-39-2))
- **GPS Time**, the time system for GPS system. GPS time varies from UTC by a whole number of seconds (for the year 2008 the difference was 14 seconds) plus a fraction of a second less than 1μs. The difference between GPS time and UTC and the current characteristics of this difference are communicated in the Navigation Message (Subframe 4, Page 18).
- **Satellite Time**, the onboard time for each of the individual satellites. The specific difference between the satellite time and GPS time and the current characteristics of this difference are also communicated in the Navigation Message (Subframe 1, Page 1-25).
- **Receiver Time**, the time within the GPS receiver. This time is usually determined from an internal quartz oscillator and is different from GPS time and/or UTC. The difference T0 is unknown at the start of operation of a GPS receiver, but can be reduced after a few measurements.

#### <span id="page-85-2"></span>**6.3.2 Determination of travel time in detail**

The following section discusses the required approach for determining signal travel time. In order to maintain an overview of the approach, the description of the procedure is greatly simplified. Travel time is used to calculate the distance or range (R) from the satellite to the receiver. [Figure](#page-85-3) 78 depicts the linear dependence of range (R) to travel time (shown are the first two microseconds).



<span id="page-85-3"></span>**Figure 78: Determination of range (R) based on the signal travel time t (c= speed of light)** 

#### <span id="page-85-4"></span>**6.3.2.1 Phase 1: Determination of signal arrival time using correlation**

The GPS receiver receives the signals from one or more satellites. For every signal a correlation takes place. The correlation procedure described here is for a single signal, but must be done for every satellite signal.

Since the number (x) of the transmitting satellite is not known by the receiver at the time of signal reception, it generates various PRN-codes (x= 1…32). These codes are shifted with respect to time until a PRN-code coincides with the correlation maximum for time and signal form for satellite signal x ([Figure](#page-86-0) 79: correlation maximum achieved by shifting time t2).





#### <span id="page-86-0"></span>**Figure 79: Correlation by searching the maxima**

The necessary time shift tKo and the receiver time mark (e.g. millisecond intervals) determine the arrival time of the observed satellite signals (time given in Receiver Time). In [Figure](#page-86-1) 80 the measured arrival time amounts to exactly 2h 25min 35.7293".



#### <span id="page-86-1"></span>**Figure 80: Determination of the satellite signal arrival time**

#### **6.3.2.2 Phase 2: reconstruction of data and/or navigation message**

The correlation maximum is sequentially searched and maintained, i.e., the satellite signal and the PRN-sequence generated by the receiver are continually synchronous. The time-shifted PRN sequence (C/A-Code) is linked to the satellite signal, and thus the Navigation Message data is reconstructed (see [Figure](#page-87-0) 81).





<span id="page-87-0"></span>**Figure 81: Reconstruction of the navigation message**

#### **6.3.2.3 Phase 3: Determination of transmission time**

Every subframe of the Navigation Message (see also Section [4.6](#page-55-0)) begins with an 8-bit preamble. The preamble in the Telemetry Word (TLM) is a defined pattern with the structure 10001011. This bit sequence is repeated every 6 seconds. The transmission time (in Satellite Time) of the preamble is included in the Handover Word (HOW) of the previous subframe with the 17-bit Time of Week (TOW) Message in the Navigation Message.



<span id="page-87-1"></span>**Figure 82: Telemetry Word (TLM) and Handover Word (HOW) of the navigation message**

The GPS receiver now searches the Navigation Message for the 10001011 pattern. Since this pattern can potentially appear in other parts of the Navigation Message, conditions for other parameters also need to be met such as:

- Two logical 0s must appear 51 and 52 bits after the end of the assumed preamble (the two last parity bits in the HOW are set to 0).
- The parity beginning 16 bits after the assumed preamble (parity of the TLM Word) must be correct.
- The two bits before the assumed preamble must be 0 (the last parity bits of every word at the end of a subframe are set to 0).
- The time given in the TOW message (17 Bit) beginning 22 bits after the end of the assumed preamble must be approximately correct. Since time information is repeatedly provided every 6 seconds, there are no great accuracy requirements for receiver time measurement.



 The preamble of the next subframe must begin exactly 300 bits following the start of the assumed preamble.

If the system achieves a confirmation then all of the controls no longer need to be performed.

The transmission time in the first bits of the preamble are provided in the Navigation Message in the TOW Message of the previous frame. This time is given in Satellite Time, but thanks to the information in the Navigation Message it can be translated into GPS Time.

#### <span id="page-88-0"></span>**6.3.3 Determination of travel time error**

If the preamble is validated, the arrival time of the first bits in the preamble is measured (see [6.3.2.1\)](#page-85-4). This time is given in Receiver Time. Since Receiver Time and GPS Time are not identical, but rather differ by a value of t0, an incorrect travel time is measured. [Figure](#page-88-2) 83 depicts the procedure of determining the travel time error (c.f. [Figure](#page-85-3) [78\)](#page-85-3). The two different time scales used are:

- GPS Time for the signal transmission time
- Receiver Time for the signal arrival time.

Depicted is also the difference between Receiver Time and GPS Time t.

tmeasured = t + t0 = Arrival TimeReceiver Time – Transmission TimeGPS Time

t: true signal travel time: Satellite to Receiver

t0: Difference between Receiver Time and GPS Time



<span id="page-88-2"></span>**Figure 83: Determination of travel time error**

#### <span id="page-88-1"></span>**6.3.4 Additional influences affecting travel time**

The signal travel time from a satellite to a receiver is not only dependent on the distance, but is also influenced by a number of other physical factors. In the document "Navstar GPS Space Segment/Navigation User Interfaces[56](#page-88-3)" examples of the use of corrections taking many parameters into account is presented ([Figure](#page-89-2) 84).

<span id="page-88-3"></span><sup>56</sup> INTERFACE SPECIFICATION, IS-GPS-200, Revision D, IRN-200D-001,7 March 2006, page 92



<span id="page-89-3"></span>

<span id="page-89-2"></span>**Figure 84: Example of determination of corrected travel time**

## <span id="page-89-0"></span>**6.4 Error analysis and DOP**

#### <span id="page-89-1"></span>**6.4.1 Introduction**

Up until now, the magnitude of error has not been taken into consideration in calculations. In GNSS technology, different causes can contribute to the total error:

- Satellite clocks: although, for example, every GPS satellite is provided with four highly accurate atomic clocks, a time error of only 10ns is enough to produce a positioning error in the order of 3m.
- Satellite orbits: generally speaking, the actual value of the satellite position is only known up to approximately 1 ... 5m.
- Speed of light: the signals from the satellites travel at the speed of light. These slow down when crossing the ionosphere and troposphere and cannot, therefore, be assumed to be a constant. This deviation from the normal speed of light creates an error in the calculated position.
- Signal travel time error measurement: the GNSS receiver is only able to determine the time of the incoming satellite signal with limited accuracy.
- Multipath: The error level is further increased by the reception of reflected signals.
- Satellite geometry: determination of position is more difficult if the four reference satellites being used for measurement are close together. The effect of satellite geometry on measurement accuracy is referred to as **DOP** (**D**ilution **O**f **P**recision) (See [Table](#page-90-1) 11).

There are various causes of measurement error. Table 1 shows the extent of horizontal position errors from different source.

By implementing corrective measures **DGPS** (**D**ifferential **GPS**, see Section [7.6\)](#page-117-0) the number of error sources can be eliminated or reduced.



| Error cause               | Error without DGPS |
|---------------------------|--------------------|
| Ephemeris data            | 1.5m               |
| Satellite clocks          | 1.5m               |
| Effect of the ionosphere  | 3.0m               |
| Effect of the troposphere | 0.7m               |
| Multipath reception       | 1.0m               |
| Effect of the receiver    | 0.5m               |
| Total RMS value           | 4.0m               |

<span id="page-90-1"></span>**Table 11: Error causes (typical ranges)** 

#### <span id="page-90-0"></span>**6.4.2 The influence of satellite geometry on accuracy, the DOP value**

#### **6.4.2.1 Introduction**

The precision of positioning with GPS navigation depends on the one hand on the precision of the individual pseudorange measurements and on the other hand on the geometric configuration of the satellites used. This configuration is expressed in terms of a scalar value, which is referred to in navigation literature as DOP (Dilution of Precision).

The DOP value describes the weakening of precision and is therefore a factor or measure of the constellation dependent imprecision. If the DOP values are high (because for example all visible satellites are close to one another), then the anticipated imprecision will be higher.

There are a variety of DOP terms used:

- GDOP (Geometric-DOP): Describes the influence of satellite geometry on the position in 3D space and time measurement.
- PDOP (Positional-DOP): Describes the influence of satellite geometry on the position in 3D space.
- HDOP (Horizontal-DOP): Describes the influence of satellite geometry on the position along upon a plane (2D)
- VDOP (Vertical-DOP): Describes the influence of satellite geometry on height (1D).
- TDOP (Time-DOP): Describes the influence of satellite geometry on time measurement.

The influence of satellite geometry on imprecision is demonstrated in [Figure](#page-91-0) 85. When both satellites are widely separated (figure left) the position error (area in red) is smaller. If the satellites are close to one another (figure right), then the area of error is more spread out. This is valid when the uncertainty for determining the position, known as the Range Error (R-E: yellow and blue areas), is the same for both satellites. R (R1 and R2) refers to the measured distance of the satellites to the user (pseudorange).





<span id="page-91-0"></span>**Figure 85: The flatter the angle with which the circles with ranges R1 and R2 intersect, the higher the DOP value** 

#### **6.4.2.2 Illustration of the causes of the DOP-value**

The precision of the calculated position for GPS in Navigation mode depends on the one hand on the precision of the individual pseudorange measurements and on the other hand the geometric configuration of the satellites used (expressed with the DOP value). The positional accuracy is reduced when the four satellites used for measurement are close together. The precision of the measurement is proportionally dependent on the DOP value. This means that when the DOP value doubles, the positional error increases by a factor of two.

Generally speaking, the total position error is a cumulation of other errors multiplied by the DOP value:

*(Position error through other influences) • (DOP value)* 

The DOP value can be seen as the reciprocal value of the volume of a tetrahedron made up of the position of the satellites and the user [\(Figure](#page-92-0) 86). As the volume of the tetrahedron increases, the magnitude of the DOP value (and thus the imprecision) decreases.





<span id="page-92-0"></span>**Figure 86: The larger the enclosed volume, the smaller the DOP value** 



#### **6.4.2.3 Practical implications of DOP values**

In open and unobstructed areas, satellite coverage is so favorable that DOP values seldom exceed 3 (see [Figure](#page-93-0) [87\)](#page-93-0).



<span id="page-93-0"></span>**Figure 87: DOP values and the number of satellites over an open area during a 24-hour period** 

In mountainous areas, forests and urban areas DOP values play an important role in planning measurement projects. This is because there are often phases when the satellites have very unfavorable geometric constellations. Thus, it is necessary to plan measurements according to the DOP values (e.g. HDOP), or to assess the achievable precision given that various DOP values can occur in a matter of a few minutes.

With all planning and evaluation tools provided by the leading GPS device manufacturers, DOP values are observable. [Figure](#page-94-0) 88 shows an example of HDOP values in an area where no obstruction of satellite visibility (referred to as shadow) is present (max. HDOP < 1.9). [Figure](#page-94-1) 89 shows an example of HDOP values in an area with strong obstruction of satellite visibility. In this location the maximum HDOP value of 20 is frequently exceeded. The area from 180° to 270° is shadowed by a high building and from 270° to 180° the obstructive effects of mountains are visible.





<span id="page-94-0"></span>**Figure 88: 24-hour HDOP values, in area with with no shadow/obstruction of satellite visibility (max. HDOP < 1.9)** 



<span id="page-94-1"></span>**Figure 89: 24-hour HDOP values, in area with with strong shadow/obstruction of satellite visibility (max. HDOP > 20)** 

With massive shadowing only occasional opportunities (e.g. between 11:00 and 12:30h, see [Figure](#page-94-1) 89) with optimal DOP values (<2) are available for determining the position. Time periods with DOP values above 6 (e.g. between 9:00 and 9:30h) should be avoided for precise measurements.

The DOP values can be estimated based on the current satellite constellation [\(Figure](#page-95-0) 90 and [Figure](#page-95-1) 91).







<span id="page-95-0"></span>**Figure 90: DOP values with unfavorable satellite constellation** 



<span id="page-95-1"></span>**Figure 91: DOP values with favorable satellite constellation** 

#### **6.4.2.4 Total error**

Measurement accuracy is proportionally dependent on the DOP value. This means that when the DOP value doubles, the positioning error is also twice as large.

Generally applicable: Error (1Total RMS Value DOP Value

Error 
$$
(2\sigma) = 2 * Total RMS Value * DOP Value
$$

In [Table](#page-96-0) 12 the One-Sigma value (1= 68%) and the Two-Sigma value (2= 95%) are given. The values are valid for a medium satellite constellation of HDOP = 1.3. The implementation of suitable correction methods (such as using several linked receivers (**D**ifferential **GPS**, **DGPS** (see Chapter [7](#page-99-0))) can eliminate or reduce the number of error sources (typically to 1...2m, One-Sigma value).



| Type of error                                      | Error |
|----------------------------------------------------|-------|
| Total RMS value (filtered, i.e. slightly averaged) | 4.0m  |
| Horizontal error (1 Sigma (68%) HDOP=1.3)          | 6.0m  |
| Horizontal error (2 Sigma (95%) HDOP=1.3)          | 12m   |

#### <span id="page-96-0"></span>**Table 12: Total error in HDOP = 1.3**

Usually the accuracy is better than shown. Long-term measurements available from the US-Federal Aviation Administration have shown that in 95% of all measurements the horizontal error was less than 7.4m and the vertical error was less than 9.0m. The time period for the measurement was always 24 hours.

The U.S. DoD maintains that their system will provide standard civilian applications with a horizontal accuracy of 13m, a vertical accuracy of 22 m and a time accuracy of ~40ns. By employing additional measures such as DGPS, longer measuring time, and special measuring techniques (phase measurement), positional accuracy can be increased to within a centimeter.

#### **6.4.2.5 Calculating the DOP value**

The individual DOP values are determined, based upon the positions of the satellites and the GPS user.

In [Figure](#page-96-1) 92 Ri (I = 1…4) is the distance from a satellite to the user.





#### <span id="page-96-1"></span>**Figure 92: Description of satellite and user position with cartesian coordinates**

With the details in [Figure](#page-96-1) 92 the so-called position matrix can be produced.





$$
P = \begin{bmatrix} \frac{X_{User} - X_{Sat\_1}}{R_1} & \frac{Y_{User} - Y_{Sat\_1}}{R_1} & \frac{Z_{User} - Z_{Sat\_1}}{R_1} & 1\\ \frac{X_{User} - X_{Sat\_2}}{R_2} & \frac{Y_{User} - Y_{Sat\_2}}{R_2} & \frac{Z_{User} - Z_{Sat\_2}}{R_2} & 1\\ \frac{X_{User} - X_{Sat\_3}}{R_3} & \frac{Y_{User} - Y_{Sat\_3}}{R_3} & \frac{Z_{User} - Z_{Sat\_3}}{R_3} & 1\\ \frac{X_{User} - X_{Sat\_4}}{R_4} & \frac{Y_{User} - Y_{Sat\_4}}{R_4} & \frac{Z_{User} - Z_{Sat\_4}}{R_4} & 1 \end{bmatrix}
$$

Through the transpostion ([] <sup>T</sup> ), multiplication (•) and inversion ([] -1) of the position matrix, the DOP matrix D can be calculated (through transposition the row vectors become column vectors[57](#page-97-0), [58](#page-97-1)):

$$
D = \left[ \begin{bmatrix} P \end{bmatrix}^T \bullet \begin{bmatrix} P \end{bmatrix} \right]^{-1}
$$

According to the rules of matrix calculation, the 16 elements of the DOP matrix receive the following designations:

$$
D = \begin{bmatrix} D_{11} & D_{12} & D_{13} & D_{14} \\ D_{21} & D_{22} & D_{23} & D_{24} \\ D_{31} & D_{32} & D_{33} & D_{34} \\ D_{41} & D_{42} & D_{43} & D_{44} \end{bmatrix}
$$

The individual DOP values are then defined from the matrix elements of matrix D:

<span id="page-97-0"></span><sup>57</sup> http://www.scilab.org/contrib/index\_contrib.php?page=download&category=MANUALS

<span id="page-97-1"></span><sup>58</sup> http://en.wikipedia.org/wiki/Transpose



$$
GDOP = \sqrt{D_{11} + D_{22} + D_{33} + D_{44}}
$$
  
\n
$$
PDOP = \sqrt{D_{11} + D_{22} + D_{33}}
$$
  
\n
$$
HDOP = \sqrt{D_{11} + D_{22}}
$$
  
\n
$$
VDOP = \sqrt{D_{33}}
$$
  
\n
$$
TDOP = \sqrt{D_{44}}
$$

<span id="page-98-0"></span>Some DOP values can be directly determined from others, e.g.:

<sup>2</sup> <sup>2</sup> *GDOP PDOP TDOP*

44

If more than four satellites are visible, the GPS receiver calculates the position from the four satellites with the best DOP values.



# <span id="page-99-0"></span>**7 Improved GPS: DGPS, SBAS, A-GPS and HSGPS**

*If you would like to . . .* 

- o know which kinds of errors influence the accuracy of determining position
- o know what DGPS means
- o know how correction values are determined and relayed
- o understand how the D-signal corrects erroneous positional measurements
- o know what DGPS services are available in Central Europe
- o know what EGNOS and WAAS mean
- o know how A-GPS functions

*then this chapter is for you!* 

## <span id="page-99-1"></span>**7.1 Introduction**

Although originally intended for military purposes, the GPS system is used today primarily for civil applications, such as surveying, navigation, positioning, measuring velocity, determining time, monitoring etc, etc, etc. GPS was not initially conceived for applications demanding high precision, security measures, or for use indoors.

- To increase the accuracy of positioning, Differential-GPS (D-GPS) was introduced.
- To improve the accuracy of positioning and the integrity (reliability, important for security applications) SBAS (Satellite Based Augmentation System) such as EGNOS and WAAS was implemented.
- To improve the sensitivity in closed rooms, or respectively to reduce the acquisition time, Assisted-GPS (A-GPS) services were offered.
- The reception properties of GPS receivers are continually being improved and increase the sensitivity of the receivers with High Sensitivity-GPS (HSGPS).

## <span id="page-99-2"></span>**7.2 Sources of GPS error**

The positioning accuracy of approx. 12m (for 95% of all measurements at HDOP of 1.5) discussed in the previous chapter is not sufficient for all applications. In order to achieve an accuracy of one meter or better, additional measures are necessary. Different sources can contribute to the total error in GPS measurements. These causes and the total error are listed in [Table](#page-90-1) 11. These values should be viewed as typical averages and can vary from receiver to receiver.

The error causes are studied in more detail below:

- **Ephemeris data**: the satellite position at the time of the signal emission is, as a general rule, only known to be accurate up to approx. 1...5m.
- **Satellite clocks:** although each satellite includes four atomic clocks, the time base contains offsets. A time error of 10ns is reached at an oscillator stability of approx. 10-13 per day. A time error of 10ns immediately results in a distance error of about 3m.
- **Effect of the ionosphere:** the ionosphere is an atmospheric layer situated between 60 to 1000 km above the Earth's surface. The gas molecules in the ionosphere are heavily ionized. The ionization is mainly caused by solar radiation (only during the day!). Signals from the satellites travel through a vacuum at the speed of light. In the ionosphere the velocity of these signals slows down and therefore can no longer be viewed as



constant. The level of ionization varies depending on time and location, and is strongest during the day and at the equator. If the ionization strength is known, this effect can, to a certain extent, be compensated with geophysical correction models. Furthermore, given that the change in the signal velocity is frequency dependent, this can additionally be corrected by the use of dual-frequency GPS receivers.

- **Effect of the troposphere:** the troposphere is the atmospheric layer located between 0...15 km above the Earth's surface. The cause of the error here is the varying density of the gas molecules and the air humidity. The density decreases as the height increases. The increase in density or humidity retards the speed of the satellite signals. In order to correct this effect, a simple model is used which is based on the standard atmosphere (P) and temperature (T):
  - o H = height [m]
  - o T = 288.15 K 6.510-3 h [K]
  - o P = 1013.25 mbar (T/288.15 K)5,256 [mbar]
- **Multipath:** GPS signals can be reflected from buildings, trees, mountains etc. and make a detour before arriving at the receiver. The signal is distorted due to interference. The effect of multipath can be partially compensated by the selection of the measuring location (free of reflections), a good antenna and the measuring time [\(Figure](#page-100-1) 93).



#### <span id="page-100-1"></span>**Figure 93: Effect of the time of measuring on the reflections**

- **Effect of the receiver:** further errors are produced due to GPS receiver measurement noise and time delays in the receiver. Advanced technologies can be used to reduce this effect.
- **Effect of the satellite constellation, including shadowing (DOP):** this effect was discussed in detail in Section [6.4.2.](#page-98-0)

## <span id="page-100-0"></span>**7.3 Possibilities for reducing the measurement error**

Reducing the effect of measurement errors can considerably increase the positioning accuracy. Different approaches are used for reducing the measurement error and are often combined. The process most frequently used is:



**Compensation of ionospheric influences through dual-frequency measurement:** The ionosphere has the greatest influence on measurement errors (see Section [7.2](#page-99-2)). If a radio signal is transmitted through the ionosphere, it is slowed down more heavily at lower frequencies. By using two different signal frequencies, e.g. L1/L2, the effect of the ionosphere can largely be compensated for. Since GALILEO and GPS (following modernization) will transmit the civil signal on at least two frequencies, the principle of compensation will be more closely adhered to.

Signal transmission times increase depending on the strength of ionization. The ionospheric effect on transmission time increases with lower frequencies. The influence on the transmission time occurs as a square of the frequency.

If the signal is slower, then a longer distance between the satellite and the receiver is assumed. The measurement error of this pseudorange (PSR) and its dependence on frequency and ionization strength is presented in [Figure](#page-101-0) 94.



<span id="page-101-0"></span>**Figure 94: PSR Measurement error and its dependence on Ionization and Frequency** 

Since every satellite signal is transmitted through a different area of ionization, the PSR measurement error is different for every satellite. It is therefore important to compensate for these errors. If a satellite transmits navigation information on two frequencies (f1 and f2) it is possible to determine the PSR measurement error ( ) for frequency f1 by using the following formula *PSR*<sup>1</sup> [59](#page-101-1):

$$
\Delta PSR_1 = \left(\frac{(f_2)^2}{(f_2)^2 - (f_1)^2}\right) \bullet (PSR_1 - PSR_2)
$$

PSR1 and PSR2 are the measured pseudoranges for frequencies f1 and f2. The calculated measurement error ( ) can be used for the correction of the PSRi value in equation 13a (Section *PSRi* [6.2.3\)](#page-84-0).

<span id="page-101-1"></span><sup>59</sup> Elliot D. Kaplan, Understanding GPS, Second Edition, Artech House, Page 313





$$
\begin{bmatrix}\n\Delta x \\
\Delta y \\
\Delta z \\
\Delta t_0\n\end{bmatrix} = \begin{bmatrix}\n\frac{X_{Total} - X_{Sat\_1}}{R_{Total\_1}} & \frac{Y_{Total} - Y_{Sat\_1}}{R_{Total\_1}} & \frac{Z_{Total} - Z_{Sat\_1}}{R_{Total\_1}} & c \\
\frac{X_{Total} - X_{Sat\_2}}{R_{Total\_2}} & \frac{Y_{Total} - Y_{Sat\_2}}{R_{Total\_2}} & \frac{Z_{Total} - Z_{Sat\_2}}{R_{Total\_2}} & c \\
\frac{X_{Total} - X_{Sat\_3}}{R_{Total\_3}} & \frac{Y_{Total} - Y_{Sat\_3}}{R_{Total\_3}} & \frac{Z_{Total} - Z_{Sat\_3}}{R_{Total\_3}} & c \\
\frac{X_{Total} - X_{Sat\_4}}{R_{Total\_4}} & \frac{Y_{Total} - Y_{Sat\_4}}{R_{Total\_4}} & \frac{Z_{Total} - Z_{Sat\_4}}{R_{Total\_4}} & c\n\end{bmatrix} \begin{bmatrix}\nPSR_1 - \Delta PSR_1 - R_{Total\_1} \\
PSR_2 - \Delta PSR_2 - R_{Total\_2} \\
PSR_3 - \Delta PSR_3 - R_{Total\_3} \\
PSR_4 - \Delta PSR_4 - R_{Total\_4}\n\end{bmatrix}
$$

- **Geophysical correction models**. This is used primarily for the compensation of the effect of the ionosphere and troposphere. Correction factors are only useful if applied to a specified and limited area.
- **Differential GPS (DGPS):** by comparing with one or several base stations, various errors can be corrected. The evaluation of the correction data available from these stations can take place either during post processing or in Real Time (RT). Real-time solutions (RT DGPS) require data communication between the base station and the mobile receiver. DGPS employs a variety of different processes:
  - o RT DGPS, normally based on the RTCM SC104 standard
    - DGPS derived from signal travel time delay measurement (Pseudorange corrections, achievable accuracy approx. 1 m)
    - DGPS derived from the phase measurement of the carrier signal (achievable accuracy approx. 1 cm)
  - o Post-processing (subsequent correction and processing of the data).
  - **Choice of location and of the measurement time** for improving the "visibility" or line of sight contact to the satellites (See explanation on DOP [6.3\)](#page-89-3).

#### <span id="page-102-0"></span>**7.3.1 DGPS based on signal travel time delay measurement**

The principle of DGPS based on signal travel time measurement (pseudorange or C/A code measurement) is very simple. A GPS reference station is located at a known and accurately surveyed point. The GPS reference station determines its GPS position using four or more satellites. Given that the position of the GPS reference station is exactly known, the deviation of the measured position to the actual position and more importantly the measured pseudorange to each of the individual satellites can be calculated. These variations are valid for all the GPS receivers around the GPS reference station in a range of up to 200 km. The satellite pseudoranges can thereby be used for the correction of the measured positions of other GPS receivers [\(Figure](#page-103-0) 95). The differences are either transmitted immediately by radio or used afterwards for correction (See post-processing, Section [7.3.3\)](#page-105-1) after carrying out the measurements.

It is important that the correction be based on the satellite pseudorange values and not the specific deviation in position of the GPS reference station. Deviations are based on the pseudoranges to the specific satellites, and these vary depending on position as well as which satellites are used. A correction based simply on the positional deviation of the reference base station fails to take this into account and will lead to false results.





<span id="page-103-0"></span>**Figure 95: Principle of DGPS with a GPS base station** 

#### **7.3.1.1 Detailed description of how it runs**

The error compensation is carried out in three phases:

- 1. Determination of the correction values at the reference station
- 2. Transmission of the correction values from the reference station to the GPS user
- 3. Compensation for the determined pseudoranges to correct the calculated position of the GPS user

#### **7.3.1.2 Definition of the correction factors**

A reference station with exactly known position measures the L1 signal travel time to all visible GPS satellites [\(Figure](#page-104-0) 96) and uses these values to calculate its position relative to the satellites. These measured values will typically include errors. Since the real position of the reference station is known, the actual distance (nominal value) to each GPS satellite can be calculated. The difference between the nominal and the measured distances can be calculated by a simple subtraction and corresponds to a correction factor. These correction factors are different for all GPS satellites and are also applicable to GPS users within a radius of several hundred kilometers.





#### <span id="page-104-0"></span>**Figure 96: Determination of the correction factors**

#### **7.3.1.3 Transmission of the correction values**

Given that the correction values can be used by other GPS users within a large area to compensate for the measured pseudoranges, they are immediately transmitted by using a suitable medium (telephone, radio, etc) [\(Figure](#page-104-1) 97).



<span id="page-104-1"></span>

#### **7.3.1.4 Correction of the measured pseudoranges**

After receiving the correction values, the GPS user can compensate for the pseudoranges in order to determine the actual distance to the satellites [\(Figure](#page-105-2) 98). These actual distances can then be used to calculate the exact position of the user. All errors, which are not caused by receiver noise and multipath reception, can be overcome in this way.





<span id="page-105-2"></span>**Figure 98: Correction of the measured pseudoranges** 

#### <span id="page-105-0"></span>**7.3.2 DGPS based on carrier phase measurement**

The DGPS accuracy of 1 meter achieved by measuring signal travel time is not enough for some requirements such as solving survey problems. In order to obtain a precision within millimeters, the carrier-phase of the satellite signal must be evaluated.

The wavelength of the carrier wave is approx. 19 cm. The distance to a satellite can be determined as shown below [\(Figure](#page-105-3) 99).



#### <span id="page-105-3"></span>**Figure 99: Principle of the phase measurement**

Since N is unknown the phase measurement is ambiguous. By observing several satellites at different times and continually comparing results from user and reference station receivers (during or after the measurement), the position can be calculated using an extensive series of mathematical equations to an accuracy of a few millimeters.

#### <span id="page-105-1"></span>**7.3.3 DGPS post-processing (signal travel time and phase measurement)**

DGPS post-processing implements the determined correction factors by using appropriate software *after* carrying out field measurements. Reference data is either obtained from private reference stations or from publicly accessible server systems. The disadvantage is that problems with the field data (e.g. poor satellite reception, damaged files etc.) are sometimes not detected until after the correction factors are calculated and broadcast, necessitating a repetition of the whole process.



#### <span id="page-106-0"></span>**7.3.4 Transmitting the correction data**

DGPS services collect data from reference stations and transmit it by radio to the mobile receiver. There are a variety of channels available over which to broadcast this correction data. Each of these broadcasting systems possesses individual radio-technical properties and frequency ranges which have specific advantages and disadvantages for DGPS ([Table](#page-106-1) 13).

| Broadcasting system                                       | Frequency<br>range    | Advantages                                                     | Disadvantages                                                       | Transmission<br>of correction<br>data                                 |
|-----------------------------------------------------------|-----------------------|----------------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------|
| Long and medium wave<br>broadcasters (LW, MW)             | 100 - 600 KHz         | Extensive range of<br>transmission<br>(1000km)                 | Low bit rates                                                       | RTCM SC104                                                            |
| Maritime radio beacon                                     | 283 - 315 KHz         | Extensive range of<br>transmission<br>(1000km)                 | Low bit rates                                                       | RTCM SC104                                                            |
| Aviation radio beacon                                     | 255 - 415 KHz         | Extensive range of<br>transmission<br>(1000km)                 | Low bit rates                                                       | RTCM SC104                                                            |
| Short wave broadcaster<br>(KW)                            | 3 – 30 MHz            | Extensive range of<br>transmission                             | Low bit rates, quality<br>depends on the time and<br>frequency      | RTCM SC104                                                            |
| VHF and FM                                                | 30 - 300 MHz          | High bit rates, joint<br>use of the existing<br>infrastructure | Range of transmission<br>limited by the quasi<br>optical conditions | RTCM SC104                                                            |
| Mobile<br>communication/telephone<br>networks (GSM, GPRS) | 450, 900, 1800<br>MHz | Joint use of<br>existing networks                              | Limited range of<br>transmission,<br>synchronization problem        | RTCM SC104                                                            |
| GEO satellite system                                      | 1.2 – 1.5 GHz         | Extensive area<br>coverage                                     | High investment cost                                                | RTCM SC104<br>(for MSAT,<br>Omnistar,<br>Landstar,<br>Starfire)       |
|                                                           |                       |                                                                |                                                                     | RTCA DO-229C<br>(for SBAS<br>systems such as<br>WAAS, EGNOS,<br>MSAS) |

<span id="page-106-1"></span>**Table 13: Transmission process of the differential signal (for code and phase measurement)** 

Many countries provide their own systems for transmitting correction data. A comprehensive description of all these systems is beyond the scope of this compendium. Some individual systems will be described below.



#### <span id="page-107-0"></span>**7.3.5 DGPS classification according to the broadcast range**

The various DGPS services available are categorized according to the broadcast range of the correction signals:

- Local DGPS: Local Area Augmentation System (LAAS). These are sometimes called Ground Based Augmentation Systems (GBAS).
- Regional DGPS
- Wide Area DGPS (WADGPS) or Satellite Based Augmentation Systems (SBAS): Employ satellites to transmit DGPS correction data. In these cases not just single reference stations, but whole networks of reference stations are used.

#### <span id="page-107-1"></span>**7.3.6 Standards for the transmission of correction signals**

DGPS broadcasters transmit the signal travel time and carrier-phase corrections. For most GBAS and some satellite based WADGPS systems (LandStar-DGPS, MSAT, Omnistar or Starfire) the DGPS correction data is transmitted according to the RTCM SC-104 standard. Typically the receiver must be equipped with a service specific decoder in order to receive and process the data.

Satellite Based Augmentation Systems such as WAAS, EGNOS and MSAS use the RTCA DO-229 standard. Since RTCA frequencies and data formats are compatible with those of GPS, modern GNSS receivers can calculate RTCA data without the use of additional hardware, in contrast to RTCM [\(Figure](#page-108-1) 100).

[Table](#page-107-2) 14 lists the standards used for DGPS correction signals as well as the references pertaining specifically to GNSS.

| Standard     |                                                                            | References pertaining to GNSS                                                                                                                 |
|--------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| RTCM SC 104: | Radio Technical Commission for Maritime<br>Services, Special Committee 104 | • RTCM Recommended Standards for<br>Differential Navstar GPS Service, Version 2.0 and<br>2.1                                                  |
|              |                                                                            | • Recommended Standards for Differential<br>GNSS Service, Version 2.2 and 2.3                                                                 |
| RTCA:        | Radio Technical Commission for<br>Aeronautics                              | • DO-229C, Minimum Operational Performance<br>Standards for Global Positioning System/Wide<br>Area Augmentation System Airborne<br>Equipment. |

<span id="page-107-2"></span>**Table 14: Standards for DGPS correction signals** 





<span id="page-108-1"></span>**Figure 100: Comparison of DGPS systems based on RTCM and RTCA standards** 

#### **7.3.7 Overview of the different correction services**

<span id="page-108-0"></span>



## <span id="page-109-0"></span>**7.4 DGPS services for real-time correction**

#### <span id="page-109-1"></span>**7.4.1 Introduction**

All correction data is transmitted to the user receiver reception area via a suitable broadcaster (AM, Shortwave, FM, GSM, internet, satellite communication, etc). In North America and Europe, the correction signals from multiple public DGPS services can be received. Depending on the service, an annual license fee may be required or a one-time fee is charged when purchasing the DGPS receiver.

Worldwide there are far too many ground-based DGPS services, also known as Ground Based Augmentation Services (GBAS), to describe them all in detail here. In many countries there are multiple systems offered. For this reason a few selected services will be introduced in the following sections. In addition, a few services offering more or less global coverage (satellite based) will be examined in more detail.

#### <span id="page-109-2"></span>**7.4.2 Terrestrial services based on RTCM SC-104**

- **SAPOS:** (German Surveying and Mapping Administration Satellite Positioning Service) is a DGPS service in permanent operation. This service is available in all of Germany. The basis of the system is a network of GPS reference stations. For real-time correction values the data is transmitted using FM radio, longwave, GSM and their own 2-meter band (VHF) frequencies. FM radio transmitters broadcast the correction data signals in RASANT (Radio Aided Satellite Navigation Technique) format. This is a conversion of RTCM 2.0 for data transmission into the Radio Data System (RDS) format used by FM sound broadcasting. SAPOS includes four services with different features and accuracies[60](#page-109-3):
  - o SAPOS EPS: Real-Time Positioning Service
  - o SAPOS HEPS: High-Precision Real-Time Positioning Service
  - o SAPOS GPPS: Geodetic Precision Positioning Service
- **Swipos:** (Swiss Positioning Service[61](#page-109-4)) distributes correction data using mobile telephone networks/GSM or via Internet/GPRS. Swipos offers two services:
  - o Swipos-NAV (Service with precision within meters)
  - o Swipos-GIS/GEO (Service with precision within centimeters)
- **Radio Beacons:** radio beacons are navigation installations distributed worldwide primarily along the coasts. These transmit DGPS correction signals at a frequency of approximately 300kHz. The signal bit rate varies depending on the broadcaster between 100 and 200 bit per second. For example, in Australia the AMSA (Australian Maritime Safety Authority) has built up a full DGPS network of 16 stations, completed in December of 2002. The stations transmit at frequencies between 294 - 320 kHz and can be received within a range of about 275 km ([Figure](#page-110-1) 101[62](#page-109-5)).

<span id="page-109-3"></span><sup>60</sup> http://www.sapos.de/

<span id="page-109-4"></span><sup>61</sup> http://www.swisstopo.admin.ch/internet/swisstopo/en/home/products/services/swipos.html

<span id="page-109-5"></span><sup>62</sup> http://www.amsa.gov.au/Publications/Fact\_sheets/DGPS\_Fact\_Sheet.pdf





<span id="page-110-1"></span>**Figure 101: Radio beacon coverage for Australia** 

#### <span id="page-110-0"></span>**7.4.3 Satellite services based on RTCM SC-104**

Several geostationary satellites continually transmit correction data. Under names such as Omnistar, Starfire and MSAT a variety of services are available.

**Omnistar** transmits correction data over 6 GEO satellites ([Figure](#page-110-4) 102[63](#page-110-2)). The three services recquire a fee and users must have a special receiver/decoder in order to use them[64](#page-110-3) . Omnistar transmits its information over the L-Band (1-2 GHz) to the Earth. The reference ground stations are distributed throughout the world.



<span id="page-110-4"></span>**Figure 102: Coverage areas of the 6 Omnistar satellites (two zones overlap each other)** 

<span id="page-110-2"></span> <sup>63</sup> http://www.seastar.co.uk/coverage.html

<span id="page-110-3"></span><sup>64</sup> http://www.omnistar.com/



**Starfire**, property of NavCom Technology, Inc., also transmits correction data over 6 GEO satellites ([Figure](#page-111-3) [103](#page-111-3)[65](#page-111-2)). The service recquires a fee and users must have a special receiver/decoder in order to use it. Starfire transmits its information over the L-Band (1-2 GHz) to the Earth. The reference ground stations are distributed throughout the world.



<span id="page-111-3"></span>**Figure 103: Coverage area of Starfire** 

## <span id="page-111-0"></span>**7.5 Wide Area DGPS (WADGPS)**

#### <span id="page-111-1"></span>**7.5.1 Satellite based augmentation systems, SBAS (WAAS, EGNOS)**

#### **7.5.1.1 Introduction**

Satellite Based Augmentation Systems (SBAS) are used to enhance the GPS, GLONASS and GALILEO (once it is operational) functions. Correction and integrity data for GPS or GLONASS is broadcast from geostationary satellites over the GNSS frequency.

#### **7.5.1.2 The most important SBAS functions**

SBAS is a considerable improvement compared to GPS because the positioning accuracy and the reliability of the positioning information are improved. SBAS, in contrast to GPS, delivers additional signals broadcast from different geostationary satellites.

- **Increased positioning accuracy using correction data:** SBAS provides differential correction data with which the GNSS positioning accuracy is improved. First of all the ionospheric error, which arises due to the signal delays in the ionosphere, has to be corrected. The ionospheric error varies with the time of day and is different from region to region. To ensure that the data is continentally valid, it is necessary to operate a complicated network of earth stations in order to be able to calculate the ionospheric error. In addition to the ionospheric values, SBAS passes on correction information concerning the satellite position location (Ephemeris) and time measurement.
- **Increased integrity and security:** SBAS monitors each GNSS satellite and notifies the user of a satellite error or breakdown within a short warning latency of 6s. This yes/no information is only transmitted if the quality of the received signals remains below specific limits.

<span id="page-111-2"></span> <sup>65</sup> http://www.navcomtech.com/StarFire/



**Increased availability through the broadcasting of navigation information:** SBAS geostationary satellites emit signals, which are similar to the GNSS signals although missing the accurate time data. A GNSS receiver can interpret position from these signals using a procedure known as "pseudoranging".

#### <span id="page-112-0"></span>**7.5.2 Overview of existing and planned systems**

Although all Satellite Based Augmentation Systems (SBAS) include very large regions (e.g. Europe) it must be ensured that they are compatible with each other (interoperability) and that the SBAS providers cooperate with each other and agree on their approach. Compatibility is guaranteed by using the RTCA DO-229C standard. At the current time, compatible SBAS systems are currently in operation or development for the areas identified in [Figure](#page-114-1) 107.

**North America (WAAS, Wide Area Augmentation System):** the US Federal Aviation Administration (FAA) is leading the development of the Wide Area Augmentation System (WAAS), which covers the United States, Canada and Mexico ([Figure](#page-112-3) 104[66](#page-112-1)). WAAS operates over two satellites (Anik F1R und Galaxy 15) located at 133°W and 107°W[67](#page-112-2).



<span id="page-112-3"></span>**Figure 104: WAAS area of coverage** 

- **Europe (EGNOS, European Geostationary Overlay Service):** The European group of three comprising ESA, the European Union and EUROCONTROL, is developing EGNOS. It is intended for the region of the European Civil Aviation Conference (ECAC). As of February 2009, the system had not yet been definitively released for operation and may not be used in high security applications (e.g. aviation). The current transmission status of the EGNOS satellites can be viewed under[68](#page-112-4). Certification is planned by the end of 2009.
- **Japan (MSAS, Multifunctional Satellite Based Augmentation System and QZSS, Quazi Zenith Satellite System):** MSAS uses two GEO satellites and for QZSS it is planned to use up to three HEO satellites (highly-inclined elliptical orbits, [Figure](#page-113-0) 105). The two MSAS signals are transmitted by the MTSAT-1R and MTSAT-2 satellites[69](#page-112-5) . As of the beginning of 2008, MTSAT-1R was operational. **QZSS** supplements

<span id="page-112-2"></span><span id="page-112-1"></span><sup>66</sup> http://www.faa.gov/about/office\_org/headquarters\_offices/ato/service\_units/techops/navservices/gnss/waas/news/

<sup>67</sup> http://www.faa.gov/about/office\_org/headquarters\_offices/ato/service\_units/techops/navservices/gnss/waas/

<span id="page-112-4"></span><sup>68</sup> [http://esamultimedia.esa.int/docs/egnos/estb/IMAGEtech/imagetech\\_realtime.htm](http://esamultimedia.esa.int/docs/egnos/estb/IMAGEtech/imagetech_realtime.htm)

<span id="page-112-5"></span><sup>69</sup> http://www.jma.go.jp/jma/jma-eng/satellite/index.html



GPS through the transmission of GPS signals and integrity or correction signals70. The especially high HEO constellation of QZSS ensures that at least one satellite in the vicinity of its zenith (75° … 90° Elevation) is visible in Japanese space (Figure 10671). This should improve positioning in narrow urban canyons. The first QZSS satellite should be operational by the end of 2010.





<span id="page-113-0"></span>**Figure 105: Satellite orbits and ground tracks of QZSS** 



<span id="page-113-2"></span>**Figure 106: QZSS satellite orbits, ground tracks and elevation over Tokyo** 

- **India (GAGAN, GPS and GEO Augmentated Navigation):** The Indian Space Research Organization (ISRO [ [72](#page-113-1)]) is developing a system, which will be compatible with the other SBAS systems. In 2008, GAGAN test signals were transmitted by Inmarsat 4F1 IOR. After 2009, GAGAN will begin operation using the GEO satellite GSAT-4. The new GAGAN satellite will be located at 82° E.
- **Russia (SDCM, System for Differential Correction and Monitoring):** Russia plans a system for its territory to control GPS and GLONASS signals using various monitoring stations. GEO satellites will transmit correction and integrity signals for GPS and GLONASS over Russian territory.

 <sup>70</sup> http://qzss.jaxa.jp/is-qzss/index\_e.html

<span id="page-113-1"></span><sup>71</sup> Quasi Zenith Satellite System Navigation Service Interface Specifications for QZSS Draft

<sup>72</sup> http://isro.gov.in/





#### <span id="page-114-1"></span>**Figure 107: Position and coverage of WAAS, EGNOS, GAGAN and MSAS**

The geostationary satellites ([Table](#page-114-4) 1[573](#page-114-2)) broadcast their signals from an altitude of approx. 36,000km above the equator in the direction of the area of use. The position of some SBAS satellites is not known at this time. The Pseudo Random Number (PRN) for each satellite has been allocated[74](#page-114-3) . The broadcasting frequency of the signals is the same as GPS (L1, 1575.42 MHz)., which means that no additional investment in receiver hardware is needed in order to receive signals from SBAS GEO satellites.

| Service | Satellite description          | Position | PRN |
|---------|--------------------------------|----------|-----|
| WAAS    | Intelsat Galaxy XV             | 133°W    | 135 |
| WAAS    | TeleSat Anik F1R               | 107,3°W  | 138 |
| EGNOS   | Inmarsat 3F2 AOR-E             | 15,5° W  | 120 |
| EGNOS   | Artemis                        | 21,5° W  | 124 |
| EGNOS   | Inmarsat 3F5 IOR-W             | 25° E    | 126 |
| MSAS    | MTSAT-1R                       | 140° E   | 129 |
| MSAS    | MTSAT-2                        | 145° E   | 137 |
| GAGAN   | Inmarsat 4F1 IOR (Testbetrieb) | 64° E    | 127 |

<span id="page-114-4"></span>**Table 15: The GEO satellites used by WAAS, EGNOS and MSAS (as of February 2008)** 

#### <span id="page-114-0"></span>**7.5.3 Overview of planned RNSS**

RNSS is the abbreviation of Regional Navigation Satellite System. RNSS systems are the counterpart to GPS, GLONASS and GALILEO, which together are designated as GNSS (Global Navigation Satellite System) systems and make possible worldwide navigation and positioning. RNSS systems can only be used for navigation in limited areas (e.g. individual countries). The transition from SBAS to RNSS is quite fluid, therefore the planned

<span id="page-114-2"></span><sup>73</sup> http://celestrak.com/NORAD/elements/sbas.txt

<span id="page-114-3"></span><sup>74</sup> http://www.losangeles.af.mil/shared/media/document/AFD-070530-036.pdf



RNSS systems are introduced together with SBAS. The following regional satellite navigation systems are planned:

- India (IRNSS, Indian Regional Navigation Satellite System): INRSS is to be an autonomous navigation system consisting of three GEO satellites and four geosynchronous satellites with an inclination of 29° to the equatorial plane[75](#page-115-1) . The system should be functional after 2014.
- Japan (QZSS, Quazi Zenith Satellite System): This system is a supplement to GPS and has already been introduced (see Section [7.5.2](#page-112-0)).

#### <span id="page-115-0"></span>**7.5.4 SBAS system description**

The complex ground segment is composed of several reference base-stations, ground control centers and 2 to 3 satellite earth stations [\(Figure](#page-115-2) 108). Each system uses its own designation for its stations. [Table](#page-115-3) 16 below compares the designations.

| General description      | EGNOS designation                                      | WAAS designation               | MSAS designation                                             |
|--------------------------|--------------------------------------------------------|--------------------------------|--------------------------------------------------------------|
| Reference Base Station   | RIMS: Reference and<br>Integrity Monitoring<br>Station | WRS: Wide Area Base<br>station | GMS: Ground Monitor<br>Station                               |
| Control Center           | MCC: Mission Control<br>Center                         | WMS: WAAS Master<br>Station    | MCS: Master Control<br>Station                               |
| Satellite Ground Station | NLES: Navigation Land<br>Earth Station                 | GES: Ground Earth<br>Station   | NES/GES: Navigation<br>Earth Station/Ground<br>Earth Station |

<span id="page-115-3"></span>**Table 16: Designation of the SBAS stations** 



<span id="page-115-2"></span>**Figure 108: Principle of all Satellite Based Augmentation Systems SBAS** 

<span id="page-115-1"></span><sup>75</sup> http://www.isro.org/newsletters/spaceindia/aprsep2006/Satnavindustry.htm



- **Reference Station:** in the SBAS area there are several reference base stations, which are networked to each other. The base stations receive the GNSS signals. They are exactly surveyed with regard to their position. Each base station determines the deviation between the actual and calculated positions relative to the satellites (the pseudorange). This data is then transmitted to a control center.
- **Control Center:** the control centers carry out the evaluation of the correction data from the reference base stations, determine the accuracy of all GNSS signals received by each base station, detect inaccuracies, possibly caused by turbulence in the ionosphere, and monitor the integrity of the GNSS system. Data concerning the variations are then integrated into a signal and transmitted via distributed satellite earth stations.
- **Satellite Ground Station:** these stations broadcast signals to the different geostationary satellites.
- **GEO satellites:** the SBAS GEO (geostationary) satellites receive the signals from the satellite ground stations and broadcast them to the GNSS users. Unlike the GNSS satellites, these GEO satellites do not have onboard signal generators but rather are equipped with transponders, which relay the signals processed on the ground and transmitted to them. The signals are transmitted to earth on the GNSS-L1 frequency (1575.42MHz). The SBAS signals are received and processed by suitably equipped GNSS receivers.

#### <span id="page-116-0"></span>**7.5.5 Satellite DGPS services using RTCM SC-104**

Several geostationary satellites continuously broadcast correction data worldwide. Below some of these services are listed. These services use the RTCM SC-104 standard and require a special decoder.

- **MSAT:** developed by the National Research Council of Canada, this service broadcasts the Canada-Wide DGPS (CDGPS) signals using two geostationary satellites.
- **Omnistar** (Fugro Group) and **LandStar-DGPS,** (Thales Company), independently broadcast correction data via 6 GEO satellites [\(Figure](#page-116-1) 109). The services must be paid for and the user must have access to a special receiver / decoder for using the service. Omnistar and Landstar broadcast their information in Lband (1-2 GHz) to earth. Base stations are distributed worldwide. The geostationary satellites are located in the central latitude deep over the horizon (10° ... 30°). Line-of-sight contact is required in order to establish radio contact.



#### <span id="page-116-1"></span>**Figure 109: LandStar-DGPS and Omnistar illumination zone**

**Starfire** Property of NavCom Technology, Inc., broadcasts correction data via 3 Inmarsat GEO satellites. The service has to be paid for and the user must have access to a special receiver / decoder in order to



use the service. Starfire broadcasts its information in L-band (1-2 GHz) to earth. The respective base stations are distributed throughout the whole world. The service is available worldwide over the range of 76° latitude.

## <span id="page-117-0"></span>**7.6 Achievable accuracy with DGPS and SBAS**

[Table](#page-117-3) 17 shows typically achievable positioning accuracy with and without DGPS/SBAS.

| Error cause and type                      | Error<br>without<br>DGPS/SBAS | Error with<br>DGPS/SBAS |
|-------------------------------------------|-------------------------------|-------------------------|
| Ephemeris data                            | 1.5m                          | 0.1m                    |
| Satellite clocks                          | 1.5m                          | 0.1m                    |
| Effect of the ionosphere                  | 3.0m                          | 0.2m                    |
| Effect of the troposphere                 | 0.7m                          | 0.2m                    |
| Multipath reception                       | 1.0m                          | 1.4m                    |
| Effect of the receiver                    | 0.5m                          | 0.5m                    |
| Total RMS value                           | 4.0m                          | 1.2m                    |
| Horizontal error (1-Sigma (68%) HDOP=1.3) | 6.0m                          | 1.8m                    |
| Horizontal error (2-Sigma (95%) HDOP=1.3) | 12.0m                         | 3.6m                    |

<span id="page-117-3"></span>**Table 17: Positioning accuracy without and with DGPS/SBAS** 

## <span id="page-117-1"></span>**7.7 Assisted-GPS (A-GPS, AGPS)**

#### <span id="page-117-2"></span>**7.7.1 Introduction**

An ever-increasing number of devices are coming onto the market combining mobile radio functions (e.g. GSM, UMTS, etc.) with satellite navigation, for instance GPS (see [Figure](#page-118-1) 110). Such a combination is often used for Location Based Services (LBS). It can be assumed that these devices are not always in operation. This is especially true when positioning is determined by GPS, since the power consumption of a GPS receiver limits battery operation time.







<span id="page-118-1"></span>**Figure 110: Mobile receiver and block diagram showing integrated GPS module** 

Because the GPS device is only infrequently in operation it is probable that no information is available regarding satellite position. After being inactive for 2 or more hours the orbital data of the satellites must first be downloaded in order to start up. A GPS receiver normally requires at least 18-36 seconds in order to obtain the orbital data and calculate the first position (this time is referred to as the Time to First Fix: TTFF). Under difficult reception conditions (e.g., in urban areas where tall buildings block direct sight to the sky) the calculation of the first position can require minutes to be completed, if at all. This slow start-up is a system-inherent limitation of GPS, which cannot be overcome with improved receiver technology.

In the absence of the orbital data, the GPS receiver must carry out a complete search procedure in order to find the available satellites, download the data and calculate the position. The search for the approximately 30 GPS satellites in the code-frequency domain is very time consuming. The integration time per level in the codefrequency domain normally requires at least 1ms (1 C/A-code period). Should the frequency range be broken into 50-Hz steps (i.e., the frequency interval amounts to (2 x 6000 / 50 Hz = 240 Hz) then there can be as many as 1023 x 50 = 51,150 positions (bins) to be searched for (requiring 51 seconds). See also Section [7.8.](#page-126-0)

## <span id="page-118-0"></span>**7.7.2 Principle of A-GPS**

A rapid determination of position and measurement during periods of weak signals can be obtained by providing additional satellite orbit data and other GPS information. This information is made available through other communications channels, for example via GSM, GPRS, CDMA or UMTS. This application is known as Aiding and is used in Assisted-GPS (A-GPS, or AGPS). A-GPS is a function or service that uses Aiding-Data in order to speed up the determination of position. The GPS receiver obtains Aiding-Data via a mobile communications network or directly over the Internet. The Aiding-Data includes information over such things as:

Satellite constellation (Almanac)

- Precise orbital data (Ephemeris, orbits)
- Time information
- Doppler frequency and frequency-offset (error) of the GPS receiver

With the availability of this Aiding-Data the GPS receiver can very quickly determine position, even under poor signal conditions. With weak signals this is often the only way to get a position fix. Depending on the complexity and completeness of the Aiding-Data the reduction of the start-up time can be significant. The start-up time remains dependent on the strength of the GPS-Signal. It is generally true that the higher the availability and the accuracy of aiding information, the faster is the start-up time.

[Figure](#page-119-0) 111 shows the approximate start-up time (Time to First Fix, TTFF) as various Aiding-Data are used[76](#page-118-2) .

<span id="page-118-2"></span><sup>76</sup> GPS-World, September 2005: Chris Carver: High Sensitivity versus Assisted Techniques





#### <span id="page-119-0"></span>**Figure 111: Time to First Fix (TTFF) with different Aiding-Data as a function of signal strength**

A mobile transmitter station with integrated GPS device still requires sight to at least four satellites. To use A-GPS the GPS receivers require an interface through which to receive the Aiding-Data.

The highest time saving occurs through eliminating the reception time for the orbital data. In addition to this, the search area can be limited when the Doppler frequency and frequency offset of the GPS receiver are known [\(Figure](#page-119-1) 112). This causes the signal acquisition to be accelerated, which saves additional time.



#### <span id="page-119-1"></span>**Figure 112: Acceleration of the search procedure with A-GPS by reducing the search area**



#### <span id="page-120-0"></span>**7.7.3 Reference network**

A-GPS Aiding-Data is produced by collecting satellite information over an extensive and worldwide network of monitoring stations, which continually and accurately monitor satellite movements. A high performance server uses this data to predict satellite movements over the next days. An example of such a network is the one developed by the International GNSS-Service (IGS, or International GPS-Service[77](#page-120-2)), which operates a permanent worldwide network ([Figure](#page-120-3) 113).



<span id="page-120-3"></span>**Figure 113: IGS reference stations (as of November 2007) with approx. 340 active stations** 

#### <span id="page-120-1"></span>**7.7.4 A-GPS network**

A typical A-GPS system, as illustrated in the below block diagram [\(Figure](#page-121-1) 114), consists of a global reference network of GPS receivers, a central server that distributes Aiding-Data, and A-GPS capable receivers (the GPS end devices). The GPS receivers of the global reference network receive the relevant satellite information and forward it to the server. The server calculates the Aiding-Data and transmits it (over a mobile communications network or over the Internet) upon request to the GPS end devices, which in turn can more quickly determine their first position.

<span id="page-120-2"></span><sup>77</sup> http://igscb.jpl.nasa.gov/





#### <span id="page-121-1"></span>**Figure 114: Assisted-GPS system**

The Aiding-Data is collected from a worldwide network of GPS-Reference Stations (GPS Reference Network).

Two different techniques are employed to use the Aiding-Data:

- With the **Online Principle** the Aiding-Data is directly downloaded from a server as needed in real- time. This information is only valid for a limited time. (e.g. AssistNow Online by u-blox AG)
- With the **Offline Principle** the Aiding-Data (generally predetermined Ephemeris or Almanac information) is downloaded from a server and stored in the GNSS device prior to the application. The data can remain valid for up to several days. As needed the stored data can be utilized in order to accelerate the start-up. (e.g. AssistNow Offline by u-blox AG)

#### <span id="page-121-0"></span>**7.7.5 A-GPS with online aiding data (real-time A-GPS)**

With Online A-GPS (Real-time Principle) the Aiding Data is directly downloaded from the server as needed and are only valid for a short time ([Figure](#page-122-1) 115). The disadvantage of this principle is the relatively slow connection time (GPRS, for example, requires up to 30 seconds) or inadequate availability of Internet Access Points.





<span id="page-122-1"></span>**Figure 115: With Online A-GPS, Aiding-Data is continuously transmitted** 

Function of Online A-GPS (see [Figure](#page-122-1) 115):

- The Mobile Station of the GPS receiver requests Aiding-Data from the Location Server. In order to make this functionality possible, an aiding program (the so-called client) must be installed in the Mobile Station.
- The Server transmits the Aiding-Data (approx. 1 to 3 KB) to the Client of the mobile station. The Client then passes this data on to the GPS module.
- The GPS module uses the Aiding-Data to determine position.

#### <span id="page-122-0"></span>**7.7.6 A-GPS with offline aiding data (predicted orbits)**

With Offline A-GPS the GPS receiver is provided with predetermined orbital data (Predicted Orbits). The orbital data is determined through information from the reference network and the current Almanac [\(Figure](#page-122-2) 116). The receiver stores this information, and the connection to the server is terminated. The next time the GPS receiver starts up the stored information is used to determine the current orbital information for navigation. Consequently, it is no longer necessary to wait until all of this information has been downloaded from the satellites and the receiver can immediately begin navigating. Depending on the provider, the Aiding Data can be valid for 10 to 20 days, although it should be considered that the resulting positional accuracy decreases with time.



<span id="page-122-2"></span>**Figure 116: From the Almanac data precise orbital data (True Orbits) are calculated** 



Function of Offline A-GPS [\(Figure](#page-122-2) 116):

- The Client requests Aiding-Data from the Location Server
- The Server sends the Aiding-Data (< 10 100 KB) to the Client
- The Client passes this data on to the GPS module
- The GPS module can use this Aiding-Data up to 14 days. During this time, no new connection to the Server is necessary.

#### <span id="page-123-0"></span>**7.7.7 Architectures**

In order to transmit the Aiding-Data, there are two different architectures:

- Control Plane Architecture
- User Plane Architecture

#### <span id="page-123-1"></span>**7.7.8 Control plane architecture**

With Control Plane based A-GPS, the server and end-device communicate over communication signal channels (SS7, Signalling System) in mobile radio and switching networks (e.g. GSM). For this, the necessary interfaces and protocols are available throughout the entire network. Control Plane architecture requires comprehensive alterations of the network infrastructure ([Figure](#page-123-7) 117) based on 3GPP Location Services Standards. These standards are available from the 3GPP organization[78](#page-123-2). Individually described standards can be downloaded[79](#page-123-3), [80](#page-123-4), [81](#page-123-5), [82](#page-123-6) .



<span id="page-123-7"></span>**Figure 117: With Control Plane Architecture the mobile network must be altered** 

<span id="page-123-2"></span><sup>78</sup> http://www.3gpp.org/

<span id="page-123-4"></span><span id="page-123-3"></span><sup>79</sup> TS 03.71, Location Services (LCS), Functional description Stage 2,

<sup>80</sup> TS 04.31, Location Services (LCS), Mobile Station – Serving Mobile Location Centre, Radio Resource LCS Protocol

<span id="page-123-5"></span><sup>81</sup> TS 44.035, Location Services (LCS), Broadcast network assistance for Enhanced Observed Time Difference and Global Positioning System positioning methods,

<span id="page-123-6"></span><sup>82</sup> TS 04.35, Location Services (LCS), Broadcast network assistance for Enhanced Observed Time Difference and Global Positioning System positioning methods



#### <span id="page-124-0"></span>**7.7.9 User plane architecture**

User Plane is an A-GPS-System where communications between the Location Server and the end device take place over a standard data connection such as GPRS or UMTS. For the integration of User Plane solutions, the existing protocols and interfaces of the mobile radio and switching networks are used. Additionally, a Location Server is integrated into the mobile network.

The server communicates directly with the mobile end devices over an IP Connection (Internet Protocol Connection), for which the radio and switching networks require no modification [\(Figure](#page-124-2) 118). The Open Mobile Alliance (OMA), an association of Mobile Network service providers and manufacturers, has produced a Standard for location technology (OMA-SUPL, see Section [7.7.11](#page-125-0)).



<span id="page-124-2"></span>**Figure 118: With User Plane Architecture the mobile network requires no alteration** 

#### <span id="page-124-1"></span>**7.7.10 Architecture advantages**

[Table](#page-125-1) 18 compares the advantages of User-plane vs. Control-plane architectures.



| Criteria                        | User-plane advantage                                                                                                                                                                              | Control-plane advantage                                                                                                                                         |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture and implementation | Fewer elements involved, resulting<br>in less complexity, cost, and impact<br>on the network                                                                                                      |                                                                                                                                                                 |
| Risk                            | Less costly to implement, offloads<br>service<br>development<br>to<br>third<br>parties,<br>while<br>the<br>operator<br>maintains<br>control<br>over<br>enabling<br>those services with a location | Utilizes<br>the<br>more<br>reliable<br>SS7<br>network                                                                                                           |
| Service options                 |                                                                                                                                                                                                   | More complex design lends itself to<br>more<br>robust<br>service<br>choices;<br>in<br>addition,<br>voice-controlled<br>services<br>are also easier to implement |
| Management/upgrades             | Fewer moving parts result in lower<br>operating expenses; upgrades don't<br>impact as many elements                                                                                               |                                                                                                                                                                 |
| Control                         |                                                                                                                                                                                                   | Standards for location gateway are<br>better defined for implementation                                                                                         |
| Extensibility (for developers)  | Allows third parties to develop and<br>host services with minimal network<br>impact                                                                                                               |                                                                                                                                                                 |
| Service addressability          |                                                                                                                                                                                                   | Allows operators to deploy services<br>to subscribers with or without data<br>connectivity                                                                      |

<span id="page-125-1"></span>**Table 18: Comparison of advantages of User-plane vs. Control-plane Architectures [83](#page-125-2)**

#### <span id="page-125-0"></span>**7.7.11 OMA-Secure User Plane Location Architecture (OMA-SUPL)**

In June 2007 the OMA (Open Mobile Alliance[84](#page-125-3)) authorized and released their Standard. All standards, regulations and protocols pertaining to User Plane are combined under the heading Secure User Plane Location (SUPL) and are available on the OMA website. SUPL requires existing Mobile Networks to transmit Aiding-Data from the Location Server to Mobil Stations with integrated GPS components. The necessary Aiding-Data for A-GPS function is stored in the Location Server.

The User Plane Location Protocol (ULP) describes the most important protocols for communication between Location Servers and mobile stations with GPS receivers for A-GPS. This Standard designates the Location Server as the SLP (SUPL Location Platform) and the combined mobile terminal with GPS receiver as the SET (SUPL Enabled Terminal) (See [Figure](#page-126-3) 119).

<span id="page-125-3"></span><span id="page-125-2"></span><sup>83</sup> http://h71019.www7.hp.com/enterprise/downloads/Article\_Dueling\_Architectures\_UserPlane-ControlPlane.pdf

<sup>84</sup> http://www.openmobilealliance.org/





<span id="page-126-3"></span>**Figure 119: Block diagram with components according to OMA** 

The significant protocols for A-GPS are:

- SUPL POS INIT (Section 6.2.4 of the Standard)
- Positioning Method (Section 7.8 of the Standard)
- Requested Assistance Data (Section 7.9 of the Standard)

## <span id="page-126-0"></span>**7.8 High Sensitivity GPS (HSGPS)**

While certain applications, such as calling emergency numbers or Location Based Services, require clear reception in buildings or in urban canyons, the reception performance of GNSS receivers is being continually improved. The primary focuses of these efforts are:

- Increased signal sensitivity
- Quicker acquisition upon activation of the receiver (time to first fix, TTFF)
- Reduced sensitivity to interference (e.g. multipath interference, or electromagnetic interference EMC)

Various strategies are being employed by different manufacturers in order to achieve improvements. The most important of these are discussed in this chapter including:

- Improved Oscillator Stability
- Antennas
- Noise Figure considerations
- Increasing the correlators and the correlation time

#### <span id="page-126-1"></span>**7.8.1 Improved oscillator stability**

The development and use of increasingly stable oscillators is an attempt to reduce or compensate for the temperature dependence of quartz in order to decrease signal acquisition time in the required frequency areas. This mostly involves the employment of temperature compensated crystal oscillators (TCXO).

Additionally, studies have shown[85](#page-126-4) that normal quartz oscillators can produce micro variations in frequency (several ppb). The causes of these frequency changes are generally structural impurity of the quartz crystal. On the basis of these sudden frequency shifts the acquisition time is increased because the search in the frequencycode domain during the correlation process is disrupted. Developing quartz oscillators with reduced tendencies to micro variations can reduce this disturbance.

#### <span id="page-126-2"></span>**7.8.2 Antennas**

Antennas can be made to be less sensitive to disturbances and to selectively receive GNSS frequencies. The disadvantage of this performance improvement is an increase in size. This contradicts the general trend towards miniaturization of mobile stations.

<span id="page-126-4"></span><sup>85</sup> GPS-World, November 2003: Vittorini und Robinson: Optimizing Indoor GPS Performance, page 40



#### <span id="page-127-0"></span>**7.8.3 Noise figure considerations**

The Noise Figure (NF) is a measure that indicates to what extent the signal-to-noise ratio of an incoming signal is decreased by the additional noise of the receiver. Minimizing the noise and maximizing the amplification at the first amplification stage (LNA) minimally improves the receiver sensitivity. As is the case with every receiver the first stage amplification determines the noise characteristics for the entire receiver (see [Equation](#page-127-2) 1).

$$
NF_{\text{Total}} = NF_1 + \frac{NF_2 - 1}{G_1} + \frac{NF_3 - 1}{G_1 \cdot G_2} + \dots + \frac{NF_N - 1}{G_1 \cdot G_2 \dots G_{N-1}}
$$

#### <span id="page-127-2"></span>**Equation 1: Calculation of noise figure**

NF: Noise Figure of the Stage

G: Gain of the Stage

Noise figure and gain are linear factors and are not to be used in logarithmic (dB) representation.

[Equation](#page-127-3) 2 and the simplified block diagram in [Figure](#page-127-4) 120 show the calculation of the total Noise Figure for the LNA and the combined subsequent stages (SS):

LNA SS Total LNA G NF NFNF

#### **Equation 2: Calculation of noise figure**

<span id="page-127-3"></span>

<span id="page-127-4"></span>**Figure 120: Block Diagram of input stages** 

With typical noise figures for the first and subsequent amplification stages of 1.6 dB and 20 dB respectively, only marginal improvements are possible with new LNA developments. Further advancement in this area appears to be unlikely.

#### <span id="page-127-1"></span>**7.8.4 Correlators and correlation time**

The spectral power density of the received GNSS signals is approx. 16 dB below the power density of the thermal background noise (see [Figure](#page-46-0) 39). The demodulation and de-spreading of the received GNSS signals creates a system gain GG of 43dB (see [Figure](#page-54-0) 49).

Increasing the correlation time (integration time or dwell time) improves the sensitivity of a GNSS module. The longer a correlator remains at a specific code-frequency level, the lower the required strength of the GNSS signal at the antenna. If the correlation time is increased by a factor of k, then there will be an increase GR in the separation to the thermal background noise of:

GR = log10 (k)

Doubling the correlation time results in an increase of the signal-background noise separation of 3 dB. In practice an increase in the correlation time of 20 ms is not a problem. When the value of the transmitted data bits is known this time can be additionally increased. Otherwise it is possible through a non-coherent integration to increase the correlation time to over 1 second, however, this procedure results in a one-time loss of several dB.



In order to increase the acquisition sensitivity the number of implemented correlators is significantly increased.

Modern GNSS receivers typically possess a sensitivity of approximately –160dBm. Given that the GPS operator (US Department of Defense) guarantees signal strength of –130dBm, GNSS receivers can therefore function in buildings that weaken the signal by up to 30dB.

## <span id="page-128-0"></span>**7.9 GNSS-repeater or re-radiation antenna**

A GNSS-Repeater (also known as a Re-radiation Antenna or Transceiver) receives GNSS-Signals from visible satellites through an externally situated antenna, amplifies the signals and transmits them to another location (e.g. into a building). They require no direct connection to the GNSS device. The reception antenna is installed outdoors in a location favorable for receiving satellite signals. The GNSS-Repeater [\(Figure](#page-128-2) 121) consists of:

- External Antenna (Reception Antenna)
- Internal Antenna (Transmission Antenna)
- Electrical adapter
- Amplifier
- Cable



**Figure 121: GNSS Repeater (external antenna, electrical adapter and power cord, amplifier and internal antenna)** 

## <span id="page-128-2"></span><span id="page-128-1"></span>**7.10Pseudolites for indoor applications**

A Pseudolite (short form for pseudo satellite) is a ground-based transmitter, which functions like a GNSS satellite. Pseudolites are often used in aviation to support aircraft landing approaches. This procedure is not commonly used for indoor applications because the necessary components are relatively expensive.



## <span id="page-129-0"></span>**8 Data formats and hardware interfaces**

*If you would like to . . .* 

- o know what NMEA and RTCM mean
- o know what a proprietary data set is
- o know what data set is available in the case of all GNSS receivers
- o know what an active antenna is
- o know whether GNSS receivers have a synchronized timing pulse

*then this chapter is for you!* 

## <span id="page-129-1"></span>**8.1 Introduction**

GNSS receivers require different signal lines in order to function [\(Figure](#page-129-2) 122). The values of different variables are broadcast after position and time have been successfully calculated. To ensure that the different types of appliances are portable, there are either international standards for data exchange (NMEA and RTCM), or the manufacturer provides defined (proprietary) formats and protocols.



<span id="page-129-2"></span>**Figure 122: Block diagram of a GNSS receiver with interfaces** 



## <span id="page-130-0"></span>**8.2 Data interfaces**

#### <span id="page-130-1"></span>**8.2.1 The NMEA-0183 data interface**

In order to relay computed GNSS variables such as position, velocity, course etc. to a peripheral (e.g. computer, screen, transceiver), GNSS modules have a serial interface (TTL or RS-232 level). The most important elements of receiver information are broadcast via this interface in a special data format. This format is standardized by the National Marine Electronics Association (NMEA) to ensure that data exchange takes place without any problems. Nowadays, data is relayed according to the NMEA-0183 specification. NMEA has specified data sets for various applications e.g. GNSS (Global Navigation Satellite System), GPS, Loran, Omega, Transit and also for various manufacturers. The following seven data sets are widely used with GNSS modules to relay GNSS information[86](#page-130-2):

- 1. GGA (GPS Fix Data, fixed data for the Global Positioning System)
- 2. GGL (Geographic Position Latitude/Longitude)
- 3. GSA (GPS DOP and Active Satellites, degradation of accuracy and the number of active satellites in the Global Satellite Navigation System)
- 4. GSV (GNSS Satellites in View, satellites in view in the Global Satellite Navigation System)
- 5. RMC (Recommended Minimum Specific GNSS Data)
- 6. VTG (Course over Ground and Ground Speed, horizontal course and horizontal velocity)
- 7. ZDA (Time & Date)

<span id="page-130-2"></span><sup>86</sup> NMEA 0183, Standard For Interfacing Marine Electronics Devices, Version 2.30



#### **8.2.1.1 Structure of the NMEA protocol**

In the case of NMEA, the rate at which data is transmitted is 4800 Baud using printable 8-bit ASCII characters. Transmission begins with a start bit (logical zero), followed by eight data bits and a stop bit (logical one) added at the end. No parity bits are used.



#### <span id="page-131-0"></span>**Figure 123: NMEA format (TTL and RS-232 level)**

The different levels must be taken into consideration depending on whether the GNSS receiver used has a TTL or RS-232 interface ([Figure](#page-131-0) 123):

- In the case of a TTL level interface, a logical zero corresponds to approx. 0V and a logical one roughly to the operating voltage of the system (+3.3V ... +5V)
- In the case of an RS-232 interface a logical zero corresponds to a positive voltage (+3V ... +15V) and a logical one a negative voltage (-3V ... –15V).

If a GNSS module with a TTL level interface is connected to an appliance with an RS-232 interface, a level conversion must be effected (see [8.3.4\)](#page-154-1).

Most GNSS receivers allow the baud rate to be increased (up to 115200 bits per second).

Each GNSS data set is formatted in the same way and has the following structure:

\$GPDTS,Inf\_1,Inf\_2, Inf\_3,Inf\_4,Inf\_5,Inf\_6,Inf\_n\*CS<CR><LF>

[Table](#page-132-0) 19 explains the functions of individual characters and character groups.



| Field              | Description                                                                  |
|--------------------|------------------------------------------------------------------------------|
| \$                 | Start of the data set                                                        |
| GP                 | Information originating from a GNSS appliance                                |
| DTS                | Data set identifier (e.g. RMC)                                               |
| Inf_1 to Inf_n     | Information with number 1  n (e.g. 175.4 for course data)                    |
| ,                  | Comma used as a separator for different items of information                 |
| *                  | Asterisk used as a separator for the checksum                                |
| CS                 | Checksum (control word) for checking the entire data set                     |
| <cr><lf></lf></cr> | End of the data set: carriage return ( <cr>) and line feed, (<lf>)</lf></cr> |

#### <span id="page-132-0"></span>**Table 19: Description of the individual NMEA DATA SET blocks**

The maximum number of characters used must not exceed 79. For the purposes of determining this number, the start sign \$ and end signs <CR><LF> are not counted.

The following NMEA protocol was recorded using a GNSS receiver ([Table](#page-132-1) 20):

| \$GPRMC,130303.0,A,4717.115,N,00833.912,E,000.03,043.4,200601,01.3,W*7D <cr><lf></lf></cr> |
|--------------------------------------------------------------------------------------------|
| \$GPZDA,130304.2,20,06,2001,,*56 <cr><lf></lf></cr>                                        |
| \$GPGGA,130304.0,4717.115,N,00833.912,E,1,08,0.94,00499,M,047,M,,*59 <cr><lf></lf></cr>    |
| \$GPGLL,4717.115,N,00833.912,E,130304.0,A*33 <cr><lf></lf></cr>                            |
| \$GPVTG,205.5,T,206.8,M,000.04,N,000.08,K*4C <cr><lf></lf></cr>                            |
| \$GPGSA,A,3,13,20,11,29,01,25,07,04,,,,,1.63,0.94,1.33*04 <cr><lf></lf></cr>               |
| \$GPGSV,2,1,8,13,15,208,36,20,80,358,39,11,52,139,43,29,13,044,36*42 <cr><lf></lf></cr>    |
| \$GPGSV,2,2,8,01,52,187,43,25,25,074,39,07,37,286,40,04,09,306,33*44 <cr><lf></lf></cr>    |
| \$GPRMC,130304.0,A,4717.115,N,00833.912,E,000.04,205.5,200601,01.3,W*7C <cr><lf></lf></cr> |
| \$GPZDA,130305.2,20,06,2001,,*57 <cr><lf></lf></cr>                                        |
| \$GPGGA,130305.0,4717.115,N,00833.912,E,1,08,0.94,00499,M,047,M,,*58 <cr><lf></lf></cr>    |
| \$GPGLL,4717.115,N,00833.912,E,130305.0,A*32 <cr><lf></lf></cr>                            |
| \$GPVTG,014.2,T,015.4,M,000.03,N,000.05,K*4F <cr><lf></lf></cr>                            |
| \$GPGSA,A,3,13,20,11,29,01,25,07,04,,,,,1.63,0.94,1.33*04 <cr><lf></lf></cr>               |
| \$GPGSV,2,1,8,13,15,208,36,20,80,358,39,11,52,139,43,29,13,044,36*42 <cr><lf></lf></cr>    |
| \$GPGSV,2,2,8,01,52,187,43,25,25,074,39,07,37,286,40,04,09,306,33*44 <cr><lf></lf></cr>    |

<span id="page-132-1"></span>**Table 20: Recording of an NMEA protocol** 

#### **8.2.1.2 GGA data set**

The GGA data set (GPS Fix Data) contains information on time, longitude and latitude, the quality of the system, the number of satellites used and the height.

An example of a GGA data set:

\$GPGGA,130305.0,4717.115,N,00833.912,E,1,08,0.94,00499,M,047,M,,\*58<CR><LF>

The function of the individual characters or character sets is explained in [Table](#page-133-0) 21.



| Field              | Description                                         |
|--------------------|-----------------------------------------------------|
| \$                 | Start of the data set                               |
| GP                 | Information originating from a GNSS appliance       |
| GGA                | Data set identifier                                 |
| 130305.0           | UTC positional time: 13h 03min 05.0sec              |
| 4717.115           | Latitude: 47° 17.115 min                            |
| N                  | Northerly latitude (N=north, S= south)              |
| 00833.912          | Latitude: 8° 33.912min                              |
| E                  | Easterly longitude (E= east, W=west)                |
| 1                  | GPS quality details (0= no GPS, 1= GPS, 2=DGPS)     |
| 08                 | Number of satellites used in the calculation        |
| 0.94               | Horizontal Dilution of Precision (HDOP)             |
| 00499              | Antenna height data (geoid height)                  |
| M                  | Unit of height (M= meter)                           |
| 047                | Height differential between an ellipsoid and geoid  |
| M                  | Unit of differential height (M= meter)              |
| ,,                 | Age of the DGPS data (in this case no DGPS is used) |
| 0000               | Identification of the DGPS reference station        |
| *                  | Separator for the checksum                          |
| 58                 | Checksum for verifying the entire data set          |
| <cr><lf></lf></cr> | End of the data set                                 |

<span id="page-133-0"></span>**Table 21: Description of the individual GGA data set blocks** 



#### **8.2.1.3 GLL data set**

The GLL data set (geographic position – latitude/longitude) contains information on latitude and longitude, time and health.

Example of a GLL data set:

\$GPGLL,4717.115,N,00833.912,E,130305.0,A\*32<CR><LF>

The function of the individual characters or character sets is explained in [Table](#page-134-0) 22.

| Field              | Description                                   |
|--------------------|-----------------------------------------------|
| \$                 | Start of the data set                         |
| GP                 | Information originating from a GNSS appliance |
| GLL                | Data set identifier                           |
| 4717.115           | Latitude: 47° 17.115 min                      |
| N                  | Northerly latitude (N=north, S= south)        |
| 00833.912          | Longitude: 8° 33.912min                       |
| E                  | Easterly longitude (E=east, W=west)           |
| 130305.0           | UTC positional time: 13h 03min 05.0sec        |
| A                  | Data set quality: A means valid (V= invalid)  |
| *                  | Separator for the checksum                    |
| 32                 | Checksum for verifying the entire data set    |
| <cr><lf></lf></cr> | End of the data set                           |

<span id="page-134-0"></span>**Table 22: Description of the individual GGL data set blocks** 



#### **8.2.1.4 GSA data set**

The GSA data set (GNSS DOP and Active Satellites) contains information on the measuring mode (2D or 3D), the number of satellites used to determine the position and the accuracy of the measurements (DOP: Dilution of Precision).

Example of a GSA data set:

\$GPGSA,A,3,13,20,11,29,01,25,07,04,,,,,1.63,0.94,1.33\*04<CR><LF>

The function of the individual characters or sets of characters is described in [Table](#page-135-0) 23.

| Field              | Description                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------|
| \$                 | Start of the data set                                                                                   |
| GP                 | Information originating from a GNSS appliance                                                           |
| GSA                | Data set identifier                                                                                     |
| A                  | Calculating mode (A= automatic selection between 2D/3D mode, M= manual selection<br>between 2D/3D mode) |
| 3                  | Calculating mode (1= none, 2=2D, 3=3D)                                                                  |
| 13                 | ID number of the satellites used to calculate position                                                  |
| 20                 | ID number of the satellites used to calculate position                                                  |
| 11                 | ID number of the satellites used to calculate position                                                  |
| 29                 | ID number of the satellites used to calculate position                                                  |
| 01                 | ID number of the satellites used to calculate position                                                  |
| 25                 | ID number of the satellites used to calculate position                                                  |
| 07                 | ID number of the satellites used to calculate position                                                  |
| 04                 | ID number of the satellites used to calculate position                                                  |
| ,,,,,              | Dummy for additional ID numbers (currently not used)                                                    |
| 1.63               | PDOP (Position Dilution of Precision)                                                                   |
| 0.94               | HDOP (Horizontal Dilution of Precision)                                                                 |
| 1.33               | VDOP (Vertical Dilution of Precision)                                                                   |
| *                  | Separator for the checksum                                                                              |
| 04                 | Checksum for verifying the entire data set                                                              |
| <cr><lf></lf></cr> | End of the data set                                                                                     |

<span id="page-135-0"></span>**Table 23: Description of the individual GSA data set blocks** 



#### **8.2.1.5 GSV data set**

The GSV data set (GNSS Satellites in View) contains information on the number of satellites in view, their identification, their elevation and azimuth, and the signal-to-noise ratio.

An example of a GSV data set:

\$GPGSV,2,2,8,01,52,187,43,25,25,074,39,07,37,286,40,04,09,306,33\*44<CR><LF>

The function of the individual characters or character sets is explained in [Table](#page-136-0) 24.

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| \$                 | Start of the data set                                          |
| GP                 | Information originating from a GNSS appliance                  |
| GSV                | Data set identifier                                            |
| 2                  | Total number of GVS data sets transmitted (up to 1  9)         |
| 2                  | Current number of this GVS data set (1  9)                     |
| 09                 | Total number of satellites in view                             |
| 01                 | Identification number of the first satellite                   |
| 52                 | Elevation (0°  90°)                                            |
| 187                | Azimuth (0°  360°)                                             |
| 43                 | Signal-to-noise ratio in db-Hz (1  99, null when not tracking) |
| 25                 | Identification number of the second satellite                  |
| 25                 | Elevation (0°  90°)                                            |
| 074                | Azimuth (0°  360°)                                             |
| 39                 | Signal-to-noise ratio in dB-Hz (1  99, null when not tracking) |
| 07                 | Identification number of the third satellite                   |
| 37                 | Elevation (0°  90°)                                            |
| 286                | Azimuth (0°  360°)                                             |
| 40                 | Signal-to-noise ratio in db-Hz (1  99, null when not tracking) |
| 04                 | Identification number of the fourth satellite                  |
| 09                 | Elevation (0°  90°)                                            |
| 306                | Azimuth (0°  360°)                                             |
| 33                 | Signal-to-noise ratio in db-Hz (1  99, null when not tracking) |
| *                  | Separator for the checksum                                     |
| 44                 | Checksum for verifying the entire data set                     |
| <cr><lf></lf></cr> | End of the data set                                            |

<span id="page-136-0"></span>**Table 24: Description of the individual GSV data set blocks** 



#### **8.2.1.6 RMC data set**

The RMC data set (Recommended Minimum Specific GNSS) contains information on time, latitude, longitude, system status, speed, course and date. All GNSS receivers relay this data set.

An example of an RMC data set:

\$GPRMC,130304.0,A,4717.115,N,00833.912,E,000.04,205.5,200601,01.3,W\*7C<CR><LF>

Field Description \$ Start of the data set GP Information originating from a GNSS appliance RMC Data set identifier 130304.0 Time of reception (world time UTC): 13h 03 min 04.0 sec A Data set quality: A signifies valid (V= invalid) 4717.115 Latitude: 47° 17.115 min N Northerly latitude (N=north, S= south) 00833.912 Longitude: 8° 33.912 min E Easterly longitude (E=east, W=west) 000.04 Speed: 0.04 knots

The function of the individual characters or character sets is explained in [Table](#page-137-0) 25.

| 00833.912          | Longitude: 8° 33.912 min                     |
|--------------------|----------------------------------------------|
| E                  | Easterly longitude (E=east, W=west)          |
| 000.04             | Speed: 0.04 knots                            |
| 205.5              | Course: 205.5°                               |
| 200601             | Date: 20th June 2001                         |
| 01.3               | Adjusted declination: 1.3°                   |
| W                  | Westerly direction of declination (E = east) |
| *                  | Separator for the checksum                   |
| 7C                 | Checksum for verifying the entire data set   |
| <cr><lf></lf></cr> | End of the data set                          |

<span id="page-137-0"></span>**Table 25: Description of the individual RMC data set blocks** 



#### **8.2.1.7 VTG data set**

The VGT data set (Course over Ground and Ground Speed) contains information on course and speed.

An example of a VTG data set:

\$GPVTG,014.2,T,015.4,M,000.03,N,000.05,K\*4F<CR><LF>

The function of the individual characters or character sets is explained in [Table](#page-138-0) 26.

| Field              | Description                                          |
|--------------------|------------------------------------------------------|
| \$                 | Start of the data set                                |
| GP                 | Information originating from a GNSS appliance        |
| VTG                | Data set identifier                                  |
| 014.2              | Course 14.2° (T) with regard to the horizontal plane |
| T                  | Angular course data relative to the map              |
| 015.4              | Course 15.4° (M) with regard to the horizontal plane |
| M                  | Angular course data relative to magnetic north       |
| 000.03             | Horizontal speed (N)                                 |
| N                  | Speed in knots                                       |
| 000.05             | Horizontal speed (Km/h)                              |
| K                  | Speed in km/h                                        |
| *                  | Separator for the checksum                           |
| 4F                 | Checksum for verifying the entire data set           |
| <cr><lf></lf></cr> | End of the data set                                  |

<span id="page-138-0"></span>**Table 26: Description of the individual VTG data set blocks** 



#### **8.2.1.8 ZDA data set**

The ZDA data set (time and date) contains information on UTC time, the date and local time.

An example of a ZDA data set:

\$GPZDA,130305.2,20,06,2001,,\*57<CR><LF>

The function of the individual characters or character sets is explained in [Table](#page-139-0) 27.

| Field              | Description                                               |
|--------------------|-----------------------------------------------------------|
| \$                 | Start of the data set                                     |
| GP                 | Information originating from a GNSS appliance             |
| ZDA                | Data set identifier                                       |
| 130305.2           | UTC time: 13h 03min 05.2sec                               |
| 20                 | Day (00 … 31)                                             |
| 06                 | Month (1 … 12)                                            |
| 2001               | Year                                                      |
|                    | Reserved for data on local time (h), not specified here   |
|                    | Reserved for data on local time (min), not specified here |
| *                  | Separator for the checksum                                |
| 57                 | Checksum for verifying the entire data set                |
| <cr><lf></lf></cr> | End of the data set                                       |

<span id="page-139-0"></span>**Table 27: Description of the individual ZDA data set blocks** 

#### **8.2.1.9 Calculating the checksum**

The checksum is determined by an exclusive-or operation involving all 8 data bits (excluding start and stop bits) from all transmitted characters, including separators. The exclusive-or operation commences after the start of the data set (\$ sign) and ends before the checksum separator (asterisk: \*).

The 8-bit result is divided into 2 sets of 4 bits (nibbles) and each nibble is converted into the appropriate hexadecimal value (0 ... 9, A ... F). The checksum consists of the two hexadecimal values converted into ASCII characters.

The principle of checksum calculation can be explained with the help of a brief example:

The following NMEA data set has been received and the checksum (CS) must be verified for its correctness.

#### \$GPRTE,1,1,c,0\***07** (**07** is the checksum)

Procedure:

- 1. Only the characters between \$ and \* are included in the analysis: GPRTE,1,1,c,0
- 2. These 13 ASCII characters are converted into 8 bit values (see [Table](#page-140-0) 28)
- 3. Each individual bit of the 13 ASCII characters is linked to an exclusive-or operation (i.e., if the number of ones is uneven, the exclusive-or value is one)
- 4. The result is divided into two nibbles
- 5. The hexadecimal value of each nibble is determined
- 6. Both hexadecimal characters are transmitted as ASCII characters to form the checksum



| Character             |      | ASCII (8 bit value) |   |   |      |   |   |   |
|-----------------------|------|---------------------|---|---|------|---|---|---|
| G                     | 0    | 1                   | 0 | 0 | 0    | 1 | 1 | 1 |
| P                     | 0    | 1                   | 0 | 1 | 0    | 0 | 0 | 0 |
| R                     | 0    | 1                   | 0 | 1 | 0    | 0 | 1 | 0 |
| T                     | 0    | 1                   | 0 | 1 | 0    | 1 | 0 | 0 |
| E                     | 0    | 1                   | 0 | 0 | 0    | 1 | 0 | 1 |
| ,                     | 0    | 0                   | 1 | 0 | 1    | 1 | 0 | 0 |
| 1                     | 0    | 0                   | 1 | 1 | 0    | 0 | 0 | 1 |
| ,                     | 0    | 0                   | 1 | 0 | 1    | 1 | 0 | 0 |
| 1                     | 0    | 0                   | 1 | 1 | 0    | 0 | 0 | 1 |
| ,                     | 0    | 0                   | 1 | 0 | 1    | 1 | 0 | 0 |
| C                     | 0    | 1                   | 1 | 0 | 0    | 0 | 1 | 1 |
| ,                     | 0    | 0                   | 1 | 0 | 1    | 1 | 0 | 0 |
| 0                     | 0    | 0                   | 1 | 1 | 0    | 0 | 0 | 0 |
| Exclusive-or value    | 0    | 0                   | 0 | 0 | 0    | 1 | 1 | 1 |
| Nibble                | 0000 |                     |   |   | 0111 |   |   |   |
| Hexadecimal value     | 0    |                     |   |   | 7    |   |   |   |
| ASCII CS characters   |      |                     |   |   | 7    |   |   |   |
| (meets requirements!) |      |                     |   |   |      |   |   |   |

Direction to proceed

<span id="page-140-0"></span>**Table 28: Determining the checksum in the case of NMEA data sets** 



#### <span id="page-141-0"></span>**8.2.2 Conversion from NMEA to KML**

#### **8.2.2.1 Introduction to Google Earth and KML**

Navigation data (e.g. a track), available in NMEA data format, can be displayed with Google Earth[87](#page-141-1) ([Figure](#page-141-2) 124).



#### <span id="page-141-2"></span>**Figure 124: Google Earth with Detail**

For this the NMEA file must first be converted into the Google Earth accessible KML (Keyhole Markup Language) format. KML is an XML syntax and file format for modeling and storing geographic elements such as points, lines, pictures, polygons and models for display in Google Earth and Google Maps[88](#page-141-3). Google Earth and Google Maps process KML files in a similar way to HTML and XML files. Like HTML, KML possesses a tag-based structure with names and attributes for special graphical display. Google Earth also supports the KMZ format, which is a ZIP-compressed KML file. Since KMZ files are compressed they cannot be directly edited. In order to alter a KMZ file, it must first be unzipped (decompressed). The file can then be changed with an XML or text editor and finally re-compressed. Further information about KML and KMZ formats can be found in the KML documentation from Google Earth[89](#page-141-4).

#### **8.2.2.2 Principle of converting NMEA to KML**

In order to illustrate the principle, a track (travelled path saved in an NMEA file) will be converted into a KML file to keep the example simple, the track is reduced to three measured points.

For conversion into KML format, the NMEA GGA (fix information) data record is sufficient. Unlike the RMC format, this also includes information about height. The following track has been stored as an NMEA file and reduced to GGA records to be displayed using Google Earth.

<span id="page-141-1"></span><sup>87</sup> [http://earth.google.com/,](http://earth.google.com/) [http://earth.google.de/,](http://earth.google.de/) etc.

<span id="page-141-3"></span><sup>88</sup> http://maps.google.com/

<span id="page-141-4"></span><sup>89</sup> <http://code.google.com/apis/kml/documentation/mapsSupport.html>





The selected track, as seen using the u-center evaluation tools [\(Figure](#page-142-0) 125):

<span id="page-142-0"></span>**Figure 125: Track, consisting of 3 measurements, displayed by u-center** 

Latitude and longitude must be converted into WGS-84 (Decimal format).

Example for the first data record: The Latitude value 4650.9180 N is expressed in the GGA format for describing 46° 50.9180'. This must be converted into decimal format.

46° 50.9180' = (46 +50.9180/60)° = 46.848633°

The longitude value 00931.8641 E stands for 9° 31.8641' and also must be converted to decimal format.

009° 31.8641' = (9° + 31.8641/60)° = 9.5310683°

The height value can be directly taken from the GGA record: 614.7m

[Figure](#page-143-0) 126 shows how latitudinal and longitudinal values are depicted.

Longitude values from 0° to 180° E and latitudes from 0° to 90° N are positive.

Longitudes from 0° to 180° W and latitudes from 0° to 90° S receive a negative value.





**Figure 126: Depiction of latitude and longitude values** 

<span id="page-143-0"></span>The converted values can now be entered in the KML-file (3\_point\_Chur.kml) as seen in [Figure](#page-143-1) 127.



<span id="page-143-1"></span>**Figure 127: KML File (3\_point\_Chur.kml) of the track** 



After starting Google Earth, selecting the newly created file 3\_point\_Chur.kml displays the following image [\(Figure](#page-144-1) 128):



**Figure 128: KML file, displayed with Google Earth** 

<span id="page-144-1"></span>The u-center GPS evaluation software from u-blox includes an integrated conversion tool that enables automatic conversion of NMEA files into KML or KMZ format. A variety of additional online and offline tools are available on the Internet[90](#page-144-2), [91](#page-144-3), [92](#page-144-4), [93](#page-144-5).

### <span id="page-144-0"></span>**8.2.3 The DGPS correction data (RTCM SC-104)**

The RTCM SC-104 standard is used to transmit correction values. RTCM SC-104 stands for "Radio Technical Commission for Maritime Services Special Committee 104" and is currently recognized around the world as the industry standard[94](#page-144-6). There are five versions of the RTCM Recommended Standards for Differential NAVSTAR GPS Service[95](#page-144-7).

- RTCM Recommended Standards for Differential Navstar GPS Service, **Version 2.0** (Code Correction for DGPS)
- RTCM Recommended Standards for Differential Navstar GPS Service, **Version 2.1** (Supplemental to Version 2.0: code and phase correction for real time navigation, Real Time Kinematik RTK)
- RTCM Recommended Standards for Differential GNSS (Global Navigation Satellite Systems) Service, **Version 2.2** (Supplemental to Version 2.1: correction signals for Glonass)

<span id="page-144-2"></span><sup>90</sup> <http://www.swisstopo.ch/en/online/calculation/kml/index>

<span id="page-144-3"></span><sup>91</sup> <http://www.gpsvisualizer.com/map?form=googleearth>

<span id="page-144-4"></span><sup>92</sup> <http://www.gpsbabel.org/>

<span id="page-144-5"></span><sup>93</sup> http://www.gpsies.com/upload.do?uploadMode=convert

<span id="page-144-6"></span><sup>94</sup> <http://www.navcen.uscg.gov/pubs/dgps/rctm104/Default.htm>

<span id="page-144-7"></span><sup>95</sup> https://ssl29.pair.com/dmarkle/puborder.php?show=3



- RTCM 10402.3 RTCM Recommended Standards for Differential GNSS (Global Navigation Satellite Systems) Service, **Version 2.3** (Supplemental to Version 2.2: information about reference antennas)
- RTCM 10403.1, Differential GNSS (Global Navigation Satellite Systems) Services, **Version 3** (Supplemental to Version 2.3: suitable for network RTK and additional navigation systems.).The Version 3 format is not compatible with Version 2.x.

All versions represent a further development of the previous and are primarily distinguished from one another on the basis of additional information provided. Each of the Version 2.x releases are divided into 63 message types, numbers 1, 2, 3 and 9 being used primarily for corrections based on code measurements.

#### **8.2.3.1 The RTCM message header (Version 2.3)**

Each message type is divided into words of 30 bits, and always begins with a uniform header consisting of two words (Word 1 and Word 2). From the information contained in the header it is apparent which message type follows[96](#page-145-0) and which reference station has determined the correction data ([Figure](#page-145-1) 129).



#### <span id="page-145-1"></span>**Figure 129: Construction of the RTCM message header**

| Contents         | Name                     | Description                                   |
|------------------|--------------------------|-----------------------------------------------|
| Preamble         | Preamble                 | Preamble                                      |
| Message type:    | Message type             | Message type identifier                       |
| Station ID       | Reference station ID No. | Reference station identification              |
| Parity           | Error correction code    | Parity                                        |
| Modified Z-Count | Modified Z-count         | Modified Z-Count, incremental<br>time counter |
| Sequence number. | Frame sequence No.       | Sequential number                             |
| Length of Frame  | Frame length             | Length of frame                               |
| Station health   | Reference station health | Technical status of the reference<br>station  |

#### <span id="page-145-2"></span>**Table 29: Contents of the RTCM message header**

<span id="page-145-0"></span><sup>96</sup> Global Positioning System: Theory and Applications, Volume II, Bradford W. Parkinson, page 31



The specific data content for the message type (WORD 3 ... WORD n) always follows the header.

| Word 1                                           | Word 2 | Word 3              | Word 4 |  | Word n |  |
|--------------------------------------------------|--------|---------------------|--------|--|--------|--|
| Header:<br>2<br>•<br>30<br>bit<br>=<br>60<br>bit |        |                     |        |  |        |  |
|                                                  |        | n<br>•<br>30<br>bit |        |  |        |  |

<span id="page-146-0"></span>**Figure 130: Total frames with RTCM SC-104 (Version 2.x)** 



#### **8.2.3.2 RTCM message type 1 (Version 2.3)**

Message type 1 transmits pseudorange correction data (PSR correction data, range correction) for all GPS satellites visible to the reference station, based on the most up-to-date orbital data (ephemeris). Type 1 additionally contains the rate-of-change correction value [\(Figure](#page-147-1) 131, extract from[97](#page-147-0), only WORD 3 to WORD 6 are shown).



<span id="page-147-1"></span>**Figure 131: Construction of RTCM message type 1** 

<span id="page-147-0"></span><sup>97</sup> User Manual: Sony GXB1000 16-channel GPS receiver module



| Inhalt                    | Name                                        | Description                              |
|---------------------------|---------------------------------------------|------------------------------------------|
| SF (Scale Factor)         | Pseudorange correction value scale factor   | PSR scale factor                         |
| UDRE                      | User differential range error index         | User differential range error<br>index   |
| Satellite ID              | Satellite ID No.                            | Satellite identification                 |
| Pseudorange<br>correction | Pseudorange correction value                | Effective range correction               |
| Range-Rate<br>Correction  | Pseudorange rate-of-change correction value | Rate-of-change of the<br>correction data |
| Issue of data             | Data issue No.                              | Issue of data                            |
| Parity                    | Error correction code                       | Check bits                               |

#### <span id="page-148-2"></span>**Table 30: Contents of RTCM message type 1**

#### **8.2.3.3 RTCM message type 2 to 9 (Version 2.3)**

Message types 2 to 9 are distinguished primarily by their data content:

- **Message type 2** transmits delta PSR correction data, based on previous orbital data. This information is required whenever the GPS user has been unable to update his satellite orbital information. In message type 2, the difference between correction values based on the previous and updated ephemeris is transmitted.
- **Message type 3** transmits the three dimensional coordinates of the reference station.
- **Message type 9** relays the same information as message type 1, but only for a limited number of satellites (max. 3). Data is only transmitted from those satellites whose correction values change rapidly.

For a noticeable improvement in accuracy using DGPS, the correction data relayed should not be older than approx. 10 to 60 seconds (different values are supplied depending on the service operator, the exact value also depends on the accuracy required, see also[98](#page-148-0)). Accuracy decreases as the distance between the reference and user station increases. Trial measurements using the correction signals broadcast by the LW transmitter in Mainflingen, Germany, (see Section [7.4.2](#page-109-2)) produced an error rate of 0.5 – 1.5 m within a radius of 250 km, and 1 – 3 m within a radius of 600 km[99](#page-148-1).

[Table](#page-149-1) 31 provides a compilation of the message types for RTCM SC-104 (Version 2.3).

<span id="page-148-0"></span><sup>98</sup> swipos, Positionierungsdienste auf der Basis von DGPS, page 6, Bundesamt für Landestopographie

<span id="page-148-1"></span><sup>99</sup> [http://www.potsdam.ifag.de/potsdam/dgps/dgps\\_2.html](http://www.potsdam.ifag.de/potsdam/dgps/dgps_2.html)



| RTCM Message Type | Description                                      |
|-------------------|--------------------------------------------------|
| 1                 | Differential GPS corrections                     |
| 2                 | Delta Differential GPS corrections               |
| 3                 | GPS reference station parameters                 |
| 4                 | Reference station Datum                          |
| 5                 | GPS constellation health                         |
| 6                 | GPS null frame                                   |
| 7                 | DGPS beacon almanac                              |
| 8                 | Pseudolite almanac                               |
| 9                 | GPS partial correction set                       |
| 10                | P-Code-differential corrections                  |
| 11                | C/A-Code, L1, L2 delta corrections               |
| 12                | Pseudolite station parameter                     |
| 13                | Ground transmitter parameter                     |
| 14                | GPS time of week                                 |
| 15                | Ionospheric delay message                        |
| 16                | GPS special message                              |
| 17                | GPS ephemerides                                  |
| 18                | RTK uncorrected carrier phases                   |
| 19                | RTK uncorrected pseudorange                      |
| 20                | RTK carrier phase corrections                    |
| 21                | RTK pseudorange corrections for high accuracy    |
| 22                | Extended reference station parameters            |
| 23                | Antenna type definition                          |
| 24                | Reference Station: antenna reference point (ARP) |
| 25, 26            | Undefined                                        |
| 27                | Extended DGPS radiobeacon almanac                |
| 28…30             | Undefined                                        |
| 31                | Differential GLONASS corrections                 |
| 32                | Differential GLONASS reference station           |
| 33                | GLONASS constellation health                     |
| 34                | GLONASS partial differential correction set      |
| 35                | GLONASS radiobeacon almanac                      |
| 36                | GLONASS special message                          |
| 37                | GNSS System Time Offset                          |
| 3858              | Undefined                                        |
| 59                | Proprietary messages                             |
| 6063              | Multipurpose messages                            |

<span id="page-149-1"></span>**Table 31: RTCM SC-104 Version 2.3 message types** 

#### <span id="page-149-0"></span>**8.2.4 Proprietary data interfaces**

The majority of manufacturers offer proprietary data interfaces for their GNSS receivers. In comparison to the NMEA standard, proprietary data interfaces have the following advantages:

Emission of an augmented data scope; e.g., information which is not supported by the NMEA Protocol.



- Higher data density: most proprietary protocols use binary data formats with which numerical and Boolean information can be transmitted in a more consolidated way. Data intensive notifications e.g. satellite ephemeris, can be contained in a notification. With higher data density, a higher emission interval with a constant data transmission speed can be carried out.
- Extensive configuration possibilities for the GNSS receiver.
- Optimal linking to manufacturer-specific evaluation and visualization tools enables precise analysis of the reception behavior.
- Possibility of downloads from the current versions of the manufacturer-specific GNSS firmware. This function is only supported in GNSS receivers with the suitable Flash memory.
- From the GNSS manufacturer's point of view, an improved distribution of GNSS information to different data sets with the objective of avoiding redundancy and the transmission of data which are not required for the application.
- Very good integrity security provided by checksums.
- Minimum work for the host computer in reading and accepting the received data. The conversion of numerical data into ASCII format in an internal binary format is not required.

Three different types of proprietary data interfaces are typically used:

- Additional NMEA data sets: the information is coded into usual NMEA data format (text based, separation of the data with commas etc.). However, immediately after the initial symbol (Dollar sign) a manufacturerspecific address data follows. Many GNSS manufacturers use the additional notifications to convey further frequently used information. The NMEA format is, however, not suitable for efficiently sending large amounts of information due to inadequate data density and the intensive conversion of binary data into text format.
- Binary format (e.g. u-blox UBX).
- Text based format.

#### **8.2.4.1 Example: UBX protocol for u-blox GNSS receivers**

Apart from NMEA and RTCM, u-blox GNSS receivers by u-blox support the binary UBX protocol. As with the NMEA format, a framework format is given as follows:

| Symbol         | SYNC<br>CHAR 1, 2            | CLASS            | ID                        | LENGTH                      | PAYLOAD                    | CHECKSUM |
|----------------|------------------------------|------------------|---------------------------|-----------------------------|----------------------------|----------|
| Explanation    | Synchronization<br>character | Message<br>class | Message<br>identification | Length of the<br>data block | Structured data<br>content | Checksum |
| Length (Bytes) | 2                            | 1                | 1                         | 2                           | LENGTH                     | 2        |
|                |                              |                  |                           |                             |                            |          |

Checksum coverage area

#### <span id="page-150-0"></span>**Figure 132: Structure of the UBX data sets**

Each data set begins with two constant synchronization characters (Hexadecimal values: always B5, 62). These characters are used for recognizing the start of a new data set. The following two fields, CLASS and ID, identify the data set type. This two-tier identification allows a clean structuring of the different data sets according to classes. The overview is obtained also after adding new data sets. Symbolic concepts, which are easy to understand such as "NAV-POSLLH" (CLASS 01, ID 02), are used for the documentation. Following this, the length information and the actual data content are given. u-blox stipulates specific data types for the data



content. Finally, each data set ends with a 2-byte checksum. A dataset is only valid if the correct synchronization characters are available and the calculated and predetermined checksum coincide.

| Message class | Description                                                     | Content (Extract)                                                                                              |  |  |
|---------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--|--|
| NAV (01)      | Navigation information                                          | Position, speed, time, DGPS and SBAS<br>information                                                            |  |  |
| RXM (02)      | Receiver Management:<br>Amplified GNSS reception data           | GNSS raw data, e.g. pseudo-ranges,<br>ephemeris, yearbook, satellite status                                    |  |  |
| CFG (06)      | Configuration notifications<br>(Configure and request)          | Serial interfaces, emission interval, reception and<br>navigation parameters, energy saving methods            |  |  |
| ACK (05)      | Reception confirmation of the<br>configuration notifications    | Accepted or rejected                                                                                           |  |  |
| MON (0A)      | Operational status of the GNSS receiver                         | CPU capacity utilization, condition of the<br>operating system, use of system resources,<br>antenna monitoring |  |  |
| AID (0B)      | Feeding of auxiliary information to<br>accelerate the start up. | Ephemeris, yearbook, cold start, last position,<br>time, satellite status                                      |  |  |
| INF (04)      | Issuing of text based information notifications                 |                                                                                                                |  |  |
| TIM (0D)      | Configuration time pulse and time measurement of input signals  |                                                                                                                |  |  |
| UPD (09)      | Download of new software                                        |                                                                                                                |  |  |
| USR (4*)      | User specific notifications                                     |                                                                                                                |  |  |

#### <span id="page-151-0"></span>**Table 32: Message classes (Hexadecimal values in brackets)**

With the aid of customer specific software additional data sets can be integrated to existing protocols or additional user-specific protocols. Furthermore, u-blox receivers support several protocols on the same interface, e.g. nested NMEA and UBX data sets in both directions so that the advantages of several protocols can be made use of.



## <span id="page-152-0"></span>**8.3 Hardware interfaces**

#### <span id="page-152-1"></span>**8.3.1 Antennas**

GNSS satellites transmit signals that are based upon polarized waves. With the term polarization the oscillation direction of a field is described. If the electric field vector (and the magnetic one) turns in a clockwise manner as it propagates, the wave is called right-hand circular polarized (RHCP). With circular polarization no adjustment of the antenna is necessary. GNSS signals are right-hand circular polarized (RHCP). This requires a different type of antenna than the well-known whip antennas typically used for linear polarized signals.

GNSS receivers operate with either passive or active antennas. An active antenna contains a built-in LNA (Low Noise Amplifier) preamplifier. The GNSS receiver provides power to the active antenna over the RF signal line. For mobile navigation purposes a combined antenna (e.g. GSM/FM and GNSS) is used.

The most common types of GNSS antenna available on the market are:

- Patch antennas
- Helix antennas
- Chip antennas

Patch antennas are flat, consist of a ceramic and metalized body and are placed upon a metallic ground plane. In order to achieve enough selectivity, the relationship between ground plane and patch area must be appropriately matched. Patch antennas are often combined with a Low Noise Amplifier (LNA) and cast in a housing ([Figure](#page-152-3) 133 left shows a passive patch antenna and right a patch antenna combined with an LNA in a plastic housing[100](#page-152-2)). Patch antennas are especially suitable for applications in which a flat assembly is required.





**Figure 133: Passive open (left) and active enclosed Patch antennas** 

<span id="page-152-3"></span>Helix antennas (also helical antennas) are cylinder shaped ([Figure](#page-153-1) 134[101](#page-152-4)) and have a spiral wire rolled up or etched onto the ceramic body. They have a more pronounced directivity than patch antennas.

<span id="page-152-2"></span><sup>100</sup> http://www.u-blox.com/

<span id="page-152-4"></span><sup>101</sup> http://www.sarantel.com/







**Figure 134: Passive (left) and active helix antenna** 

<span id="page-153-1"></span>Chip antennas are especially small and can be built directly into a board ([Figure](#page-153-3) 135[102](#page-153-2)). Generally, the RF characteristics of chip antennas are not as well suited for GNSS as patch or helix antennas. They target primarily low-cost and mass market applications.



**Figure 135: Chip antenna** 

<span id="page-153-3"></span>For more information about GPS antennas see the *[GPS Antennas Application Note](http://www.u-blox.ch/images/downloads/Product_Docs/GPS_Antennas_ApplicationNote%28GPS-X-08014%29.pdf)*, available on the u-blox website.

#### <span id="page-153-0"></span>**8.3.2 Supply**

GNSS modules must be powered from an external voltage source of 3.3V to 6 Volts. In each case, the current consumption is very different.

<span id="page-153-2"></span><sup>102</sup> http://www.rainsun.com/



#### <span id="page-154-0"></span>**8.3.3 Time pulse: 1PPS and time systems**

Most GNSS receivers generate a time pulse every second, referred to as 1 PPS (1 pulse per second), which is synchronized to UTC. This signal usually has a TTL level ([Figure](#page-154-2) 136).



#### <span id="page-154-2"></span>**Figure 136: 1PPS signal**

The time pulse can be used to synchronize communication networks (Precision Timing).

#### <span id="page-154-1"></span>**8.3.4 Converting the TTL level to RS-232**

#### **8.3.4.1 Basics of serial communication**

The purpose of the RS-232 interface is mainly

- to link computers to each other (mostly bidirectional)
- to control serial printers
- to connect PCs to external equipment, such as GSM modems, GNSS receivers, etc.

The serial ports in PCs are designed for asynchronous transfer. Persons engaged in transmitting and receiving operations must adhere to a compatible transfer protocol, i.e., an agreement on how data is to be transferred. Both partners must work with the same interface configuration, and this will affect the rate of transfer measured in baud. The baud rate is the number of bits per second to be transferred. Typical baud rates are 4800, 9600, 19200, 38400, 57600 and 115200 baud, i.e. bits per second. These parameters are laid down in the transfer protocol. In addition, agreement must be reached by both sides on what checks should be implemented regarding the ready to transmit and receive status.

During transmission, 7 to 8 data bits are condensed into a data word in order to relay the ASCII codes. The length of a data word is laid down in the transfer protocol.

A start bit identifies the beginning of a data word, and at the end of every word 1 or 2 stop bits are appended.

A check can be carried out using a parity bit. In the case of even parity, the parity bit is selected in such a way that the total number of transferred data word »1 bits« is even (in the case of uneven parity there is an uneven number). Checking parity is important, because interference in the link can cause transmission errors. Even if one bit of a data word is altered, the error can be identified using the parity bit.

#### **8.3.4.2 Determining the level and its logical allocation**

Data is transmitted in inverted logic on the TxD and RxD lines. T stands for transmitter and R for receiver.

In accordance with standards, the levels are:

- Logical 0 = positive voltage, transmit mode: +5..+15V, receive mode:+3..+15V
- Logical 1 = negative voltage, transmit mode: -5..-15V, receive mode -3..-15V

The difference between the minimum permissible voltage during transmission and reception means that line interference does not affect the function of the interface, provided the noise amplitude is below 2V.



Converting the TTL level of the interface controller (UART, universal asynchronous receiver/ transmitter) to the required RS-232 level and vice versa is carried out by a level converter (e.g. MAX3221 and many others). The following figure ([Figure](#page-155-0) 137) illustrates the difference between TTL and RS-232 levels. Level inversion can clearly be seen.



<span id="page-155-0"></span>**Figure 137: Difference between TTL and RS-232 levels** 

#### **8.3.4.3 Converting the TTL level to RS-232**

Many GNSS receivers and GNSS modules only make serial NMEA and proprietary data available using TTL levels (approx. 0V or approx. Vcc = +3.3V or +5V). It is not always possible to evaluate this data directly through a PC, as a PC input requires RS-232 level values.

As a circuit is needed to carry out the necessary level adjustment, the industry has developed integrated circuits specifically designed to deal with conversion between the two level ranges, to undertake signal inversion, and to accommodate the necessary equipment to generate negative supply voltage (by means of built-in charge pumps).

A complete bidirectional level converter that uses a "Maxim MAX3221"[103](#page-155-1) is illustrated on the following circuit diagram ([Figure](#page-156-0) 138). The circuit has an operational voltage of 3V ... 5V and is protected against voltage peaks (ESD) of ±15kV. The function of the C1 ... C4 capacitors is to increase or invert the voltage.

<span id="page-155-1"></span><sup>103</sup> [http://www.maxim-ic.com](http://www.maxim-ic.com/)





<span id="page-156-0"></span>**Figure 138: Block diagram pin assignment of the MAX32121 level converter** 

The following test circuit [\(Figure](#page-156-1) 139) clearly illustrates the way in which the modules function. In the case of this configuration, a TTL signal (0V ... 3.3V) is applied to line T\_IN. The inversion and voltage increase to ±5V can be seen on lines T\_OUT and R\_IN of the RS-232 output.



<span id="page-156-1"></span>**Figure 139: Functional test on the MAX3221 level converter** 



# <span id="page-157-0"></span>**9 GNSS RECEIVERS**

*If you would like to . . .* 

- o know how a GNSS receiver is constructed
- o understand why several stages are necessary to reconstruct GNSS signals
- o know how an RF stage functions
- o know how the signal processor functions
- o understand how both stages interact
- o know how a receiver module functions

*then this chapter is for you!* 

## <span id="page-157-1"></span>**9.1 Basics of GNSS handheld receivers**

A GNSS receiver can be divided into the following main stages ([Figure](#page-157-2) 140).



<span id="page-157-2"></span>



- **Antenna**: The antenna receives extremely weak satellite signals on a frequency of 1572.42MHz. Signal output is around –163dBW. Some (passive) antennas have a 3dB gain.
- **LNA 1:** This low-noise amplifier (LNA) amplifies the signal by approx. 15 ... 20dB.
- **RF filter:** The GNSS signal bandwidth is approx. 2MHz. The RF filter reduces the affects of signal interference. The RF stage and signal processor actually represent the special circuits in a GNSS receiver and are adjusted to each other.
- **RF stage:** The amplified GNSS signal is mixed with the frequency of the local oscillator. The filtered IF signal is maintained at a constant level in respect of its amplitude and digitalized via Amplitude Gain Control (AGC)
- **IF filter:** The intermediate frequency is filtered out using a bandwidth of several MHz. The image frequencies arising at the mixing stage are reduced to a permissible level.
- **Signal processor:** Up to 16 different satellite signals can be correlated and decoded at the same time. Correlation takes place by constant comparison with the C/A code. The RF stage and signal processor are simultaneously switched to synchronize with the signal. The signal processor has its own time base (Real Time Clock, RTC). All the data ascertained is broadcast (particularly signal transit time to the relevant satellites determined by the correlator), and this is referred to as source data. The signal processor can be programmed by the controller via the control line to function in various operating modes.
- **Controller:** Using the source data, the controller calculates position, time, speed and course etc. It controls the signal processor and relays the calculated values to the display. Important information (such as ephemeris, the most recent position etc.) are decoded and saved in RAM. The program and the calculation algorithms are saved in ROM.
- **Keyboard:** Using the keyboard, the user can select, which coordinate system he wishes to use and which parameters (e.g. number of visible satellites) should be displayed.
- **Display:** The position calculated (longitude, latitude and height) must be made available to the user. This can either be displayed using a 7-segment display or shown on a screen using a projected map. The positions determined can be saved, whole routes being recorded.
- **Power supply:** The power supply delivers the necessary operational voltage to all electronic components.

## <span id="page-158-0"></span>**9.2 GNSS receiver modules**

#### <span id="page-158-1"></span>**9.2.1 Basic design of a GNSS module**

GNSS modules have to evaluate weak antenna signals from at least four satellites, in order to determine a correct three-dimensional position. A time signal is also often emitted in addition to longitude, latitude and height. This time signal is synchronized with UTC (Universal Time Coordinated). From the position determined and the exact time, additional physical variables, such as speed and acceleration can also be calculated. The GNSS module issues information on the constellation, satellite health, and the number of visible satellites etc.

[Figure](#page-159-0) 141 shows a typical block diagram of a GNSS module.

The signals received (1575.42 MHz) are pre-amplified and transformed to a lower intermediate frequency. The reference oscillator provides the necessary carrier wave for frequency conversion, along with the necessary clock frequency for the processor and correlator. The analog intermediate frequency is converted into a digital signal by means of an ADC.

Signal travel time from the satellites to the GNSS receiver is determined by correlating PRN pulse sequences. The satellite PRN sequence must be used to establish this time, otherwise there is no correlation maximum. Data is recovered by mixing it with the correct PRN sequence. At the same time, the useful signal is amplified above the interference level[104](#page-158-2). Up to 16 satellite signals are processed simultaneously. A signal processor carries out the

<span id="page-158-2"></span><sup>104</sup> Satellitenortung und Navigation, Werner Mansfield, page 157, Vieweg Verlag



control and generation of PRN sequences and the recovery of data. Calculating and saving the position, including the variables derived from this, is carried out by a processor with a memory facility.



<span id="page-159-0"></span>**Figure 141: Typical block diagram of a GNSS module** 



# <span id="page-160-0"></span>**10 GNSS applications**

*If you would like to . . .* 

- o know what variables can be determined using GNSS
- o know what applications are possible with GNSS
- o know how time is precisely determined

*then this chapter is for you!* 

## <span id="page-160-1"></span>**10.1 Introduction**

Using GNSS the following two values can be determined anywhere on Earth:

- Exact position (longitude, latitude and height coordinates) accurate to within a range of 20 m to approx. 1mm
- Precise time (Universal Time Coordinated, UTC) accurate to within a range of 60ns to approx. 1ns.

In addition, other values can also be determined, such as:

- speed
- acceleration
- course
- local time
- range measurements

The established fields for GNSS usage are surveying, shipping and aviation. However, satellite navigation is currently enjoying a surge in demand for Location Based Services (LBS) and systems for the automobile industry. Applications such as Automatic Vehicle Location (AVL) and the management of vehicle fleets also appear to be on the rise. In addition, GNSS is increasingly being utilized in communications technology. For example, the precise GNSS time signal is used to synchronize telecommunications networks around the world. Since 2001, the US Federal Communications Commission (FCC) has required that, when Americans call 911 in an emergency, their position be automatically determined to within approx. 125m. This law, known as E-911 (Enhanced 911), necessitates that mobile telephones be upgraded with this new technology.

In the leisure industry, GNSS is becoming increasingly widespread and important. Whether hiking, hunting, mountain biking, or windsurfing across Lake Constance in Southern Germany, a GNSS receiver provides invaluable information for a great variety of situations.

GNSS can essentially be used anywhere on Earth where satellite signal reception is possible and knowledge of position is of benefit.



## <span id="page-161-0"></span>**10.2 Description of the various applications**

GNSS aided navigation and positioning is used in many sectors of the economy, as well as in science, technology, tourism, research and surveying. GNSS can be utilized wherever precise three-dimensional positional data has a significant role to play. A few important sectors are detailed below.

#### <span id="page-161-1"></span>**10.2.1 Location Based Services (LBS)**

Location Based Services (LBS) are services based on the current position of a user (e.g., Mobile Communications Network users equipped with a cell-phone). Normally, the mobile station (e.g. cell-phone) must be logged on and its position given in order to request or obtain specific information/services from the provider. An example of this is the distribution of local information, such as the location of the nearest restaurant or automatically providing the caller position to emergency number services (E-911 or E-112).

The prerequisite for LBS is the determination of accurate position information. Location is determined either through signals from the cell-phone network or through using satellite signals.

The location of the user is either given with absolute geographic coordinates (longitude and latitude) or relative to the position of a given reference point (e.g., "the user is located within a radius of 500m to the monument…"). There are basically two kinds of services provided, known as "push services" or "pull services". A push service sends the user information on the basis of his or her position without their having to request it (e.g. "In the vicinity is …"). A pull service requires that the user first request the information from the service (e.g., calling an emergency number E-911 or E-112).

Knowing location is of critical importance for surviving emergencies. However, public security and rescue services have shown in a study that 60% of those making emergency calls with mobile telephones were unable to communicate their exact position (in comparison to 2% of callers from fixed-net telephones). Every year within the European Union there are 80 million emergency calls made, of these 50% are made with mobile telephones.

The determination of the user's position can either be obtained within the mobile station or by the mobile network. For determining the position the mobile station refers to information from the mobile communication network or satellite signals.

Countless technologies for positioning have already been introduced and have been standardized. Few of these are currently being used and it remains to be seen if all the ideas will ever be realized. In Europe, the most common applications currently being used are:

- Position determination through the identification of active cells in the cell-phone network (Cell-ID). This procedure is also known as Cell of Origin (COO) or Cell Global Identity (CGI).
- Position determination by the time delay of GSM-Signals TA (Timing Advance). TA is a parameter in GSM-Networks through which the distance to the base station can be determined.
- Satellite Positioning through Satellite Navigation: e.g. GNSS

#### <span id="page-161-2"></span>**10.2.2 Commerce and industry**

For the time being, road transportation continues to be the biggest market for GNSS. Of a total market value estimated at 60 billion US-\$ in 2005, 21.6 billion alone was accounted for by road transportation and 10.6 billion by telecommunications technology[105](#page-161-3). Vehicles will be equipped with a computer and a screen, so that a suitable map showing position can be displayed at all times. This will enable selecting the best route to the destination. During traffic jams alternative routes can be easily determined and the computer will calculate the journey time and the amount of fuel needed to get there.

<span id="page-161-3"></span><sup>105</sup> [http://www.alliedworld.com](http://www.alliedworld.com/)



Vehicle navigation systems will direct the driver to his or her destination with visual and audible directions and recommendations. Using the necessary maps stored on CD-ROM and position estimates based on GNSS, the system will determine the most favorable routes.

GNSS is already used as a matter of course in conventional navigation (aviation and shipping). Many trains are equipped with GNSS receivers that relay the train's position to stations down the line. This enables personnel to inform passengers of the arrival time of a train.

GNSS can be used for locating vehicles or as an anti-theft device. Armored cars, limousines and trucks carrying valuable or hazardous cargo will be fitted with GNSS. An alarm will automatically be set off if the vehicle deviates from its prescribed route. With the press of a button the driver can also operate the alarm. Anti-theft devices will be equipped with GNSS receivers, allowing the vehicle to be electronically immobilized as soon as monitoring centers receive a signal.

GNSS can assist in emergency calls. This concept has already been developed to the marketing level. An automobile is equipped with an onboard GNSS receiver connected to a crash detector. In the event of an accident this signals an emergency call center providing precise information about which direction the vehicle was traveling and its current location. As a result, the consequences of an accident can be made less severe and other drivers can be given advanced warning.

Railways are other highly critical transportation applications, where human life is dependent on technology functioning correctly. Precautions need to be taken here against system failure. This is typically achieved through backup systems, where the same task is performed in parallel by redundant equipment. During ideal operating situations, independent sources provide identical information. Well-devised systems indicate (in addition to a standard warning message) if the available data is insufficiently reliable. If this is the case, the system can switch to another sensor as its primary data source, providing self-monitoring and correction. GNSS can provide a vital role here in improving system reliability and safety.

Other possible uses for GNSS include:

- Navigation systems
- Fleet management
- Geographical tachographs
- Railways
- Transport companies, logistics in general (aircraft, water-borne craft and road vehicles)
- Automatic container movements
- Extensive storage sites
- Laying pipelines (geodesy in general)
- Positioning of drill platforms
- Development of open-pit mining
- Reclamation of landfill sites
- Exploration of geological deposits

#### <span id="page-162-0"></span>**10.2.3 Communications technology**

Synchronizing computer clocks is vital in situations with separated processors. The foundation of this is a highly accurate reference clock used to receive GNSS satellite signals along with Network Time Protocol (NTP), specified in RFC 1305.

Other possible uses for GNSS include:

- Synchronization of system time-staggered message transfer
- Synchronization in common frequency radio networks



#### <span id="page-163-0"></span>**10.2.4 Agriculture and forestry**

GNSS contributes to precision farming in the form of area and use management, and the mapping of sites in terms of yield potential. In a precision farming system, combined harvest yields are recorded by GNSS and processed initially into specific plots on digital maps. Soil samples are located with the help of GNSS and the data added to the system. Analysis of these entries then serves to establish the amount of fertilizer that needs to be applied to each point. The application maps are converted into a form that onboard computers can process and are transferred to these computer using memory cards. In this way, optimal practices can be devised over a long term that can provide high time /resource savings and environmental conservation.

Other possible uses for GNSS include:

- Use and planning of areas
- Monitoring of fallow land
- Planning and managing of crop rotation
- Use of harvesting equipment
- Seeding and spreading fertilizer
- Optimizing logging operations
- Pest management
- Mapping diseased and infested areas

For the forest industry as well, there are many conceivable GNSS applications. The USDA (United States Department of Agriculture) Forest Service GPS Steering Committee 1992, has identified over 130 possible applications in this field.

Examples of some these applications are briefly detailed below:

- Optimizing log transportation: By equipping commercial vehicle fleets with onboard computers and GNSS, and using remote data transfer facilities, transport vehicles can be efficiently directed from central operations units.
- Inventory Management: Manual identification prior to timber harvesting is made redundant by satellite navigation. For the workers on site, GNSS can be used as a tool for carrying out specific instructions.
- Soil Conservation: By using GNSS, remote roads and tracks used in harvesting wood can be identified and their frequency of use established.
- Management of private woodlots: In wooded areas divided up into small parcels, cost-effective and highly mechanized harvesting processes can be employed using GNSS, allowing the transport of increased quantities of timber.

#### <span id="page-163-1"></span>**10.2.5 Science and research**

With the advent of the use of aerial and satellite imaging in archaeology, GNSS has also become firmly established in this field. By combining GIS (Geographic Information Systems) with satellite and aerial photography, as well as GNSS and 3D modeling, it has been possible to answer some of the following questions:

- What conclusions regarding the distribution of cultures can be made based on the location of the finds?
- Is there a correlation between areas favoring the growth of certain arable plants and the spread of certain cultures?
- What did the landscape look like in this vicinity 2000 years ago?

Surveyors use (D)GPS, in order to carry out surveys (satellite geodesy) quickly and efficiently to within an accuracy of a millimeter. For surveyors, the introduction of satellite-based surveying represents a progress comparable to that between the abacus and the computer. The applications are endless. These range from land registry and



property surveys to surveying roads, railway lines, rivers and the ocean depths. Geological variations and deformations can be measured and landslides and other potential catastrophes can be monitored, etc.

In land surveying, GNSS has virtually become the exclusive method for pinpointing sites in basic grids. Everywhere around the world, continental and national GNSS networks are developing that, in conjunction with the global ITRF, provide consistent and highly accurate networks of points for density and point-to-point measurements. At a regional level, the number of tenders to set up GNSS networks as a basis for geoinformation systems and cadastral land surveys is growing.

GNSS already has an established place in photogrammetry. Apart from determining coordinates for ground reference points, GNSS is regularly used to determine aerial survey navigation and camera coordinates for aerotriangulation. Using this method, over 90% of ground reference points can be dispensed with. Future reconnaissance satellites will be equipped with GNSS receivers to aid the evaluation of data for producing and updating maps in underdeveloped countries.

In hydrography, GNSS can be used to determine the exact height of a survey boat. This can simplify the establishment of clearly defined reference points. The expectation is that usable GNSS procedures in this field will be operational in the near future.

Other possible areas of application for GNSS are:

- Archaeology
- Seismology (geophysics)
- Glaciology (geophysics)
- Geology (mapping)
- Surveying deposits (mineralogy, geology)
- Physics (flow measurements, time standardization measurement)
- Scientific expeditions
- Engineering sciences (e.g. shipbuilding, general construction industry)
- Cartography
- Geography
- Geo-information technology
- Forestry and agricultural sciences
- Landscape ecology
- Geodesy
- Aerospace sciences



#### <span id="page-165-0"></span>**10.2.6 Tourism and sport**

In sailplane and hang glider competitions GNSS receivers are often used to maintain protocols with no risk of bribery.

GNSS can be used to locate persons who have found themselves in a maritime or alpine emergency. (SAR: Search and Rescue)

Other possible uses for GNSS include:

- Route planning and selecting points of particular significance (natural and culturally/historically significant monuments)
- Orienteering (training routes)
- Outdoor activities and trekking
- Sporting activities

#### <span id="page-165-1"></span>**10.2.7 Military**

GNSS is used anywhere where combatants, vehicles, aircraft and guided missiles are deployed in unfamiliar terrain. GNSS is also suitable for marking the position of minefields and underground depots, as it enables a location to be determined and found again without any great difficulty. As a rule, the more accurate, encrypted GNSS signal (PPS) is used for military applications, and can only be used by authorized agencies.

#### <span id="page-165-2"></span>**10.2.8 Time measurement**

GNSS provides the opportunity to exactly measure time on a global basis. Around the world "time" (UTC Universal Time Coordinated) can be accurately determined to within 1 ... 60 ns. Measuring time with GNSS is much more accurate than with so-called radio clocks, which are unable to compensate for signal travel times between the transmitter and the receiver. If, for example, the receiver is 300 km from the radio clock transmitter, the signal travel time already accounts for 1ms, which is 10,000 times less accurate than time measured by a GNSS receiver. Globally precise time measurements are necessary for synchronizing control and communications facilities, for example.

Currently, the most common method for making precision time comparisons between clocks in different places is a "common-view" comparison with the help of GNSS satellites. Institutes that wish to compare clocks measure the same GNSS satellite signals at the same time and calculate the time difference between the local clocks and GNSS system time. As a result of the differences in measurement, the difference between the clocks at the two institutes can be determined. Because this involves a differential process, GNSS clock status is irrelevant. Time comparisons between the PTB and time institutes are made in this way throughout the world. The PTB atomic clock status, determined with the help of GNSS, is also relayed to the International Bureau for Weights and Measures (BIPM) in Paris for calculating the international atomic time scales TAI and UTC.



# <span id="page-166-0"></span>**Appendix**

## <span id="page-166-1"></span>**A Resources in the World Wide Web**

*If you would like to...* 

- o know, where you can get more information about GNSS
- o know, where the GPS system is documented
- o become a GNSS expert
- *then this chapter is for you!*

## <span id="page-166-2"></span>**A.1 Summary reports and links**

Global Positioning System Overview by Peter H. Dana, University of Colorado

[http://www.colorado.edu/geography/gcraft/notes/gps/gps\\_f.html](http://www.colorado.edu/geography/gcraft/notes/gps/gps_f.html)

Global Positioning System (GPS) Resources by Sam Wormley,

<http://www.edu-observatory.org/gps/gps.html>

NMEA-0183 and GPS Information by Peter Bennett,

<http://vancouver-webpages.com/peter/>

Joe Mehaffey, Yeazel and Dale DePriest's GPS Information

[http://gpsinformation.net](http://gpsinformation.net/)

The Global Positioning Systems (GPS) Resource Library

<http://www.gpsy.com/gpsinfo/>

GPS SPS Signal Specification, 2nd Edition (June 2, 1995), USCG Navigation Center

<http://www.navcen.uscg.gov/pubs/gps/sigspec/default.htm>

## <span id="page-166-3"></span>**A.2 Differential GPS**

Differential GPS (DGPS) by Sam Wormley,

<http://www.edu-observatory.org/gps/dgps.html>

DGPS corrections over the Internet

<http://www.wsrcc.com/wolfgang/gps/dgps-ip.html>

EGNOS Operations Manager

<http://www.essp.be/>

Wide Area Differential GPS (WADGPS), Stanford University

<http://waas.stanford.edu/>

## <span id="page-166-4"></span>**A.3 GPS institutes**

Institute for applied Geodesy: GPS information and observing system

[http://gibs.leipzig.ifag.de/cgi-bin/Info\\_hom.cgi?de](http://gibs.leipzig.ifag.de/cgi-bin/Info_hom.cgi?de)



GPS PRIMER: Aerospace Corporation

<http://www.aero.org/publications/GPSPRIMER/index.html>

U.S. Coast Guard (USCG) Navigation Center

<http://www.navcen.uscg.gov/>

U.S. Naval Observatory

<http://tycho.usno.navy.mil/gps.html>

Royal Institute of Navigation, London

<http://www.rin.org.uk/>

The Institute of Navigation

<http://www.ion.org/>

University NAVSTAR Consortium (UNAVCO)

[http://www.unavco.org](http://www.unavco.org/)

## <span id="page-167-0"></span>**A.4 GNSS newsgroup and GNSS technical journal**

Newsgroup: sci.geo.satellite-nav [http://groups.google.com/groups?oi=djq&as\\_ugroup=sci.geo.satellite-nav](http://groups.google.com/groups?oi=djq&as_ugroup=sci.geo.satellite-nav) Technical journal : GPS World (appears monthly)

[http://www.gpsworld.com](http://www.gpsworld.com/)



<span id="page-168-1"></span><span id="page-168-0"></span>

| Figure 1: The basic function of satellite navigation10                                                               |  |
|----------------------------------------------------------------------------------------------------------------------|--|
| Figure 2: Determining the distance of a lightning flash 12                                                           |  |
| Figure 3: In the simplest case distance is determined by measuring the travel time  13                               |  |
| Figure 4:  With two transmitters it is possible to calculate the exact position despite time errors.  14             |  |
| Figure 5: Four satellites are needed to determine longitude, latitude, altitude and time  14                         |  |
| Figure 6: Determining the signal travel time15                                                                       |  |
| Figure 7: The position of the receiver at the intersection of the two circles  16                                    |  |
| Figure 8: The position is determined at the point where all three spheres intersect  16                              |  |
| Figure 9: Four satellites are required to determine a position in 3-D space.  17                                     |  |
| Figure 10: A geoid is an approximation of the Earth's surface 19                                                     |  |
| Figure 11: Producing a spheroid 19                                                                                   |  |
| Figure 12: Customized local reference ellipsoid 20                                                                   |  |
| Figure 13: Difference between geoid and ellipsoid 20                                                                 |  |
| Figure 14: Illustration of the Cartesian coordinates21                                                               |  |
| Figure 15:  Illustration of the ellipsoidal coordinates 22                                                           |  |
| Figure 16: Geodetic datum23                                                                                          |  |
| Figure 17: Gauss-Krüger projection 25                                                                                |  |
| Figure 18: Principle of projecting one zone (of sixty) 26                                                            |  |
| Figure 19: Designation of the zones using UTM, with examples 26                                                      |  |
| Figure 20: The principle of double projection27                                                                      |  |
| Figure 21: From satellite to position27                                                                              |  |
| Figure 22: Raster map with pixel coordinates X,Y (left) and vector map with geographic coordinates X', Y' (right) 29 |  |
| Figure 23: Definition of the source points30                                                                         |  |
| Figure 24: The 3 calibration points must be well distributed on the map 30                                           |  |
| Figure 25: Raster map with three calibration points 32                                                               |  |
| Figure 26: Determining position with the pixel coordinates X = 643 and Y = 370  33                                   |  |
| Figure 27: Verifying the calculated geographic coordinates with Google Earth  33                                     |  |
| Figure 28: Satellites move along a plane34                                                                           |  |
| Figure 29: Depiction of Kepler's second law 35                                                                       |  |
| Figure 30: Determining the orbital altitude (h) of a satellite  36                                                   |  |
| Figure 31: Satellite orbits36                                                                                        |  |
| Figure 32: Almanac 37                                                                                                |  |
| Figure 33: Azimuth37                                                                                                 |  |
| Figure 34: The three GPS segments43                                                                                  |  |
| Figure 35: GPS satellites orbit the Earth on 6 orbital planes  44                                                    |  |
| Figure 36: 24 hour tracking of a GPS satellite with its effective range  44                                          |  |
| Figure 37: Position of the GPS satellites at 12:00 hrs UTC on 14th April 2001  45                                    |  |
| Figure 38: A GPS satellite 46                                                                                        |  |



|                                                                                                                        | Figure 39: Spectral Power Density of received signal and thermal noise  47 |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Figure 40: Pseudo Random Noise (PRN) 48                                                                                |                                                                            |
| Figure 41: Simplified satellite block diagram 49                                                                       |                                                                            |
| Figure 42: Data structure of a GPS signal49                                                                            |                                                                            |
| Figure 43: Detailed block diagram of a GPS satellite 50                                                                |                                                                            |
| Figure 44: Improvement of position accuracy after the deactivation of SA on May 2, 2000 51                             |                                                                            |
| Figure 45: Improvement of position accuracy as function of time  52                                                    |                                                                            |
| Figure 46: Measuring signal travel time 53                                                                             |                                                                            |
| Figure 47: Demonstration of the correction process across 30 bits 53                                                   |                                                                            |
| Figure 48: Search for the maximum correlation in the code and carrier frequency domains  54                            |                                                                            |
| Figure 49: Spectral power density of the correlated signal and thermal signal noise 55                                 |                                                                            |
| Figure 50: Structure of the entire navigation message 57                                                               |                                                                            |
| Figure 51: Ephemeris terms59                                                                                           |                                                                            |
| Figure 52: With BPSK the navigation data signal is first spread by a code 60                                           |                                                                            |
| Figure 53: Power spectral density of BPSK(1) signals (signal strength normalized at 1 W per signal)  60                |                                                                            |
| Figure 54: Block schematic of a BOC(10,5) modulator61                                                                  |                                                                            |
| Figure 55: With BPSK(1) and BOC(1,1) the signal maxima are separated (signal strength normalized at 1 W per signal) 62 |                                                                            |
| Figure 56: MBOC(6,1,1/11) modulators for L1C and L1 OS 62                                                              |                                                                            |
| Figure 57: Power spectral density of MBOC(6,1,1/11) compared with BPSK(1) (P = 1W per signal) 63                       |                                                                            |
| Figure 58: GPS IIF satellite (left) und GPS III satellite (right)  64                                                  |                                                                            |
| Figure 59: With modernization the number of available GPS frequencies will be increased  65                            |                                                                            |
| Figure 60: Status of GLONASS as of July 200967                                                                         |                                                                            |
| Figure 61: The three orbitals of GLONASS 68                                                                            |                                                                            |
| Figure 62: GLONASS-M satellite and the launch of a Proton-K-DM2 rocket  69                                             |                                                                            |
| Figure 63: GLONASS development plan69                                                                                  |                                                                            |
| Figure 64: By completion of development the measured positioning accuracy should equal that of GPS  70                 |                                                                            |
| Figure 65: Rubidium and Hydrogen-Maser atomic clocks 71                                                                |                                                                            |
| Figure 66: Unlike SARSAT-COSPAS, GALILEO's Search and Rescue service also provides a reply to the distress signal 73   |                                                                            |
| Figure 67: Constellation of the GALILEO satellites (picture: ESA-J.Huart)  75                                          |                                                                            |
|                                                                                                                        |                                                                            |
| Figure 68: GALILEO satellite (Picture: ESA-J.Huart) 75                                                                 |                                                                            |
| Figure 69: Ariane 5 rocket delivering 8 GALILEO satellites into space (GALILEO-industries.net) 76                      |                                                                            |
| Figure 70: Frequencies with reserved bandwidths for GALILEO services  77                                               |                                                                            |
| Figure 71: Planned GALILEO frequencies 77                                                                              |                                                                            |
| Figure 72: GIOVE-A and its launch on December 28, 2005 (picture ESA)  78                                               |                                                                            |
| Figure 73: Launch of 1st Compass MEO satellite in April 2007 with ChangZheng 3A rocket 80                              |                                                                            |
| Figure 74: Four satellite signals must be received81                                                                   |                                                                            |
| Figure 75: Three-dimensional coordinate system 82                                                                      |                                                                            |
| Figure 76: Conversion of the Taylor series83                                                                           |                                                                            |
| Figure 77: Estimating a position84                                                                                     |                                                                            |
| Figure 78: Determination of range (R) based on the signal travel time t (c= speed of light)  86                       |                                                                            |
| Figure 79: Correlation by searching the maxima 87                                                                      |                                                                            |
| Figure 80: Determination of the satellite signal arrival time 87                                                       |                                                                            |



| Figure 82: Telemetry Word (TLM) and Handover Word (HOW) of the navigation message  88                                   |  |
|-------------------------------------------------------------------------------------------------------------------------|--|
| Figure 83: Determination of travel time error89                                                                         |  |
| Figure 84: Example of determination of corrected travel time  90                                                        |  |
| Figure 85: The flatter the angle with which the circles with ranges R1 and R2 intersect, the higher the DOP value 92    |  |
| Figure 86: The larger the enclosed volume, the smaller the DOP value 93                                                 |  |
| Figure 87: DOP values and the number of satellites over an open area during a 24-hour period  94                        |  |
| Figure 88: 24-hour HDOP values, in area with with no shadow/obstruction of satellite visibility (max. HDOP < 1.9) 95    |  |
| Figure 89: 24-hour HDOP values, in area with with strong shadow/obstruction of satellite visibility (max. HDOP > 20) 95 |  |
| Figure 90: DOP values with unfavorable satellite constellation  96                                                      |  |
| Figure 91: DOP values with favorable satellite constellation  96                                                        |  |
| Figure 92: Description of satellite and user position with cartesian coordinates 97                                     |  |
| Figure 93: Effect of the time of measuring on the reflections 101                                                       |  |
| Figure 94:  PSR Measurement error and its dependence on Ionization and Frequency 102                                    |  |
| Figure 95: Principle of DGPS with a GPS base station104                                                                 |  |
| Figure 96: Determination of the correction factors 105                                                                  |  |
| Figure 97: Transmission of the correction factors105                                                                    |  |
| Figure 98: Correction of the measured pseudoranges106                                                                   |  |
| Figure 99:  Principle of the phase measurement 106                                                                      |  |
| Figure 100: Comparison of DGPS systems based on RTCM and RTCA standards 109                                             |  |
| Figure 101: Radio beacon coverage for Australia 111                                                                     |  |
| Figure 102: Coverage areas of the 6 Omnistar satellites (two zones overlap each other)  111                             |  |
| Figure 103: Coverage area of Starfire 112                                                                               |  |
| Figure 104: WAAS area of coverage113                                                                                    |  |
| Figure 105: Satellite orbits and ground tracks of QZSS114                                                               |  |
| Figure 106: QZSS satellite orbits, ground tracks and elevation over Tokyo 114                                           |  |
| Figure 107: Position and coverage of WAAS, EGNOS, GAGAN and MSAS  115                                                   |  |
| Figure 108: Principle of all Satellite Based Augmentation Systems SBAS 116                                              |  |
| Figure 109: LandStar-DGPS and Omnistar illumination zone  117                                                           |  |
| Figure 110: Mobile receiver and block diagram showing integrated GPS module 119                                         |  |
| Figure 111: Time to First Fix (TTFF) with different Aiding-Data as a function of signal strength 120                    |  |
| Figure 112: Acceleration of the search procedure with A-GPS by reducing the search area 120                             |  |
| Figure 113: IGS reference stations (as of November 2007) with approx. 340 active stations 121                           |  |
| Figure 114: Assisted-GPS system 122                                                                                     |  |
| Figure 115: With Online A-GPS, Aiding-Data is continuously transmitted 123                                              |  |
| Figure 116: From the Almanac data precise orbital data (True Orbits) are calculated 123                                 |  |
| Figure 117: With Control Plane Architecture the mobile network must be altered  124                                     |  |
| Figure 118: With User Plane Architecture the mobile network requires no alteration  125                                 |  |
| Figure 119: Block diagram with components according to OMA  127                                                         |  |
| Figure 120: Block Diagram of input stages 128                                                                           |  |
| Figure 121: GNSS Repeater (external antenna, electrical adapter and power cord, amplifier and internal antenna)  129    |  |
| Figure 122: Block diagram of a GNSS receiver with interfaces 130                                                        |  |
| Figure 123: NMEA format (TTL and RS-232 level) 132                                                                      |  |
| Figure 124: Google Earth with Detail142                                                                                 |  |



| Figure 125: Track, consisting of 3 measurements, displayed by u-center 143    |  |
|-------------------------------------------------------------------------------|--|
| Figure 126: Depiction of latitude and longitude values 144                    |  |
| Figure 127: KML File (3_point_Chur.kml) of the track144                       |  |
| Figure 128: KML file, displayed with Google Earth145                          |  |
| Figure 129: Construction of the RTCM message header  146                      |  |
| Figure 130: Total frames with RTCM SC-104 (Version 2.x) 147                   |  |
| Figure 131: Construction of RTCM message type 1 148                           |  |
| Figure 132: Structure of the UBX data sets151                                 |  |
| Figure 133: Passive open (left) and active enclosed Patch antennas 153        |  |
| Figure 134: Passive (left) and active helix antenna154                        |  |
| Figure 135: Chip antenna154                                                   |  |
| Figure 136: 1PPS signal 155                                                   |  |
| Figure 137: Difference between TTL and RS-232 levels156                       |  |
| Figure 138: Block diagram pin assignment of the MAX32121 level converter  157 |  |
| Figure 139: Functional test on the MAX3221 level converter  157               |  |
| Figure 140: Simplified block diagram of a GNSS receiver  158                  |  |
| Figure 141: Typical block diagram of a GNSS module 160                        |  |
|                                                                               |  |

<span id="page-171-0"></span>

| Table 1: National reference systems21                                                                       |  |
|-------------------------------------------------------------------------------------------------------------|--|
| Table 2: The WGS-84 ellipsoid22                                                                             |  |
| Table 3: Datum parameters23                                                                                 |  |
| Table 4: Satellite communication and navigation frequencies  39                                             |  |
| Table 5: Time systems, January 200941                                                                       |  |
| Table 6: L1 carrier link budget analysis modulated with the C/A code 46                                     |  |
| Table 7: Comparison between ephemeris and almanac data  58                                                  |  |
| Table 8: Planned positioning accuracies for GALILEO 74                                                      |  |
| Table 9: Frequency plan of GALILEO and distribution of services 76                                          |  |
| Table 10: Comparison of the most important properties of GPS, GLONASS and GALILEO (as of February 2008)  79 |  |
| Table 11:  Error causes (typical ranges) 91                                                                 |  |
| Table 12: Total error in HDOP = 1.397                                                                       |  |
| Table 13: Transmission process of the differential signal (for code and phase measurement)  107             |  |
| Table 14: Standards for DGPS correction signals108                                                          |  |
| Table 15: The GEO satellites used by WAAS, EGNOS and MSAS (as of February 2008)  115                        |  |
| Table 16: Designation of the SBAS stations 116                                                              |  |
| Table 17: Positioning accuracy without and with DGPS/SBAS  118                                              |  |
| Table 18: Comparison of advantages of User-plane vs. Control-plane Architectures  126                       |  |
| Table 19: Description of the individual NMEA DATA SET blocks 133                                            |  |
| Table 20: Recording of an NMEA protocol133                                                                  |  |
| Table 21: Description of the individual GGA data set blocks  134                                            |  |
| Table 22: Description of the individual GGL data set blocks 135                                             |  |
| Table 23: Description of the individual GSA data set blocks 136                                             |  |



| Table 24: Description of the individual GSV data set blocks  137      |  |
|-----------------------------------------------------------------------|--|
| Table 25: Description of the individual RMC data set blocks  138      |  |
| Table 26: Description of the individual VTG data set blocks  139      |  |
| Table 27: Description of the individual ZDA data set blocks  140      |  |
| Table 28: Determining the checksum in the case of NMEA data sets  141 |  |
| Table 29: Contents of the RTCM message header 146                     |  |
| Table 30: Contents of RTCM message type 1 149                         |  |
| Table 31: RTCM SC-104 Version 2.3 message types 150                   |  |
| Table 32: Message classes (Hexadecimal values in brackets) 152        |  |
|                                                                       |  |

## <span id="page-172-0"></span>**B.3 Sources**

| [I]                                                                                                                    | Global Positioning System, Standard Positioning System Service,<br>Signal Specification, 2nd Edition, 1995, page 18, http://www.navcen.uscg.gov/pubs/gps/sigspec/gpssps1.pdf |  |  |  |  |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| [II]                                                                                                                   | NAVCEN: GPS SPS Signal Specifications, 2nd Edition, 1995, http://www.navcen.uscg.gov/pubs/gps/sigspec/gpssps1.pdf                                                            |  |  |  |  |
| [III]                                                                                                                  | Lemme H.: Schnelles Spread-Spectrum-Modem auf einem Chip, Elektronik 1996,<br>H. 15 p. 38 to p. 45                                                                           |  |  |  |  |
| [IV]                                                                                                                   | http://www.maxim-ic.com/appnotes.cfm/appnote_number/1890                                                                                                                     |  |  |  |  |
| [V]                                                                                                                    | Parkinson B., Spilker J.: Global Positioning System, Volume 1, AIAA-Inc.                                                                                                     |  |  |  |  |
| [VI]                                                                                                                   | GPS Standard Positioning Service Signal Specification, 2nd Edition, June 2, 1995                                                                                             |  |  |  |  |
| [VII]                                                                                                                  | Journal of the Institute of Navigation, 2002, Vol.48, No. 4, pp 227-246, Author: John W. Betz                                                                                |  |  |  |  |
| [VIII]                                                                                                                 | http://www.glonass-center.ru/nagu.txt                                                                                                                                        |  |  |  |  |
| [IX]                                                                                                                   | http://www.dlr.de/dlr/News/pi_191004.htm                                                                                                                                     |  |  |  |  |
| [X]                                                                                                                    | http://www.cospas-sarsat.org/Status/spaceSegmentStatus.htm                                                                                                                   |  |  |  |  |
| [XI]                                                                                                                   | http://europa.eu.int/comm/dgs/energy_transport/galileo/documents/brochure_en.htm                                                                                             |  |  |  |  |
| [XII]                                                                                                                  | http://www.esa.int/esaCP/SEMT498A9HE_Austria_0.html                                                                                                                          |  |  |  |  |
| [XIII]                                                                                                                 | http://europa.eu.int/scadplus/leg/de/lvb/l24004.htm                                                                                                                          |  |  |  |  |
| [XIV]                                                                                                                  | http://www.spiegel.de/wissenschaft/weltraum/0,1518,392467,00.html                                                                                                            |  |  |  |  |
| [XV]                                                                                                                   | http://www.esa.int/esaCP/SEMQ36MZCIE_Improving_0.html                                                                                                                        |  |  |  |  |
| [XVI]                                                                                                                  | http://www.esa.int/esaCP/SEM0198A9HE_Germany_0.html                                                                                                                          |  |  |  |  |
| [XVII]<br>Manfred Bauer: Vermessung und Ortung mit Satelliten, Wichman-Verlag, Heidelberg, 1997,<br>ISBN 3-87907-309-0 |                                                                                                                                                                              |  |  |  |  |
| [XVIII]                                                                                                                | http://www.geocities.com/mapref/mapref.html                                                                                                                                  |  |  |  |  |
| [XIX]                                                                                                                  | B. Hofmann-Wellenhof: GPS in der Praxis, Springer-Verlag, Wien 1994, ISBN 3-211-82609-2                                                                                      |  |  |  |  |
| [XX]                                                                                                                   | Bundesamt für Landestopographie: http://www.swisstopo.ch                                                                                                                     |  |  |  |  |
| [XXI]                                                                                                                  | Elliott D. Kaplan: Understanding GPS, Artech House, Boston 1996,<br>ISBN 0-89006-793-7                                                                                       |  |  |  |  |
| [XXII]                                                                                                                 | http://www.tandt.be/wis                                                                                                                                                      |  |  |  |  |
| [XXIII]                                                                                                                | http://www.egnos-pro.esa.int/IMAGEtech/imagetech_realtime.html                                                                                                               |  |  |  |  |
| [XXIV]                                                                                                                 | http://igscb.jpl.nasa.gov/                                                                                                                                                   |  |  |  |  |
| [XXV]                                                                                                                  | GPS-World, November 2003: Vittorini und Robinson: Optimizing Indoor GPS Performance, page 40                                                                                 |  |  |  |  |
| [XXVI]                                                                                                                 | www.maxim-ic.com/quick_view2.cfm Datenblatt MAX2640, MAX2641                                                                                                                 |  |  |  |  |
| [XXVII]                                                                                                                | NMEA 0183, Standard For Interfacing Marine Electronics Devices, Version 2.30                                                                                                 |  |  |  |  |
| [XXVIII]                                                                                                               | http://www.navcen.uscg.gov/pubs/dgps/rctm104/Default.htm                                                                                                                     |  |  |  |  |
| [XXIX]                                                                                                                 | Global Positioning System: Theory and Applications, Volume II, Bradford W. Parkinson, page 31                                                                                |  |  |  |  |



- [XXX] User Manual: Sony GXB1000 16-channel GPS receiver module
- [XXXI] User Manual: Sony GXB1000 16-channel GPS receiver module
- [XXXII] swipos, Positionierungsdienste auf der Basis von DGPS, page 6, Bundesamt für Landestopographie
- [XXXIII] [http://www.potsdam.ifag.de/potsdam/dgps/dgps\\_2.html](http://www.potsdam.ifag.de/potsdam/dgps/dgps_2.html)
- [XXXIV] [http://www.maxim-ic.com](http://www.maxim-ic.com/)
- [XXXV] Satellitenortung und Navigation, Werner Mansfield, page 157, Vieweg Verlag
- [XXXVI] [http://www.alliedworld.com](http://www.alliedworld.com/)

## <span id="page-173-0"></span>**C Revision history**

| Revision | Date       | Name | Status / Comments                                                                                                                                                                                                                                                 |
|----------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -        | 11/10/2001 | jzog | Initial release                                                                                                                                                                                                                                                   |
| A        | 1/12/2006  | jzog | Update of Chapters:<br><br>SBAS (WAAS, EGNOS)<br><br>GPS Modernization<br><br>Galileo<br><br>High Sensitivity GPS<br><br>AGPS Errors and DOP<br><br>UTM-Projection<br><br>DGPS-Services<br><br>Proprietary Data Interfaces<br><br>GPS Receivers          |
| B        | 27/2/2007  | tgri | Update of Chapters:<br><br>Introduction to Satellite Navigation<br><br>Satellite Navigation made simple                                                                                                                                                         |
| C        | 26/4/2007  | tgri | Update of Sections:<br><br>Space Segment<br><br>User Segment<br><br>The GPS Message<br><br>Calculating a position (equations)<br><br>DGPS Services for real-time correction<br><br>Wide Area DGPS<br><br>Hardware Interfaces<br><br>GNSS Receiver Modules |
| D        | 7/9/2009   | jzog | Completely revised edition                                                                                                                                                                                                                                        |