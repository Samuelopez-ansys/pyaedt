"""
EMIT Example
--------------------------------------------
This tutorial shows how you can use PyAEDT to create a project in in EMIT.
"""

# TODO: update thumbnail
# sphinx_gallery_thumbnail_path = 'Resources/circuit.png'

from pyaedt import Emit
from pyaedt import Circuit
from pyaedt import Desktop

###############################################################################
# Initialization Settings
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change NonGraphical Boolean to False to open AEDT in graphical mode
# With NewThread = False, an existing instance of AEDT will be used, if available.
# This example will use AEDT 2021.2
NonGraphical = False
NewThread = False
desktopVersion = "2021.2"


###############################################################################
# Launch AEDT and EMIT Design
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Desktop class initializes AEDT and starts it on specified version and specified 
# graphical mode. NewThread Boolean variable defines if a user wants to create 
# a new instance of AEDT or try to connect to existing instance of it.
d = Desktop(desktopVersion, NonGraphical, NewThread)
aedtapp = Emit()


###############################################################################
# Create and Connect EMIT Components
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create 3 radios and connect an antenna to each.
rad1 = aedtapp.modeler.components.create_component("UE - Handheld")
ant1 = aedtapp.modeler.components.create_component("Antenna")
ant1.move_and_connect_to(rad1)

rad2 = aedtapp.modeler.components.create_component("GPS Receiver")
ant2 = aedtapp.modeler.components.create_component("Antenna")
ant2.move_and_connect_to(rad2)

rad3 = aedtapp.modeler.components.create_component("Bluetooth")
ant3 = aedtapp.modeler.components.create_component("Antenna")
ant3.move_and_connect_to(rad3)


###############################################################################
# Define Coupling Among the RF Systems
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This portion of the EMIT API is not yet implemented.


###############################################################################
# Run the EMIT Simulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This portion of the EMIT API is not yet implemented.


###############################################################################
# Close Desktop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# After the simulaton is completed user can close the desktop or release it 
# (using release_desktop method). All methods give possibility to save projects 
# before exit.
aedtapp.save_project()
aedtapp.release_desktop(close_projects=True, close_desktop=True)