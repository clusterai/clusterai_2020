# clusterai_2020
Repository for the UTN BA Data Science Course 2020 
## Installing dependancies / Instalando dependencias
##### English
Before we start working we need to install all dependancies for this project.

Open the command line or anaconda prompt and run:

```bash
pip install -r requirements.txt
```
Remember to ALWAYS do this before you start working on the repository

##### Español
Antes de arrancar a trabajar en este proyecto necesitamos instalar las dependencias de este proyecto.

Abri la linea de comandos o el anaconda prompt y corre

```bash
pip install -r requirements.txt
```

Recorda hacer esto SIEMPRE antes de empezar a trabajar con el repositorio

## Working with datasets / Trabajando con datasets
### Use a dataset / Usar un dataset
##### English
The idea is to let the users import the dataset as a module within the jupyter notebook or python script.

First of all we need to add the datasets path to our PYTHONPATH in order to be able to import the module
```python
# Use this from inside a jupyter notebook (file.ipynb)
import pathlib
import sys
sys.path.append(str([path for path in list(pathlib.Path().resolve().parents) if str(path).endswith('clusterai_2020')][0]))

# Use this for a python script (file.py)
import pathlib
import sys
sys.path.append(str([path for path in list(pathlib.Path(__file__).resolve().parents) if str(path).endswith('clusterai_2020')][0]))
```
Afterwards we will be able to import the datasets module directly
```python
# Dot notation
import datasets.<Dataset Group Name> 
# Explicit notation (recommended)
from datasets import <Dataset Group Name> as <Name>
```

Each dataset module will have a download function associaten which takes the source and destination as an input, returning the path where it left the downloaded file.

```python
# Dot notation examples
## Example of download from cluster ai server to run on google collaboratory
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='clusterAI',destination='gcollaboratory')
## Example of download from origin server to run on google collaboratory
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='origin',destination='gcollaboratory')
## Example of download from cluster ai server to run locally on your computer
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='clusterAI',destination='local')
## Example of download from origin server to run locally on your computer
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='origin',destination='local')

# Explicit notation examples
## Example of download from cluster ai server to run on google collaboratory
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='clusterAI',destination='gcollaboratory')
## Example of download from origin server to run on google collaboratory
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='origin',destination='gcollaboratory')
## Example of download from cluster ai server to run locally on your computer
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='clusterAI',destination='local')
## Example of download from origin server to run locally on your computer
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='origin',destination='local')
```
As I have the path stored in the variable myDatasetPath, I can directly load it on pandas. 

```python
import pandas as pd
myDataset = pd.read_csv(myDatasetPath)
```

Here an example on complexity where a dataset module has more than one file to be dowloaded

```python
import pandas as pd
import datasets.acero
import pathlib

# Check possible datasets:
print(datasets.acero.resources())

# First approach - downloading one dataset at a time
## Downloading specific resource -> myDatasetPath contains str with path
myDatasetPath = datasets.acero.download(resource=<Dataset Name>,source='origin',destination='local')

myDataset = pd.read_csv(myDatasetPath)

# Second approach - downloading all datasets at once - Unsopported for now
## Downloading all resources -> myDatasetPath contains List[str] with each path
myDatasetPaths = datasets.acero.download(source='origin',destination='local')

myDatasetsDict = {}
for datasetPath in myDatasetPaths:
    dataset = pathlib.PurePath(datasetPath)
    myDatasetsDict.setdefault(keyname=dataset.name, value=pd.read_csv(datasetPath))

## myDatasetsDict will have a key for each dataset in the module

print(myDatasetsDict.keys) #shows all loaded datasets

specificDataset = myDatasetsDict.get("datasetName") # datasetName is one of the keys of myDatasetsDict 
```
It's recomended to use the first approach due to it's legibility and simplicity in usage per dataset

##### Español
La idea es permitirle a los usuarios importar el dataset como un modulo dentro del juyter notebook o el script de python.

Antes que nada, tenemos que agregar la carpeta datasets a nuestro PYTHONPATH para poder importar el modulo
```python
# Correr esto si estas dentro de un jupyter notebook (file.ipynb)
import pathlib
import sys
sys.path.append(str([path for path in list(pathlib.Path().resolve().parents) if str(path).endswith('clusterai_2020')][0]))

# Correr esto si estas dentro de un script python (file.py)
import pathlib
import sys
sys.path.append(str([path for path in list(pathlib.Path(__file__).resolve().parents) if str(path).endswith('clusterai_2020')][0]))
```
Luego podremos importar el modulo directamente

```python
# Notacion con punto
import datasets.<Dataset Group Name>
# Notacion explicita (recomendada)
from datasets import <Dataset Group Name> as <Name>
```

Cada modulo de dataset va a tener una funcion descarga asociada que toma como parametros de entrada el origen y el destino del dataset, devolviendo el path al archivo decargado

```python
# Dot notation examples
## Ejemplo de descarga del servidor de cluster ai para correrlo en google collaboratory
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='clusterAI',destination='gcollaboratory')
## Ejemplo de descarga de la pagina origen para correrlo localmente en google collaboratory
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='origin',destination='gcollaboratory')
## Ejemplo de descarga del servidor de cluster ai para correrlo localmente en tu maquina
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='clusterAI',destination='local')
## Ejemplo de descarga de la pagina origen para correrlo localmente en tu maquina
myDatasetPath = datasets.<Dataset Group Name>.download(resource=<Dataset Name>,source='origin',destination='local')

# Explicit notation examples
## Ejemplo de descarga del servidor de cluster ai para correrlo en google collaboratory
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='clusterAI',destination='gcollaboratory')
## Ejemplo de descarga de la pagina origen para correrlo localmente en google collaboratory
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='origin',destination='gcollaboratory')
## Ejemplo de descarga del servidor de cluster ai para correrlo localmente en tu maquina
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='clusterAI',destination='local')
## Ejemplo de descarga de la pagina origen para correrlo localmente en tu maquina
myDatasetPath = <Name>.download(resource=<Dataset Name>,source='origin',destination='local')
```
Como el path al dataset esta guardado en la variable myDatasetPath, puedo usar dicha variable para cargarlo en pandas. 

```python
import pandas as pd
myDataset = pd.read_csv(myDatasetPath)
```

Aca hay un ejemplo de complejidad cuando un modulo de datasets posee mas de un archivo para descargar

```python
import pandas as pd
import datasets.acero
import pathlib

# Veo posibles datasets en el modulo:
print(datasets.acero.resources())

# Primer enfoque - descargo un dataset a la vez
## Descargo recurso especificoe -> myDatasetPath contiene un str con el path
myDatasetPath = datasets.acero.download(resource=<Dataset Name>,source='origin',destination='local')

myDataset = pd.read_csv(myDatasetPath)

# Segundo enfoque - descargar todos los datasets de una - No soportado aun
## Descargo todos los recursos -> myDatasetPath contiene una List[str] (lista de strings) con cada path
myDatasetPaths = datasets.acero.download(source='origin',destination='local')

myDatasetsDict = {}
for datasetPath in myDatasetPaths:
    dataset = pathlib.PurePath(datasetPath)
    myDatasetsDict.setdefault(keyname=dataset.name, value=pd.read_csv(datasetPath))

## myDatasetsDict va a tener una key por cada dataset en el modulo

print(myDatasetsDict.keys) #muestra todos los datasets cargados

specificDataset = myDatasetsDict.get("datasetName") # datasetName es una de las keys de myDatasetsDict 
```
Se recomienda utilizar el primer enfoque por un tema de legibilidad del codigo y simplicidad en el uso de cada dataset

### Uploading a dataset / Subir un dataset
#### Upload a new dataset / Subir un dataset nuevo
##### English
To upload a new dataset you will need to create a folder for the module, and inside it you will need to put an empty __init__.py an the module.py
```
datasets/
    newDatasetModuleFolder/
        __init__.py
        newDatasetModule.py
```
newDatasetModule.py file will contain the code that applies the download function. 

Minimum require to pass this would be to have it download it from cluster ai and to run locally

##### Español
Para cargar un nuevo modulo de datasets se tiene que crear una carpeta con el nuevo modulo, y dentro de ella tiene que estar ujn archivo vacio de __init__.py y un archivo que sea el modulo.py
```
datasets/
    newDatasetModuleFolder/
        __init__.py
        newDatasetModule.py
```
El archivo newDatasetModule.py file va a tener la logica para aplicar la funcion descarga. 

El requerimiento minimo es que pueda descargar del servidor de cluster ai y que pueda correr localmente como destino

#### Upload a new resource to an existing dataset / Subir un recurso a dataset existente
##### English
TBD
##### Español
TBD
