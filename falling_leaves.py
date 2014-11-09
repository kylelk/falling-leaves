import xml.etree.cElementTree as ET
from math import sin
import random

# author Kyle Kersey

# configuation
leaf_count = 30
min_fall_duration = 10.0
max_fall_duration = 15.0
min_leaf_size = 0.25
max_leaf_size = 0.75

root = ET.Element("svg")
root.set("xmlns","http://www.w3.org/2000/svg")
root.set("xmlns:xlink", "http://www.w3.org/1999/xlink")
root.set("version", "1.1")
root.set("width", "1000px")
root.set("height", "1000px")

# define a leaf
defs = ET.SubElement(root, "defs")
g = ET.SubElement(defs, "g")
g.set("id", "leaf")
path = ET.SubElement(g, "path")
#path.set("fill", "#D40000")
path.set("transform", "scale(0.25)")
path.set("d", """M127.251-22.679l-26.198,49.003c-2.974,5.326-8.297,4.834-13.625,1.858l-18.97-9.851l14.14,75.266
		c2.975,13.752-6.564,13.752-11.272,7.808L38.223,64.245l-5.376,18.872c-0.617,2.478-3.345,5.078-7.433,4.457l-41.855-8.82
		l10.994,40.08c2.354,8.92,4.187,12.613-2.377,14.967l-14.919,7.032l72.054,58.692c2.855,2.22,4.295,6.216,3.28,9.829l-6.307,20.753
		c24.806-2.863,47.054-5.434,71.859-8.297c2.205-0.028,3.646,1.199,3.63,3.741l-4.423,76.692h19.814l-4.424-76.692
		c-0.016-2.542,1.426-3.77,3.631-3.741c24.805,2.863,47.053,5.434,71.859,8.297l-6.307-20.753c-1.016-3.613,0.424-7.609,3.279-9.829
		l72.054-58.692l-14.919-7.032c-6.563-2.354-4.73-6.047-2.377-14.967l10.994-40.08l-41.855,8.82
		c-4.087,0.621-6.815-1.979-7.433-4.457l-5.376-18.872l-33.102,37.161c-4.707,5.944-14.246,5.944-11.271-7.808l14.139-75.266
		l-18.97,9.851c-5.329,2.976-10.651,3.468-13.626-1.858L127.251-22.679z""")


for a in range(0,10):
    points = []
    offset = random.randrange(-25,25)
    
    for i in range(-10,100):
        points.append([(a*100)+(100*sin(i)), (20*i)+offset])
    
    first = points.pop(0)
    point_list = "M%0.3f,%0.3f "%(first[0], random.randrange(-1000,0))
    point_list += " ".join( map(lambda a: "L%0.3f,%0.3f"%(a[0],a[1]), points) )
        
    path = ET.SubElement(root, "path")
    path.set("d", point_list)
    path.set("class", "mPath")
    path.set("fill", "none")
    # uncomment this line to see path
    #path.set("stroke", "black")
    path.set("stroke-width", "2")
    path.set("id", "p%d"%a)
    

for i in range(0, leaf_count):
    #g = ET.SubElement(root, "g")
    #g.set("transform", "scale(%0.3f)"%random.uniform(min_leaf_size, max_leaf_size))
    
    use = ET.SubElement(root, "use")
    use.set("xlink:href", "#leaf")
    use.set("x", "0")
    use.set("y", "0")
    use.set("fill", "hsla(%d, 100%%, 50%%, .75)"%random.randrange(0,100))
    
    animateMotion = ET.SubElement(use, "animateMotion")
    animateMotion.set("dur", "%0.3f"%random.uniform(min_fall_duration, max_fall_duration))
    animateMotion.set("repeatCount", "indefinite")
    mpath = ET.SubElement(animateMotion, "mpath")
    mpath.set("xlink:href", "#p%d"%(i%10))
    
    leaf_rotation = random.randrange(0,360)
    animateTransform = ET.SubElement(use, "animateTransform")
    animateTransform.set("attributeName", "transform")
    animateTransform.set("attributeType", "XML")
    animateTransform.set("type", "rotate")
    animateTransform.set("from", str(leaf_rotation))
    animateTransform.set("to",str(leaf_rotation+360))
    animateTransform.set("dur", "2s")
    animateTransform.set("repeatCount", "indefinite")
    

tree = ET.ElementTree(root)
tree.write("test.svg")

svg_data = ""
with open("test.svg", "r") as f:
    svg_data = f.read()

html = """
<!DOCTYPE html>
<html>
<head>
<title>svg test</title>
<style>
svg {
	 overflow:hidden;
}
mPath {
	fill:none;
	stroke-width:3;
	stroke: black;
}
</style>
</head>
<body>
{%svg_data%}
</body>
</html>
"""

html = html.replace("{%svg_data%}", svg_data)
print html
