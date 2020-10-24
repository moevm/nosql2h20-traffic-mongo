from xml.sax import ContentHandler, make_parser
from get_model import get_mongo
from db_types import *
import sys

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


def print_progress_bar (completed, started, printEnd = "\r"):
    prefix = 'Done: ' + str(completed)
    print(f'\r{prefix}', end = printEnd)
    if completed == started:
        print()

def set_pointers_for_nodes(db):
    dbnodes = db.nodes
    dbways = db.ways
    dbrel = db.relations
    for node in dbnodes.find():
        node_id = node['_id']
        n_ways = find_ways_for_node(node_id, dbways)
        n_relations = find_relations_for_node(node_id, dbrel)
        dbnodes.update_one(
            {'_id': node_id},
            {'$set':
                 {'in_ways': n_ways,
                  'in_relations': n_relations}
             })


def find_ways_for_node(id, ways):
    res = []
    for way in ways.find({'nodes': {'$all': [id]}}):
        res.append(way['_id'])
    return res


def find_relations_for_node(id, relations):
    res = []
    for rel in relations.find({'members.ref': {'$all': [id]}}):
        res.append(rel['_id'])
    return res


class OSMXMLFileParser(ContentHandler):
    def __init__(self, db):
        self.db = db
        self.curr_node = None
        self.curr_way = None
        self.curr_relation = None
        self.nodesCount = 0
        self.waysCount = 0
        self.relationsCount = 0
        self.count_started = 0
        self.count_completed = 0

    def startElement(self, name, attrs):
        self.count_started += 1
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
        self.count_completed += 1
        print_progress_bar(self.count_completed, self.count_started)

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
            for node in self.curr_way.nodes:
                ways = self.db.nodes.find_one({'_id': node})['in_ways']
                ways.append(self.curr_way.id)
                self.db.nodes.update_one(
                    {'_id': node},
                    {'$set':
                         {'in_ways': ways}
                    })
            self.db.ways.save(dbway)
            self.curr_way = None

        elif name == 'relation':
            dbrelation = {'_id': self.curr_relation.id, 'members': []}
            for member in self.curr_relation.members:
                dbrelation['members'].append(member.list())
            dbrelation['tags'] = self.curr_relation.tags
            self.db.relations.save(dbrelation)
            self.curr_relation = None


if __name__ == "__main__":
   db = import_to_bd(sys.argv[1])
   #set_pointers_for_nodes(db)
