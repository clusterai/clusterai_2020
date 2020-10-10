import pathlib
import requests
import zipfile
from typing import List

class DatasetModule():    
    def __init__(self,resources_name,resources_config):
        self.name=resources_name
        self.config=resources_config
    def resources(self) -> List[str]:
        """
        English
        \nLists available datasets files in the module
        \nEspañol
        \nLista los archivos datasets en el modulo
        """
        return [conf.get("name") for conf in self.config]

    def sources(self,resource: str) -> List[str]:
        """
        English
        \nresource: str that indicates specific dataset within dataset group.
        \nLists sources for specific resource
        \nEspañol
        \nresource: str que indica que dataset especifico se va a descargar dentro del grupo
        \nLista fuentes (sources) para un recurso (resource) especifico
        """
        sources = [conf.get("url") for conf in self.config if conf.get("name")==resource][0]
        return [source[0] for source in sources]

    def download(self,resource: str,source: str = 'origin',destination: str = 'local') -> str:
        """
        English
        \nresource: str that indicates specific dataset within dataset group.
        \nsource: str that flags from where the dataset should be downloaded.
        \ndestination: str that flags where the dataset should be left, preps google collab if necessary. Supported values > [local, gcolab]
        \nIt downloads the datset file on /dwnl/ folder within dataset group folder and returns its path
        \nEspañol
        \nresource: str que indica que dataset especifico se va a descargar dentro del grupo.
        \nsource: str que indica de donde se descargara el dataset.
        \ndestination: str que indica donde se dejara el dataset, prepara google collab si es necesario. Valores validos > [local, gcolab]
        \nDescarga el archivo dataset dentro de la carpeta /dwnl/ que se crea dentro de la carpeta del grupo y devuelve el path del archivo.
        """
        # Get resource conf. / Obtener config del recurso
        try:
            config = [conf for conf in self.config if conf.get("name")==resource][0]
        except:
            return print('resource not found - Use function resources() to get available values \nrecurso no encontrado - Use funcion resources() para obtener valores validos')
        
        # Get source url
        try:
            url = [url for url in config.get("url") if url[0]==source][0][1]
        except:
            return print('source not found - Use function sources() to get available values \nfuente no encontrada - Use funcion sources() para obtener valores validos')

        # Make destination folder
        try:
            base_path = (pathlib.Path(__file__).parent / 'downloads')
            if not base_path.exists():
                base_path.mkdir()
            dwnl_file_path = (base_path / self.name)
            if not dwnl_file_path.exists():
                dwnl_file_path.mkdir()
        except:
            return print('destination not found - raise issue to address it \ndestino no encontrado - levante un issue en el repositorio para corregirlo')
        
        #Downloading dataset
        print("calling endpoint / golpeando url")
        dataset = requests.get(url=url, allow_redirects=True, stream = True)
        print("writting file / escribiendo archivo")
        with open(dwnl_file_path / config.get("name") ,"wb") as dataset_file:
            for chunk in dataset.iter_content(chunk_size = 1024):
                if chunk:
                    dataset_file.write(chunk)
        zip_file_path=str(dwnl_file_path / config.get("name"))
        if config.get("name").endswith('.zip'):
            with zipfile.ZipFile(zip_file_path,"r") as zip_ref:
                # TODO
                # support multiple file within zip file
                FileName = zip_ref.namelist()[0]
                zip_ref.extractall(dwnl_file_path)
                print("finished download / descarga finalizada")
                return str(dwnl_file_path / FileName)
        else:
            print("finished download / descarga finalizada")
            return str(dwnl_file_path / config.get("name"))
