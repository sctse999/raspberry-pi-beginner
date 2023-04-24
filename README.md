### Installing Jupyter Lab

```
sudo apt-get install python3-virtualenv
python3 -m virtualenv -p python3 env --system-site-packages
echo "source ~/env/activate" >> ~/.bashrc
```

### Installing as a service

1. Put [juptyer-lab.services](jupyter-lab.services) under /etc/systemd/system
2. Execute the following command

```
sudo systemctl daemon-reload
sudo systemctl enable jupyter.service
```

### Installing luma.oled

```
sudo apt-get install python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y 
pip3 install luma.oled
```