#!/bin/bash
mongoimport --db map_spb -c relations --file relations.json
mongoimport --db map_spb -c ways --file ways.json
mongoimport --db map_spb -c nodes --file nodes.json
