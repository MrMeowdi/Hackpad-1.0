"""Enable a second USB serial channel for PC telemetry and control commands."""
import usb_cdc

usb_cdc.enable(console=True, data=True)
