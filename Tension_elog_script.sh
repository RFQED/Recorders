#!

# Auto elog entry command

echo $TENSION_ELOG_COMMENT | elog -h vm-g2.ph.liv.ac.uk -p 8080 -s -l "Hardware" -u TensionTester $PASSWORD-v -a Type="Tension Testeting" -a Subject="Tension Testing Module $MODULE_NUMBER" -a Author="Tension Tester" -f $TENSION_FILENAME -n 1
