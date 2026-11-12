# Hackpad-1.0

<img width="1667" height="783" alt="image" src="https://github.com/user-attachments/assets/6c5b4ffc-d158-4c81-9e37-a7ae3f2979bb" />

This is by far my first project made completely from Tutorials and Guides on YouTube however I made some of the changes by seeking ideas from 2 old hack club events i.e. highway and statis from where I gathered more ideas and easy techniques to do so.

I basically made a hackpad consisting of 8 keys and 1 rotary encoder each having per key RGB and also an OLED screen to view various stats of PC its connected to like resource used etc

I have done the code on VsCode from some of my knowledge and some of ChatGPT

USE ANY KEYCAPS AND ENCODER KNOB OF YOUR CHOICE xd!

## How To Assemble

> Solder all components on the PCB board carefully at its place,  wiring diagram is also shown below  in images section, visit if necessary

> Place the PCB on the desired spot on the Base part of the 3d printed case

> Now close the case by putting some doublesided tape on the poles that get inserted in the spot in the bottom part of the case


## How to Upload Firmware

Now since the assembling part is completed, we need to focus on the firmware part

> Connect the XIAO while a usb-c cable and connect it to your computer

> Use any microcontroller firmware uploading software like "Thonny" or "ArduinoIDE" and install micropython

> Copy and paste the firmware from the main.py or directly download and upload the file in the XIAO

> Upload the 2nd file also named as boot.py enabling Pc stats tramsfer over USB 

### REQUIREMEMTS

These modules are required to install the firmware and make it work 

> psutil
 
> pyserial

## Features And Operations 

**KEY1** — Copy (`Ctrl+C`)  
**KEY2** — Paste (`Ctrl+V`)  
**KEY3** — Undo (`Ctrl+Z`)  
**KEY4** — Cut (`Ctrl+X`)  
**KEY5** — Save (`Ctrl+S`)  
**KEY6** — Switch between open apps (`Alt+Tab`)  
**KEY7** — Go to the start of the current line (`Home`)  
**KEY8** — Open the system task manager (`Ctrl+Shift+Esc`)  
**EC11 single press** — Switch OLED page  
**EC11 double press** — Switch between volume and brightness mode  
**EC11 turn** — Adjust volume or brightness, depending on the selected mode  

## Pricing And BOM

## Pricing And BOM

| Designator | Component | Selected part / description | Qty on PCB | Purchase pack | Allocated cost |
|---|---|---|---:|---:|---:|
| MX1–MX8 | Mechanical key switches | [GranVela Outemu Red, 3-pin linear, 45 g](https://www.amazon.in/GranVela-Red-Hot-Swappable-Equivalent-Keyboard-20/dp/B073WBY7J3) | 8 | $18.32 / 20 | $7.80 |
| LED1–LED8 | Addressable RGB LEDs | [Lonoa SK6812 MINI-E, 5 V](https://www.ubuy.co.in/productjp/QW0BOLVDC-lonoa-50pcs-sk6812-mini-e-rgb-same-as-ws2812b-sk6812-3228-pixels-led-chip-individually-addressable-full-color-dc5v) | 8 | $2.00 / 50 pcs | $0.40 |
| R1 | Resistor | [Electronic Spices 330 Ω, 1/4 W, ±5%](https://www.amazon.in/Electronic-Spices-Tolerance-Through-Resistors/dp/B0BDG2F7FL) | 1 | $0.84 / 50 | $0.05 |
| U2 | OLED display module | [Robocraze 0.91 in blue, 128×32, I²C](https://www.amazon.in/dp/B084H9HLCS) | 1 | $2.94 / 1 | $3.20 |
| SW1 | Rotary encoder with push switch | [CentIoT EC11, 5-pin, 20 mm half shaft](https://www.amazon.in/dp/B0888RVZSN) | 1 | $2.63 / 2 | $1.50 |
| U1 | Controller module | [Seeed Studio XIAO RP2040, SKU 102010428](https://www.amazon.in/Microcontroller-Dual-Core-MicroPython-CircuitPython-Interfaces/dp/B09NNVNW7M) | 1 | $16.20 / 1 | $17.00 |
| PCB | Printed circuit board | Custom Macropad PCB | 1 | $14.00 / 1 | $19.07 |
| KC1–KC8 | Transparent PBT keycaps | [CALANDIS 10× 1U Thick PBT Transparent Keycaps](https://www.amazon.in/dp/B0F13YK4D6) | 8 | ₹635 / 10 pcs | $5.48 |
| | **TOTAL** | | **29** | | **$54.50** |

### Estimated Total: $54.50 USD


<img width="1452" height="803" alt="image" src="https://github.com/user-attachments/assets/576c7a14-6cf8-45cd-b8cf-b58da087a63b" />

<img width="1063" height="568" alt="image" src="https://github.com/user-attachments/assets/c94df439-2b61-4750-bb0c-f96872d26a3d" />


## Images
<img width="1448" height="817" alt="image" src="https://github.com/user-attachments/assets/8adef572-e858-4407-8ee3-58f3bf1f3406" />

<img width="707" height="809" alt="image" src="https://github.com/user-attachments/assets/38990d06-ead9-44a8-a9d7-c8c84f1ff7f0" />

<img width="971" height="845" alt="image" src="https://github.com/user-attachments/assets/4ebbb98c-c2ee-4460-8a51-21dd16d4f614" />

<img width="1107" height="871" alt="image" src="https://github.com/user-attachments/assets/6d3771c0-98f8-4c77-a5a7-706377caf235" />

<img width="1607" height="778" alt="image" src="https://github.com/user-attachments/assets/7e7e2a8c-456f-4967-8ec5-5a0c07bc2121" />



<img width="1535" height="732" alt="image" src="https://github.com/user-attachments/assets/2806c6e7-2bcf-4004-8169-7e1d09cf0440" />

<img width="1602" height="742" alt="image" src="https://github.com/user-attachments/assets/a77e34a5-7305-4860-8bdc-8b030ecde321" />

<img width="913" height="805" alt="image" src="https://github.com/user-attachments/assets/43a01b57-84c6-4a13-94cc-e04ad0b1eceb" />

<img width="1662" height="803" alt="image" src="https://github.com/user-attachments/assets/c0fb11ea-06c3-4acc-84d9-0d0bfe02ecfa" />


