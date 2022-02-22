#!/bin/bash
echo "pipeline name"
read ppln_name

echo "enter repo name"
read repo_name
az pipelines create --name $ppln_name --description 'Pipeline for contoso project' --repository $repo_name --branch master --repository-type tfsgit --yml-path azure-pipelines.yml