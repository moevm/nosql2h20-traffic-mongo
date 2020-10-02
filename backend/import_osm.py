from xml.sax import ContentHandler, make_parser
from models.get_model import get_mongo
from db_types import *


def db_clear(db):
    db.nodes.remove()
    db.ways.remove()
    db.relations.remove()


def create_db(name):
    client = get_mongo()
    db = client[name]
    dbnodes = db.nodes
    dbways = db.ways
    dbrelations = db.relations
    db_clear(db)
    return db


def import_to_bd(filename):
    db = create_db('map_spb')
    parser = make_parser()
    parser.setContentHandler(OSMXMLFileParser(db))
    parser.parse(filename)
    return db


class OSMXMLFileParser(ContentHandler):
    def __init__(self, db):
        self.db = db
        self.curr_node = None
        self.curr_way = None
        self.curr_relation = None
        self.nodesCount = 0
        self.waysCount = 0
        self.relationsCount = 0

    def startElement(self, name, attrs):
        if name == 'node':
            self.curr_node = Node(id=int(attrs['id']), lon=float(attrs['lon']), lat=float(attrs['lat']),
                                  visible='true')
        elif name == 'way':
            self.curr_way = Way(id=int(attrs['id']), visible='true')

        elif name == 'relation':
            self.curr_relation = Relation(id=int(attrs['id']))

        elif name == 'tag':
            if self.curr_node:
                self.curr_node.tags[attrs['k']] = attrs['v']
            elif self.curr_way:
                self.curr_way.tags[attrs['k']] = attrs['v']
            elif self.curr_relation:
                self.curr_relation.tags[attrs['k']] = attrs['v']

        elif name == 'nd':
            self.curr_way.nodes.append(int(attrs['ref']))

        elif name == 'member':
            member = Member(type=attrs['type'], ref=int(attrs['ref']))
            if 'role' in attrs.keys():
                member.role = attrs['role']
            self.curr_relation.members.append(member)

    def endElement(self, name):
        if name == 'node':
            dbnode = {'_id': self.curr_node.id,
                      'lon': self.curr_node.lon,
                      'lat': self.curr_node.lat,
                      'visible': self.curr_node.visible,
                      'in_ways': [], 'in_relations': []}

            if len(self.curr_node.tags) > 0:
                dbnode['tags'] = self.curr_node.tags
            self.db.nodes.save(dbnode)
            self.curr_node = None

        elif name == 'way':
            dbway = {'_id': self.curr_way.id, 'visible': self.curr_way.visible,
                     'nodes': self.curr_way.nodes, 'tags': self.curr_way.tags}
            self.db.ways.save(dbway)
            self.curr_way = None

        elif name == 'relation':
            dbrelation = {'_id': self.curr_relation.id, 'members': []}
            for member in self.curr_relation.members:
                dbrelation['members'].append(member.list())
            dbrelation['tags'] = self.curr_relation.tags
            self.db.relations.save(dbrelation)
            self.curr_relation = None