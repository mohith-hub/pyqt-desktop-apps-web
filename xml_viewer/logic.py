import xml.etree.ElementTree as ET

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    data = []
    for student in root.findall("student"):
        data.append({
            "Name": student.find("name").text,
            "Roll Number": student.find("rollNumber").text,
            "Branch": student.find("branch").text,
            "CGPA": student.find("cgpa").text,
            "Year": student.find("year").text
        })
    return data
