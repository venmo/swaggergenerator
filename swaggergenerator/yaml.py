from __future__ import absolute_import

import yaml


class _Dumper(yaml.SafeDumper):
    """A dumper that outputs yaml closer to idiomatic swagger yaml than the default settings."""

    def ignore_aliases(self, data):
        # see http://stackoverflow.com/a/21019031/1231454
        return True

    def increase_indent(self, flow=False, indentless=False):
        # see http://pyyaml.org/ticket/64#comment:5
        return super(_Dumper, self).increase_indent(flow, False)


def get_yaml(schema):
    """Return a string of yaml appropriate to paste under the ``paths:`` key in a swagger schema."""

    output = yaml.dump(schema, default_flow_style=False, Dumper=_Dumper,)

    # indent the yaml so it can be pasted directly into the paths section.
    return '\n'.join(' ' * 2 + line for line in output.split('\n'))
