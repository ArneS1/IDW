name = data.get("name","world")
logger.info("Hallo %s", name)
hass.bus.fire(name, {"wow": "from a Python Script!"})
