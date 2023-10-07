#from requests.sessions import _FileName
from loguru import logger
import os
import requests
from urllib.parse import urlparse

#
relative_path_to_data = "data/"

# links supplied by page
#    https://www.spaceappschallenge.org/develop-the-oracle-of-dscovr-experimental-data-repository/

links_2_data = {
    "y2016":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2016_v01.zip",
    "y2017":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2017_v01.zip",
    "y2018":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2018_v01.zip",
    "y2019":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2019_v01.zip",
    "y2020":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2020_v01.zip",
    "y2021":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2021_v01.zip",
    "y2022":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2022_v01.zip",
    "y2023":
    "https://opensource.gsfc.nasa.gov/spaceappschallenge/dsc_fc_summed_spectra_2023_v01.zip"
}

msg = "Downloading data from:"
logger.info(msg)
for year, url in links_2_data.items():
  msg = year + " => " + url
  logger.info(msg)
  response = requests.get(url, stream=True)
  a = urlparse(url)
  file_name = os.path.basename(a.path)
  path_plus_file = relative_path_to_data + file_name
  logger.info(path_plus_file)
  
  with open(path_plus_file, mode="wb") as file:
    for chunk in response.iter_content(chunk_size=10 * 1024):
      file.write(chunk)
