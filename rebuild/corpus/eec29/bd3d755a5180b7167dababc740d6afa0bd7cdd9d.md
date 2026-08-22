# Solution Step 2: Pages-Pagenumber-Map

From the Chapter-Pages-Map can now be built the Pages-Pagenumbers-Map (parameter PagesPagenumbersMap). The keys are the pages, the values are the calculated page numbers.

The aim of the solution step:

| Pages-Pagenumber-Map | |
| --- | --- |
| Key | Value |
| --- | --- |
| <<PageA>> | 1 |
| <<PageB>> | 1 |
| <<PageC>> | 2 |
| <<PageD>> | 1 |
| <<PageE>> | 2 |
| <<PageF>> | 3 |

```
$SeitenSeitennummernMap=mroot.rmos('ECAD.ChapterElement').intoInject(seite,map|  
map.add(Pair{seite, $KapitelSeitenMap.value(seite.$Kapitel).indexOf(seite)+1}),Map{})
```

The page numbers are calculated by the following formula:

```
$Seitennummer=mroot.$SeitenSeitennummernMap.value(origin.ifNull(this))
```

The performance will not increase by the Pages-Pagenumbers-Map, because even without this map the page number is accessed only once per page. Strictly speaking, the performance decreases slightly, because in addition to the indexOf(this) in the construction of the map the hash function to determine the keys is performed n times for the query on the map.

The page numbers without Pages-Pagenumbers-Map are calculated by the following formula:

```
$Seitennumer=mroot.$KapitelSeitenMap.value($Kapitel).indexOf(origin.ifNull(this))+1
```