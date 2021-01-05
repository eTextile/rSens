# rSens
## E-textile resistive sensors signal conditioning
### "What about the "E" in e-textiles?"

- Team project:
    - **Pauline Vierne** <pauline.vierne[AT]gmail.com>
    - **Maurin Donneaud** <maurin[AT]etextile.org>
- Repository: https://github.com/eTextile/rSens/tree/master
- Project web page: http://rsens.eTextile.org (TODO)
- License: CC-BY-SA (see the License file)


The rSens solution is a PCB that is useful for **signal conditioning** (scale, offset and filtering). It is placed between the Analog pin of your chosen microcontroller and a resistive sensor to improve its sensitivity.

It seemed to us that signal conditioning for e-textile sensors is often underestimate or ignored, and in the best case made as bricolage at software level (thinking of Arduino map() function or interpolating methods).

You will use this hardware e-textile PCB to zoom into the sensor's significant values without losing any resolution. Furthermore, rSens is able to pick up and amplify small resistance variations, so to exploit "weak signals" e.g. from micro-movements in the case of body-worn sensors.
It should also offer advantages of filtering out noise usually picked up by voltage dividers and correcting non-linear behaviours of resistive sensors.

The rSens PCB is built on top of a quad op-Amp and allows to connect and amplify two FSR (SMD version).

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

