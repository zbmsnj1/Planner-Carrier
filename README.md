![icon](https://github.com/lslll0302/Planner-Carrier/blob/master/images/PlannerCarrier.png)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

**This is a simple framework to help testing vast [AI planning](https://planning.wiki/) benchmarks in parallel with multiple planners, collecting and analyzing data with customizable keywords. Done in pure Python.**

## Table of Contents

* [Background](#background)
* [Install](#install)
* [Usage](#usage)
* [Directory Structure](#directory)
* [Contributing](#contributing)
* [License](#license)


## Background
In my honour year project about FOND planning, we have large numbers of benchmarks to test, get the results and analyze the data.The command of each planner to run one benchmark is very long because it includes the path of domain and problem files. First, we use shell script to run commands automatically for multiple benchmarks in series. But for some planners like SAT-based planner, it takes one hour to finish a benchmark frequently. In order to speed up the experiment, my supervisor  and I wish to develop a simple framework for testing planning benchmarks parallelly on one machine or clusters. It will greatly improve the efficiency of the experiment, based on the computer CPU core numbers or clusters size. This is the original reason for this project. After finishing the framework, we add some additional features such as collecting and analyzing data to make the framework more useful.


## Install
#### Prerequisites
* Linux (tested on Ubuntu 20.04.1)
* Python3.6 or above
* [Dask](https://dask.org/)
#### Clone repo from GitHub
```
$ git clone https://github.com/lslll0302/Planner-Carrier.git
```
#### Install complete Dask 
```
$ python -m pip install "dask[complete]"
```
## Usage

Check details in [usage-readme]()

## Directory Structure
* `Database/`: 
    * `path/`: store relative path of corresponding domain and problem files for benchmarks
    * `benchmarks.csv`: a csv file includes names and problem sizes corresponding to all benchmarks in `benchmarks/`
* `benchmarks/`: the current benchmarks of FOND planning (`*.pddl`)
* `planner/`: the source code for the-state-of-art of FOND planners
    * Implemented: [PRP](https://github.com/QuMuLab/planner-for-relevant-policies), [SAT](https://github.com/tomsons22/FOND-SAT)
    * Not yet: [MBP](http://mbp.fbk.eu/), [myND](https://bitbucket.org/robertmattmueller/mynd), [Gamer](http://fai.cs.uni-saarland.de/kissmann/planning/downloads/),  [FIP](http://cs2.uco.edu/~fu/research.html)([Code+Sample Problems] can be found in the end of the publication: *Fast strong planning for fully observable nondeterministic planning problems*)
* `results/`:
	* `PRP/`or `SAT/`:
		* `data/`: all digitial data collected using corresponding key words stored in a `.csv` file for each benchamark
		* `mean/`: the average of the data in `data/` with customized sizes stored in `.csv` files
		* ` output/`: all **standard output** (**stdout**) of tested experiments stored in `.txt` files
* `src/`: including the code files to updat database, to create task file, to run the planning benchmarks in parallel on a single machine or on a distrubted cluster

## Contributing

Feel free to dive in! [Open an issue](https://github.com/lslll0302/Planner-Carrier/issues/new) or submit PRs.


#### Acknowledgement

This project exists thanks to my supervisor [Sebastian Sardina](https://sites.google.com/view/ssardina/home)

<a href="https://github.com/ssardina"><img src="https://github.com/lslll0302/Planner-Carrier/blob/master/images/Sebastian%20Sardina.jfif" class="round_icon" title="Sebastian Sardina" width="80" height="80"></div>


## License

[MIT](LICENSE) © Richard Littauer

