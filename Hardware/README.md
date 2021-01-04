# rSens / Hardwear
## Resistive sensors signal conditioning
### How to improve your resistive sensor (FSR) sensitivity

- Team project:
    - **Pauline Vierne** <pauline.vierne[AT]gmail.com>
    - **Maurin Donneaud** <maurin[AT]etextile.org>
- Repository: https://github.com/eTextile/rSens/tree/master
- Project web page: http://rsens.eTextile.org (TODO)
- License: CC-BY-SA (see the License file)

## Hardware folder
This folder is contaning two versions of the project.
The first one (rSens_DIL) is a proof of concept that have been done for an e-Textile one stage performance.
The second one (rSens_SMD) is a redesign that have been done to optimize the form factor of the PCB and add a second amplification line. All source files are made with [KiCad](https://kicad.org/) 5.0.* 

## Prerequisite
- Calculate the onboard DIL resistor **R1** using the included Python script [R1_calculator.py](../docs/R1_calculator.py)
This Python script will calculate automaticly the optimised resistor you need in order to get the best voltage divider Efficiency.

To run this script you will need to pass it some arguments
1. First is the minimum value of your FSR
2. Second is the maximum value of your FSR
3. Third is the input voltage of the voltage divider

```
cd rSens/docs
python R1_calculator.py 200 3450 3.3
```
4. After all you can proceed to solder the calculated DIL resistor on to the PCB

# External links
- Article : A Comprehensive Review of Sensors and Instrumentation Methods in Devices for Musical Expression
- op-Amp datasheet : TODO
