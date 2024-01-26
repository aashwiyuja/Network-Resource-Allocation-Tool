import random

k = int(input('number of ports each switch: \n'))
input("migration coefficient : ")
lab = 4
mu = 0
# w = int(k * 3/4)
while 1:
    
    if k>= lab:
        
        i =  int(input("number of VM pairs: \n"))
        if k < i:
            
            m = int(input("number of middleboxes : \n"))
            rc = int(input("the initial resource capacity of each PM \n"))
            if rc < m:
                with open("scf_migration.inp",mode="w") as file:
                    
                    print(f"p min {k} {i}")
                    y = (f"p min {k} {i}\n")
                    file.write(y)
                    print(f"c min-cost flow problem with {k} nodes and {i} arcs ")
                    y = (f"c min-cost flow problem with {k} nodes and {i} arcs \n")
                    file.write(y)
                    
                    print(f"n {rc} {m}")
                    y = (f"n {rc} {m}\n")
                    file.write(y)
                    
                    print(f"c supply of {m}  at nodes {rc}")
                    y = (f"c supply of {m}  at nodes {rc} \n")
                    file.write(y)
                    print(f"n {lab} -{m}")
                    y = (f"n {lab} -{m}\n")
                    file.write(y)
                    
                    print(f"c demand of {m} at node {k}")
                    y = (f"c demand of {m} at node {k}\n")
                    file.write(y)
                    print(f"c arc list follows ")
                    y = (f"c arc list follows \n")
                    file.write(y)
                    print(f"c arc has  <tail> <head> <capacity l.b.> <capacity u.b> <cost>")
                    y = (f"c arc has  <tail> <head> <capacity l.b.> <capacity u.b> <cost>\n")
                    file.write(y)
                    for x in range(i):
                        x1 = random.randint(1,4)
                        x2 = random.randint(4,6)
                        x3 = random.randint(6,9)
                        x4 = random.randint(0,9)
                        print(f"a {x1} {x2} {mu} {x3} {x4}")
                        
                        y = (f"a {x1} {x2} {mu} {x3} {x4} \n")
                        file.write(y)
                    break
            else:
                print("The initial resource capacity of each PM must be less than number of middleboxes")    
                
        else:
            print("number of VM pairs must be greater than ports each switch")
            
    else:
        print("number of ports each switch must be greater than six !!")
        break