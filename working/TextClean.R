#https://rpubs.com/pjmurphy/265713
#https://www.tidytextmining.com/topicmodeling.html
library(tm)
toSpace <- content_transformer(function(x, pattern) {return (gsub(pattern,"", x))})
cname <- file.path("C:\\Users\\amnag\\DATA515\\Project\\word-rnn-tensorflow\\word-rnn-tensorflow\\data\\tinyshakespeare\\input.txt")   

my_lines = readLines(cname)

doc = VCorpus(VectorSource(my_lines))
#summary(doc)
doc <- tm_map(doc,removePunctuation)  
doc <- tm_map(doc, tolower)  
doc <- tm_map(doc, stripWhitespace)  

removeNonAscii = function(x) gsub("[^\x20-\x7E]", "", x)
doc <- tm_map(doc,removeNonAscii)
doc <- tm_map(doc, PlainTextDocument)

#writeCorpus(doc)
#writeCorpus(doc,path="C:\\Users\\amnag\\DATA515\\Project\\word-rnn-tensorflow\\word-rnn-tensorflow\\data\\tinyshakespeare")
#writeLines(as.character(doc), con="C:\\Users\\amnag\\DATA515\\Project\\word-rnn-tensorflow\\word-rnn-tensorflow\\data\\tinyshakespeare\\input_small_processed.txt")

save.corpus.to.files = function( my_corpus, filename="input_processed" ) {
  out_file = file( paste( filename, ".txt", sep="" ) )
  open( out_file, open="w" )
  ig = sapply( my_corpus, function( x ) { writeLines( content(x), out_file ) } )
  close(out_file)
}

save.corpus.to.files(doc)
