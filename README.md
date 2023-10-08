# Develop the Oracle of DISCOVR

> Team: Shockwave Surfers [:link:](https://www.spaceappschallenge.org/2023/find-a-team/shockwave-surfers/)

> NASA Space Apps Challenge Tacoma Location [:link:](https://www.spaceappschallenge.org/2023/locations/tacoma-wa/)

----
### Usage

In the shell

Install the dependencies
```bash
pip install -r requirements.txt
```

Acquire the data, only once (if data is already there no need to repeat)
```bash
python3 01_preprocessing/01-aqcuire.py
```

Unzip the data, only once (if data is already there no need to repeat)
```bash
python3 01_preprocessing/02-unzip-data-files.py
```

Optionally delete the zip files
```bash
python3 01_preprocessing/03-delete-zip-files.py 
```

### Run the app

In the shell type
```bash
streamlit run main.py
```

### Notes
* Experimentation Data
  * 1 minute timestamp in UTC (1st column) 
  * Working with magnetic field vector data (2nd - 4th columns)
    * expressed in units of nanoTesla (nT) and provided in the Geocentric Solar Ecliptic reference frame (GSE)
    * Total vector bt = bx + by + bz
  * Last fifty values (columns 5-54) represent a "raw" measurement spectrum interval from the Faraday cup plasma detector. With each value corresponding to the flow strength of the solar wind in a particular range of energies (or flow speeds). Hence each column represents a particular interval for the range of flow speeds.
* kP Index Data
  * Goes off 3 hour intervals

### NEXT TODO
* Centralize data storage for easy access
* Data Cleaning and Visualization
  * Experimentation data
  * Canadian data
    * Ground observatories
      * CARISMA
        * Interprating data
          * https://carisma.ca/carisma-data/fgm-data-format
    * Canadian satellite
  * kP Index data
    * Compare to experimentation data for predicting kP index
    * Can this comparison be used to spot the anomalies?
* Use other data to validate experimentation data
  * What are the anomalies?
* Build the model
  * Pytorch vs Tensorflow?
  * Predict kP index
  * How do anamolies affect the model?
  * Classification of larger kP index storms?
* Presentation method
  * Slides and video for demonstration/explanation?

----

### Reference

#### DISCOVR

* __develop-the-oracle-of-dscovr__  challenge description [:link:](https://www.spaceappschallenge.org/2023/challenges/develop-the-oracle-of-dscovr/)

* Faraday Cup | Wikipedia [:link:](https://en.wikipedia.org/wiki/Faraday_cup) 

* DSCOVR portal [:link:](https://www.ngdc.noaa.gov/dscovr/portal/#/#swi)
* Glossary: [:link:](https://nesdis-prod.s3.amazonaws.com/migrated/dscovr_glossary.pdf?_ga=2.40759142.51687696.1696295331-1439926062.1696295331)
* SME discussion | github [:link:](https://github.com/nasa/spaceapps/discussions/361)
* https://donnees-data.asc-csa.gc.ca/dataset/98466021-2q1w-5g2d-677zwru214wx68
* https://omniweb.gsfc.nasa.gov/form/dx2.html
* https://hpde.io/NASA/NumericalData/OMNI/PT1H
* https://omniweb.gsfc.nasa.gov/coho/form/helios1_f.html
* https://www.swpc.noaa.gov/products/planetary-k-index
  * -> Products and Data
    * -> Observations - Boulder magnetometer
      * https://www.swpc.noaa.gov/products/boulder-magnetometer
        * -> Data  https://www.usgs.gov/programs/geomagnetism
          * -> Data -> Programmatic Access to Geomagnetism Data
            *  https://code.usgs.gov/ghsc/geomag/geomag-algorithms  (Geomag Algorithms is an open source library for processing
Geomagnetic timeseries data. It includes algorithms and input/output factories
used by the USGS Geomagnetism Program to
translate between data formats,
generate derived data and indices in near-realtime,
and research and develop new algorithms.)
* papers

  - CCMC, Shreeya Khurana [:link:](https://ccmc.gsfc.nasa.gov/RoR_WWW/SWREDI/contest-presentations/2017/CCMCPaper_ShreeyaKhurana_Final.pdf)

  - Level one requirements, pg. 9 [:link:](https://www.space.commerce.gov/wp-content/uploads/DSCOVR-L1RD-Signed-NOAA-NASA-v1.1-Aug-15-2013-FINAL-2.pdf)
#### Space Weather

* Space Weather Prediction Center (SWPC) | NOAA [:link:](https://www.swpc.noaa.gov/)
* 

#### Python
* python-download-file-from-url  realpython.com [:link:](https://realpython.com/python-download-file-from-url/)
