SCRIPT_DIR=`pwd`
sudo chown -R AzDevOps:gAzDevOps /var/AzDevOps/sonic-mgmt

sudo rm -f  ~/sonic-mgmt/ansible/testbed.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
sudo rm -rf  ~/sonic-mgmt/ansible/group_vars/snappi-sonic/
sudo rm -f  ~/sonic-mgmt/ansible/snappi-sonic

cp -f  $SCRIPT_DIR/base.py  /var/AzDevOps/sonic-mgmt/tests/common/devices/base.py
cp -f  $SCRIPT_DIR/snappi_fixtures.py /var/AzDevOps/sonic-mgmt/tests/common/snappi_tests/snappi_fixtures.py
cp -f  $SCRIPT_DIR/vms-snappi-sonic.json  /var/AzDevOps/sonic-mgmt/tests/metadata/vms-snappi-sonic.json
cp -f  $SCRIPT_DIR/conftest.py /var/AzDevOps/sonic-mgmt/tests/conftest.py
cp -f  $SCRIPT_DIR/variables.py /var/AzDevOps/sonic-mgmt/tests/snappi_tests/variables.py
echo $SCRIPT_DIR
if [ "$1" = "Novus" ] || [ "$1" = "novus" ]; then 
    echo "Novus"
    cp -f  $SCRIPT_DIR/Novus/ansible/testbed.csv  /var/AzDevOps/sonic-mgmt/ansible/testbed.csv
    cp -f  $SCRIPT_DIR/Novus/ansible/files/sonic_snappi-sonic_links.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
    cp -f  $SCRIPT_DIR/Novus/ansible/files/sonic_snappi-sonic_devices.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
    cp -rf  $SCRIPT_DIR/Novus/ansible/group_vars/snappi-sonic/  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/
    cp -f  $SCRIPT_DIR/Novus/ansible/snappi-sonic  /var/AzDevOps/sonic-mgmt/ansible/snappi-sonic
    cp -f  $SCRIPT_DIR/Novus/vms-snappi-sonic.json /var/AzDevOps/sonic-mgmt/tests/metadata/vms-snappi-sonic.json

elif [ "$1" = "AresOne" ] || [ "$1" = "aresone" ]; then
    echo "AresOne"
    cp -f  $SCRIPT_DIR/AresOne/ansible/testbed.csv  /var/AzDevOps/sonic-mgmt/ansible/testbed.csv
    cp -f  $SCRIPT_DIR/AresOne/ansible/files/sonic_snappi-sonic_links.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
    cp -f  $SCRIPT_DIR/AresOne/ansible/files/sonic_snappi-sonic_devices.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
    cp -rf  $SCRIPT_DIR/AresOne/ansible/group_vars/snappi-sonic/  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/
    cp -f  $SCRIPT_DIR/AresOne/ansible/snappi-sonic  /var/AzDevOps/sonic-mgmt/ansible/snappi-sonic
    cp -f  $SCRIPT_DIR/AresOne/vms-snappi-sonic.json /var/AzDevOps/sonic-mgmt/tests/metadata/vms-snappi-sonic.json
else
    echo "Invalid Card Type"
fi