FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip3 install -r requirements.txt
# Installing uwsgi server
RUN pip3 install uwsgi
COPY . /code/

EXPOSE 8000
# This is not the best way to DO, SEE BELOW!!
CMD uwsgi --http "0.0.0.0:8000" --module melissa.wsgi
#CMD uwsgi --http :9090 --wsgi-file melissa/wsgi.py
#CMD uwsgi --chdir=/melissa \
#      --module=melissa.wsgi:application \
#     --env DJANGO_SETTINGS_MODULE=melissa.settings \
#     --master --pidfile=/tmp/project-master.pid \
#     --socket=127.0.0.1:49152 \      
#     # can also be a file
#     --processes=4 \                 
#     # number of worker processes
#     --uid=1000 --gid=2000 \         
#     # if root, uwsgi can drop privileges
#     --harakiri=20 \                 
#     # respawn processes taking more than 20 seconds
#     --max-requests=5000 \           
#     # respawn processes after serving 5000 requests
#     --vacuum \                      
#     # clear environment on exit
#     #--home=/path/to/virtual/env \   
#     # optional path to a virtual environment
#     #--daemonize=/var/log/uwsgi/yourproject.log      
#     # background the process
