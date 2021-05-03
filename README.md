# open-audio-controller
------------------------------------------------------------------------------------------------------
### Overview - Purpose of system
The goal of this project is to create a REST API which can be used as a platform on which audio controller applications can be built. The aim is to provide our API as a tool with which varied and interesting projects can be created and modified. This will require a highly modular design with abstracted features in place to support plugin packages. For this reason we will be implementing very broad functionality which can be applied in a myriad of ways. Through our open source model we will be providing our API as a public package which will be available to any/all aspiring developers. Our API will be Raspberry Pi based thus we aim to have a “Plug and Play” model in order to reduce friction in all use cases and allowing non tech savvy users to benefit from our product.

### Scope
The scope of this project focuses on a REST API package/platform to be implemented for a Raspberry Pi. The core of the package should be capable of supporting the interfacing of audio I/O, support MIDI driven devices, and provide RESTful endpoints to access the data being handled by the Pi, as well as control over its configuration. Also included is an example addon package which makes use of the features that the platform provides in the form of a microphone audio enhancer. The enhancer includes the ability to perform general noise cancelation, equalising, and is built to be extendable to further methods of enhancement. The control of this example package would make use of the core platform’s modular nature to add its configuration to the platform with minimal package overrides and effort from the developers. The project as a whole would not use any proprietary software and the only cost incurred to the user would be Raspberry Pi itself.

### Current system

Currently, there are hundreds of VST applications and plug-ins, dozens of DAW applications and a handful of free, open source software all available to purchase and download over the internet. These are complex pieces of software with large teams developing them usually with huge budgets and up to years of development time which can sometimes warrant a large price tag. On the other hand, free software tends to be limited or lower quality.

Companies like AKAI and Rolland produce different types of MIDI controllers which are external devices to be used alongside DAW’s or as input devices in general to navigate through some software. The inputs from these devices come in the form of a key on a keyboard, faders, dials, etc. Combining this hardware with the software allows the process of recording, producing, mixing and mastering musical pieces to be made much more efficient and welcoming to musicians starting with digital music production.

Most of these larger products tend to be quite expensive and as such make them unavailable to those who do not have the funds for them. As Well as this the cheaper ones on the cheaper end of the spectrum tend to be of much lower quality than what would be desired by those who employ them.
 
### Proposed System
Our proposed solution involves the use of a Python Flask based package on the Pi to provide the endpoints for our configuration utilities and potentially MIDI device output. Streaming audio data through a REST API is not feasible thus we shall operate on data acquired through the USB or audio ports on the Raspberry Pi. The core package will also feature the ability to intercept audio streams from either of these ports, apply any preconfigured processing and route that to the connected machine.
Given that Raspberry Pi’s run a Unix environment, the installation of the core package will reconfigure certain boot settings to ensure the service is launched on startup and the previously set up mode of operation is ready to plug in and use straight away.
The initial UI will likely be a simple CLI, but with plans to build a WebUI to allow for easy viewing of what the device is doing and what settings the user can access.
The microphone enhancer will be a proof of concept package to be recognised and loaded by the core, adding its functionality into the platform. Any UI present will immediately add the configurations for the plugin to the available options.

