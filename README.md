#Lab Recorders

## How to use

 `ssh g2share@hep72 `

 `cd /hepstore/g2share/LabRecorders `

 `source setup.sh` 

 `python TensionRecord.py` 

## To setup

 `sudo apt-get install libssl-dev`

 `git clone https://bitbucket.org/ritt/elog`

 `make`

 `sudo make install`

can edit the Makefile to your local PREFIX then add this prefix to your PATH


More here = http://hep.ph.liv.ac.uk/~wturner/LabRecorders.html