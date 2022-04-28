#list1 = [1, 2, 3, 4, 5];
list2 = ['banana', 'apples', 'mango', 'orange'];
#list1.extend(list2); # da haben wir die zwei Listen zusammengefügt, also liste1 mit 2
#print(list1); 
#print(len(list2)); # Zählt die Elemente der Liste

#list2.insert(1, 'cherry'); # da fügen wir 'cherry' in die Liste hinzu und der Index ist 1 (also zweites Element der Liste)
#list2.clear - so löscht man alle Werte raus
#list2.remove('banana'); - so löscht man einen Wert aus der Liste
#print(list2); 
list1 = [3, 5, 4, 1, 2, 6, 9, 8];

#print(list2.index('mango')); # So findet man den Index dieses Stringswertes heraus

#list1.sort(); - so werden Listen sortiert
#list1.reverse(); - so werden Listen umgedreht
#list3 = list2.copy(); # so werden Listen kopiert
#print(list3);
#del list2[0] - so wirde der genannte Index der liste gelöscht
list2.pop(); # Hier wirde der letzte Wert einfach gelöscht, mit dem Index geht es so - 1 list2.pop(1)
print(list2);