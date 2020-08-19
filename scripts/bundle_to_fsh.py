import os
import sys
import logging
import json
import argparse
from fhir.resources.bundle import Bundle


logging.basicConfig()
logger = logging.getLogger(__name__)

def is_code(path):
    if path in ('status', 'intent', 'priority', ''):
        return True
    return False


def dump_resource(entry, directory):
    resource = entry.resource
    resource_id = resource.id
    with open(os.path.join(directory, f"{resource.resource_type.lower()}_{resource_id}.fsh"), "w") as fh:
        fh.write(f"Instance: {resource_id}\n")
        fh.write(f"InstanceOf: {resource.resource_type}\n\n")
        fh.write(f"* url = {entry.fullUrl}\n")
        for (key, values) in resource.__dict__.items():
            if key.startswith('_'):
                continue
            if key in ('id', 'resourceType'):
                continue
            if not values:
                continue
            if isinstance(values, (list, tuple)):
                pass
            else:
                if is_code(key):
                    fh.write(f"* {key} = #{values}\n")
                else:
                    fh.write(f"* {key} = \"{values}\"\n")


def unbundle(bundle_file, prefix):
    if not os.path.exists(bundle_file):
        logger.error(f"{bundle_file} not found")
        sys.exit(1) 
    with open(bundle_file, "r") as fh:
        doc = json.load(fh)
    # load the bundle
    bundle = Bundle(doc)
    destination = os.path.join(os.path.dirname(bundle_file), prefix)
    if not os.path.exists(destination):
        logger.info(f"Creating {destination}")
        os.makedirs(destination) 
    for resource in bundle.entry:
        dump_resource(resource, destination)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="bundle_file")
    parser.add_argument("-o", dest="output_dir")
    args = parser.parse_args()
    if not args.bundle_file:
        logger.error("Need a bundle_file")
        sys.exit(1)
    if not args.output_dir:
        logger.error("Need an output_dir")
        sys.exit(1)
    unbundle(args.bundle_file, args.output_dir)

