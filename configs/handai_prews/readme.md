# Cryo-EM CS-Schemes Setup on PREWS

## Overview
This document provides a step-by-step guide to setting up the following software components:

* Python environment (pyenv and conda)
* GoToCloud scripts
* crYOLO
* CTFFIND-4
* UCSF Chimera
* select_class3d
* CS-Schemes

This guide **assumes that RELION is already installed and available** on the system.

This setup is based on: https://sites.google.com/sbrc.jp/gotocloud-install/installation



## 1) Preliminaries
### 1.1) Create the base directories:

```bash
mkdir -p /home/user/shared_for_all/apps
mkdir -p /home/user/shared_for_all/apps/modulefiles
mkdir -p /home/user/shared_for_all/apps/rln_external
mkdir -p /home/user/shared_for_all/data
```

* All applications and scripts installed under `apps`
* All datasets stored under `data/<user>`

### 1.2) Add modulefiles directory to MODULEPATH (persistent)
Edit your shell configuration file:
```bash
nano ~/.bashrc
```

Add the following line:
```bash
export MODULEPATH="/home/user/shared_for_all/apps/modulefiles:$MODULEPATH"
```

Apply the changes:
```bash
source ~/.bashrc
```

### 1.3) Add RELION extra submission parameters (persistent)
Edit your shell configuration file:

```bash
nano ~/.bashrc
```

Add the following lines:

```bash
export RELION_QSUB_EXTRA_COUNT=2

export RELION_QSUB_EXTRA1="Partition"
export RELION_QSUB_EXTRA1_DEFAULT=cpu
export RELION_QSUB_EXTRA1_HELP="Partitions: cpu, gpu"

export RELION_QSUB_EXTRA2="Number of nodes"
export RELION_QSUB_EXTRA2_DEFAULT=1
```

Apply the changes:

```bash
source ~/.bashrc
```

## 2) Install pyenv and conda
### 2.1) Install pyenv
Clone the pyenv repository:

```bash
cd /home/user/shared_for_all/apps/
git clone https://github.com/pyenv/pyenv
```

#### Add pyenv to your PATH (persistent)

Edit your shell configuration file:

```bash
nano ~/.bashrc
```

Add the following lines to the end of the file:

```bash
export PATH=/home/user/shared_for_all/apps/pyenv/bin:$PATH
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Save the file and reload your shell.
```bash
source ~/.bashrc
```
### 2.2) Install conda via pyenv

Install a specific Anaconda distribution:

```bash
pyenv install anaconda3-2025.06-1
```

#### Set the Anaconda version as the default

```bash
pyenv global anaconda3-2025.06-1
```

#### Verify the installation

List installed Python/Conda versions managed by pyenv:

```bash
pyenv versions
```

You should see `anaconda3-2025.06-1` marked as the active version.

Refresh the terminal:
```bash
conda init bash
source ~/.bashrc
```

----
## 3) Install GoToCloud scripts

Clone the **GoToCloud** repository into the shared applications directory:

```bash
cd /home/user/shared_for_all/apps
git clone https://github.com/KEK-SBRC-CryoEM/gotocloud.git
```
## 4) Install crYOLO
Before proceeding, move the crYOLO integration scripts from the GoToCloud repository into their own directory:
```bash
cp -r /home/user/shared_for_all/apps/gotocloud/cryolo /home/user/shared_for_all/apps/rln_external/
```

### 4.1) Installation in a Conda environment

Create a dedicated Conda environment for crYOLO (version 1.9.6):
```bash
conda create -n cryolo-1.9.6 -c conda-forge -c anaconda pyqt=5 python=3 numpy=1.18.5 libtiff wxPython=4.1.1 adwaita-icon-theme 'setuptools<66'
```

Activate the environment using pyenv and install crYOLO:
```bash
pyenv shell anaconda3-2025.06-1/envs/cryolo-1.9.6
pip install nvidia-pyindex
pip install 'cryolo[c11]==1.9.6'

pyenv shell --unset
```

### 4.2) System module for crYOLO
Create a modulefile for crYOLO:
```bash
mkdir -p /home/user/shared_for_all/apps/modulefiles/crYOLO
cd /home/user/shared_for_all/apps/modulefiles/crYOLO
```

Create the module file:
```bash
cat > 1.9.6
```

Paste the following contents:
```bash
#%Module -*- tcl -*-
set root /home/user/.pyenv/versions/anaconda3-2025.06-1/envs/cryolo-1.9.6

setenv CRYOLOPATH $root
prepend-path PATH $root/bin

setenv CRYOLO_SUBMIT_CMD		sbatch
setenv CRYOLO_SUBMIT_SCRIPT     /home/user/shared_for_all/apps/gotocloud/submission_script/apps/gotocloud/submission_script/prews_slurm_relion500_gpu4.sh
```
Save and exit.

Then, set the default module version

```bash
cat > .version
```

Paste:

```bash
#%Module 1.0
set ModulesVersion 1.9.6
```

Save and exit.

### 4.3) Download crYOLO general models
Download the official pre-trained crYOLO models.

First, change to the models directory:
```bash
mkdir -p /home/user/shared_for_all/apps/rln_external/cryolo/models
cd /home/user/shared_for_all/apps/rln_external/cryolo/models
```

Then download the models:

Source:
[https://cryolo.readthedocs.io/en/stable/installation.html#download-the-general-models](https://cryolo.readthedocs.io/en/stable/installation.html#download-the-general-models)

```bash
wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO-GENERAL-MODELS/gmodel_phosnet_202005_N63_c17.h5
wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO-GENERAL-MODELS/gmodel_phosnet_202005_nn_N63_c17.h5
wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO-GENERAL-MODELS/gmodel_phosnet_negstain_20190226.h5
```

### 4.4) Create symbolic links for RELION integration

Create symbolic links:

```bash
ln -s /home/user/shared_for_all/apps/rln_external/cryolo/models/gmodel_phosnet_202005_N63_c17.h5 /home/user/shared_for_all/apps/rln_external/cryolo/gmodel_phosnet_lpf_link.h5

ln -s /home/user/shared_for_all/apps/rln_external/cryolo/models/gmodel_phosnet_202005_nn_N63_c17.h5 /home/user/shared_for_all/apps/rln_external/cryolo/gmodel_phosnet_denoise_link.h5

ln -s /home/user/shared_for_all/apps/rln_external/cryolo/models/gmodel_phosnet_negstain_20190226.h5 /home/user/shared_for_all/apps/rln_external/cryolo/gmodel_phosnet_negstain_link.h5
```
## 5) Install CTFFIND-4

CTFFIND-4 must be downloaded manually from the official website:

[https://grigoriefflab.umassmed.edu/ctf_estimation_ctffind_ctftilt](https://grigoriefflab.umassmed.edu/ctf_estimation_ctffind_ctftilt)

### Download and transfer to the server

On your **local machine**, download the Linux binary archive, then copy it to the server:

```bash
scp ctffind-4.1.14-linux64.tar.gz user@prews-login.pdbj.org:/home/user/shared_for_all/apps/
```

### Extract files

On the **server**, change to the destination directory and extract the archive:

```bash
cd /home/user/shared_for_all/apps/
tar -zxf ctffind-4.1.14-linux64.tar.gz
```
## 6) Install UCSF Chimera

### 6.1) Download and transfer to the server
Download the Chimera installer on your **local machine**, then copy it to the server:
```bash
scp chimera-1.19-linux_x86_64.bin user@prews-login.pdbj.org:/home/user/shared_for_all/apps/chimera/
```

### 6.2) Install Chimera
On the **server**, make the installer executable and run it:
```bash
cd /home/user/shared_for_all/apps/chimera
chmod +x chimera-1.19-linux_x86_64.bin
./chimera-1.19-linux_x86_64.bin
```

When prompted, use the following installation path:
```text
/home/user/shared_for_all/apps/chimera/UCSF-Chimera64-1.19
```

### 6.3) Module setup
Create a modulefile for Chimera:
```bash
mkdir -p /home/user/shared_for_all/apps/modulefiles/chimera
cd /home/user/shared_for_all/apps/modulefiles/chimera
```

Create the module file:
```bash
cat > 1.19
```

Paste the following:

```
#%Module1.0
set-alias chimera /home/user/shared_for_all/apps/chimera/UCSF-Chimera64-1.19/bin/chimera
```

Save and exit.

Set the default module version:

```bash
cat > .version
```

Paste:

```
#%Module 1.0
set ModulesVersion 1.19
```

Save and exit.

---

### 6.4) Usage

After setup, Chimera can be loaded with:

```bash
module load chimera
```

The Chimera GUI cannot be launched directly and is only available via command-line execution. Some other modules (e.g., CryoRead) require this module to be loaded.

## 7) Install select_class3d
Move the necessary integration scripts from the GoToCloud repository into their own directory:

```bash
cp -r /home/user/shared_for_all/apps/gotocloud/select_class3d /home/user/shared_for_all/apps/rln_external/
```
## 8) CS-Schemes

### 8.1) Download
Clone the CS-Schemes repository:
```bash
cd /home/user/shared_for_all/apps
git clone https://github.com/KEK-SBRC-CryoEM/CS-Schemes
```

#### Checkout the required branch (temporary)

> **Note:** Until the related PR is merged, switch to the `handai-prews` branch.

```bash
git checkout handai-prews
```

#### Verify configuration files

Confirm the following configuration paths are correctly set.

**1. Submission script configuration**

File:
```bash
cat configs/handai_prews/config_level_submission.yml
```

Ensure `SubmissionScript:` points to the installed GoToCloud submission scripts:
```bash
/home/user/shared_for_all/apps/gotocloud/submission_script/
```

**2. System settings configuration**
File:
```
cat configs/handai_prews/config_system_settings.yml
```

Verify the following entries:
```yaml
CTFFIND4Executable: '/apps/packages/cisTEM-2.0.0-alpha-183/bin/ctffind'
CrYOLORepo: '/home/user/shared_for_all/apps/rln_external/cryolo/'
SelectClass3DExecutable: '/home/user/.pyenv/versions/anaconda3-2025.06-1/envs/cryolo-1.9.6/bin/python /home/user/shared_for_all/apps/rln_external/select_class3d/gtf_relion4_run_select_class3d.py'
```

### 8.2) Create Conda environment
Use the Anaconda version managed by pyenv:
```bash
pyenv shell anaconda3-2025.06-1
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n schemes-editing python=3.8
```

### 8.3) Install additional Python libraries
Activate the environment and install required packages:
```bash
conda activate schemes-editing
conda install starfile
conda install pyyaml
```

### 8.4) System module
Create a modulefile for the CS-Schemes editing environment:
```bash
mkdir -p /home/user/shared_for_all/apps/modulefiles/schemes-editing
cat > /home/user/shared_for_all/apps/modulefiles/schemes-editing/1.0
```

Paste the following:

```
#%Module 1.0
set root /home/user/.pyenv/versions/anaconda3-2025.06-1/envs/schemes-editing/
prepend-path PATH $root/bin
```

### 8.5) Usage
```bash
module load schemes-editing
```
### 8.6) Test run using the RELION Tutorial dataset

This section verifies that **CS-Schemes and the schemes editor** are correctly installed and integrated with RELION.

#### Step 1: Run CS-Schemes setup for the `handai_prews` configuration
```bash
python3 /home/user/shared_for_all/apps/CS-Schemes/kek_schemes_setup.py -e handai_prews -s /home/user/shared_for_all/apps/
```

#### Step 2: Download the RELION tutorial dataset
```bash
mkdir -p /home/user/shared_for_all/data/schemes_editor_test_dataset
cd /home/user/shared_for_all/data/schemes_editor_test_dataset

wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion30_tutorial_data.tar
tar -xf relion30_tutorial_data.tar
```

#### Step 3: Copy the sample configuration file to the project directory
```bash
cp /home/user/shared_for_all/apps/schemes_editor/configs/common_tutorial/config_sample_settings.yml /home/user/shared_for_all/data/schemes_editor_test_dataset/
```

#### Step 4: Set environment-dependent configuration path
```bash
export SE_ENV_DEFAULT_CONFIGS=/home/user/shared_for_all/apps/schemes_editor/configs/environment_dependent_tutorial/default_configs.yml
```

#### Step 5: Run `schemes_editor.py`
Change to your RELION project directory:
```bash
cd /home/user/shared_for_all/data/relion_tutorial_cs_schemes_test001
```

Load required modules:
```bash
module load relion
module load schemes-editing
```

Run the schemes editor:
```bash
python3 -W ignore::FutureWarning /home/user/shared_for_all/apps/schemes_editor/schemes_editor.py -t /home/user/shared_for_all/apps/schemes_editor/schemes_template/cs_schemes -s ./config_sample_settings.yml
```

Copy the generated schemes into the project directory:
```bash
cp -r Schemes_Edited/Schemes ./
```
#### Step 6: Confirm that scheme parameters were correctly replaced
Check the template values:
```bash
cat /home/user/shared_for_all/apps/schemes_editor/schemes_template/cs_schemes/*/*_External_cryolo*/job.star | grep param3_value
```

Expected output:
```
param3_value     XXX_JSE_REPLACE_PARALLEL_XXX
```

Check the edited schemes:
```bash
cat ./Schemes/*/*_External_cryolo*/job.star | grep param3_value
```

Expected output:
```
param3_value          0
```

This confirms that the schemes editor successfully replaced template placeholders.



#### Step 7: Run RELION Scheme GUI
Unload the editing environment and load RELION:

```bash
module unload schemes-editing
module load relion
```

Launch RELION and the scheme GUIs:
```bash
cd /home/user/shared_for_all/data/relion_tutorial_cs_schemes_test001
relion &

relion_schemegui.py 010_GTF_MotionCorr &
relion_schemegui.py 020_GTF_CtfFind &
relion_schemegui.py 030_GTF_Create_Stack &
relion_schemegui.py 060_CSS_Clean_Stack_3D &
relion_schemegui.py 070_CSS_Init_Refine3D &
relion_schemegui.py 090_CSS_Res_Fish_3D &
```

[//]: # (relion_schemegui.py 040_GTF_Class2D_PMDs &)
[//]: # (relion_schemegui.py 050_GTF_AbInitReconst3D &)
[//]: # (relion_schemegui.py 080_CSS_PPRefine_Cycle &)

