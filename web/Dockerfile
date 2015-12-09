FROM elenaalexandrovna/opencv-python3

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-pip \
    && apt-get -y clean all \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN /usr/bin/pip install -r requirements.txt
COPY . /usr/src/app
WORKDIR /usr/src/app/web
