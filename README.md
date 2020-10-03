# clusterai_2020
Repository for the UTN BA Data Science Course 2020 
## Working with datasets / Trabajando con datasets
### Use a dataset / Usar un dataset
##### Eng
The idea is to let the users import the dataset as a module within the jupyter notebook or python script.
```python
import datasets.<Nombre Dataset>
```

Each dataset module will have a download function associaten which takes the source and destination as an input, returning the path where it left the downloaded file.

```python
# Example of download from cluster ai server to run on google collaboratory
myDatasetPath = datasets.<Dataset Name>.download(source='clusterAI',destination='gcollaboratort')
# Example of download from origin server to run on google collaboratory
myDatasetPath = datasets.<Dataset Name>.download(source='origin',destination='gcollaboratort')
# Example of download from cluster ai server to run locally on your computer
myDatasetPath = datasets.<Dataset Name>.download(source='clusterAI',destination='local')
# Example of download from origin server to run locally on your computer
myDatasetPath = datasets.<Dataset Name>.download(source='origin',destination='local')
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
myDatasetPath = datasets.acero.<resource>.download(source='origin',destination='local')

myDataset = pd.read_csv(myDatasetPath)

# Second approach - downloading all datasets at once
## Downloading all resources -> myDatasetPath contains List[str] with each path
myDatasetPaths = datasets.acero.<resource>.download(source='origin',destination='local')

myDatasetsDict = {}
for datasetPath in myDatasetPaths:
    dataset = pathlib.PurePath(datasetPath)
    myDatasetsDict.setdefault(keyname=dataset.name, value=pd.read_csv(datasetPath))

## myDatasetsDict will have a key for each dataset in the module

print(myDatasetsDict.keys) #shows all loaded datasets

specificDataset = myDatasetsDict.get("datasetName") # datasetName is one of the keys of myDatasetsDict 
```
It's recomended to use the first approach due to it's legibility and simplicity in usage per dataset

##### Esp
La idea es permitirle a los usuarios importar el dataset como un modulo dentro del juyter notebook o el script de python.
```python
import datasets.<Nombre Dataset>
```

Cada modulo de dataset va a tener una funcion descarga asociada que toma como parametros de entrada el origen y el destino del dataset, devolviendo el path al archivo decargado

```python
# Ejemplo de descarga del servidor de cluster ai para correrlo en google collaboratory
myDatasetPath = datasets.<Dataset Name>.download(source='clusterAI',destination='gcollaboratort')
# Ejemplo de descarga de la pagina origen para correrlo localmente en google collaboratory
myDatasetPath = datasets.<Dataset Name>.download(source='origin',destination='gcollaboratort')
# Ejemplo de descarga del servidor de cluster ai para correrlo localmente en tu maquina
myDatasetPath = datasets.<Dataset Name>.download(source='clusterAI',destination='local')
# Ejemplo de descarga de la pagina origen para correrlo localmente en tu maquina
myDatasetPath = datasets.<Dataset Name>.download(source='origin',destination='local')
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
myDatasetPath = datasets.acero.<resource>.download(source='origin',destination='local')

myDataset = pd.read_csv(myDatasetPath)

# Segundo enfoque - descargar todos los datasets de una
## Descargo todos los recursos -> myDatasetPath contiene una List[str] (lista de strings) con cada path
myDatasetPaths = datasets.acero.<resource>.download(source='origin',destination='local')

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
#### Subir un dataset nuevo
##### Eng
The structure 
##### Esp

#### Subir un recurso a dataset existente
##### Eng
The structure 
##### Esp
