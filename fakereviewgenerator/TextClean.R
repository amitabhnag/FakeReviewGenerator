# This is a utility to clean input text
# It takes a csv as input, converts text to lower case, removes
# all characters except numbers, letters and comma (for csv format)
# Few references for text cleanup:
#  https://rpubs.com/pjmurphy/265713
#  https://www.tidytextmining.com/topicmodeling.html
#  https://github.com/cran/textreg/blob/master/R/clean_text.R

library(tm)

#update below three variables based on your data and path
file_path = "C:\\Users\\amnag\\DATA515\\Project\\FakeReviewGenerator\\data\\amazonfoodreviews\\"
input_file_name = "Reviews.csv"
output_file_name = "input.txt"

cname <- file.path(file_path,input_file_name)   
my_lines = readLines(cname)
doc = VCorpus(VectorSource(my_lines))
doc <- tm_map(doc, tolower)  
removeNonAlphaNumeric = function(x) gsub("[^,a-zA-Z0-9 ]", "", x)
doc <- tm_map(doc,removeNonAlphaNumeric)
doc <- tm_map(doc, PlainTextDocument)

save.corpus.to.files = function( my_corpus ) {
  out_file = file( paste( file_path,output_file_name, sep="" ) )
  open( out_file, open="w" )
  ig = sapply( my_corpus, function( x ) { writeLines( content(x), out_file ) } )
  close(out_file)
}

save.corpus.to.files(doc)
