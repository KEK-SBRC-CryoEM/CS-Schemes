# RELION / CS-Schemes Parameter Automation

Automate the computation of RELION CS-Schemes parameters. This tool runs user-defined analysis scripts (CTF limits, box size estimation, masking, etc.), 
extracts their results, and uses them to generate a: `config_sample_settings.yml` for the CS-Schemes.

---
## What It Does

User provides a single configuration file describing:

1. Analyses to run  
2. Which outputs to extract  
3. How those outputs map to CS-Scheme parameters  

The pipeline then:

Run analyses → Collect results → Compute parameters → Write RELION config

---
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Running the Pipeline](#running-the-pipeline)
<!-- - [Configuration](#configuration) -->
<!-- - [Output](#output) -->
<!-- - [Examples](#examples) -->
<!-- - [Troubleshooting](#troubleshooting) -->
<!-- - [License](#license) -->

---
## Requirements

### 1. Core Pipeline

- Python 3.10+
- PyYAML
- NumPy

---

### 2. External Analyses

The pipeline only manage execution and  does **not** install or manage third-party tool dependencies. For this reason, any scripts executed by the pipeline must have their own dependencies installed in the environments they run in.

## Installation

### 1. Get the source code

Clone the repository:

```bash
git clone https://github.com/KEK-SBRC-CryoEM/CS-Schemes/
cd CS-Schemes
````

Since this script is still in development, switch branch to:

```bash
git switch auto_parameters
```

---

### 2. Install core dependencies

You can use either **pip** or **conda**.

#### Using pip

```bash
pip install pyyaml numpy
```

#### Using conda

Create an environment and install the requirements:

```bash
conda create -n auto_csschemes python=3.10 pyyaml numpy
conda activate auto_csschemes
```

---

### 3. Prepare external analysis environments

Ensure any external tools or scripts referenced in your
pipeline configuration have their required dependencies
installed in their respective environments.

## Quick Start
todo

## Running the Pipeline

### 1. Create a pipeline config file

Example: `config.yaml`

### Define analyses

Each analysis is an external script you want to run.

```yaml
analyses:
  - name: contour_size
    executable: /envs/dev/bin/python
    script: /apps/contour.py
    args:
      - ["--input_mask", "mask.mrc"]
```
---

#### Reference outputs from one analysis in another

```yaml
(...)
- ["--particle_diameter", {from: "contour_size", attribute: "radius"}]
(...)
```

---

## Argument Format
Arguments are defined as in the example below:

```yaml
args:
  - "--flag"              # flag only
  - ["--param", "value"]  # literal value
  - ["--param", {from: "A", attribute: "attr"}] # get 'attr' from analysis 'A'
```

---

### 2. Define parameter mappings

Use analysis outputs to populate RELION parameters.

```yaml
parameters:
  GTF_lbin_extract_mics_box: {from: "fresnel", attribute: "boxsize"}
```

---

### 3. Run the Pipeline

Finally, run the pipeline script.

```bash
python run_pipeline.py -c config.yaml
```

---
