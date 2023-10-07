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
* On replit.com
  * Then press the green `Run` button.
  * View the app in the Webview pane
    *  To see full screen, press the Webview "Open in a new tab" button

### NEXT TODO
* 
* figure out if 'b' column labels are accurate
  * bx, by, bz were a guess. What is the correct orientation 
* evaluate csv with pandas etc
* add `tensorflow` to the project as part of stream lit?
* calculate total vector bt = bx + by + bz for each row?
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
