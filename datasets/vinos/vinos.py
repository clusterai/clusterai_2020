import pathlib
import requests

resources_config=[
    {
    "name":"winequality-red.csv",
    "url":[("origin","https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"),("clusterAI","https:")]
    }
]


def download(resource: str='winequality-red.csv',source: str='clusterAI',destination: str='local'):
    """
    English
    resource: str that indicates specific dataset within dataset group. Supported values > [winequality]
    source: str that flags from where the dataset should be downloaded. Supported values > [origin, clusterAI]
    destination: str that flags where the dataset should be left, preps google collab if necessary. Supported values > [local, gcolab]
    Español
    resource: str que indica que dataset especifico se va a descargar dentro del grupo. Valores validos > [winequality]
    source: str que indica de donde se descargara el dataset. Valores validos > [origin, clusterAI]
    destination: str que indica donde se dejara el dataset, prepara google collab si es necesario. Valores validos > [local, gcolab]
    """
    # Get resource conf. / Obtener config del recurso
    try:
        config = [conf for conf in resources_config if conf.get("name")==resource][0]
    except:
        return print('resource not found - Use function resources() to get available values \nrecurso no encontrado - Use funcion resources() para obtener valores validos')
    
    # Get source url
    try:
        url = [url for url in config.get("url") if url[0]==source][0][1]
    except:
        return print('source not found - Use function sources() to get available values \nfuente no encontrada - Use funcion sources() para obtener valores validos')

    # Make destination folder
    try:
        dwnl_file_path = (pathlib.Path(__file__).parent / 'dwnl')
        if not dwnl_file_path.exists():
            dwnl_file_path.mkdir()
    except:
        return print('destination not found - raise issue to address it \ndestino no encontrado - levante un issue en el repositorio para corregirlo')
    print("callin endpoint")
    dataset = requests.get(url=url, allow_redirects=True, stream = True)
    print("Open file")
    with open(dwnl_file_path / config.get("name") ,"wb") as dataset_file:
        for chunk in dataset.iter_content(chunk_size = 1024):
            if chunk:
                dataset_file.write(chunk)
    print("finished download")
    print(dataset_file)
    print(dwnl_file_path)