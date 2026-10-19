# Units

**Type:** data

Every unit the verifier understands, each defined from the SI base units or from a unit above it. The verifier reads the first table as unit definitions and the second as SI prefixes. Add a row before using a new unit in a verify block.

The SI base units are defined by fixing seven constants of nature (see [constants](constants.md)), so this table depends on no artefact or institution: a reader who can measure the caesium frequency, the speed of light, and the Planck constant can rebuild every row.

| Symbol | Name | Value | In terms of | Exact | Source | Locator |
|---|---|---|---|---|---|---|
| m | metre | base | | yes | bipm-si-9 | section 2.3.1 |
| kg | kilogram | base | | yes | bipm-si-9 | section 2.3.1 |
| s | second | base | | yes | bipm-si-9 | section 2.3.1 |
| A | ampere | base | | yes | bipm-si-9 | section 2.3.1 |
| K | kelvin | base | | yes | bipm-si-9 | section 2.3.1 |
| mol | mole | base | | yes | bipm-si-9 | section 2.3.1 |
| cd | candela | base | | yes | bipm-si-9 | section 2.3.1 |
| rad | radian | 1 | 1 | yes | bipm-si-9 | Table 4 |
| sr | steradian | 1 | 1 | yes | bipm-si-9 | Table 4 |
| rev | revolution | 6.283185307179586 | rad | yes (2 pi rad) | definition | |
| deg | degree of angle | 0.017453292519943295 | rad | yes (pi/180 rad) | bipm-si-9 | Table 8 |
| % | percent | 0.01 | 1 | yes | definition | |
| percent | percent | 0.01 | 1 | yes | definition | |
| g | gram | 0.001 | kg | yes | bipm-si-9 | section 3 |
| min | minute | 60 | s | yes | bipm-si-9 | Table 8 |
| h | hour | 3600 | s | yes | bipm-si-9 | Table 8 |
| d | day | 86400 | s | yes | bipm-si-9 | Table 8 |
| Hz | hertz | 1 | s^-1 | yes | bipm-si-9 | Table 4 |
| N | newton | 1 | kg m/s^2 | yes | bipm-si-9 | Table 4 |
| Pa | pascal | 1 | N/m^2 | yes | bipm-si-9 | Table 4 |
| J | joule | 1 | N m | yes | bipm-si-9 | Table 4 |
| W | watt | 1 | J/s | yes | bipm-si-9 | Table 4 |
| C | coulomb | 1 | A s | yes | bipm-si-9 | Table 4 |
| V | volt | 1 | W/A | yes | bipm-si-9 | Table 4 |
| ohm | ohm | 1 | V/A | yes | bipm-si-9 | Table 4 |
| S | siemens | 1 | A/V | yes | bipm-si-9 | Table 4 |
| F | farad | 1 | C/V | yes | bipm-si-9 | Table 4 |
| Wb | weber | 1 | V s | yes | bipm-si-9 | Table 4 |
| T | tesla | 1 | Wb/m^2 | yes | bipm-si-9 | Table 4 |
| H | henry | 1 | Wb/A | yes | bipm-si-9 | Table 4 |
| VA | volt-ampere, the name used for apparent power | 1 | V A | yes (a watt by dimension) | definition | |
| var | var, the name used for reactive power | 1 | V A | yes (a watt by dimension) | definition | |
| L | litre | 0.001 | m^3 | yes | bipm-si-9 | Table 8 |
| bar | bar | 100000 | Pa | yes | nist-sp811 | Appendix B.8 |
| atm | standard atmosphere | 101325 | Pa | yes | nist-sp811 | Appendix B.8 |
| eV | electronvolt | 1.602176634e-19 | J | yes | bipm-si-9 | Table 8 |
| ft | foot | 0.3048 | m | yes | nist-sp811 | Appendix B.8 |
| in | inch | 0.0254 | m | yes | nist-sp811 | Appendix B.8 |
| lb | pound (avoirdupois) | 0.45359237 | kg | yes | nist-sp811 | Appendix B.8 (listed there rounded to 0.4535924) |
| lbf | pound-force | 9.80665 | lb m/s^2 | yes (lb times standard gravity) | nist-sp811 | Appendix B.8 (listed there rounded to 4.448222 N) |
| psi | pound-force per square inch | 1 | lbf/in^2 | yes | nist-sp811 | Appendix B.8 (6.894757 kPa, rounded) |
| ksi | kilopound-force per square inch | 1000 | psi | yes | nist-sp811 | Appendix B.8 |
| hp | horsepower (550 ft lbf/s) | 550 | ft lbf/s | yes | nist-sp811 | Appendix B.8 (745.6999 W, rounded) |
| BtuIT | British thermal unit (IT) | 1055.05585262 | J | yes | nist-sp811 | Appendix B.8 (1.055056 kJ, rounded) |

SI prefixes:

| Prefix | Factor |
|---|---|
| Y | 1e24 |
| Z | 1e21 |
| E | 1e18 |
| P | 1e15 |
| T | 1e12 |
| G | 1e9 |
| M | 1e6 |
| k | 1e3 |
| h | 1e2 |
| da | 1e1 |
| d | 1e-1 |
| c | 1e-2 |
| m | 1e-3 |
| u | 1e-6 |
| n | 1e-9 |
| p | 1e-12 |
| f | 1e-15 |
| a | 1e-18 |
