#!/bin/bash

venv_dir='venv'

python_bin='/usr/bin/python3'


required_pkgs='python-pip openjdk-8-jdk sqlite3'

# sudo add-apt-repository ppa:jonathonf/backports

# sudo add-apt-repository ppa:openjdk-r/ppa 
# sudo apt-get update

install_package() {
    # FIXME: if you have other locale than en_EN you must check that answer from
    #        command bellow will not be exactly 'install ok installed' in this
    #        other language
    result=$(dpkg-query --show --showformat='${Status}' $1 2> /dev/null)
    if [ "$result" != 'install ok installed' ] ; then
        sudo apt-get install -y $1
    fi
}


for pkg in $required_pkgs; do
    install_package $pkg
done


# wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
# apt-get install apt-transport-https
# echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
# sudo apt-get update && sudo apt-get install elasticsearch
# sudo update-rc.d elasticsearch defaults 95 10
# sudo -i service elasticsearch start

file="elasticsearch-6.2.4.deb"
if [ ! -f "$file" ]; then

	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.deb
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.deb.sha512
	shasum -a 512 -c elasticsearch-6.2.4.deb.sha512 
	sudo dpkg -i elasticsearch-6.2.4.deb
fi

#rm *.deb


sudo -i service elasticsearch start


if [ ! -f "$(which virtualenv)" ]; then
    sudo pip install virtualenv
fi

if [ ! -d "${venv_dir}" ]; then
    virtualenv --python=${python_bin} --no-site-packages ${venv_dir}
fi


source venv/bin/activate

pip3 install -r requirements.txt


