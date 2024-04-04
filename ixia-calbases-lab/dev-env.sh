SCRIPT_DIR=`pwd`
sudo chown -R AzDevOps:gAzDevOps ~/sonic-mgmt

sudo rm -f  ~/sonic-mgmt/ansible/testbed.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
sudo rm -rf ~/sonic-mgmt/ansible/group_vars/snappi-sonic/
sudo rm -f  ~/sonic-mgmt/ansible/snappi-sonic

cp -f  $SCRIPT_DIR/ansible/testbed.csv ~/sonic-mgmt/ansible/testbed.csv
cp -f  $SCRIPT_DIR/ansible/files/sonic_snappi-sonic_links.csv ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
cp -f  $SCRIPT_DIR/ansible/files/sonic_snappi-sonic_devices.csv ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
cp -rf $SCRIPT_DIR/ansible/group_vars/snappi-sonic/ ~/sonic-mgmt/ansible/group_vars/snappi-sonic/
cp -f  $SCRIPT_DIR/ansible/snappi-sonic ~/sonic-mgmt/ansible/snappi-sonic
