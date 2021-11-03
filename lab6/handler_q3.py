import xml.etree.ElementTree as ET
import computeGpaModule

tree = ET.parse('output.xml')
root = tree.getroot()

avgScore=0

for curStudent in root.findall('student'):
    
    item = curStudent.find('xml_class')
    score = int(item.text)
    score+=5
    avgScore=score
    item.text = str(score)
    item.set('gpa', str(computeGpaModule.computeGPA(score)))

    item = curStudent.find('data_structure')
    score = int(item.text)
    score+=5
    avgScore+=score
    item.text = str(score)
    item.set('gpa', str(computeGpaModule.computeGPA(score)))

    item = curStudent.find('algorithm')
    score = int(item.text)
    score+=5
    avgScore+=score
    item.text = str(score)
    item.set('gpa', str(computeGpaModule.computeGPA(score)))

    item = curStudent.find('network')
    score = int(item.text)
    score+=5
    avgScore+=score
    item.text = str(score)
    item.set('gpa', str(computeGpaModule.computeGPA(score)))

    student_id = curStudent.get('student_id')
    avgScore = avgScore/4
    print("For Student : " +  str(student_id) + " , Avg Sum is: " + str(avgScore))
    print("GPA is: " + str(computeGpaModule.computeGPA(avgScore)))

    avgGPA = ET.SubElement(curStudent, 'avgGPA')
    avgGPA.text = str(computeGpaModule.computeGPA(avgScore))

tree.write('new_output.xml')


