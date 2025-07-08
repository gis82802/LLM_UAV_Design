

## **Information Note**

**Author Topic GPS week number roll-over workaround for u-blox GNSS receivers** UBX-19039990 JunJun Lu

**Date** 10 September 2019

Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

## **1 Description of issue and workaround**

Because the GPS L1 C/A signal presents the GPS week number with only 10 bits, the week number rolls from 1023 to 0 every 19.6 years. The GPS week number has now rolled over twice since starting the GPS era in January 1980. These roll-overs first happened in August 1999, followed by a recent one in April 2019. The next roll-over will happen in November 2038.

To mitigate the impact of the GPS week number roll-over, u-blox has adopted the common industry practice of using a compensation value for delaying the roll-over impact until about 20 years from the creation of the GNSS receiver firmware. All u-blox GNSS receivers are performing well after the recent April 2019 GPS week number roll-over.

In a continuous effort to offer excellent technical support to the customers, u-blox has evaluated all u-blox 5, 6, 7, 8 and M8 receivers and listed the GPS week number roll-over compensation value for each u-blox GNSS receiver firmware version as shown in **[Table 1](#page-0-0)**.

| Generation  | Firmware | Week number | Start date | End date   |
|-------------|----------|-------------|------------|------------|
| u-blox 5    | 5.x      | 1460        | 2007-12-30 | 2027-08-14 |
|             | 6.x      | 1528        | 2009-04-19 | 2028-12-02 |
| u-blox 6    | 6.x      | 1528        | 2009-04-19 | 2028-12-02 |
|             | 7.x      | 1603        | 2010-09-26 | 2030-05-11 |
|             | 1.x      | 1691        | 2012-06-03 | 2032-01-17 |
| u-blox 7    | 7.x      | 1603        | 2010-09-26 | 2030-05-11 |
|             | 1.x      | 1691        | 2012-06-03 | 2032-01-17 |
| u-blox 8/M8 | 2.0x     | 1756        | 2013-09-01 | 2033-04-16 |
|             | 3.0x     | 1867        | 2015-10-18 | 2035-06-02 |
|             | 3.5x     | 1936        | 2017-02-12 | 2036-09-27 |

<span id="page-0-0"></span>**Table 1: Default GPS week number roll-over compensation values of u-blox GNSS receivers**

For more information and recommended workarounds, refer to the Application Note **[\[1\].](#page-1-0)**



## **2 Customer impact and recommended action**

As a result of the GPS week number roll-over, the GNSS receiver will show a 20-year-old date when only GPS satellites are used after expiry of the "end-date" mentioned in [Table 1.](#page-0-0) The rollover only impacts the displaying of the date. It does not impact the navigation function, time of day information, or time pulse accuracy.

It is recommended that customers study the application note and take the necessary measures to mitigate the possible impact of the GPS week number roll-over whenever applicable.

## **3 Reference documents**

<span id="page-1-0"></span>[1] GPS Week Number Roll-over Workaround Application Note, [UBX-19016936](https://www.u-blox.com/sites/default/files/GPS-WeekNumber-Rollover-Workaround_AppNote_%28UBX-19016936%29.pdf)