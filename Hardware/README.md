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
- This folder is contaning two versions of the project.
- **rSens_DIL** is a proof of concept that have been done for an e-Textile one stage performance.
- **rSens_SMD** is a redesign that have been done to optimize the form factor of the PCB and add a second amplification line.
- All source files are made with [KiCad](https://kicad.org/) 5.0.* 

## Prerequisite
Calculate the onboard DIL resistor **R1** using the included Python script [R1_calculator.py](../docs/R1_calculator.py)
This Python script will automaticly calculate the best resistor value that you need to get the best voltage divider efficiency.

To run this script you will need first to identify your sensor characteristics in order to be able to pass those values as arguments to the script :

1. First Arg is the resistivity (in Ohm) of your FSR sensor at rest
2. Second Arg is the resistivity (in Ohm) of your FSR sensor at maximum effort

```
cd rSens/docs
```
```
python R1_calculator.py 200 3450
```

3. If you run the script with the above arguments you must get the following result

```
R1 = 830 Ohm
Efficiency = 61.19 %
```
5. After all you can solder the calculated R1 resistor on to the PCB

# External links
- Article : A Comprehensive Review of Sensors and Instrumentation Methods in Devices for Musical Expression
- op-Amp datasheet : TODO
