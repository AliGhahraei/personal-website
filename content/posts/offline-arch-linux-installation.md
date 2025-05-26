+++
title = "Arch Linux Installation with offline laptop (and optional Realtek rtl8723de driver installation)"
lastmod = 2025-05-26T13:23:36-07:00
tags = ["tech-guides"]
draft = false
weight = 2001
+++

This is for laptops without an ethernet port and for which the Arch live ISO doesn't have a working wifi driver.
It assumes you have another computer with internet and a USB. You can substitute the driver installation instructions.
They are marked as "(driver)".

I wrote this back in 2020 and better methods probably existed or exist now. This worked at the time, but I haven't tried
it again, so attempt to replicate it at your own risk.


## Steps {#steps}


### Start in online PC {#start-in-online-pc}


#### Download get_pacman_dbs and change the mirror variable in it if needed {#download-get-pacman-dbs-and-change-the-mirror-variable-in-it-if-needed}

```bash
wget -O get_pacman_dbs https://gist.githubusercontent.com/AliGhahraei/e46d45cef55cf13068da52d8ca1a2c7a/raw
```


#### Make the script executable and run it inside a new dbs directory {#make-the-script-executable-and-run-it-inside-a-new-dbs-directory}

```bash
mkdir dbs
chmod +x get_pacman_dbs
cd dbs
../get_pacman_dbs
```


#### Download the arch bootstrap images at <https://www.archlinux.org/download/> {#download-the-arch-bootstrap-images-at-https-www-dot-archlinux-dot-org-download}


#### Find the path to your USB and copy your dbs and bootstrap image {#find-the-path-to-your-usb-and-copy-your-dbs-and-bootstrap-image}

```bash
cd ..
mount
# Sample output:
# /dev/disk1s1 on / (apfs, local, read-only, journaled)
# devfs on /dev (devfs, local, nobrowse)
# /dev/disk1s5 on /System/Volumes/Data (apfs, local, journaled, nobrowse)
# /dev/disk1s4 on /private/var/vm (apfs, local, journaled, nobrowse)
# map auto_home on /System/Volumes/Data/home (autofs, automounted, nobrowse)
# /dev/disk2s1 on /Volumes/ALI (msdos, local, nodev, nosuid, noowners)
cp -r dbs <bootstrap image> <online usb mount dir>
```

I used /Volumes/ALI (last line of mount output). The bootstrap image has this
format: archlinux-bootstrap-&lt;date&gt;-&lt;architecture&gt;.tar.gz and the one I used was
archlinux-bootstrap-2020.02.01-x86_64.tar.gz


### Switch to offline laptop {#switch-to-offline-laptop}


#### Follow <https://wiki.archlinux.org/index.php/installation_guide> up to before mirror selection (but skip connecting to the internet) {#follow-https-wiki-dot-archlinux-dot-org-index-dot-php-installation-guide-up-to-before-mirror-selection--but-skip-connecting-to-the-internet}


#### Find the path to your USB and mount it {#find-the-path-to-your-usb-and-mount-it}

```bash
mkdir /usb
lsblk
# NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# loop0     7:0    0 531.2M  1 loop /run/archiso/sfs/airootfs
# sda       8:0    1   7.3G  0 disk
# └─sda1    8:1    1   7.3G  0 part /run/archiso/bootmnt
# sdb       8:16   1  14.4G  0 disk
# └─sdb1    8:17   1  14.4G  0 part
# nvme0n1 259:0    0 238.5G  0 disk
# nvme1n1 259:5    0  13.4G  0 disk
mount <usb device> /usb
```

I used /dev/sdb1 (find a device with a number that matches your USB capacity and add "dev")


#### Extract your bootstrap image into your new root {#extract-your-bootstrap-image-into-your-new-root}

```bash
cd /mnt
tar xzvf <bootstrap image>
mv root.x86_64/^boot .
rm -r root.x86_64
```


#### Generate an fstab file and check if its contents look correct {#generate-an-fstab-file-and-check-if-its-contents-look-correct}

```bash
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab
```


#### Copy your dbs into the new system {#copy-your-dbs-into-the-new-system}

```bash
cp /usb/dbs/* var/lib/pacman/sync/
```


#### Edit its mirrors file {#edit-its-mirrors-file}

```bash
vim etc/pacman.d/mirrorlist
```


#### Change root into it {#change-root-into-it}

```bash
arch-chroot .
```


#### Save a package list (add or remove packages/groups as needed, this is only what I used then) to a file {#save-a-package-list--add-or-remove-packages-groups-as-needed-this-is-only-what-i-used-then--to-a-file}

```bash
pacman -Sp --noconfirm base linux linux-firmware netctl dialog wpa_supplicant dhcpcd neovim refind-efi > pkglist
```


#### (driver) Save packages necessary for building/installing the driver and connecting to the internet {#driver--save-packages-necessary-for-building-installing-the-driver-and-connecting-to-the-internet}

```bash
pacman -Sp --noconfirm base-devel dkms git linux-headers >> pkglist
```


#### Exit chroot, copy the file and unmount your USB {#exit-chroot-copy-the-file-and-unmount-your-usb}

```bash
exit
mv pkglist /usb
umount /usb
```


### Switch to online PC {#switch-to-online-pc}


#### Download your packages {#download-your-packages}

```bash
cp <online usb mount dir>/pkglist .
mkdir packages
cd packages
wget -nv -i ../pkglist  # You can ignore locale warnings if you get them
```


#### (driver) Download the network driver {#driver--download-the-network-driver}

```bash
cd ..
wget https://aur.archlinux.org/cgit/aur.git/snapshot/rtlwifi_new-extended-dkms.tar.gz
tar xzf rtlwifi_new-extended-dkms.tar.gz
git clone https://github.com/lwfinger/rtlwifi_new.git -b extended
```


#### (driver) Copy the network driver {#driver--copy-the-network-driver}

```bash
cp -r rtlwifi_new-extended-dkms rtlwifi_new <online usb mount dir>
```


#### Copy your packages {#copy-your-packages}

```bash
cp -r packages/ <online usb mount dir>
```

Warning! some of your packages may contain invalid character names and in my
case, the mac I was using just silently renamed them and wouldn't let me rename them myself
afterwards. If you get "Could not resolve host" when installing, check the name
pacman searches and the name of the packages in your cache match


### Switch to offline laptop {#switch-to-offline-laptop}


#### Copy your packages from the USB {#copy-your-packages-from-the-usb}

```bash
mount <usb device> /usb
cp -r /usb/packages/* var/cache/pacman/pkg
```


#### Chroot again {#chroot-again}

```bash
arch-chroot .
```


#### Initialize pacman keyring {#initialize-pacman-keyring}

```bash
pacman-key --init
pacman-key --populate archlinux
```


#### Install packages {#install-packages}

```bash
pacman -S --needed base linux linux-firmware netctl dialog wpa_supplicant dhcpcd neovim refind-efi
```


#### (driver) Install driver packages {#driver--install-driver-packages}

```bash
pacman -S --needed base-devel dkms linux-headers
```


#### Follow the rest of the installation guide from just after the arch-chroot {#follow-the-rest-of-the-installation-guide-from-just-after-the-arch-chroot}


#### (driver) Install and load driver (use non-root user) {#driver--install-and-load-driver--use-non-root-user}

```bash
mount <usb device> /mnt
cp -r /mnt/rtlfwifi_new-extended-dkms rtlwifi_new /tmp
cd /tmp/rtlfwifi_new-extended-dkms
cp -r /mnt/rtlwifi_new .
makepkg -sri
sudo modprobe rtl8723de
```


#### Verify the module is loaded and a new wireless interface was detected {#verify-the-module-is-loaded-and-a-new-wireless-interface-was-detected}

```bash
lsmod | grep rtl8723de
# rtl8723de             110592  0
# btcoexist             479232  1 rtl8723de
# phydm_mod             917504  1 rtl8723de
# rtl8723_common         28672  1 rtl8723de
# rtl_pci                36864  1 rtl8723de
# rtlwifi               184320  5 rtl_pci,rtl8723de,btcoexist,phydm_mod,rtl8723_common
ip addr
# 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
#     link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
#     inet 127.0.0.1/8 scope host lo
#        valid_lft forever preferred_lft forever
#     inet6 ::1/128 scope host
#        valid_lft forever preferred_lft forever
# 2: wlo1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
#     link/ether c0:e4:34:68:0c:69 brd ff:ff:ff:ff:ff:ff
```


#### Follow the installation guide's internet connection instructions {#follow-the-installation-guide-s-internet-connection-instructions}


## Why I didn't use [the archiso wiki's guide](https://wiki.archlinux.org/index.php/Offline_installation) {#why-i-didn-t-use-the-archiso-wiki-s-guide}

The wiki's method seems quite brittle as it will have to change if new
customizations are added to the Archiso and I wanted a method that I (or anyone
else) could use in the future with low probabilities of changing. The article
itself criticizes using archiso and mentions using the bootstrap images.
I was also curious and wanted to test if I could use
[the offline installation of packages guide](https://wiki.archlinux.org/index.php/Offline_installation_of_packages#Normal_Method:_Pacman) with slight modifications together
with the bootstrap image for this.


## Why I needed the bootstrap image to generate packages {#why-i-needed-the-bootstrap-image-to-generate-packages}

I thought I wouldn't need this image since I already had a running Arch (the
live USB) to get a list of packages to download. I used pacman -Sp on the live
system for this, but this doesn't work as packages already in the live USB don't
get listed and I ended up missing dependencies for some packages, so I had to
use a bootstrapped system.


## Credits {#credits}

-   <https://wiki.archlinux.org/index.php/installation_guide>
-   <https://wiki.archlinux.org/index.php/Install_Arch_Linux_from_existing_Linux#From_a_host_running_another_Linux_distribution>
-   <https://wiki.archlinux.org/index.php/Offline_installation>
-   <https://wiki.archlinux.org/index.php/Offline_installation_of_packages#Normal_Method:_Pacman>
-   <https://github.com/lwfinger/rtlwifi_new> (no longer available)
