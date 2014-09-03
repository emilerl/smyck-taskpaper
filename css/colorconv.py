#!/usr/bin/env
# Converts the SMYCK css file to XML for TaskPaper theme

import struct
import cssutils

def hex_to_rgb(rgbstr):
	return struct.unpack('BBB',rgbstr.decode('hex'))

def rgb32(rgbtuple):
	return (float(rgbtuple[0])/255.0, float(rgbtuple[1])/255.0, float(rgbtuple[2])/255.0)

if __name__ == '__main__':
	template = '<color id="%s" red="%f" green="%f" blue="%f" alpha="1.0"/>'
	parsed = cssutils.parseFile("./style.css")
	for rule in parsed.cssRules:
		if isinstance(rule, cssutils.css.CSSStyleRule):
			if rule.selectorText.startswith("#"):
				if len(rule.style.backgroundColor) == 7:
					rgb = rgb32(hex_to_rgb(rule.style.backgroundColor.replace("#","")))
					print template % (rule.selectorText.replace("#",""), rgb[0], rgb[1], rgb[2])