FROM python:3.9

COPY . ./

RUN pip install Flask && pip install pylint

EXPOSE 5000

CMD python tphook.py