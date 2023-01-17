'''credit - tutorial point'''
import nltk
sentence = [
   ("a", "DT"),
   ("clever", "JJ"),
   ("fox","NN"),
   ("was","VBP"),
   ("jumping","VBP"),
   ("over","IN"),
   ("the","DT"),
   ("wall","NN")
]
grammar = "NP:{<DT>?<JJ>*<NN>}" 
Reg_parser = nltk.RegexpParser(grammar)
Reg_parser.parse(sentence)
Output = Reg_parser.parse(sentence)
Output.draw()
