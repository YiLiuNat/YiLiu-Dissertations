FROM pklehre/niso2019-lab5



RUN apt-get update
RUN apt-get -y install python-numpy
RUN apt-get -y install python-sexpdata
RUN apt-get -y install python-sklearn
RUN apt-get -y install python-pyparsing
RUN apt-get -y install python-argparse
RUN apt-get -y install python-pathlib

ADD yxl605.py /bin

CMD ["-username", "yxl605", "-submission", "python /bin/yxl605.py"]