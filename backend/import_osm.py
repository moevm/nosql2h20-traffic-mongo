import xml.sax
from pymongo import MongoClient
from db_types import *

def db_clear(db):
    db.nodes.remove()
    db.ways.remove()
    db.relations.remove()


class OSMXMLFileParser(xml.sax.ContentHandler):
    def __init__(self, db):
        self.db = db
        self.curr_node = None
        self.curr_way = None
        self.curr_relation = None
        self.nodesCount = 0
        self.waysCount = 0
        self.relationsCount = 0

    def startElement(self, name, attrs):
        print('START!!!!!!!!!!!')
        if name == 'node':
            self.curr_node = Node(id=int(attrs['id']), lon=float(attrs['lon']), lat=float(attrs['lat']),
                                  visible='true')

        elif name == 'way':
            # self.containing_obj.ways.append(Way())
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
            if attrs.has_key('role') == True:
                member.role = attrs['role']
            self.curr_relation.members.append(member)

    def endElement(self, name):
        print('END!!!!!!!!!!!')
        # assert not self.curr_node and not self.curr_way, "curr_node (%r) and curr_way (%r) are both non-None" % (self.curr_node, self.curr_way)
        if name == 'node':
            dbnode = {'_id': self.curr_node.id,
                      'lon': self.curr_node.lon,
                      'lat': self.curr_node.lat,
                      'visible': self.curr_node.visible,
                      'in_ways': [],
                      'in_relations': []}

            if len(self.curr_node.tags) > 0:
                dbnode['tags'] = self.curr_node.tags
            self.db.nodes.save(dbnode)
            self.curr_node = None

        elif name == 'way':
            dbway = {'_id': self.curr_way.id,
                     'visible': self.curr_way.visible,
                     'in_relations': []}
            dbway['nodes'] = self.curr_way.nodes
            dbway['tags'] = self.curr_way.tags
            self.db.ways.save(dbway)
            self.curr_way = None

        elif name == 'relation':
            dbrelation = {'_id': self.curr_relation.id,
                          'in_relations': []}
            dbrelation['members'] = []
            for member in self.curr_relation.members:
                dbrelation['members'].append(member.list())
            dbrelation['tags'] = self.curr_relation.tags
            self.db.relations.save(dbrelation)
            self.curr_relation = None

def create_db():
    client = MongoClient('localhost', 27017)
    db = client['spb_map']
    dbnodes = db.nodes
    dbways = db.ways
    dbrelations = db.relations
    return db

def import_to_bd(filename):
    db = create_db()
    parser = xml.sax.make_parser()
    parser.setContentHandler(OSMXMLFileParser(db))
    parser.parse(filename)

with open("../map") as file:
    file.close()
    import_to_bd('../map')
