# coding=UTF-8
__author__ = 'krilo'

import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        # python有環境管理器，透過with as 簡化檔案讀寫
        # 2.7 不支援encoding: with open(filepath, mode='r', encoding='utf-8')
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('firstname: {}'.format(liar.find('firstName').text))
        print('lastname: {}'.format(liar.find('lastName').text))
        for p in liar.find('phoneNumbers'):
            print 'phone number({}):'.format(p.attrib['type']), p.text
    print


    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        for t in donut['topping']:
            print 'topping: {} {}'.format(t['id'], t['type'])


if __name__ == '__main__':
    main()

# class A(object):
#     pass
#
#
# if __name__ == '__main__':
#     a = A()
#     b = A()
#
#     print(id(a) == id(b))
#     print(a, b)
