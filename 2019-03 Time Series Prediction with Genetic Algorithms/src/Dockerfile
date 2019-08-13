FROM pklehre/niso2019-lab3

ADD ass4.py /bin

RUN apt-get update
RUN apt-get -y install python-numpy
RUN apt-get -y install python-sexpdata
RUN apt-get -y install python-sklearn
RUN apt-get -y install python-pyparsing
RUN apt-get -y install python-argparse
RUN apt-get -y install python-pathlib



CMD ["-username", "natliu", "-submission", "python /bin/ass4.py"]