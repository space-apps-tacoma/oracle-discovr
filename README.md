# Develop the Oracle of DISCOVR

> Team: Shockwave Surfers [:link:](https://www.spaceappschallenge.org/2023/find-a-team/shockwave-surfers/)

> NASA Space Apps Challenge Tacoma Location [:link:](https://www.spaceappschallenge.org/2023/locations/tacoma-wa/)

----
### Data Collection

#### NASA DSCOVR Experimentation Data

To download and extract the experimentation data, perform the following.

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

#### Canada Carisma Magnetometer Network

Data from Canada's magnetometer network can be downloaded from this [site](https://donnees-data.asc-csa.gc.ca/dataset/06f5e364-6e2c-4d1c-95c2-9fb7d871ca20) for the 2016 and 2017 years to validate the readings of the magnetic field vector from NASA's experimentation data. The .tar files will need to be downloaded to your personal system due to large file size.

Once the desired .tar files have been downloaded, you can run the following to extract the files from the .tar encryption. Be sure to change directory to the directory housing your tar file for extraction.

```bash
python3 file_path_to/tar_extract.py your_tar_file_name desired_directory_for_extracted_file
```

After the .tar file contents have been extracted to a directory for the year, nesting directories for month and days, then you'll need to extract the data from the gzip files.

From your terminal you can run `gz_extract.py` with the proper parameters to extract the data from the gzip files.

Utilizing code within `carisma_preprocess_to_csv.ipynb`, the text files extracted from the gzip files could then be cleaned, condensed, and put into a csv for ease of use.

Finally, `carisma_preprocesses_data_selected_range.ipynb` could then be used to select a specific range of data for assessment.

----

### References

#### NASA and Canadian Space Agency

* __develop-the-oracle-of-dscovr__  challenge description [:link:](https://www.spaceappschallenge.org/2023/challenges/develop-the-oracle-of-dscovr/)

* Experimentation Data [:link:](https://www.spaceappschallenge.org/develop-the-oracle-of-dscovr-experimental-data-repository/)

* Faraday Cup | Wikipedia [:link:](https://en.wikipedia.org/wiki/Faraday_cup) 

* DSCOVR portal [:link:](https://www.ngdc.noaa.gov/dscovr/portal/#/#swi)
* Glossary: [:link:](https://nesdis-prod.s3.amazonaws.com/migrated/dscovr_glossary.pdf?_ga=2.40759142.51687696.1696295331-1439926062.1696295331)
* SME discussion | github [:link:](https://github.com/nasa/spaceapps/discussions/361)
* https://donnees-data.asc-csa.gc.ca/dataset/98466021-2q1w-5g2d-677zwru214wx68
* https://omniweb.gsfc.nasa.gov/form/dx2.html
* https://carisma.ca/carisma-data/fgm-data-format
* https://science.nasa.gov/mission/dscovr/
* https://hpde.io/NASA/NumericalData/OMNI/PT1H
* https://omniweb.gsfc.nasa.gov/coho/form/helios1_f.html
* https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-information-policy/data-levels 
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
