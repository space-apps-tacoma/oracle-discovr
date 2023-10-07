import zipfile
from os import walk

from loguru import logger

relative_path_to_data = "data/"

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
filenames = next(walk(relative_path_to_data), (None, None, []))[2]  # [] if no file

msg = "Unzipping files:"
logger.info(msg)
for filename in filenames:
  path_to_zip_file = relative_path_to_data + filename
  logger.info(path_to_zip_file)

  with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
      try:
          zip_ref.extractall(relative_path_to_data)    
      except BadZipFile as e:
          logger.info(e)
