# Docker_python_dash

* build -t khadimgueyekgy1/dockerpythondash . 
* docker container run -d -p 3000:8050 khadimgueyekgy1/dockerpythondash
* docker container stop container_id
* docker push khadimgueyekgy1/dockerpythondash (to push it in your Docker web account  )
* * docker pull khadimgueyekgy1/dockerpythondash:latest

note:
  * host = '0.0.0.0'
  * port = xxxxx
  * e.g app.run_server(host='0.0.0.0',debug=True, port=3000)
