# set base image (host OS)
FROM python:3

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# download dependencies
RUN apt-get install -y wget
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1MD2VrCGivp_xpBhQ43iFUZSpfMcc9sJw' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1MD2VrCGivp_xpBhQ43iFUZSpfMcc9sJw" -O sentiment140.csv && rm -rf /tmp/cookies.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1n5T2tzBSaKhfo6DJbsvqhR3UDcpM5rn_' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1n5T2tzBSaKhfo6DJbsvqhR3UDcpM5rn_" -O imdb-movie-reviews.csv && rm -rf /tmp/cookies.txt

# copy the content of the local src directory to the working directory
COPY src/ .

#RUN /usr/local/bin/python -m pip install --upgrade pip
#RUN apk update
#RUN apk add make automake gcc g++ subversion python3-dev

# install dependencies
#RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "sentiment-analysis.py" ]