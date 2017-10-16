import argparse
import json
import logging
import os
import sys
from time import time

from jinja2 import Template, Environment

log = logging.getLogger("generate")
BLACKLISTED_KEYS = {"default", "description"}


def generate(index, output, template_readme, readme_ext, template_model, model_ext):
    with open(index) as fin:
        data = json.load(fin)
    models = data["models"]
    links = {}
    for name, items in models.items():
        for key in items:
            if key in BLACKLISTED_KEYS:
                continue
            links[key] = os.path.join(name, "%s.%s" % (key, model_ext))
    os.makedirs(output, exist_ok=True)
    readme = os.path.join(output, "README." + readme_ext)
    with open(readme, "w") as fout:
        fout.write(template_readme.render(models=models, links=links))
    log.info("Generated %s", readme)
    for name, items in models.items():
        mdir = os.path.join(output, name)
        os.makedirs(mdir, exist_ok=True)
        for key, val in items.items():
            if key in BLACKLISTED_KEYS:
                continue
            model = os.path.join(mdir, key + "." + model_ext)
            with open(model, "w") as fout:
                fout.write(template_model.render(uuid=key, details=val, links=links))
            log.info("Generated %s", model)


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="Path to index.json")
    parser.add_argument("-o", "--output", default=".", help="Output path.")
    parser.add_argument("--template-readme", default="template_readme.md.jinja2",
                        help="Jinja2 template to use to generate README.md")
    parser.add_argument("--template-model", default="template_model.md.jinja2",
                        help="Jinja2 template to use to generate model descriptions.")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    return args


def load_templates(template_readme, template_model):
    env = dict(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=False)
    jinja2_ext = ".jinja2"
    if not template_readme.endswith(jinja2_ext):
        raise ValueError("README template file name must end with %s" % jinja2_ext)
    if not template_model.endswith(jinja2_ext):
        raise ValueError("Model description template file name must end with %s" % jinja2_ext)
    try:
        readme_ext = template_readme[:-len(jinja2_ext)].split(".", 1)[1]
    except IndexError:
        raise ValueError("README template file name must contain the target file "
                         "extension prepended to %s" % jinja2_ext) from None
    try:
        model_ext = template_model[:-len(jinja2_ext)].split(".", 1)[1]
    except IndexError:
        raise ValueError("Model description template file name must contain the target file "
                         "extension prepended to %s" % jinja2_ext) from None
    with open(template_readme) as fin:
        template_readme_obj = Template(fin.read(), **env)
    template_readme_obj.filename = template_readme
    log.info("Loaded %s", template_readme)
    with open(template_model) as fin:
        template_model_obj = Template(fin.read(), **env)
    template_model_obj.filename = template_model
    log.info("Loaded %s", template_model)
    return (template_readme_obj, readme_ext), (template_model_obj, model_ext)


def main():
    start_time = time()
    args = setup()
    template_readme, template_model = load_templates(args.template_readme, args.template_model)
    generate(args.index, args.output, *template_readme, *template_model)
    elapsed = time() - start_time
    log.info("Elapsed: %.3f s", elapsed)

if __name__ == "__main__":
    sys.exit(main())
