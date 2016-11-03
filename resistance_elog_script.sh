#!

# Auto elog entry command

echo $RESISTANCE_ELOG_COMMENT | elog -h vm-g2.ph.liv.ac.uk -p 8080 -s -l "Hardware" -u ResistanceTester $PASSWORD -v -a Type="Resistance Testeting" -a Subject="Resistance Testing Module $MODULE_NUMBER" -a Author="Resistance Tester" -f $RESISTANCE_FILENAME -n 1
