import json
import os

pnm = input("enter pipeline name ")
print("avaliable repos in azure ")
dm = (os.system('az repos list >repos.json'))
f=open('repos.json')
data = json.load(f)
for i in data:
    print(i['name'])
f.close()
rpnm = input("enter repo name")
os.system(
    f'az pipelines create --name {pnm} --description "Pipeline for contoso project" --repository {rpnm} --branch master --repository-type tfsgit --yml-path azure-pipelines.yml>done.json')
fz=open('done.json')
dataa=json.load(fz)
print(dataa['buildNumber'])
print(dataa['definition']['name'])
fz.close()