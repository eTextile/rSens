# rSens
## Resistive sensors signal conditioning
### How to improve your resistive sensor sensitivity

- Team project:
    - **Pauline Vierne** <pauline.vierne[AT]gmail.com>
    - **Maurin Donneaud** <maurin[AT]etextile.org>
- Repository: https://github.com/eTextile/rSens/tree/master
- Project web page: http://rsens.eTextile.org (TODO)
- License: CC-BY-SA (see the License file)

The rSens solution is a PCB that is useful for **signal conditioning** (scale & offset) before using your microcontroller Analog to Digital Converter (ADC). In other words this project can be compared to the Arduino map() function but instead of using software fonction you will use this hardware eTextile PCB to zoom into the significant values without losing any resolution. The rSens PCB is built on top of a quad op-Amp that offers the possibility to work with two FSR.

## Project content
- **Hardware**: containing all PCB source files of the project
- **Firmware**: read and graph the analog sensor values with [Arduino](https://www.arduino.cc/)

## Prerequisite
- The rSens PCB can be used in combination with any resistive sensors (custom or industrial)
- Adding R1 resistor to form an [optimised voltage divider](./Hardware#prerequisite)

**Keywords** `FSR`,`strain gages`,`e-textile`,`digital musical instruments`,`Do-It-Yourself`

# External links
- The Arduino [map() function](https://www.arduino.cc/reference/en/language/functions/math/map/)
- op-Amp datasheet

