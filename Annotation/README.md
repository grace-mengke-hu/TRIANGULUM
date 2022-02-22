# Annotation
- **annotDataFeatureMongo.py** loads the ehost annotated text file and original text file to extract annotations and relationships.
- **annotDataFeatureMongo_relationship.py** searches Mongo Database for original text according to the post ID from the annotated data.
- **annotStat.py** calculates the frequencies of *poly-use*, *co-use*, *dual-use*,*cessation*,*vaping-marijana* in the annotated dataset.
- **CollectRelationshipData.py** finds annotations with relation and copy relation-annotation files into new folder.
- **countAnnot.py** counts the total number of annotation from given range of initiating post.
- **reader.py** contains three function:
    1) `annotFileReader()` reads in annotation files in xml fomat and extract all the annotation information and convert into dictionary
    2) `annotFileReader_relationship()` reads in annotaion files in xml and extract relation annotation and convert into dictionary.
    3) `corpusFileReader()` reads in orignal text files.
- **TagAndRelationshipCount.py** counts class annotation and relation annotation.
- **TagAndRelationshipDistribution.py** counts the number of annotations and relations from annotated dataset.
- **testFindAnnot.py** loads both annotated file and corresponding text file and checks if they match.
- **testFindAnnotRelationship.py** tests reading in annotation files and parse the class annotation and relation annotation.
- **testRulebased.py** tests rule-base annotation prediction system and counts
- **\<bin__range__\>findAnotData.p** for example (4_10_findAnotData.p) contains the file paths to the annotation files for each bin range. For example, 4_10_ means sampled from authors who have at the number of initiating post between 4 and 10.

