#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe
import xml.etree.ElementTree as eTree
tree = eTree.parse('C:/Users/barraud/Documents/tech-sessions/sitemap.xml')
root = tree.getroot()

#findall: get all nodes at a path
countries = root.findall(".//country")

for country in countries :
    # find: get a node attrib
    print (country.attrib["name"])
    # get the first (or only) node at a path
    rank = country.find("./rank")
    #tag: get the name of a node
    print (rank.tag)
    #text: get the inner text of a node
    print (rank.text)

    #getchildren: all children of a node
    for iteminCountry in country.getchildren():
        print (iteminCountry)

    #iterate attribs
    for countryattrib in country.attrib :
        print (countryattrib)


print ("all done")

# Important notes:
# If you're getting the parse error for characters like &nbsp, you need to exclude these in the XML parser
    # parser = eTree.XMLParser()
    # parser.entity["nbsp"] = chr(160)

# If your XML defines namespaces
#create a namespace alias
    # ns_alias = {'sitemap':'http://www.sitemaps.org/schemas/sitemap/0.9'}
# use the alias in the xpath query
    # locs = root.findall(".//sitemap:url/sitemap:loc",ns_alias)
