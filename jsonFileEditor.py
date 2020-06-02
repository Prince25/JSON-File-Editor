import os
import json

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [ Created by: Prabhjot (Prince) Singh, 2020 ]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class JsonFile:
  def __init__(self, filename: str, directory: str = os.getcwd()):
    if filename is None or directory is None or filename is '' or directory is ''\
      or type(filename) is not str or type(filename) is not str:
      raise Exception('Usage: file = JsonFile(filename: str, [directory: str])')
    
    # Ensure file name has the extension
    if filename[-5:] != '.json':
      filename += '.json'
    
    self.name = filename
    self.dir = directory
    self.path = os.path.join(self.dir, self.name)

    # Create directory if it doesn't exist
    if not os.path.isdir(self.dir):
      print("Directory doesn't exist. Creating new directory.")
      os.mkdir(self.dir)

    # Creates JSON file with empty dict if it doesn't exist
    self.file = open(self.path, 'a')
    if os.stat(self.path).st_size == 0:
      self.file = open(self.path, 'r+')
      json.dump({}, self.file, indent=2)
    self.file.close()
    print("File Created: " + self.path + "\n")
  

  # Adds a single entry to the file (key: str, data: dict, [verbose: bool])
  # Returns False if key already exists, True if added successfully
  def addSingleEntry(self, key: str, data: dict, verbose: bool = True):
    if self.file.closed:  # Open file for reading+writing if closed
      self.file = open(self.path, "r+")

    try:
      if type(key) is not str:
        raise Exception('Key is not of type string')

      # 
      file_data = json.load(self.file)
      if key in file_data.keys():
        print(f'Key {key} already exists!')
        self.file.seek(0)
        return False

      if type(data) is dict:
        if verbose: print('Writing data to file: ', {key: data})
        file_data.update({key: data})
        self.file.seek(0)
        json.dump(file_data, self.file, indent=2)
      else:
        raise Exception('Data is not of type dict')

    finally: 
      self.file.close()
      return True

  