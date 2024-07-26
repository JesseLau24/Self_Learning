# Imports the ElementTree module, 
# which provides tools for parsing and creating XML data.
import xml.etree.ElementTree as ET

# XML data:
data1 = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

# Converts the XML string into an ElementTree object, which can be 
# used to navigate and access XML elements.
tree1 = ET.fromstring(data1)

print('Name:', tree1.find('name').text)
print('Attr:', tree1.find('email').get('hide'))

data2 = '''
<contacts>
    <contact>
        <name>John Doe</name>
        <email>john.doe@example.com</email>
        <phone>555-1234</phone>
    </contact>
    <contact>
        <name>Jane Smith</name>
        <email>jane.smith@example.com</email>
        <phone>555-5678</phone>
    </contact>
</contacts>
'''

# Parse the XML data from the string
tree2 = ET.fromstring(data2)

# Iterate over all 'contact' elements to access 'name' and 'email' under each
for contact in tree2.findall('contact'):
    name = contact.find('name').text
    email = contact.find('email').text
    print('Name:', name)
    print('Email:', email)
