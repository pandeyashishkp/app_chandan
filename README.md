# app_chandan
Bigquery-Fastapi-App
    a) create service account on gcp for bigquery read/write and modify access , get the json file and copy the same to the bq_com.json
    b) url.json - this file is a json document having the url address of the git files, key will be the parameter that user will specify in the url "www.localhost.com:8080/report1" 
this will fetch report1 from the server
you can define multiple urls for sql scripts to fetch other reports and share the key name with the end user 
   c) "merge_script_path.txt"  - this file has the github url of all the merge scripts you will create , this will modify the existing data on bigquery - so be careful .
      Also if you want to specify any file and not use it , just put a '#' infront of the file-name , please avoid putting URL names in quotes within this file.
   d) another important file is "env.txt" - this will be used to give name of your credential json file and project_id  and jobConfig parameters for bigquery. 
   e) I have included Dockerfile , you can copy the required files as mentioned above and directly run as per your requirements , you can also change the port number in this file. 
        f) main.py is the file that will be called , all the files are important in this folder so make sure if you remove any files just make sure it is not used.
