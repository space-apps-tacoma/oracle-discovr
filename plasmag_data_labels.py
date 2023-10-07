"""
What is in a measurement set?

Each line begins (column 0) with a date and time in Coordinated Universal Time
(UTC), formatted like YYYY-MM-DD hh:mm:ss. So, for example,
October 7, 2023 at 9:00 a.m in Greenwich, England, would be
written 2023-10-07 09:00:00.

The next three values in the line (columns 1-3) represent components of the
magnetic field vector that was measured at this time. They are expressed in
units of nanoTesla (nT) and provided in the Geocentric Solar Ecliptic
reference frame (GSE).
    https://sscweb.gsfc.nasa.gov/users_guide/Appendix_C.shtml

The last fifty values (columns 4-53) represent a "raw" measurement spectrum
from the Faraday cup plasma detector. Each value corresponds to the flux, or
flow strength, of the solar wind in a particular range of energies
(or flow speeds). These numbers are not calibrated or converted-- they are
dimensionless numbers as encoded in the instrument computer.
"""
data_labels = [
"utc_date","bx","by","bz",
"fs01",
"fs02",
"fs03",
"fs04",
"fs05",
"fs06",
"fs07",
"fs08",
"fs09",
"fs10",
"fs11",
"fs12",
"fs13",
"fs14",
"fs15",
"fs16",
"fs17",
"fs18",
"fs19",
"fs20",
"fs21",
"fs22",
"fs23",
"fs24",
"fs25",
"fs26",
"fs27",
"fs28",
"fs29",
"fs30",
"fs31",
"fs32",
"fs33",
"fs34",
"fs35",
"fs36",
"fs37",
"fs38",
"fs39",
"fs40",
"fs41",
"fs42",
"fs43",
"fs44",
"fs45",
"fs46",
"fs47",
"fs48",
"fs49",
"fs50"
]