class Member(object):
    def __init__(self, type, ref, role=''):
        self.type = type
        self.ref = ref
        self.role = role

    def list(self):
        return {'type': self.type, 'ref': self.ref, 'role': self.role}

    def __repr__(self):
        return "Member({}, {}, {})".format(self.type, self.ref, self.role)


class Node(object):
    def __init__(self, id, lon, lat, visible, tags=None):
        self.id = id
        self.lon = lon
        self.lat = lat
        self.visible = visible

        if tags:
            self.tags = tags
        else:
            self.tags = {}

    def __repr__(self):
        return "Node(id={}, lon={}, lat={}, visible={}, tags={})".format(self.id, self.lon,
                                                                         self.lat, self.visible, self.tags)


class Way(object):
    def __init__(self, id, visible, nodes=None, tags=None):
        self.id = id
        self.visible = visible

        if nodes:
            self.nodes = nodes
        else:
            self.nodes = []

        if tags:
            self.tags = tags
        else:
            self.tags = {}

    def __repr__(self):
        return "Way(id={}, visible={}, nodes={}, tags={})".format(self.id, self.visible, self.nodes, self.tags)


class Relation(object):
    def __init__(self, id, members=None, tags=None):
        self.id = id

        if members:
            self.members = members
        else:
            self.members = []

        if tags:
            self.tags = tags
        else:
            self.tags = {}

    def __repr__(self):
        return "Relation(id={}, members={}, tags={})".format(self.id, self.members, self.tags)