import os
import pathlib
from os import walk

from loguru import logger

relative_path_to_data = "data/"

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
filenames = next(walk(relative_path_to_data), (None, None, []))[2]  # [] if no file

msg = "Deleting zip files:"
logger.info(msg)
for filename in filenames:
  path_to_zip_file = relative_path_to_data + filename
  #logger.info(path_to_zip_file)
  if pathlib.Path(path_to_zip_file).suffix == ".zip":
      # delete this file
      msg = "Deleting " + path_to_zip_file
      logger.info(msg)
      os.remove(path_to_zip_file)

    