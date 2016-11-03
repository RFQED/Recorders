#!

# Auto elog entry command

echo $ELOG_COMMENT | elog -h vm-g2.ph.liv.ac.uk -p 8080 -s -l "Hardware" -u $USER $PASSWORD -v -a Type=$TYPE -a Subject=$SUBJECT -a Author=$AUTHOR -f $FILENAME -n 1
