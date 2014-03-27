#!/usr/bin/python

# this will be a class used to manage a list of packages.
# this should default to instantiating on a systemid or on a packagelist.
# if we instanciate the list on a packageid, then we want the list to be fetched from satellite
# if we instanciate against a file, it should be read and treated as a list of rpms.
# the file format expected is package-name-version-release.arch
# sadly exceptions will happen to the format, but basically it should be the left line from a installed-packages of a sosreport

