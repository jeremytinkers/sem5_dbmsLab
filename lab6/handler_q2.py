import xml.etree.ElementTree as ET
import computeGpaModule

tree = ET.parse('score_data.xml')
root = tree.getroot()

for curStudent in root.findall('student'):
    
    print(curStudent.get('student_id'))

    score = int(curStudent.find('xml_class').text)
    print("xml", score)
    curStudent.find('xml_class').set('gpa', str(computeGpaModule.computeGPA(score)))
 
    score = int(curStudent.find('data_structure').text)
    print("DS", score)
    curStudent.find('data_structure').set('gpa', str(computeGpaModule.computeGPA(score)))

    score = int(curStudent.find('algorithm').text)
    print("Algorithm", score)   
    curStudent.find('algorithm').set('gpa', str(computeGpaModule.computeGPA(score)))
    
    score = int(curStudent.find('network').text)
    print("Network", score)
    curStudent.find('network').set('gpa', str(computeGpaModule.computeGPA(score)))
    

#Write into output file
tree.write('output.xml')
