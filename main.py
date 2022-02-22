import json
import os

pnm = input("enter pipeline name")
print("avaliable repos in azure")
dm = (os.system('az repos list >av.json'))
f=open('av.json')
data = json.load(f)
for i in data:
    print(i['name'])

rpnm = input("enter repo name")
os.system(
    f'az pipelines create --name {pnm} --description "Pipeline for contoso project" --repository {rpnm} --branch master --repository-type tfsgit --yml-path azure-pipelines.yml')
