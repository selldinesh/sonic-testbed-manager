SCRIPT_DIR=`pwd`
sudo chown -R AzDevOps:gAzDevOps /var/AzDevOps/sonic-mgmt

sudo rm -f  ~/sonic-mgmt/ansible/testbed.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
sudo rm -f  ~/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
sudo rm -f  ~/sonic-mgmt/ansible/group_vars/snappi-sonic/
sudo rm -f  ~/sonic-mgmt/ansible/snappi-sonic


echo $SCRIPT_DIR
if [ "$1" = "Novus" ] || [ "$1" = "novus" ]; then 
    echo "Novus"
    cp -f  $SCRIPT_DIR/Novus/ansible/testbed.csv  /var/AzDevOps/sonic-mgmt/ansible/testbed.csv
    cp -f  $SCRIPT_DIR/Novus/ansible/files/sonic_snappi-sonic_links.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
    cp -f  $SCRIPT_DIR/Novus/ansible/files/sonic_snappi-sonic_devices.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
    cp -f  $SCRIPT_DIR/Novus/ansible/group_vars/snappi-sonic/snappi-sonic.yml  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/snappi-sonic.yml
    cp -f  $SCRIPT_DIR/Novus/ansible/group_vars/snappi-sonic/secrets.yml  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/secrets.yml
    cp -f  $SCRIPT_DIR/Novus/ansible/snappi-sonic  /var/AzDevOps/sonic-mgmt/ansible/snappi-sonic

elif [ "$1" = "AresOne" ] || [ "$1" = "aresone" ]; then
    echo "AresOne"
    cp -f  $SCRIPT_DIR/AresOne/ansible/testbed.csv  /var/AzDevOps/sonic-mgmt/ansible/testbed.csv
    cp -f  $SCRIPT_DIR/AresOne/ansible/files/sonic_snappi-sonic_links.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_links.csv
    cp -f  $SCRIPT_DIR/AresOne/ansible/files/sonic_snappi-sonic_devices.csv  /var/AzDevOps/sonic-mgmt/ansible/files/sonic_snappi-sonic_devices.csv
    cp -f  $SCRIPT_DIR/AresOne/ansible/group_vars/snappi-sonic/snappi-sonic.yml  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/snappi-sonic.yml
    cp -f  $SCRIPT_DIR/AresOne/ansible/group_vars/snappi-sonic/secrets.yml  /var/AzDevOps/sonic-mgmt/ansible/group_vars/snappi-sonic/secrets.yml
    cp -f  $SCRIPT_DIR/AresOne/ansible/snappi-sonic  /var/AzDevOps/sonic-mgmt/ansible/snappi-sonic
else
    echo "Invalid Card Type"
fi