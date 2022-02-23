echo "az dev login script"
echo "enter dev azure organization name here "
read orgname
echo "enter project name here "
read projname
az devops login --organization https://dev.azure.com/$orgname
echo "dev azure login success"
az devops configure --defaults organization=https://dev.azure.com/$orgname/
az devops configure --defaults project=$projname
echo "login success"
