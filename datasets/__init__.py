# Manage paths
from .datasets import DatasetModule

resources_config=[
    {
        "Module":"vinos",
        "Datasets":[
            {
                "name":"winequality-red.csv",
                "url":[
                    ("origin","https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"winequality-white.csv",
                "url":[
                    ("origin","https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"winequality.names",
                "url":[
                    ("origin","https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names"),
                    ("clusterAI","https:")
                    ]
            }
        ]
    },
    {
        "Module":"subtes",
        "Datasets":[
            {
                "name":"molinetes-2020.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-viajes-molinetes/molinetes-2020.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-2019.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2019.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-subte-18.zip",
                "url":[("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-subte-18.zip"),
                ("clusterAI","https:")
                ]
            },
            {
                "name":"molinetes-2017.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2017.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-2016.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2016.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-2015.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2015.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-2014.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2014.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"molinetes-2013-junio-diciembre.zip",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/molinetes-2013-junio-diciembre.zip"),
                    ("clusterAI","https:")
                    ]
            },
            {
                "name":"registro-historico-del-precio-del-boleto.csv",
                "url":[
                    ("origin","http://cdn.buenosaires.gob.ar/datosabiertos/datasets/subte-viajes-molinetes/registro-historico-del-precio-del-boleto.csv"),
                    ("clusterAI","https:")
                    ]
            }
        ]
    }
]

vinos_config = [config for config in resources_config if config.get("Module")=="vinos"][0]
vinos = DatasetModule("vinos",vinos_config.get("Datasets"))

subtes_config = [config for config in resources_config if config.get("Module")=="subtes"][0]
subtes = DatasetModule("subtes",subtes_config.get("Datasets"))

