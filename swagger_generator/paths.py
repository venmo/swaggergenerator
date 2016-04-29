def build_paramaterized_path(components):
    i = 0
    path = []
    for component in components:
        if component is None:
            i += 1
            component = "{param%s}" % i
        path.append(component)

    return '/' + '/'.join(path)


def component_matches(c1, c2):
    if len(c1) != len(c2):
        return False

    for e1, e2 in zip(c1, c2):
        if e1 != e2 and e2 is not None:
            return False

    return True
