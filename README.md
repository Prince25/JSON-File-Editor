# JSON File Editor
I couldn't find anything similar to this so I decided to write it myself.\
Create and edit JSON files with Python!

## Usage
* Constructor: JsonFile(filename: str, [directory: str])
  * filename: Name of JSON file you wish to create or edit (adding .json extension isn't necessary)
  * directory: OPTIONAL. Default: current working directory. The path of where the JSON file should be created. If a JSON file with the name of filename already exists at that directory, it will open it for editing.
  * Examples
  ```
  from jsonFileEditor import JsonFile
  file = JsonFile('example')
  file2 = JsonFile('example2.json', os.path.join(os.getcwd(), 'files'))
  ```
  
* Method: addSingleEntry(key: str, data: dict, [verbose: bool])\
  Adds a single key, value pair to the file. Returns False if key already exists, True if added successfully.
  * key: key as string
  * data: dictionary of data 
  * verbose: OPTIONAL. Default: True. Prints whatever is written to the file.
  * Examples (assuming an object has already been constructed) 
  ```
  dict1 = {'name': 'prince', 'age': 25}
  file.addSingleEntry('86fsdf', dict1, False)
  file.addSingleEntry('2f54s2', {'name': 'Sonia', 'age': 22})
  ```
  * Console
  ```
  Writing data to file:  {'2f54s2': {'name': 'Sonia', 'age': 22}}
  ```
  * JSON File
  ```
  {
    "86fsdf": {
      "name": "prince",
      "age": 25
    },
    "2f54s2": {
      "name": "Sonia",
      "age": 22
    }
  }
  ```
