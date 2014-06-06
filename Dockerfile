# xtream-profundity
#
# VERSION 0.0.1

FROM fedora/python
MAINTAINER Ethan Rowe <ethan@the-rowes.com>

# Install our inspired web service.
ADD profundity.py /usr/local/bin/profundity

# Make it's readable and runnable.
RUN chmod 755 /usr/local/bin/profundity

# And make the web app the default executable.
CMD ["/usr/local/bin/profundity"]

