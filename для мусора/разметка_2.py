import xml.etree.ElementTree as ET
root_node = ET.parse('master.xml').getroot()
print(root_node.tag)
print(root_node.attrib)
print()
print(root_node[0].tag)
print(root_node[0].attrib)
print()
for child in root_node[0]:
    print(child.tag)
    print(child.attrib)
    print()

print(root_node[0][0][0][3].tag)
print(root_node[0][0][0][3].attrib)
# for elem in root_node.iter():
#     print(elem.tag, elem.attrib)
# We need to go one level below to get
# and then one more level from that to go to

for tag in root_node.findall('AdaptationSet'):
    # h_value = tag.get('heading')
    # if h_value is not None:
    #     print(h_value)
    print(tag)
