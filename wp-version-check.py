import sys, requests


def parse_version(text):
  # TODO implement
  return "7.5.0"

print("Usage: wp-version-check.py <url to scan>")

url = sys.argv[1]

r = requests.get(url)

version = parse_version(r.text)

print("[ ] Site appears to be running WordPress " + version)
