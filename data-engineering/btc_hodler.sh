#!/bin/bash

#pentaho path
PENTAHO=/home/ubuntu/data-integration/

cd $PENTAHO
bash kitchen.sh -file="/home/ubuntu/etl_pentaho/bp_scheduled2.kjb" 
