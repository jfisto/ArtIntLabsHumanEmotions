#!/bin/bash
rm -r sample_data
pip install dvc==0.93.0 pydrive2==1.4.9 catalyst==20.4.1 alchemy==20.4
dvc remote modify yandexcloud credentialpath /content/.dvc/aws/credentials
