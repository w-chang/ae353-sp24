# AE353-SP24

Below is an installation guide for all the software that will be used in the Spring 2024 semester of AE353 at UIUC.



# Windows Installation

## 1. Install Git for Windows
If you do not have Git already installed, download the most recent Git installer for Windows 64 from the [git-scm website](https://git-scm.com/download/win) or just click [here](https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe) to download it automatically. Once the .exe is downloaded, run it. The .exe file has the format Git-VERSION-64-bit and will be in your default downloads folder C:\Users\USER NAME\Downloads. 

* Once the wizard is running, click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_1.png?raw=true" alt="git_1" width="495" height="375"/>



* Click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_2.png?raw=true" alt="git_2" width="495" height="375"/>



* Click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_3.png?raw=true" alt="git_3" width="495" height="375"/>



* Click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_4.png?raw=true" alt="git_4" width="495" height="375"/>



* Select **Let Git decide** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_5.png?raw=true" alt="git_5" width="495" height="375"/>



* Select **Use Git from Git Bash only** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_6.png?raw=true" alt="git_6" width="495" height="375"/>



* Select **Use bundled OpenSSH** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_7.png?raw=true" alt="git_7" width="495" height="375"/>



* Select **Use the OpenSSL library** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_8.png?raw=true" alt="git_8" width="495" height="375"/>



* Select **Checkout Windows-style, commit Unix-style line endings** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_9.png?raw=true" alt="git_9" width="495" height="375"/>



* Select **Use Windows' default console window** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_10.png?raw=true" alt="git_10" width="495" height="375"/>



* Select **Fast-forward or merge** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_11.png?raw=true" alt="git_11" width="495" height="375"/>



* Select **Git Credential Manager** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_12.png?raw=true" alt="git_12" width="495" height="375"/>



* Check only **Enable file system caching** then click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_13.png?raw=true" alt="git_13" width="495" height="375"/>



* Make sure nothing is checked then click **install**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_14.png?raw=true" alt="git_14" width="495" height="375"/>



* Once installation is finished, click **finish**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_15.png?raw=true" alt="git_15" width="495" height="375"/>



* Navigate to **C:\Program Files\Git** in your file explorer.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_16.png?raw=true" alt="git_16" width="495" height="375"/>



* To create a desktop shortcut to git-cmd (the application that will be used to pull and push Git repositories), right click on **git-cmd**, navigate to **Send to**, then click **Desktop (create shortcut)**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/git_17.png?raw=true" alt="git_17" width="495" height="375"/>



* To verify that Git is installed properly, open **git-cmd** and type 

```bash
Git --version
```


* You should get a response that lists the version of Git you just installed.

Git is now installed on your machine.





## 2. Clone the ae353-sp24 Repository using Git

- Open **git-cmd** and navigate to the directory you want to clone the ae353-sp24 code repository into. This is done using the  change directory command.

To move up a directory, type

```bash
cd ..
```

To move down a directory, type

```bash
cd DIR
```

Where ``DIR`` is the name of the directory you want to move into.

For example, if you start in:

```bash
C:\Program Files\Git
```

and want to get to

```bash
C:\Example\Projects
```

you would type the following commands:

```bash
cd ..
cd ..
cd Example
cd Projects
```

- Clone the repository into the current directory by typing the command

```bash
git clone https://github.com/w-chang/ae353-sp24.git
```

The ae353-sp24 code repository is now cloned to your machine. You will find all design projects in this repository.





## 3. Install Miniconda for Windows
If you do not have Miniconda already installed, download the most recent Miniconda installer for Windows 64 from the [miniconda website](https://docs.conda.io/projects/miniconda/en/latest/) or just click [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) to download it automatically. Once the .exe is downloaded, run it. The .exe file has the format Miniconda3-latest-Windows-x86_64 and will be in your default downloads folder C:\Users\USER NAME\Downloads. 

* Once the wizard is running, click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_1.png?raw=true" alt="conda_1" width="495" height="375"/>



* Click **I Agree**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_2.png?raw=true" alt="conda_2" width="495" height="375"/>



* Ensure **Just Me (recommended)** is selected and click **Next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_3.png?raw=true" alt="conda_3" width="495" height="375"/>



* Click **Next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_4.png?raw=true" alt="conda_4" width="495" height="375"/>



* Ensure **Create start menu shortcuts (supported packages only)** is checked and **Register Miniconda3 as my default Python 3.11** is ***NOT CHECKED***.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_5.png?raw=true" alt="conda_5" width="495" height="375"/>



* Once installation is complete, click **next**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_6.png?raw=true" alt="conda_6" width="495" height="375"/>



* You may deselected **Getting started with Conda** and **Welcome to Anaconda** then click **Finish**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_7.png?raw=true" alt="conda_7" width="495" height="375"/>



* Navigate to the Windows Start Menu folder located at **C:\Users\USER NAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Miniconda3 (64-bit)**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_8.png?raw=true" alt="conda_8" width="495" height="375"/>



* To create a desktop shortcut to Anaconda Prompt (the application that will be used interact with Miniconda), right click on **Anaconda Prompt (Miniconda3)**, navigate to **Send to**, then click **Desktop (create shortcut)**.

<img src="https://github.com/w-chang/ae353-sp24/blob/main/Images/conda_9.png?raw=true" alt="conda_9" width="495" height="375"/>



To verify that Miniconda is installed properly, open **Anaconda Prompt (Miniconda3)** and type 

```bash
conda --version
```

You should get a response that lists the version of Miniconda you just installed.

Miniconda is now installed on your machine.



## 4. Install condynsate in a Miniconda virtual environment
To install condynsate in a Miniconda virtual environment, open **Anaconda Prompt (Miniconda3)** and type

```bash
conda create -n ae353 python==3.8.18
```
Press enter.

When prompted, type 

```bash
y
```
then press enter.

When complete, type

```bash
conda activate ae353
```
then press enter.

You can confirm the virtual environment is activated when 

```
(base)
```
changes to 
```
(ae353)
```
at the beginning of the prompt line. Once the virtual environment is activated, type
```bash
pip install condynsate[edu]
```
and press enter. This installs condynsate and some other optional dependencies that are helpful when using condynsate.

Once the installation is complete, you can confirm that condynsate has been successfully installed and the virtual environment is set up correctly by typing

```bash
python
```
and pressing enter. This starts a Python shell in your Anaconda prompt. Next type
```python
import condynsate
```
and press enter. Finally type
```python
condynsate.__version__
```
and press enter. If condynsate is installed correctly, the current version will be shown.

condynsate is now installed on your machine. You may type 

```python
quit()
```
to quit the Python shell and exit out of the Anaconda prompt.





# Linux Installation

## 1. Clone the ae353-sp24 Repository using Git

Open the terminal. To open the terminal press **ctrl+alt+t**. Navigate to the directory you want to clone the ae353-sp24 code repository into. This is done using the  change directory command.

To move up a directory, type

```bash
cd ..
```

To move down a directory, type

```bash
cd DIR
```

Where ``DIR`` is the name of the directory you want to move into.

For example, if you start in:

```bash
user@name:~
```

and want to get to

```bash
user@name:~/Documents
```

you would type the following command:

```bash
cd Documents
```

Now, clone the repository into the current directory by typing the command

```bash
git clone https://github.com/w-chang/ae353-sp24.git
```

The ae353-sp24 code repository is now cloned to your machine. You will find all design projects in this repository.





## 2. Install Miniconda for Linux

If you do not have Miniconda already installed, run these four commands in the terminal to quickly and quietly install the latest 64-bit version of the installer. To open the terminal press **ctrl+alt+t**.

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

**Restart the terminal.** After installing, initialize your newly-installed Miniconda. 

```bash
~/miniconda3/bin/conda init bash
```

To verify that Miniconda is installed properly,  run the command 
```bash
conda --version
```

You should get a response that lists the version of Miniconda you just installed. If you do not, more help on installation can be found [here](https://docs.conda.io/projects/miniconda/en/latest/).





## 3. Install condynsate in a Miniconda virtual environment
To install condynsate in a Miniconda virtual environment, open the terminal and create a new virtual environment with python 3.8.18. To open the terminal press **ctrl+alt+t**. When the terminal is open, run the command:
```bash
conda create -n ae353 python==3.8.18
```

When complete activate the new environment
```bash
conda activate ae353
```
You can confirm the virtual environment is activated when 
```
(base)
```
changes to 
```
(ae353)
```

Install condynsate with edu dependencies to the environment using the pip package manager: 
```bash
pip install condynsate[edu]
```

Once the installation is complete, you can confirm that condynsate has been successfully installed and the virtual environment is set up correctly by running the following three commands:
```python
python
import condynsate
condynsate.__version__
```
If condynsate is installed correctly, the current version will be shown. condynsate is now installed on your machine. You may type 
```python
quit()
```
to quit the Python shell.





# MacOS Installation

## 1. Install Miniconda for MacOS

If you do not have Miniconda already installed, run these four commands in the terminal to quickly and quietly install the latest 64-bit version of the installer. To open the terminal do one of the following:

- Click the Launchpad icon ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/a1f94c9ca0de21571b88a8bf9aef36b8.png) in the Dock, type Terminal in the search field, then click Terminal.
- In the Finder ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/058e4af8e726290f491044219d2eee73.png), open the /Applications/Utilities folder, then double-click Terminal.

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

**Restart the terminal.**  After installing, initialize your newly-installed Miniconda. 

```bash
~/miniconda3/bin/conda init bash
```

To verify that Miniconda is installed properly,  run the command 

```bash
conda --version
```

You should get a response that lists the version of Miniconda you just installed. If you do not, more help on installation can be found [here](https://docs.conda.io/projects/miniconda/en/latest/).





## 2. Install Git for MacOS

If you do not have Git already installed, install it via Homebew. First, open the terminal. To open the terminal do one of the following:

- Click the Launchpad icon ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/a1f94c9ca0de21571b88a8bf9aef36b8.png) in the Dock, type Terminal in the search field, then click Terminal.
- In the Finder ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/058e4af8e726290f491044219d2eee73.png), open the /Applications/Utilities folder, then double-click Terminal.

Next, type the command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Restart the terminal.** This will install [Homebrew](https://brew.sh/) on your machine. Homebrew is a package manager for MacOS. Next , install Git via Homebrew. Open a new instance of the terminal. Next, type the command:

```bash
brew install git
```

This installs Git to your system. To verify that Git installed correctly,  run the command 

```bash
git --version
```

You should get a response that lists the version of Git you just installed. If you do not, more help on installation can be found [here](https://git-scm.com/download/mac).





## 3. Clone the ae353-sp24 Repository using Git

Open the terminal. To open the terminal do one of the following:

- Click the Launchpad icon ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/a1f94c9ca0de21571b88a8bf9aef36b8.png) in the Dock, type Terminal in the search field, then click Terminal.
- In the Finder ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/058e4af8e726290f491044219d2eee73.png), open the /Applications/Utilities folder, then double-click Terminal.

Navigate to the directory you want to clone the ae353-sp24 code repository into. This is done using the  change directory command.

To move up a directory, type

```bash
cd ..
```

To move down a directory, type

```bash
cd DIR
```

Where ``DIR`` is the name of the directory you want to move into.

For example, if you start in:

```bash
user@name ~ %
```

and want to get to

```bash
user@name ~/Documents %
```

you would type the following command:

```bash
cd Documents
```

Now, clone the repository into the current directory by typing the command

```bash
git clone https://github.com/w-chang/ae353-sp24.git
```

The ae353-sp24 code repository is now cloned to your machine. You will find all design projects in this repository.





## 4. Install condynsate in a Miniconda virtual environment

To install condynsate in a Miniconda virtual environment, open the terminal and create a new virtual environment with python 3.8.18. To open the terminal do one of the following:

- Click the Launchpad icon ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/a1f94c9ca0de21571b88a8bf9aef36b8.png) in the Dock, type Terminal in the search field, then click Terminal.
- In the Finder ![img](https://help.apple.com/assets/63FFD63D71728623E706DB4F/63FFD63E71728623E706DB56/en_US/058e4af8e726290f491044219d2eee73.png), open the /Applications/Utilities folder, then double-click Terminal.

When the terminal is open, run the command: 

```bash
conda create -n ae353 python==3.8.18
```

When complete activate the new environment

```bash
conda activate ae353
```

You can confirm the virtual environment is activated when 

```
(base)
```

changes to 

```
(ae353)
```

Install condynsate with edu dependencies to the environment using the pip package manager: 

```bash
pip install condynsate control sympy spyder notebook
```

Once the installation is complete, you can confirm that condynsate has been successfully installed and the virtual environment is set up correctly by running the following three commands:

```python
python
import condynsate
condynsate.__version__
```

If condynsate is installed correctly, the current version will be shown. condynsate is now installed on your machine. You may type 

```python
quit()
```

to quit the Python shell.
